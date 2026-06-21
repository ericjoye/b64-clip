# Pricing — b64-clip

## Model: Free & Open Source (MIT)

b64-clip is free, open source, and always will be. The core tool — encode, decode, clipboard, file input, stdin pipes, URL-safe mode — is fully functional at no cost.

## Rationale

- **PyPI distribution**: Python developers expect CLI tools to be free. Charging for a single-purpose CLI tool would kill adoption.
- **Trust & security**: Open source builds trust. Users handling secrets (auth tokens, certificates) need to verify the code does nothing shady.
- **Ecosystem play**: b64-clip is a developer utility that drives awareness of the broader product portfolio.

## Future monetization (optional)

If demand warrants, a **b64-clip-pro** could add:
- Batch file processing (`--batch *.pem`)
- Base64url / custom alphabet support
- Clipboard history (last N operations)
- Shell completions (bash/zsh/fish)
- TUI mode with interactive prompt

But the core tool stays free. Pro would be a separate package for power users only.
