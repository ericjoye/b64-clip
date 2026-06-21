# b64-clip — PyPI Store Listing

## Package Name

`b64-clip`

## Short Description

Base64 encode/decode CLI with automatic clipboard copy. Zero dependencies.

## Long Description

b64-clip is a zero-dependency Python CLI tool that base64-encodes or decodes any input — strings, files, or stdin — and copies the result to your clipboard automatically. It works on macOS, Linux, and Windows with no runtime dependencies.

**WHY B64-CLIP?**

Every developer needs base64 encoding at some point: auth tokens, config values, certificate data, API keys, or embedding assets. Existing options require remembering different flags across platforms, or manually copying output. b64-clip makes it effortless — one command, result in your clipboard.

**CLIPBOARD INTEGRATION**
The output is automatically copied to your clipboard on macOS (pbcopy), Linux (xclip/wl-copy), and Windows (clip.exe). If no clipboard tool is available, the result is still printed to stdout — so it works everywhere.

**FLEXIBLE INPUT MODES**
Pass a string argument, encode a file with `--file`, or pipe data from stdin. URL-safe base64 decoding is supported via the `--url-safe` flag. The tool is a single Python file with zero pip dependencies — you can even run it directly without installing.

**PRIVACY-FIRST**
Nothing is logged, stored, or sent over the network. All processing happens in memory. Your sensitive data never touches disk or the network.

## Key Features

- **Encode strings, files, or stdin** to base64
- **Decode base64** back to plaintext
- **Automatic clipboard copy** on macOS, Linux, and Windows
- **URL-safe base64** support via `--url-safe` flag
- **Zero dependencies** — Python stdlib only, no pip install needed at runtime
- **Cross-platform** — same command on every OS
- **Privacy-first** — no logging, no network calls, in-memory only
- **Pipe-friendly** — works with stdin for scripting workflows

## Installation

```bash
pip install b64-clip
```

Or run directly (no install needed):

```bash
python3 b64_clip.py encode "hello world"
```

## Requirements

- **Python:** 3.11+
- **Clipboard tools (optional):** `xclip` on Linux (`sudo apt install xclip`), `pbcopy` on macOS (built-in), `clip.exe` on Windows (built-in)

## Support

- **Contact:** eric@ericjoye.com
- **GitHub:** https://github.com/ericjoye/b64-clip
- **Issues:** https://github.com/ericjoye/b64-clip/issues
- **License:** MIT

## Keywords

base64, clipboard, cli, encode, decode, developer-tools, devops, terminal, command-line, cross-platform, zero-dependencies, python, pip, automation, productivity
