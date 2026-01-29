# GitHub Pages Site Audit Report

**Date:** 2026-01-27
**Scope:** Full review of docs/ directory for the Methods and Algorithms MSc course

## Executive Summary

The GitHub Pages site is **well-built and functional** with no broken internal links or missing assets. 1 critical UX issue, several warnings, and useful improvements identified.

**Scores:** Links 100% | Images 100% | PDFs 100% | Structure 95% | Content 95%

---

## CRITICAL Issues (1)

### C1: No back-navigation from slide decks to index.html
- **Location:** All 12 slide HTML files (docs/slides/L0X_*.html)
- **Impact:** Users viewing slides have no way to return to the main page
- **Fix:** Add a "Back to Index" button/link in the slide header or footer

---

## WARNING Issues (6)

### W1: Unpinned CDN version for chalkboard plugin
- All 12 slide HTMLs use `reveal.js-plugins@latest` instead of a pinned version
- Risk: Plugin could break silently on upstream update

### W2: Generic slide HTML titles
- Titles read "L1: overview" instead of "L01: Introduction & Linear Regression - Overview"
- Impact: Poor browser tab/bookmark identification

### W3: Dead code in main.js
- `buildDynamicToc()` function (lines 114-135) defined but never called

### W4: Section JSON files are orphaned
- All 18 files in docs/slides/sections/ are never loaded by any HTML or JS
- They appear to be unused artifacts from a planned feature

### W5: L02_deepdive.json missing slide 34
- JSON defines slides 1-33 but the actual presentation has 34 slides

### W6: Quiz title inconsistency
- index.html uses thematic names ("Regression Methods")
- manifest.json uses topic names ("Linear & Logistic Regression")
- Same quizzes, different labels -- potentially confusing

---

## INFO Observations (5)

### I1: L03 title varies in manifest.json
- manifest.json: "K-Nearest Neighbours & K-Means"
- Everywhere else: "KNN & K-Means"
- Minor inconsistency, not user-facing

### I2: 6 legacy TopicName.json files
- docs/slides/sections/L0X_TopicName.json files have minimal 3-section structure
- Appear to be placeholders or legacy files

### I3: Potential layout conflict in style.css
- `margin-left: var(--sidebar-width)` on .main-content may cause double offset with CSS grid

### I4: 18 external links need manual verification
- 6 Colab notebook links, 6 GitHub dataset links, 3 GitHub content links, 3 CDN links
- All point to Digital-AI-Finance/methods-algorithms repo

### I5: No .nojekyll file
- GitHub Pages will process files through Jekyll by default
- Not causing issues currently but could in the future

---

## Verified PASS (Full List)

| Check | Result |
|-------|--------|
| All 12 slide HTML files exist | PASS |
| All 12 PDF files exist (113K-379K) | PASS |
| All 400+ image references resolve | PASS |
| All internal links in index.html work | PASS |
| All 26 anchor links match targets | PASS |
| Navigation consistent (sidebar, mobile, TOC) | PASS |
| CDN versions consistent (Reveal.js 4.5.0) | PASS |
| Reveal.js config identical across files | PASS |
| Custom theme (ml-theme.css) correctly linked | PASS |
| No placeholder content (TODO/TBD/Lorem) | PASS |
| Dates consistent (January 2026) | PASS |
| Course metadata consistent | PASS |
| Topic descriptions accurate | PASS |
| All 18 section JSONs valid syntax | PASS |

---

## Recommended Fix Priority

| Priority | Issue | Effort |
|----------|-------|--------|
| HIGH | C1: Add back-navigation to slides | Small (12 files, template change) |
| HIGH | W1: Pin chalkboard plugin version | Trivial |
| MEDIUM | W2: Improve slide HTML titles | Small |
| MEDIUM | W6: Align quiz titles | Trivial |
| LOW | W3: Remove dead code in main.js | Trivial |
| LOW | W4: Clean up orphaned JSON files | Small |
| LOW | W5: Fix L02_deepdive.json slide count | Trivial |
