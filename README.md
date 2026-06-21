# b64-clip

Base64 encode/decode with clipboard, zero dependencies.

Encode auth tokens, config values, certificate data, and more — result is
automatically copied to your clipboard.

## Install

```bash
pip install b64-clip
```

Or run directly (no install):

```bash
python3 b64_clip.py encode "hello world"
```

## Usage

```bash
# Encode a string
b64-clip encode "hello world"
# Output: aGVsbG8gd29ybGQ=
# (also copied to clipboard)

# Decode a string
b64-clip decode "aGVsbG8gd29ybGQ="
# Output: hello world
# (also copied to clipboard)

# Encode a file
b64-clip encode --file cert.pem

# Decode a file
b64-clip decode --file encoded.txt

# Pipe from stdin
echo "test" | b64-clip encode

# URL-safe base64 decode
b64-clip decode --url-safe "PDw_Pz4-"
```

## What it does

- **Encode**: Takes any input (string, file, or stdin) and outputs base64
- **Decode**: Takes base64 input and outputs the decoded plaintext
- **Clipboard**: Automatically copies the result to your clipboard on macOS,
  Linux (xclip/wl-copy), and Windows (clip.exe)
- **Zero dependencies**: Python stdlib only — no pip install needed at runtime

## Requirements

- Python 3.11+
- For clipboard support: `xclip` on Linux (install with `sudo apt install xclip`),
  `pbcopy` on macOS (built-in), `clip.exe` on Windows (built-in)

## Security

Nothing is logged or stored. The tool processes data in memory only and does not
write any temporary files or make network requests.

## License

MIT
