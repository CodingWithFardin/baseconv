#!/usr/bin/env python3
"""baseconv - base conversion with 0x/0b/0o prefix detection."""
import argparse
import sys

DIGITS = "0123456789abcdefghijklmnopqrstuvwxyz"


def parse(text: str, base: int = 0) -> int:
    text = text.strip().replace("_", "")
    sign = -1 if text.startswith("-") else 1
    text = text.lstrip("+-")
    if text[:2].lower() == "0x":
        return sign * int(text[2:], 16)
    if text[:2].lower() == "0b":
        return sign * int(text[2:], 2)
    if text[:2].lower() == "0o":
        return sign * int(text[2:], 8)
    return sign * int(text, base or 10)


def render(value: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("base out of range")
    if value == 0:
        return "0"
    sign = "-" if value < 0 else ""
    n = abs(value)
    out = []
    while n:
        n, rem = divmod(n, base)
        out.append(DIGITS[rem])
    return sign + "".join(reversed(out))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="baseconv", description=__doc__)
    ap.add_argument("value")
    ap.add_argument("--from", dest="src", type=int, default=0)
    ap.add_argument("--to", type=int, default=10)
    args = ap.parse_args(argv)
    try:
        n = parse(args.value, args.src)
        print(render(n, args.to))
    except ValueError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
