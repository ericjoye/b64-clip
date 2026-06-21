# BRIEF: b64-clip

## Title
b64-clip — Base64 encode/decode with clipboard, zero dependencies

## One-liner
A zero-dependency CLI tool that base64-encodes or decodes any input (stdin, string arg, or file) and copies the result to your clipboard automatically.

## Target user
Developers and DevOps engineers who work with base64 daily — encoding auth tokens, config values, data URIs, SAML assertions, Kubernetes secrets, and certificate data.

## Problem
Base64 encoding/decoding is a daily task for developers, but the current workflow is painful:
- `echo "foo" | base64` works on Linux but macOS uses `base64` with different flags (`-e` vs no flag, `-d` vs `-D`)
- No built-in clipboard integration — you encode, then manually select and copy
- Online base64 tools are a privacy risk (you paste secrets into random websites)
- Writing a quick Python one-liner works but you have to remember the `import base64; print(base64.b64encode(b"...").decode())` syntax every time

## MVP scope (4 features)
1. **Encode**: `b64-clip encode "hello world"` → prints `aGVsbG8gd29ybGQ=` and copies to clipboard
2. **Decode**: `b64-clip decode "aGVsbG8gd29ybGQ="` → prints `hello world` and copies to clipboard
3. **File input**: `b64-clip encode --file cert.pem` → base64-encodes the file contents
4. **Stdin pipe**: `cat secret.txt | b64-clip encode` → reads from stdin when no arg given

## Tech approach
- **Language**: Python 3.11+ (stdlib only: `base64`, `argparse`, `subprocess` for clipboard)
- **Clipboard**: `pbcopy` on macOS, `xclip -selection clipboard` on Linux, `clip.exe` on Windows (WSL)
- **Distribution**: Single-file script, installable via `pip install b64-clip` (PyPI) or `curl | bash`
- **No external dependencies** — only Python stdlib

## Risks
1. **Clipboard tool availability**: `xclip` may not be installed on minimal Linux systems — mitigate by printing a clear warning and still outputting to stdout
2. **Cross-platform differences**: macOS/Linux/Windows all have different base64 CLI flags — this tool abstracts that away, but clipboard integration needs per-OS handling
3. **Existing alternatives**: `base64` CLI exists on all platforms — the value prop is clipboard integration + cross-platform consistency, which needs to be obvious in marketing
4. **Security perception**: Users may worry about clipboard history — document that nothing is logged or stored

## Definition of done for the MVP
- [ ] `b64-clip encode <string>` works on Linux (WSL), macOS, and Windows
- [ ] `b64-clip decode <string>` works on all three platforms
- [ ] `--file` flag reads and encodes/decodes file contents
- [ ] Stdin pipe mode works (`echo "test" | b64-clip encode`)
- [ ] Clipboard copy works on Linux (xclip), macOS (pbcopy), Windows (clip.exe)
- [ ] Falls back gracefully to stdout-only if clipboard tool is missing
- [ ] Published to PyPI as `b64-clip`
- [ ] README with install instructions and examples
