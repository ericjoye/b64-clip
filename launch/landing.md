# Landing Page — b64-clip

## Headline

**b64-clip: Base64 in your terminal. In your clipboard. Zero dependencies.**

## Subhead

Stop pasting secrets into random websites. Stop fighting with `base64` flag differences across macOS and Linux. b64-clip encodes or decodes any input and copies the result to your clipboard automatically — one command, every platform, no install hassle.

## Benefit Bullets

- **Clipboard-first workflow** — Result is copied to your clipboard instantly on macOS, Linux, and Windows. No select, no Ctrl+C, just paste and go.
- **Zero dependencies, zero drama** — Python stdlib only. `pip install b64-clip` and you're done. No virtualenv, no requirements.txt, no node_modules.
- **Pipes, files, strings — it just works** — Pass a string argument, pipe from stdin, or use `--file` for cert.pem and config files. Same command every time.

## CTA

```bash
pip install b64-clip
```

Then try it:

```bash
b64-clip encode "hello world"
# → aGVsbG8gd29ybGQ= (already in your clipboard)
```

[View on PyPI](https://pypi.org/project/b64-clip/) · [GitHub](https://github.com/ericjoye/b64-clip)
