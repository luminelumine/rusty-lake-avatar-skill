#!/usr/bin/env python3
"""Validate clean face-plane samples against the bundled canonical color."""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError as exc:  # pragma: no cover - environment failure
    raise SystemExit("Pillow is required: install the 'pillow' package in the active Python environment.") from exc


DEFAULT_REFERENCE = Path(__file__).resolve().parents[1] / "assets" / "face-color-reference.png"


def parse_box(value: str) -> tuple[int, int, int, int]:
    try:
        coords = tuple(int(part.strip()) for part in value.split(","))
    except ValueError as exc:
        raise argparse.ArgumentTypeError("face boxes must be x1,y1,x2,y2 integers") from exc
    if len(coords) != 4:
        raise argparse.ArgumentTypeError("face boxes must contain exactly four integers")
    x1, y1, x2, y2 = coords
    if x1 < 0 or y1 < 0 or x2 <= x1 or y2 <= y1:
        raise argparse.ArgumentTypeError("face boxes must satisfy 0 <= x1 < x2 and 0 <= y1 < y2")
    return coords


def median_rgb(image: Image.Image, box: tuple[int, int, int, int] | None = None) -> tuple[int, int, int]:
    sample = image.crop(box) if box else image
    rgb_sample = sample.convert("RGB")
    pixel_source = (
        rgb_sample.get_flattened_data()
        if hasattr(rgb_sample, "get_flattened_data")
        else rgb_sample.getdata()
    )
    pixels = list(pixel_source)
    return tuple(round(statistics.median(pixel[channel] for pixel in pixels)) for channel in range(3))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check clean, unshadowed face-plane rectangles against the canonical bundled color."
    )
    parser.add_argument("image", type=Path, help="generated image to validate")
    parser.add_argument(
        "--face-box",
        action="append",
        required=True,
        type=parse_box,
        metavar="X1,Y1,X2,Y2",
        help="clean unshadowed face-plane rectangle; repeat at least twice per generated human",
    )
    parser.add_argument("--reference", type=Path, default=DEFAULT_REFERENCE)
    parser.add_argument(
        "--tolerance",
        type=int,
        default=6,
        help="maximum absolute difference allowed for each RGB channel (default: 6)",
    )
    args = parser.parse_args()

    if args.tolerance < 0:
        parser.error("--tolerance must be non-negative")
    if len(args.face_box) < 2:
        parser.error("provide at least two --face-box samples")

    reference = Image.open(args.reference)
    generated = Image.open(args.image)
    target = median_rgb(reference)
    width, height = generated.size
    results = []
    passed = True

    for index, box in enumerate(args.face_box, start=1):
        x1, y1, x2, y2 = box
        if x2 > width or y2 > height:
            parser.error(f"face box {index} exceeds image bounds {width}x{height}")
        actual = median_rgb(generated, box)
        delta = tuple(abs(actual[channel] - target[channel]) for channel in range(3))
        sample_passed = max(delta) <= args.tolerance
        passed = passed and sample_passed
        results.append(
            {
                "box": box,
                "median_rgb": actual,
                "channel_delta": delta,
                "passed": sample_passed,
            }
        )

    print(
        json.dumps(
            {
                "image": str(args.image),
                "reference": str(args.reference),
                "target_median_rgb": target,
                "tolerance": args.tolerance,
                "samples": results,
                "passed": passed,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
