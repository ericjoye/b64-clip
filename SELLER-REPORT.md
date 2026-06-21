# SELLER-REPORT: PyPI / GitHub Publish Plan — b64-clip

**Product:** b64-clip — Base64 encode/decode CLI with clipboard, zero dependencies
**Slug:** b64-clip
**Date:** 2026-06-20
**QA Status:** PASS (15/15 tests)

---

## Publishing Summary

- **PyPI Package Name:** `b64-clip` (v1.0.0)
- **GitHub Repo:** `github.com/ericjoye/b64-clip`
- **Build System:** setuptools (pyproject.toml ready)
- **Entry Point:** `b64_clip:main`
- **Blockers:** None — fully ready to publish

---

## PyPI Publishing Steps

1. Ensure PyPI account exists (https://pypi.org/account/register/)
2. Ensure API token is configured in `~/.pypirc` or env vars
3. Build:
   ```
   cd ~/businesses/b64-clip/
   python3 -m build
   ```
4. Upload:
   ```
   python3 -m twine upload dist/*
   ```
5. Verify: https://pypi.org/project/b64-clip/

---

## GitHub Repository Steps

1. Create public repo at https://github.com/new — name: `b64-clip`
2. Push code:
   ```
   cd ~/businesses/b64-clip/
   git init
   git add .
   git commit -m "Initial release"
   git remote add origin git@github.com:ericjoye/b64-clip.git
   git branch -M main
   git push -u origin main
   ```
3. Add MIT license file
4. Enable Issues in repo settings

---

## Marketing Launch

- **Hacker News:** "Show HN: b64-clip — Base64 encode/decode with clipboard, zero deps"
- **Reddit:** r/Python, r/commandline, r/devops
- **Twitter:** pip install b64-clip + demo GIF

---

## Success Metrics (30 days)

- PyPI downloads: 100+
- GitHub stars: 20+
- HN upvotes: 25+
