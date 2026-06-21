# PyPI Store Listing — b64-clip

## Package Name

b64-clip

## Short Description

Base64 encode/decode CLI with automatic clipboard copy. Zero dependencies.

## Long Description

b64-clip is a zero-dependency Python CLI tool that base64-encodes or decodes any input and copies the result to your clipboard automatically.

**Why b64-clip?**

- **Clipboard integration**: Result is copied to clipboard on macOS (pbcopy), Linux (xclip/wl-copy), and Windows (clip.exe) — with graceful fallback if no clipboard tool is available.
- **Cross-platform consistency**: Same command on macOS, Linux, and Windows. No more remembering `-e` vs no flag, `-d` vs `-D`.
- **Multiple input modes**: String arguments, file input (`--file`), or stdin pipes.
- **URL-safe base64**: Supports `--url-safe` flag for URL-safe base64 decoding.
- **Zero dependencies**: Python stdlib only. No runtime pip installs.
- **Privacy-first**: Nothing is logged, stored, or sent over the network. All processing is in-memory.

**Install:**

```bash
pip install b64-clip
```

**Quick start:**

```bash
b64-clip encode "hello world"        # → aGVsbG8gd29ybGQ= (in clipboard)
b64-clip decode "aGVsbG8gd29ybGQ="   # → hello world (in clipboard)
b64-clip encode --file cert.pem      # → base64 of file (in clipboard)
echo "test" | b64-clip encode       # → cGVzdAo= (in clipboard)
```

**Requirements:** Python 3.11+

**License:** MIT

## Keywords

base64, clipboard, cli, encode, decode, developer-tools, devops, terminal, command-line, cross-platform, zero-dependencies, python, pip, pbcopy, xclip, automation, productivity
