#!/usr/bin/env python3
"""Normalize generated human skin regions to the bundled canonical base color."""

from __future__ import annotations

import argparse
import statistics
from pathlib import Path

from PIL import Image

DEFAULT_REFERENCE = Path(__file__).resolve().parents[1] / "assets" / "face-color-reference.png"


def parse_box(value: str) -> tuple[int, int, int, int]:
    try:
        coords = tuple(int(part.strip()) for part in value.split(","))
    except ValueError as exc:
        raise argparse.ArgumentTypeError("boxes must be x1,y1,x2,y2 integers") from exc
    if len(coords) != 4:
        raise argparse.ArgumentTypeError("boxes must contain exactly four integers")
    x1, y1, x2, y2 = coords
    if x1 < 0 or y1 < 0 or x2 <= x1 or y2 <= y1:
        raise argparse.ArgumentTypeError("boxes must satisfy 0 <= x1 < x2 and 0 <= y1 < y2")
    return coords


def median_rgb(image: Image.Image, box: tuple[int, int, int, int] | None = None) -> tuple[int, int, int]:
    sample = (image.crop(box) if box else image).convert("RGB")
    pixels = list(sample.get_flattened_data() if hasattr(sample, "get_flattened_data") else sample.getdata())
    return tuple(round(statistics.median(pixel[channel] for pixel in pixels)) for channel in range(3))


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply a measured RGB correction only to explicit skin regions.")
    parser.add_argument("image", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--sample-box", action="append", required=True, type=parse_box)
    parser.add_argument("--skin-box", action="append", required=True, type=parse_box)
    parser.add_argument("--reference", type=Path, default=DEFAULT_REFERENCE)
    parser.add_argument("--radius", type=int, default=45, help="maximum per-channel distance from sampled skin base")
    args = parser.parse_args()

    source = Image.open(args.image).convert("RGBA")
    width, height = source.size
    for box in [*args.sample_box, *args.skin_box]:
        if box[2] > width or box[3] > height:
            parser.error(f"box {box} exceeds image bounds {width}x{height}")

    sample_medians = [median_rgb(source, box) for box in args.sample_box]
    sampled_base = tuple(round(statistics.median(rgb[channel] for rgb in sample_medians)) for channel in range(3))
    target = median_rgb(Image.open(args.reference))
    correction = tuple(target[channel] - sampled_base[channel] for channel in range(3))

    pixels = source.load()
    changed = 0
    for x1, y1, x2, y2 in args.skin_box:
        for y in range(y1, y2):
            for x in range(x1, x2):
                red, green, blue, alpha = pixels[x, y]
                if max(abs(red - sampled_base[0]), abs(green - sampled_base[1]), abs(blue - sampled_base[2])) > args.radius:
                    continue
                # Skin in this art has a restrained warm ordering. This rejects gray walls and yellow clothes.
                if not (red > green > blue and 8 <= red - green <= 42 and 5 <= green - blue <= 42):
                    continue
                pixels[x, y] = tuple(max(0, min(255, value + correction[index])) for index, value in enumerate((red, green, blue))) + (alpha,)
                changed += 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    source.save(args.output)
    print(f"sampled_base={sampled_base} target={target} correction={correction} changed_pixels={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
