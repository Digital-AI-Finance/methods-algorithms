<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-25 | Updated: 2026-01-25 -->

# Deployed Slide Assets

**Parent:** [../AGENTS.md](../AGENTS.md)
**Generated:** 2026-01-25
**Type:** Output/Deployment Directory

## Purpose

This directory contains **deployed slide presentations** for the Methods and Algorithms course. All files here are auto-generated from LaTeX/PDF sources and should not be edited directly.

Contents:
- **Reveal.js HTML presentations** (interactive web slides with 2D navigation)
- **PDF downloads** (original compiled Beamer PDFs for offline use)
- **PNG slide images** (extracted from PDFs at 150 DPI, see images/AGENTS.md)
- **Section configurations** (JSON files mapping slides to PMSP sections)
- **Custom CSS theme** (ML-specific Reveal.js styling)

## Structure

```
slides/
├── L01_overview.html       # Reveal.js HTML (L01 overview, ~10 slides)
├── L01_deepdive.html       # Reveal.js HTML (L01 deep dive, ~35 slides)
├── L02_overview.html       # ...
├── L02_deepdive.html       # (6 topics × 2 types = 12 HTML files)
├── L03_overview.html
├── L03_deepdive.html
├── L04_overview.html
├── L04_deepdive.html
├── L05_overview.html
├── L05_deepdive.html
├── L06_overview.html
├── L06_deepdive.html
├── css/
│   └── ml-theme.css        # Custom Reveal.js theme (colors, fonts, layout)
├── pdf/                    # Original PDFs for download
│   ├── L01_overview.pdf
│   ├── L01_deepdive.pdf
│   ├── L02_overview.pdf
│   ├── L02_deepdive.pdf
│   ├── L03_overview.pdf
│   ├── L03_deepdive.pdf
│   ├── L04_overview.pdf
│   ├── L04_deepdive.pdf
│   ├── L05_overview.pdf
│   ├── L05_deepdive.pdf
│   ├── L06_overview.pdf
│   └── L06_deepdive.pdf
├── images/                 # PNG slide images (see images/AGENTS.md)
│   ├── L01_overview/
│   ├── L01_deepdive/
│   ├── L01_Introduction_Linear_Regression/  # Chart images
│   ├── L02_overview/
│   ├── L02_deepdive/
│   └── ...
└── sections/               # JSON section configs for vertical navigation
    ├── L01_overview.json   # Maps slide numbers to sections
    ├── L01_deepdive.json
    ├── L01_Introduction_Linear_Regression.json  # Chart metadata
    ├── L02_overview.json
    ├── L02_deepdive.json
    ├── L02_Logistic_Regression.json
    └── ...
```

## Key Files

### HTML Presentations (*.html)

Each HTML file is a **Reveal.js slideshow** generated from a Beamer PDF:

- **L01_overview.html** - Introduction & Linear Regression (overview)
  - ~10 slides covering key concepts
  - Vertical sections: Title, Problem, Method, Solution, Practice, Summary
  - Converted from `slides/L01_Introduction_Linear_Regression/L01_overview.pdf`

- **L01_deepdive.html** - Introduction & Linear Regression (deep dive)
  - ~35 slides with full mathematical theory
  - More detailed vertical sections with formulas, proofs, examples
  - Converted from `slides/L01_Introduction_Linear_Regression/L01_deepdive.pdf`

- **L02-L06 (overview/deepdive).html** - Same pattern for other topics
  - L02: Logistic Regression
  - L03: KNN & K-Means
  - L04: Random Forests
  - L05: PCA & t-SNE
  - L06: Embeddings & RL

**Features:**
- 2D navigation: left/right for topics, up/down for sections within a topic
- Plugins: menu, chalkboard, spotlight cursor, zoom
- Full-screen mode (95vh height, 0 margin)
- Responsive design (works on mobile/tablet)
- Print support (PDF export via browser print)

### Reveal.js Theme (css/ml-theme.css)

Custom CSS overrides for Reveal.js presentations:

