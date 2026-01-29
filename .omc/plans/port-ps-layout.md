# Plan: Port P&S Layout to Methods & Algorithms GitHub Pages

## Context

### Original Request
Port the Probability & Statistics GitHub Pages layout (compact GitHub-style, interactive quizzes, chart galleries) to the Methods & Algorithms site, replacing the current wiki-style 3-column layout.

### Research Findings

**P&S Source** (`D:\Joerg\Research\slides\Probability_Statistics\`):
- Single `index.html` with ~78 lines of inline minified CSS
- Layout: dark nav (#24292e), sticky sidebar (180px) with `<details>` sections, 6-column lesson card grid, chart thumbnail gallery (`cgrid`), inline quiz links
- 17 interactive quiz HTML files in `quiz/` folder -- each self-contained with inline CSS+JS, JSON question data embedded in `<script>`, KaTeX for math
- Quiz features: 3-column question cards, MCQ with instant feedback, progress bar, score tracking, grading (A-F), "Next" button pagination (loads 3 questions at a time)
- Chart galleries use `thumb.png` thumbnails linking to PDFs

**M&A Target** (`D:\Joerg\Research\slides\Methods_and_Algorithms\docs\`):
- Wiki 3-column layout: `index.html` + `css/style.css` (565 lines) + `js/main.js` (109 lines)
- 6 lectures (L01-L06) with material cards (slides, PDFs, notebooks, datasets)
- 3 Moodle XML quiz files in `quizzes/` (15 questions each, 45 total) -- static quiz cards, no interactivity
- Reveal.js slide decks in `docs/slides/` -- MUST remain unchanged
- Chart PNG images already exist at `docs/slides/images/L0X_TopicName/XX_chart_name.png`
- 49 chart.py files across L01-L06, charts output `chart.pdf` in source folders

## Work Objectives

### Core Objective
Replace the M&A wiki layout with the P&S compact GitHub-style layout, add interactive quizzes, and add chart thumbnail galleries -- all adapted to M&A's 6-lecture structure and ML color palette.

### Deliverables
1. Redesigned `docs/index.html` with P&S-style layout
2. New `docs/quiz/` folder with 3 interactive quiz HTML files
3. Chart gallery sections on index page using existing PNG images as thumbnails
4. Reveal.js slides untouched

### Definition of Done
- index.html renders with dark nav, sticky sidebar, lesson cards, chart galleries, quiz links
- 3 quiz HTML files are interactive (MCQ, feedback, scoring, grading)
- All existing material links (slides, PDFs, notebooks, datasets, capstone) preserved
- Reveal.js slide decks still load from `docs/slides/`
- Site works on GitHub Pages (static files only)

## Must Have
- P&S compact layout adapted for 6 lectures
- Interactive quizzes converted from Moodle XML
- Chart thumbnail galleries per lecture
- All current material links preserved
- ML color palette (#3333B2, #0066CC, #FF7F0E, #2CA02C, #D62728)
- Mobile responsive (P&S already has media queries)
- KaTeX support for math in quiz questions

## Must NOT Have
- Changes to `docs/slides/` (Reveal.js decks)
- External CSS frameworks (keep inline like P&S or minimal external)
- Backend/server-side code
- Changes to source `slides/` folder chart.py files
- New quiz questions beyond the 45 in the XML files

## Architecture Decisions

### Decision 1: Inline CSS (like P&S) vs External CSS
**Decision: Inline CSS in index.html, inline CSS in each quiz HTML.**
- Matches P&S pattern exactly
- Eliminates external file dependencies
- Each quiz file is fully self-contained (portable)
- Delete `docs/css/style.css` and `docs/js/main.js` after migration

### Decision 2: Chart Thumbnails
**Decision: Reuse existing PNG images from `docs/slides/images/`.**
- Chart PNGs already exist at `docs/slides/images/L0X_TopicName/XX_chart_name.png` for L01-L05
- These are full-size PNGs from the Reveal.js slide build -- use directly as thumbnails (browser scales via CSS `object-fit: contain`)
- For L06 (if images missing), generate PNGs by running chart.py scripts or use placeholder
- No need for separate `thumb.png` generation -- the existing PNGs serve the purpose
- Link thumbnails to corresponding chart.pdf files in the source `slides/` folder (or to the PNG itself for web viewing)

### Decision 3: Quiz Conversion Strategy (Moodle XML to Interactive HTML)
**Decision: XML -> JSON extraction -> embed in self-contained HTML files.**

Pipeline:
1. Parse each Moodle XML file to extract: question text, answer options (A-D), correct answer, feedback text
2. Strip CDATA/HTML wrappers, extract plain text
3. Structure as JSON matching P&S quiz format: `{id, question, options: {A,B,C,D}, correct, explanation}`
4. Embed JSON in `<script>` tag of quiz HTML template (copied from P&S quiz1.html structure)
5. Adapt nav links to point to M&A index.html and GitHub repo

This can be done manually (45 questions) or with a one-off Python script.

### Decision 4: Color Palette Adaptation
**Mapping P&S colors to M&A ML palette:**

| P&S Element | P&S Color | M&A Replacement |
|-------------|-----------|-----------------|
| Nav bar | #24292e (dark gray) | #1a1a4e (dark ML purple) |
| Section I (green) | #22c55e | #2CA02C (MLGreen) |
| Section II (yellow) | #f59e0b | #FF7F0E (MLOrange) |
| Section III (red) | #ef4444 | #D62728 (MLRed) |
| Links | #0366d6 | #0066CC (MLBlue) |
| Quiz accent | #8b5cf6 | #3333B2 (MLPurple) |
| Hero gradient | #24292e -> #0366d6 | #3333B2 -> #0066CC |

### Decision 5: Sidebar Structure
**M&A has 6 lectures in 3 logical groups (matching the 3 quizzes):**
- Group I "Regression": L01 Linear Regression, L02 Logistic Regression
- Group II "Instance & Ensemble": L03 KNN & K-Means, L04 Random Forests
- Group III "Dimensionality & Advanced": L05 PCA & t-SNE, L06 Embeddings & RL

Use `<details>` sections with color-coded borders (MLGreen, MLOrange, MLRed).

## Task Flow

```
Task 1 (Quiz Conversion)     Task 2 (Index Rewrite)     Task 3 (Chart Gallery)
  Parse 3 XML files            Rewrite index.html          Inventory chart PNGs
  Extract JSON                 P&S layout + ML colors      Map to lectures
  Build 3 quiz HTMLs           Sidebar, nav, hero          Add cgrid sections
       |                            |                           |
       +----------------------------+---------------------------+
                                    |
                              Task 4 (Integration)
                                Wire quiz links
                                Wire chart galleries
                                Test all links
                                    |
                              Task 5 (Cleanup)
                                Delete old css/style.css
                                Delete old js/main.js
                                Verify Reveal.js unaffected
```

Tasks 1, 2, 3 can run in parallel. Task 4 depends on all three. Task 5 is final cleanup.

## Detailed TODOs

### Task 1: Quiz Conversion (Moodle XML to Interactive HTML)

**1.1** Create `docs/quiz/` directory

**1.2** Write a one-off Python script `scripts/convert_moodle_to_quiz.py` that:
- Parses each XML file (`quizzes/quiz1_topics_1_2.xml`, `quiz2_topics_3_4.xml`, `quiz3_topics_5_6.xml`)
- Extracts question text (strip CDATA + HTML tags), 4 answer options, correct answer (fraction="100"), feedback
- Outputs JSON array matching P&S format
- **Acceptance:** Script produces 3 JSON arrays with 15 questions each

**1.3** Create quiz HTML template adapted from P&S `quiz/quiz1.html`:
- Copy P&S quiz1.html structure (inline CSS + JS)
- Replace P&S colors with M&A ML palette (see Decision 4)
- Change nav title, links (point to `../index.html`, M&A GitHub repo)
- Replace `quizData` JSON with converted questions
- Keep KaTeX CDN links for math rendering
- **Acceptance:** Each quiz renders, questions display, clicking answers shows feedback, score tracks, grading works

**1.4** Generate 3 quiz files:
- `docs/quiz/quiz1_regression.html` (L01+L02, 15 questions)
- `docs/quiz/quiz2_classification_ensemble.html` (L03+L04, 15 questions)
- `docs/quiz/quiz3_advanced.html` (L05+L06, 15 questions)
- **Acceptance:** All 3 files load in browser, all 45 questions are interactive

### Task 2: Index Page Rewrite

**2.1** Rewrite `docs/index.html` with P&S-style inline CSS:
- Dark nav bar with "Methods & Algorithms" title and links (Lectures, Quizzes, Charts, GitHub)
- Sticky sidebar (180px) with 3 `<details>` sections (Groups I-III, color-coded)
- Hero banner with gradient (#3333B2 -> #0066CC), stats (6 Lectures, 12 Decks, ~48 Charts, 45 Quiz Qs)
- **Acceptance:** Page renders with P&S compact style, sidebar is sticky and collapsible

**2.2** Add lesson card grid for each group:
- 3-column grid within each group (since only 2-3 lectures per group)
- Each card links to the lecture section lower on the page
- **Acceptance:** Cards are clickable, styled with group colors

**2.3** Add lecture detail sections (one per lecture, L01-L06):
- Each section has: lecture number badge, title, "View Slides" link
- Material links grid: Overview Slides, Deep Dive Slides, Overview PDF, Deep Dive PDF, Colab Notebook, Dataset
- Preserve all existing href targets exactly
- **Acceptance:** All 6 lecture sections render, all material links work

**2.4** Add quiz section:
- Quiz card grid (3 cards) linking to `quiz/quiz1_regression.html`, etc.
- Style with MLPurple accent (like P&S purple quiz section)
- Show question count per quiz
- **Acceptance:** Quiz cards render, links point to correct quiz HTML files

**2.5** Add capstone section:
- Preserve existing capstone links (specification, template, rubric)
- Style as material cards
- **Acceptance:** All 3 capstone links preserved

**2.6** Add responsive media queries:
- Adapt P&S breakpoints (1400px, 1000px, 800px) for M&A's 6 lectures
- **Acceptance:** Site is usable on mobile (sidebar collapses, grids reflow)

### Task 3: Chart Gallery Sections

**3.1** Inventory all chart PNG files per lecture:
- Map `docs/slides/images/L0X_TopicName/XX_chart_name.png` files to lectures
- L06 may not have chart images yet in docs -- check and note gaps
- **Acceptance:** Complete list of available chart PNGs per lecture

**3.2** Add `cgrid` chart gallery to each lecture section:
- Use P&S `.ccard` pattern: thumbnail image + chart name below
- Image src: `slides/images/L0X_TopicName/XX_chart_name.png` (relative to docs/)
- Link target: the PNG image itself (since chart.pdf is in source, not docs)
- CSS: `object-fit: contain`, 80px height, responsive grid
- **Acceptance:** Each lecture shows its chart thumbnails in a gallery grid

**3.3** Add "All Charts" section at bottom of page (like P&S):
- Group by lecture with lesson-section wrapper
- Show chart count per lecture
- **Acceptance:** Full chart gallery section renders with all available charts

### Task 4: Integration and Link Verification

**4.1** Wire quiz section links to quiz HTML files
- **Acceptance:** Clicking quiz cards opens correct quiz page

**4.2** Wire sidebar navigation to all sections
- **Acceptance:** Sidebar links scroll to correct sections

**4.3** Verify all material links (slides, PDFs, notebooks, datasets, capstone)
- Cross-check against current index.html hrefs
- **Acceptance:** Zero broken links

**4.4** Verify Reveal.js slide decks still load
- Test `docs/slides/L01_overview.html` etc. in browser
- **Acceptance:** Slide decks render normally

### Task 5: Cleanup

**5.1** Delete `docs/css/style.css` (replaced by inline CSS)

**5.2** Delete `docs/js/main.js` (replaced by inline JS or no JS needed)

**5.3** Remove Google Fonts `<link>` (P&S uses system font stack)

**5.4** Verify no orphaned references to old CSS/JS files

**5.5** Test full site locally (open index.html, click through all sections and quizzes)

## Commit Strategy

| Commit | Contents |
|--------|----------|
| 1 | Add quiz conversion script and 3 interactive quiz HTML files |
| 2 | Rewrite index.html with P&S compact layout and ML colors |
| 3 | Add chart gallery sections to index and lecture details |
| 4 | Remove old CSS/JS files, final link verification |

## Success Criteria

1. `docs/index.html` visually matches P&S layout style (compact, GitHub-style, dark nav, sticky sidebar)
2. All 45 quiz questions are interactive with instant feedback, scoring, and grading
3. Chart galleries show thumbnail images for all lectures with available PNGs
4. All existing material links (slides, PDFs, notebooks, datasets, capstone) remain functional
5. Reveal.js slide decks in `docs/slides/` are completely untouched
6. Site uses M&A's ML color palette throughout
7. Mobile responsive at 3 breakpoints
8. No external CSS/JS dependencies (except KaTeX CDN for quiz math)

## Risk Areas

| Risk | Impact | Mitigation |
|------|--------|------------|
| L06 chart images missing from docs/ | Chart gallery incomplete for L06 | Run L06 chart.py scripts to generate PNGs, or show placeholder text |
| Moodle XML has complex HTML/math in questions | Quiz conversion may lose formatting | Use KaTeX rendering; manually review converted questions |
| Existing material links break during rewrite | Students lose access to resources | Copy all hrefs from current index.html verbatim; diff old vs new |
| Chart PNGs are full-size (not thumbnails) | Slow page load with ~48 full-size PNGs | CSS `object-fit: contain` with fixed 80px height; browser handles scaling; optionally add `loading="lazy"` |
| Reveal.js slide decks reference old CSS/JS | Slide decks break | Slide decks are self-contained in docs/slides/; they do NOT reference docs/css/ or docs/js/ |
| Quiz questions reference math notation | Rendering issues without KaTeX | Include KaTeX CDN (same as P&S quizzes); test math-heavy questions |

## Dependencies

- KaTeX CDN (`https://cdn.jsdelivr.net/npm/katex@0.16.9/`) for math in quizzes
- Python 3 + xml.etree for quiz conversion script (one-time use)
- Chart PNG files in `docs/slides/images/` (already exist for L01-L05)
