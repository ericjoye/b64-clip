# BUILD-REPORT: b64-clip

## What was built

A zero-dependency CLI tool that base64-encodes or decodes any input (string arg,
file, or stdin pipe) and copies the result to the clipboard automatically.

## File layout

```
b64-clip/
  b64_clip.py       # Main script — single file, stdlib only (~130 lines)
  pyproject.toml    # PyPI packaging config (setuptools)
  README.md         # Install instructions and usage examples
  BUILD-REPORT.md   # This file
  .venv/            # Local venv for testing
```

## How to run

### Direct (no install)
```bash
python3 b64_clip.py encode "hello world"
python3 b64_clip.py decode "aGVsbG8gd29ybGQ="
```

### Installed via pip
```bash
pip install -e .
b64-clip encode "hello world"
b64-clip decode "aGVsbG8gd29ybGQ="
```

### From PyPI (after publish)
```bash
pip install b64-clip
b64-clip encode "hello world"
```

## Features implemented (all 4 MVP features)

1. **Encode string**: `b64-clip encode "hello world"` → prints base64 + copies to clipboard
2. **Decode string**: `b64-clip decode "aGVsbG8gd29ybGQ="` → prints plaintext + copies
3. **File input**: `b64-clip encode --file cert.pem` → encodes file contents
4. **Stdin pipe**: `echo "test" | b64-clip encode` → reads from stdin

## Additional features

- **URL-safe base64 decode**: `--url-safe` flag + auto-detection of URL-safe alphabet
- **Cross-platform clipboard**: pbcopy (macOS), xclip/wl-copy (Linux), clip.exe (Windows)
- **Graceful fallback**: If clipboard tool is missing, prints warning to stderr and still outputs to stdout
- **Error handling**: Clear error messages for invalid base64, missing files, no input

## Test results (manual)

| Test | Result |
|------|--------|
| Encode string | PASS — `hello world` → `aGVsbG8gd29ybGQ=` |
| Decode string | PASS — `aGVsbG8gd29ybGQ=` → `hello world` |
| Stdin pipe | PASS — `echo "pipe test" \| b64-clip encode` works |
| File encode | PASS — `--file b64_clip.py` encodes file contents |
| Roundtrip | PASS → encode then decode returns original input |
| URL-safe decode | PASS — auto-detects and decodes URL-safe base64 |
| Invalid input | PASS — clear error message, exit code 1 |
| pip install | PASS — `pip install -e .` works, CLI entry point functional |
| Help output | PASS — `--help` shows encode/decode subcommands |

## Known gaps

- **Clipboard on WSL**: No xclip installed in this environment — prints warning.
  Users need `sudo apt install xclip` for clipboard support on Linux/WSL.
- **PyPI publish**: Not published yet — `pyproject.toml` is ready for `twine upload`
  but the actual `twine upload dist/*` step requires PyPI credentials.
- **No unit tests**: Manual testing only. A TESTER should add pytest tests.
- **Binary file decode**: Decoding binary files (e.g. images) will fail at `.decode()`
  since not all bytes are valid UTF-8. This is acceptable for an MVP focused on
  text/config encoding.
