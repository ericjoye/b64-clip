# Privacy Policy — b64-clip

**Last updated:** June 20, 2026

## Overview

b64-clip ("we", "our", "the tool") is a command-line utility for base64 encoding and decoding. It processes data in memory and copies results to your clipboard.

## Data Collection

**b64-clip does NOT collect, store, or transmit any data.**

When you use b64-clip:

- **No data is logged or stored.** All encoding and decoding happens in memory. The tool does not write temporary files, logs, or databases.
- **No network calls.** b64-clip does not make any network requests. It operates entirely offline.
- **No telemetry.** There is no usage tracking, analytics, or telemetry of any kind.
- **No accounts.** There is no signup, login, or user account system.

## How It Works

b64-clip takes input from the command line arguments, a file, or stdin, performs base64 encoding or decoding using Python's standard library, and outputs the result to stdout and your system clipboard. Your data is never written to disk by the tool.

## Clipboard Access

b64-clip copies results to your system clipboard for convenience. This uses your operating system's native clipboard mechanism (`pbcopy` on macOS, `xclip` on Linux, `clip.exe` on Windows). The tool does not read from the clipboard — it only writes to it.

## Open Source

b64-clip is open source under the MIT license. It has zero runtime dependencies — it uses only Python 3.11+ standard library modules.

## Changes to This Policy

We may update this privacy policy from time to time. Any changes will be reflected in the project's source code repository.

## Contact

If you have questions about this privacy policy, contact us at: [YOUR EMAIL ADDRESS]
