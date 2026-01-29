# Plan: GitHub Pages Site Review

## Context

### Original Request
Review the entire GitHub Pages site for the MSc Data Science "Methods and Algorithms" course to verify content, links, navigation, structure, and overall quality.

### Interview Summary
Direct planning mode (ralplan) - context pre-gathered by orchestrator.

### Research Findings

**Site URL:** https://digital-ai-finance.github.io/methods-algorithms/

**Site Inventory (verified from filesystem):**
- `docs/index.html` - Main landing page, wiki-style 3-column layout (sidebar + content + right TOC)
- `docs/css/style.css` + `docs/js/main.js` - Styling and navigation JS
- 12 slide HTML files: `docs/slides/L0{1-6}_{overview,deepdive}.html` (Reveal.js 4.5.0)
- 12 PDFs: `docs/slides/pdf/L0{1-6}_{overview,deepdive}.pdf`
- 18 section JSONs: `docs/slides/sections/` (3 per topic: overview, deepdive, TopicName)
- `docs/slides/css/ml-theme.css` - Reveal.js custom theme
- 400+ PNG images in `docs/slides/images/`

**External Dependencies:**
- CDN: Reveal.js 4.5.0 (unpkg.com), plugins (menu, chalkboard)
- CDN: Font Awesome 6.4.0 (cdnjs.cloudflare.com)
- CDN: Google Fonts (Inter)
- GitHub: Colab notebook links, dataset downloads, capstone materials (Digital-AI-Finance/methods-algorithms)

**Key Observations from index.html:**
- Stats claim: 6 lectures, 12 slide decks, 6 notebooks, 45 quiz questions
- Each lecture section has 6 material cards: overview HTML, deepdive HTML, overview PDF, deepdive PDF, Colab notebook, dataset
- Slide count claims vary per topic (e.g., L01 overview "10 slides", L01 deepdive "35 slides", L05 deepdive "24 slides")
- Quizzes section: 3 quizzes x 15 questions = 45 total (matches stat card)
- Capstone links point to GitHub blob/raw URLs
- Footer and sidebar both say "Last updated: January 2026"
- L06 dataset is JSON (text_corpus_synthetic.json), all others are CSV

---

## Work Objectives

### Core Objective
Produce a comprehensive audit report identifying all issues across the GH Pages site, categorized by severity.

### Deliverables
1. Audit report at `.omc/reports/gh-pages-audit.md` with categorized findings (CRITICAL / WARNING / INFO)

### Definition of Done
- Every internal link in index.html verified against actual files
- Every image reference in all 12 slide HTMLs verified against filesystem
- All 18 JSON files validated (parseable, correct structure)
- All 12 PDFs confirmed present and non-empty
- Content consistency checked across all pages
- Slide count claims verified against actual content
- Report written with actionable findings

---

## Guardrails

### Must Have
- Check every internal link resolves to an existing file
- Validate all JSON files parse correctly
- Verify topic names are consistent across sidebar, TOC, sections, and slide titles
- Check external link URL patterns are well-formed and consistent
- Verify slide count claims vs actual slide images

### Must NOT Have
- Modifying any source files (read-only audit)
- Testing live HTTP responses (local file checks only)
- Fixing any issues found (report only)
- Deleting any assets

---

## Task Flow

```
[T1: index.html Link Audit]  ----+
[T2: Slide HTML Image Audit] ----+
[T3: Section JSON Validation] ---+---> [T7: Compile Report]
[T4: Slide HTML Structure]   ----+         |
[T5: Content Consistency]     ----+         v
[T6: CSS/JS Review]           ----+   .omc/reports/gh-pages-audit.md
[T7a: PDF Verification]       ----+
```

T1-T6 and T7a are all independent and run in parallel. T7 depends on all others.

---

## Detailed TODOs

### T1: index.html Internal Link Audit
**Priority:** HIGH | **Agent:** `explore-medium` (sonnet) | **Dependencies:** None

**Instructions:**
1. Read `docs/index.html` and extract ALL `href` values
2. Categorize: local links vs external links vs anchor links
3. For each local link (`slides/*.html`, `slides/pdf/*.pdf`): verify file exists under `docs/`
4. For each anchor link (`#home`, `#l01`-`#l06`, `#quizzes`, `#capstone`): verify matching `id` attribute exists in the HTML
5. For external links: verify URL patterns are well-formed (correct GitHub org/repo, correct branch)
6. Verify the stat card numbers: 6 lectures, 12 slide decks, 6 notebooks, 45 quiz questions
7. Check that dataset filenames in download links are plausible (housing_synthetic.csv, credit_synthetic.csv, customers_synthetic.csv, transactions_synthetic.csv, portfolio_synthetic.csv, text_corpus_synthetic.json)

**Acceptance Criteria:**
- Complete list of all links with pass/fail status
- Any broken internal links flagged as CRITICAL
- Any malformed external URLs flagged as WARNING

---

### T2: Slide HTML Image Reference Audit
**Priority:** HIGH | **Agent:** `explore-medium` (sonnet) | **Dependencies:** None

**Instructions:**
1. For each of the 12 slide HTML files in `docs/slides/`:
   - Extract all `<img src="...">` references
   - Resolve each path relative to `docs/slides/`
   - Verify each referenced image file exists on the filesystem
2. Count actual slide images per presentation folder in `docs/slides/images/`
3. Compare actual image counts to the slide counts claimed in `docs/index.html`:
   - L01 overview: claimed 10 | L01 deepdive: claimed 35
   - L02 overview: claimed 10 | L02 deepdive: claimed 34
   - L03 overview: claimed 10 | L03 deepdive: claimed 30
   - L04 overview: claimed 10 | L04 deepdive: claimed 30
   - L05 overview: claimed 10 | L05 deepdive: claimed 24
   - L06 overview: claimed 10 | L06 deepdive: claimed 26
