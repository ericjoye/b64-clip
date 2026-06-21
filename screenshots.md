# Screenshots — b64-clip

**Product:** b64-clip — Base64 encode/decode with clipboard, zero dependencies.

**Type:** CLI Tool (Python)

---

## Screenshot 1: Main Interface — Terminal Hero Shot

**What to capture:** A terminal window showing the basic encode/decode workflow. Clean, dark terminal with syntax-highlighted output showing the tool in action.

**Terminal Output Mockup:**

```
$ b64-clip encode "hello world"
aGVsbG8gd29ybGQ=
✓ Copied to clipboard

$ b64-clip decode "aGVsbG8gd29ybGQ="
hello world
✓ Copied to clipboard

$ b64-clip encode --file cert.pem
LS0tLS1CRUdJTi...
✓ Copied to clipboard (2,048 chars)

$ echo "test" | b64-clip encode
dGVzdA==
✓ Copied to clipboard
```

---

## Screenshot 2: Key Feature — Encoding Auth Tokens

**What to capture:** Terminal showing encoding of a realistic auth token/header value, demonstrating the primary use case.

**Terminal Output Mockup:**

```
$ b64-clip encode "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
QXV0aG9yaXphdGlvbjogQmVhcmVyIGV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOQ==
✓ Copied to clipboard

$ b64-clip encode "user:password@host"
dXNlcjpwYXNzd29yZEBob3N0
✓ Copied to clipboard

$ b64-clip decode --url-safe "PDw_Pz4-"
<<??>>
✓ Copied to clipboard
```

---

## Screenshot 3: Help & Options

**What to capture:** Terminal showing the `--help` output with all available options.

**Terminal Output Mockup:**

```
$ b64-clip --help
Usage: b64-clip <command> [options]

Commands:
  encode    Encode input to base64
  Decode    Decode base64 to plaintext

Options:
  --file PATH       Read input from file
  --url-safe        Use URL-safe base64 alphabet
  --help            Show this help message

Input sources (in priority order):
  1. --file PATH    Read from file
  2. Positional arg  Use string argument
  3. stdin          Pipe from stdin

Examples:
  b64-clip encode "hello world"
  b64-clip decode "aGVsbG8gd29ybGQ="
  b64-clip encode --file cert.pem
  echo "test" | b64-clip encode
  b64-clip decode --url-safe "PDw_Pz4-"

Clipboard support: macOS (pbcopy), Linux (xclip), Windows (clip.exe)
```

---

## Screenshot 4: Results — Batch Processing

**What to capture:** Terminal showing batch encoding of multiple values, demonstrating pipe mode and clipboard integration.

**Terminal Output Mockup:**

$ cat secrets.txt | while read line; do
>   echo "$(b64-clip encode "$line")"
> done
aGVsbG8gd29ybGQ=
c2VjcmV0LXBhc3N3b3Jk
YXBpLWtleS0xMjM0NTY3OA==

$ b64-clip encode "postgres://user:pass@localhost:5432/mydb"
cG9zdGdyZXM6Ly91c2VyOnBhc3NAbG9jYWxob3N0OjU0MzIvbXlkYg==
✓ Copied to clipboard

$ b64-clip encode "-----BEGIN CERTIFICATE-----
> MIIDXTCCAkWgAwIBAgIJAKL...
> -----END CERTIFICATE-----"
LS0tLS1CRUdJTi...
✓ Copied to clipboard (1,856 chars)
```

---

## Notes for Actual Screenshots

1. **Use a dark terminal theme** (e.g., Dracula, One Dark) for visual appeal
2. **Show the clipboard confirmation** (✓ Copied to clipboard) — this is a key differentiator
3. **Use realistic data:** auth tokens, database URLs, certificate snippets
4. **Show the zero-dependency angle:** `python3 b64_clip.py encode "hello"` (no pip install needed)
5. **Multi-line input** for certificates/files shows the tool handles complex data
6. **Keep terminal clean** — no extra noise, just the command and output
7. **Font:** Use a monospace font like JetBrains Mono or Fira Code
8. **Window title bar** should show the shell name and current directory
