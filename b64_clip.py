#!/usr/bin/env python3
"""b64-clip — Base64 encode/decode with clipboard, zero dependencies."""

import argparse
import base64
import os
import platform
import subprocess
import sys


def copy_to_clipboard(text: str) -> bool:
    """Copy text to clipboard. Returns True on success, False on failure."""
    system = platform.system()
    try:
        if system == "Darwin":
            proc = subprocess.run(["pbcopy"], input=text.encode(), check=True)
        elif system == "Windows":
            proc = subprocess.run(["clip.exe"], input=text.encode(), check=True)
        else:
            # Linux and other Unix — try xclip, then wl-copy (Wayland)
            for cmd in (["xclip", "-selection", "clipboard"],
                        ["wl-copy"]):
                try:
                    proc = subprocess.run(cmd, input=text.encode(), check=True)
                    break
                except FileNotFoundError:
                    continue
            else:
                print("WARNING: No clipboard tool found (xclip or wl-copy). "
                      "Install xclip for clipboard support.", file=sys.stderr)
                return False
        return True
    except (FileNotFoundError, subprocess.CalledProcessError) as e:
        print(f"WARNING: Clipboard copy failed ({e}). "
              "Output is still shown above.", file=sys.stderr)
        return False


def read_input(args) -> bytes:
    """Read input from --file, positional string, or stdin."""
    if args.file:
        fpath = os.path.expanduser(args.file)
        if not os.path.isfile(fpath):
            print(f"Error: File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        with open(fpath, "rb") as f:
            return f.read()

    if args.string:
        return args.string.encode()

    # Stdin pipe mode
    if not sys.stdin.isatty():
        return sys.stdin.buffer.read()

    print("Error: No input provided. Pass a string argument, --file, or pipe data via stdin.",
          file=sys.stderr)
    sys.exit(1)


def encode(args):
    """Base64-encode input and print + copy to clipboard."""
    raw = read_input(args)
    encoded = base64.b64encode(raw).decode()
    print(encoded)
    copy_to_clipboard(encoded)


def decode(args, url_safe: bool = False):
    """Base64-decode input and print + copy to clipboard."""
    raw = read_input(args).strip()
    raw_str = raw.decode()

    # Auto-detect URL-safe base64
    if not url_safe and ("-" in raw_str or "_" in raw_str):
        url_safe = True

    try:
        if url_safe:
            # Add padding if missing
            padding = 4 - len(raw_str) % 4
            if padding != 4:
                raw_str += "=" * padding
            decoded = base64.urlsafe_b64decode(raw_str).decode()
        else:
            decoded = base64.b64decode(raw_str).decode()
    except Exception as e:
        print(f"Error: Decode failed ({e}). Check that input is valid base64.",
              file=sys.stderr)
        sys.exit(1)

    print(decoded)
    copy_to_clipboard(decoded)


def main():
    parser = argparse.ArgumentParser(
        prog="b64-clip",
        description="Base64 encode/decode with clipboard, zero dependencies."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # encode subcommand
    enc = subparsers.add_parser("encode", help="Encode input to base64")
    enc.add_argument("string", nargs="?", default=None, help="String to encode")
    enc.add_argument("--file", "-f", default=None, help="File to encode")
    enc.set_defaults(func=encode)

    # decode subcommand
    dec = subparsers.add_parser("decode", help="Decode base64 to plaintext")
    dec.add_argument("string", nargs="?", default=None, help="Base64 string to decode")
    dec.add_argument("--file", "-f", default=None, help="File containing base64 to decode")
    dec.add_argument("--url-safe", action="store_true", default=False,
                      help="Use URL-safe base64 alphabet")
    dec.set_defaults(func=lambda args: decode(args, url_safe=args.url_safe))

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
