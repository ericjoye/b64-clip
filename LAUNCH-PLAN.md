# LAUNCH PLAN: b64-clip

**Product:** b64-clip — Base64 encode/decode CLI with clipboard, zero dependencies
**Slug:** b64-clip
**Date:** 2026-06-20
**QA Status:** PASS (15/15 tests, 7/8 DoD criteria met)

---

## Launch Channels

### 1. PyPI (Primary)
- **What:** Publish the package to PyPI so `pip install b64-clip` works
- **Why:** This is the main distribution channel for Python CLI tools
- **Status:** pyproject.toml is ready; needs credentials and publish

### 2. GitHub Repository
- **What:** Public repo with README, MIT license, and source code
- **Why:** Drives discoverability, builds trust (open source), enables contributions
- **Status:** Code is ready; needs repo creation and push

### 3. Reddit
- **What:** Post to r/Python, r/commandline, r/devops, r/webdev
- **Why:** Target audience (developers/DevOps) hangs out here
- **Status:** Post copy needed (see below)

### 4. Hacker News
- **What:** "Show HN: b64-clip — Base64 encode/decode with clipboard, zero deps"
- **Why:** High-signal audience for developer tools
- **Status:** Post copy ready (use landing page headline + short description)

### 5. Twitter/X
- **What:** Announce with a short demo GIF or terminal recording
- **Why:** Developer tool discovery happens here
- **Status:** Needs a short demo clip (asciinema or similar)

### 6. Python Discord / Dev Communities
- **What:** Share in #showcase or #python channels
- **Why:** Direct access to Python developers
- **Status:** Copy ready

---

## First-Week Plan

### Day 1 (Launch Day)
1. **Publish to PyPI** — `twine upload dist/*` (human action required)
2. **Create GitHub repo** — Push code, add MIT license, enable Issues (human action required)
3. **Post to Reddit** — r/Python and r/commandline
4. **Post to Hacker News** — "Show HN" format

### Day 2
5. **Twitter/X announcement** — With terminal demo GIF
6. **Python Discord** — Share in showcase channel
7. **Monitor** — Check PyPI download stats, GitHub stars, Reddit comments

### Day 3-4
8. **Respond to feedback** — Answer questions on Reddit, HN, GitHub Issues
9. **Fix any reported bugs** — Quick turnaround builds trust

### Day 5-7
10. **Write a blog post** — "Why I built b64-clip" (dev.to or personal blog)
11. **Submit to Python newsletters** — Python Weekly, PyCoder's Weekly
12. **Evaluate traction** — Downloads, stars, feedback → decide on next steps

---

## Human Actions Required (EXACT checklist)

These are the real-world actions that must be done by a human. The agent cannot perform these.

### PyPI Publishing
- [ ] Create PyPI account at https://pypi.org/account/register/ (if not exists)
- [ ] Create API token at https://pypi.org/manage/account/token/
- [ ] Configure `~/.pypirc` with the token OR set `TWINE_USERNAME=__token__` and `TWINE_PASSWORD=<token>`
- [ ] Run `python3 -m build` in `~/businesses/b64-clip/`
- [ ] Run `twine upload dist/*`
- [ ] Verify at https://pypi.org/project/b64-clip/

### GitHub Repository
- [ ] Create public repo at https://github.com/new (name: `b64-clip`)
- [ ] `cd ~/businesses/b64-clip && git init && git add . && git commit -m "Initial commit"`
- [ ] `git remote add origin git@github.com:ericjoye/b64-clip.git`
- [ ] `git push -u origin main`
- [ ] Add MIT license file
- [ ] Enable Issues in repo settings

### Reddit Posts
- [ ] Post to r/Python: title "b64-clip — Base64 encode/decode CLI with clipboard, zero dependencies" + link to PyPI/GitHub
- [ ] Post to r/commandline: same format
- [ ] Post to r/devops: emphasize the cross-platform consistency angle

### Hacker News
- [ ] Submit "Show HN: b64-clip — Base64 encode/decode with clipboard, zero deps" at https://news.ycombinator.com/submit
- [ ] URL: GitHub repo link
- [ ] Comment with the one-liner and install command

### Twitter/X
- [ ] Create account or use existing
- [ ] Post: "b64-clip is live on PyPI 🎉 Base64 encode/decode with automatic clipboard copy. Zero dependencies. `pip install b64-clip` [link]"
- [ ] Attach terminal demo GIF (optional but recommended)

### Newsletter Submissions
- [ ] Submit to Python Weekly: https://www.pythonweekly.com/submit/
- [ ] Submit to PyCoder's Weekly: https://pycoders.com/submit-link

---

## Success Metrics (First 2 Weeks)

| Metric | Target |
|--------|--------|
| PyPI downloads | 100+ |
| GitHub stars | 20+ |
| Reddit upvotes (combined) | 50+ |
| Hacker News points | 25+ |
| Issues/feedback | < 5 bugs reported |

---

## Assets Ready

- `launch/landing.md` — Headline, subhead, 3 benefit bullets, CTA
- `launch/store-listing.md` — PyPI name, short + long description, keywords
- `launch/pricing.md` — Free/open-source model with optional pro tier concept
- `README.md` — Already in repo, install instructions and examples
- `pyproject.toml` — Ready for PyPI publish