4. Identify orphaned images (on disk but not referenced by any HTML)

**Acceptance Criteria:**
- Missing images flagged as CRITICAL
- Slide count mismatches flagged as WARNING
- Orphaned images flagged as INFO

---

### T3: Section JSON Validation
**Priority:** MEDIUM | **Agent:** `explore` (haiku) | **Dependencies:** None

**Instructions:**
1. Read and parse all 18 JSON files in `docs/slides/sections/`
2. Verify each is valid JSON
3. Check expected structure: `sections` array with objects having `name` and `slides` fields
4. Determine if the 3 types per topic (overview, deepdive, TopicName) serve different purposes
5. Check if any JavaScript in the slide HTML files actually loads these JSONs

**Acceptance Criteria:**
- Invalid JSON flagged as CRITICAL
- Unused/orphaned JSONs flagged as INFO
- Structure inconsistencies flagged as WARNING

---

### T4: Slide HTML Structure and Navigation
**Priority:** MEDIUM | **Agent:** `explore-medium` (sonnet) | **Dependencies:** None

**Instructions:**
1. For each of 12 slide HTML files, check:
   - `<title>` tag is descriptive (currently L01 says "L1: overview" - note the inconsistent numbering)
   - Reveal.js CDN URLs are valid and consistent across all files
   - ml-theme.css reference is correct (`css/ml-theme.css` relative to slides/)
   - No hardcoded `localhost` or `file://` URLs
   - Plugin configuration (menu, chalkboard, spotlight) is present
2. Check for any back-to-index navigation link in presentations

**Acceptance Criteria:**
- Title tag inconsistencies flagged as WARNING
- Missing/broken CDN references flagged as CRITICAL
- Missing back-navigation flagged as INFO

---

### T5: Content Consistency Audit
**Priority:** HIGH | **Agent:** `explore-medium` (sonnet) | **Dependencies:** None

**Instructions:**
1. Extract topic names from every location they appear and compare:
   - Left sidebar nav items
   - Mobile TOC links
   - Right TOC sidebar links
   - Section `<h2>` headers
   - Slide HTML `<title>` tags
2. Known inconsistency to verify: sidebar says "Linear Regression" but section says "Introduction & Linear Regression"
3. Verify quiz topic groupings make sense:
   - Quiz 1: Linear Regression + Logistic Regression
   - Quiz 2: KNN/K-Means + Random Forests
   - Quiz 3: PCA/t-SNE + Embeddings/RL
4. Verify capstone links use correct GitHub paths (`capstone/specification.md`, `capstone/report_template.tex`, `rubrics/capstone_rubric.md`)
5. Check "Last updated" date appears in both sidebar footer and page footer and they match

**Acceptance Criteria:**
- Naming inconsistencies documented as WARNING
- Quiz grouping errors flagged as CRITICAL
- Date mismatches flagged as WARNING

---

### T6: CSS/JS Functionality Review
**Priority:** LOW | **Agent:** `explore` (haiku) | **Dependencies:** None

**Instructions:**
1. Read `docs/css/style.css` - check for any `url()` references to missing assets
2. Read `docs/js/main.js` - check DOM selectors reference elements that exist in index.html
3. Read `docs/slides/css/ml-theme.css` - check for broken references
4. Verify the JS handles: sidebar nav active state, smooth scrolling, mobile menu toggle, scroll spy for TOC

**Acceptance Criteria:**
- Broken asset references flagged as CRITICAL
- Missing DOM element references flagged as WARNING

---

### T7a: PDF Presence Verification
**Priority:** HIGH | **Agent:** `explore` (haiku) | **Dependencies:** None

**Instructions:**
1. Confirm all 12 PDFs exist in `docs/slides/pdf/`
2. Check file sizes are non-zero (not empty placeholders)
3. List: L01-L06 overview + deepdive = 12 total

**Acceptance Criteria:**
- Missing PDFs flagged as CRITICAL
- Empty (0-byte) PDFs flagged as CRITICAL

---

### T7: Compile Final Report
**Priority:** HIGH | **Agent:** `executor` (sonnet) | **Dependencies:** T1-T6, T7a

**Instructions:**
1. Collect findings from all previous tasks
2. Categorize each issue:
   - **CRITICAL:** Broken links, missing files, invalid JSON, empty PDFs
   - **WARNING:** Content inconsistencies, slide count mismatches, naming differences
   - **INFO:** Orphaned assets, enhancement suggestions, minor observations
3. Write report to `.omc/reports/gh-pages-audit.md` with:
   - Executive summary (overall health score)
   - Findings by category
   - Detailed issue list with file paths
   - Recommendations

**Acceptance Criteria:**
- Report saved to `.omc/reports/gh-pages-audit.md`
- All findings categorized with evidence
- Zero false positives

---

## Commit Strategy

No commits. This is a read-only audit. Output goes to `.omc/reports/gh-pages-audit.md`.

---

## Success Criteria

| Criterion | Target |
|-----------|--------|
| Internal links checked | All 30+ local links |
| External links checked | All 15+ external URLs |
| Slide count claims verified | All 12 presentations |
| JSON files validated | All 18 files |
| PDFs confirmed present | All 12 files |
| Image references verified | All 12 HTML files |
| Content consistency checked | All 6 locations per topic |
| Report generated | `.omc/reports/gh-pages-audit.md` exists |