- **Colors:** MLPurple (#3333B2), MLBlue (#0066CC), MLOrange (#FF7F0E)
- **Fonts:** Inter (headings), system fonts (body)
- **Layout:** Full-screen slides with minimal chrome
- **Navigation:** Custom controls with course colors
- **Animations:** Smooth transitions between slides

### PDF Downloads (pdf/*.pdf)

Original compiled Beamer PDFs copied from source directory:

- **Purpose:** Offline viewing, printing, archival
- **Source:** `slides/L0X_Topic/*.pdf` (compiled from .tex files)
- **Format:** Standard PDF with Beamer metadata
- **Size:** ~1-3 MB per file (depends on number of embedded chart images)

### Section Configurations (sections/*.json)

JSON files that define **vertical navigation structure** for each presentation:

**Example:** `L01_overview.json`
```json
{
  "title": "Introduction & Linear Regression",
  "sections": [
    {"title": "Title", "start": 1, "end": 1},
    {"title": "Problem", "start": 2, "end": 2},
    {"title": "Method", "start": 3, "end": 5},
    {"title": "Solution", "start": 6, "end": 8},
    {"title": "Practice", "start": 9, "end": 9},
    {"title": "Summary", "start": 10, "end": 10}
  ]
}
```

**Purpose:**
- Maps slide numbers to PMSP framework sections
- Enables vertical navigation (up/down arrows) within each section
- Allows users to skip directly to specific sections via menu

**Generation:** Created manually or by parsing LaTeX `\section{}` commands

### Chart Images (images/L0X_Topic/)

PNG versions of Python-generated chart.pdf files embedded in slides:

- **images/L01_Introduction_Linear_Regression/** - 8 charts for L01
  - 01_simple_regression.png
  - 02_multiple_regression_3d.png
  - 03_residual_plots.png
  - 04_gradient_descent.png
  - 05_learning_curves.png
  - 06_regularization_comparison.png
  - 07_bias_variance.png
  - 08_decision_flowchart.png

- **images/L02_Logistic_Regression/** - 7 charts for L02
- **images/L03_KNN_KMeans/** - 7 charts for L03
- **images/L04_Random_Forests/** - 7 charts for L04
- **images/L05_PCA_tSNE/** - 7 charts for L05
- **images/L06_Embeddings_RL/** - 7 charts for L06

**Source:** Extracted from PDF by `pdf_to_revealjs.py` or copied directly
**Format:** PNG, 150 DPI, optimized for web
**See:** [images/AGENTS.md](images/AGENTS.md) for details

## For AI Agents

### DO NOT Edit Directly

This is an **OUTPUT DIRECTORY**. All files are generated from source materials:

| File Type | Source | Generator |
|-----------|--------|-----------|
| `*.html` | `slides/L0X_Topic/*.pdf` | `infrastructure/pdf_to_revealjs.py` |
| `pdf/*.pdf` | `slides/L0X_Topic/*.pdf` | (copy) |
| `images/L0X_overview/*.png` | `slides/L0X_Topic/*.pdf` | `pdf_to_revealjs.py` → pdf2image |
| `images/L0X_Topic/*.png` | `slides/L0X_Topic/XX_chart/chart.pdf` | Manual copy or PDF extraction |
| `sections/*.json` | `slides/L0X_Topic/*.tex` | Manual creation or LaTeX parser |
| `css/ml-theme.css` | `templates/reveal_theme.css` | Manual copy |

**Never edit files in slides/ directly. Always edit source files and regenerate.**

### Regeneration Workflow

**Regenerate a single slide deck:**

```bash
# 1. Compile LaTeX source to PDF (if changed)
cd slides/L01_Introduction_Linear_Regression
pdflatex -interaction=nonstopmode L01_overview.tex
mv L01_overview.pdf L01_overview.pdf

# 2. Convert PDF to Reveal.js HTML + images
cd ../..
python infrastructure/pdf_to_revealjs.py

# 3. Verify output
# Open: docs/slides/L01_overview.html in browser
```

**Regenerate all slide decks:**

```bash
# Build all PDFs first
python infrastructure/course_cli.py build slides --topic all

# Convert all PDFs to HTML
python infrastructure/pdf_to_revealjs.py

# Deploy to GitHub Pages
python infrastructure/course_cli.py deploy github
```

**Update section configuration:**

```bash
# Edit JSON file to adjust slide→section mapping
# Example: docs/slides/sections/L01_overview.json
# Change "start" and "end" values to match slide numbers
# Regenerate HTML if needed
```

### Dependencies

**Required:**
- `pdf2image` - Python library for PDF→PNG conversion (requires poppler)
- `reveal.js` - JavaScript framework (loaded from CDN in HTML)
- Source PDFs in `slides/L0X_Topic/*.pdf` (must be compiled first)

**Optional:**
- `sections/*.json` - For vertical navigation (if missing, falls back to horizontal only)
- `css/ml-theme.css` - For custom styling (if missing, uses default Reveal.js theme)

### Common Tasks

**Add a new slide deck (L07):**
1. Compile LaTeX: `slides/L07_NewTopic/L07_overview.pdf`
2. Run converter: `python infrastructure/pdf_to_revealjs.py`
3. Verify output: `docs/slides/L07_overview.html`
4. Create section config: `docs/slides/sections/L07_overview.json`
5. Update main index: `docs/index.html` (add L07 section)
6. Deploy: `python infrastructure/course_cli.py deploy github`

**Fix broken images:**
- Check `docs/slides/images/L0X_overview/` exists
- Verify PNG files are named `slide_01.png`, `slide_02.png`, etc.
- Regenerate if missing: `python infrastructure/pdf_to_revealjs.py`
- Check DPI setting in converter (default: 150)

**Update Reveal.js theme:**
- Edit `templates/reveal_theme.css` (source)
- Copy to `docs/slides/css/ml-theme.css`
- Hard refresh browser (Ctrl+F5) to clear cache

**Test vertical navigation:**
- Open HTML in browser
- Press Up/Down arrows to navigate within sections
- Check `sections/*.json` for correct slide ranges
- Verify section titles match PMSP framework

### Reveal.js Features

**Navigation:**
- Left/Right arrows: Move between slides horizontally
- Up/Down arrows: Move between sections vertically (if configured)
- Space: Next slide
- Shift+Space: Previous slide
- Home/End: First/last slide
- Escape: Slide overview mode

**Plugins:**
- **Menu** (M key): Slide navigation menu
- **Chalkboard** (C key): Draw on slides
- **Spotlight** (S key): Spotlight cursor for presentations
- **Zoom** (Alt+Click): Zoom into slide regions
- **Notes** (S key): Speaker notes view (if available)

**Export:**
- Print to PDF: Add `?print-pdf` to URL, then browser print
- Export images: Right-click on slide images → Save As

## Related Documentation

- [../AGENTS.md](../AGENTS.md) - GitHub Pages deployment overview
- [../../slides/AGENTS.md](../../slides/AGENTS.md) - LaTeX source files
- [../../infrastructure/AGENTS.md](../../infrastructure/AGENTS.md) - Build tools
- [images/AGENTS.md](images/AGENTS.md) - PNG slide images
