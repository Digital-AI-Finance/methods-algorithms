<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-25 | Updated: 2026-02-07 -->

# GitHub Pages Deployment Directory

**Parent:** [../AGENTS.md](../AGENTS.md)
**Generated:** 2026-01-25 | **Updated:** 2026-02-07
**Type:** Output/Deployment Directory

## Purpose

This is the **GitHub Pages deployment directory** for the Methods and Algorithms course. It contains the compiled, web-ready versions of all course materials, including:

- Interactive Reveal.js slide presentations (converted from LaTeX/PDF)
- PNG slide images (extracted from PDF at 150 DPI)
- Static HTML site with wiki-style navigation
- CSS/JS assets for the course website
- PDF downloads for print-friendly versions

**URL:** https://digital-ai-finance.github.io/methods-algorithms/

## Structure

```
docs/
├── index.html              # Main landing page (wiki-style layout)
├── css/
│   └── style.css          # Wiki-style CSS (3-column layout)
├── js/
│   └── main.js            # Navigation and interactivity
├── assets/                # Static assets (logos, icons)
├── quiz/                  # Interactive JavaScript quizzes
└── slides/
    ├── L01_overview.html  # Reveal.js presentation (L01 overview)
    ├── L01_deepdive.html  # Reveal.js presentation (L01 deep dive)
    ├── ...                # All 12 HTML slide decks (6 topics × 2 types)
    ├── css/
    │   └── ml-theme.css   # Custom Reveal.js ML theme
    ├── pdf/               # Original PDFs for download
    │   ├── L01_overview.pdf
    │   ├── L01_deepdive.pdf
    │   └── ...
    ├── images/            # PNG slide images (see images/AGENTS.md)
    └── sections/          # JSON section configs for vertical navigation
        ├── L01_overview.json
        ├── L01_deepdive.json
        └── ...
```

## Key Files

### Main Site

- **index.html** - Course homepage with navigation sidebar, lecture cards, materials grid
  - Uses 3-column wiki layout (left sidebar, main content, right TOC)
  - Responsive mobile design with hamburger menu
  - Links to all 6 lectures (L01-L06) with overview/deepdive slides
  - Quiz and capstone project sections

- **css/style.css** - Modern wiki-style CSS
  - Three-column grid layout (220px sidebar, fluid main, 200px TOC)
  - Dark blue sidebar (#0f172a) with white main content
  - Material cards for slides, notebooks, datasets
  - Mobile-first responsive breakpoints

- **js/main.js** - Interactive navigation
  - Smooth scrolling between sections
  - Active link highlighting
  - Mobile menu toggle
  - Intersection observer for TOC sync

### Slide Presentations

- **LXX_overview.html** / **LXX_deepdive.html** - Reveal.js HTML presentations
  - Generated from PDF by `infrastructure/pdf_to_revealjs.py`
  - Each slide is a PNG image embedded in Reveal.js framework
  - Supports 2D navigation (horizontal topics + vertical sections)
  - Plugins: menu, chalkboard, spotlight, zoom

- **css/ml-theme.css** - Custom Reveal.js theme
  - Matches course branding colors (MLPurple, MLBlue, etc.)
  - Full-screen slides (95vh height, 0 margin)
  - Custom navigation controls

- **sections/*.json** - Section configurations for vertical navigation
  - Maps slide numbers to sections (Problem, Method, Solution, Practice)
  - Enables vertical navigation within each topic
  - Example: L01_overview.json defines 4 vertical sections

### Static Downloads

- **pdf/*.pdf** - Original compiled LaTeX PDFs
  - Generated from slides/LXX_Topic/*.tex source files
  - Downloadable for print-friendly offline use
  - 12 files total (6 topics × 2 types)

## For AI Agents

### DO NOT Edit Directly

This is an **OUTPUT DIRECTORY**. All files here are auto-generated from source materials:

- HTML/CSS/JS → Built by deployment scripts
- Slide images → Extracted from PDF by `pdf_to_revealjs.py`
- PDFs → Copied from source LaTeX compilation

**Never edit files in docs/ directly. Always edit source files and regenerate.**

### Regeneration Workflow

To update the GitHub Pages site:

1. **Build slide PDFs** (if LaTeX source changed):
   ```bash
   python infrastructure/course_cli.py build slides --topic L01
   # Or build all: --topic all
   ```

2. **Convert PDFs to Reveal.js HTML** (generates images + HTML):
   ```bash
   python infrastructure/pdf_to_revealjs.py
   # Processes all PDFs in slides/L0X_Topic/*.pdf
   # Outputs to docs/slides/*.html and docs/slides/images/
   ```

3. **Update main index.html** (if course structure changed):
   - Edit template or regenerate from infrastructure scripts
   - Manually copy to docs/index.html

4. **Deploy to GitHub Pages**:
   ```bash
   python infrastructure/course_cli.py deploy github
   # Or use: python infrastructure/deployers/github_deployer.py
   ```

5. **Verify deployment**:
   - Check https://digital-ai-finance.github.io/methods-algorithms/
   - Test slide navigation, downloads, mobile responsiveness

### Dependencies

**Source directories:**
- `slides/L0X_Topic/*.tex` - LaTeX Beamer source slides
- `slides/L0X_Topic/*.pdf` - Compiled PDFs (must exist before conversion)
- `slides/L0X_Topic/XX_chart/chart.pdf` - Chart images (embedded in LaTeX)

**Infrastructure tools:**
- `infrastructure/pdf_to_revealjs.py` - PDF→PNG→HTML converter
- `infrastructure/tex_to_revealjs.py` - Alternative LaTeX→HTML converter
- `infrastructure/deployers/github_deployer.py` - Git deployment automation
- `infrastructure/course_cli.py` - Main CLI orchestrator

### File Generation

| Source | Tool | Output |
|--------|------|--------|
| slides/L01.../L01_overview.pdf | pdf_to_revealjs.py | docs/slides/L01_overview.html |
| slides/L01.../L01_overview.pdf | pdf_to_revealjs.py | docs/slides/images/L01_overview/*.png |
| slides/L01.../L01_overview.pdf | (copy) | docs/slides/pdf/L01_overview.pdf |
| templates/index_template.html | (manual) | docs/index.html |
| templates/style.css | (manual) | docs/css/style.css |

### Common Tasks

**Add a new lecture (L07):**
1. Create source files in `slides/L07_NewTopic/`
2. Compile LaTeX to PDF
3. Run `pdf_to_revealjs.py` to generate HTML/images
4. Update `docs/index.html` to add L07 section
5. Update `docs/slides/sections/` with L07 section configs
6. Deploy to GitHub

**Update slide content:**
1. Edit LaTeX source in `slides/L0X_Topic/*.tex`
2. Recompile PDF: `pdflatex -interaction=nonstopmode L0X_overview.tex`
3. Regenerate HTML: `python infrastructure/pdf_to_revealjs.py`
4. Verify changes locally (open docs/slides/L0X_overview.html)
5. Deploy: `python infrastructure/course_cli.py deploy github`

**Fix broken navigation:**
- Check `docs/slides/sections/*.json` for correct slide→section mapping
- Verify section titles match PMSP framework (Problem, Method, Solution, Practice)
- Test vertical navigation in Reveal.js (up/down arrows)

## Deployment Notes

- **Branch:** GitHub Pages serves from `master` branch `/docs` folder
- **Custom domain:** Can configure CNAME file in docs/ if desired
- **Build time:** ~2-3 minutes for full site regeneration (all 12 slide decks)
- **Image size:** ~100-200 KB per slide PNG (150 DPI), ~10-30 MB per lecture
- **Caching:** Browser may cache old CSS/JS - use Ctrl+F5 for hard refresh

## Related Documentation

- [../infrastructure/AGENTS.md](../infrastructure/AGENTS.md) - Build and deployment tools
- [../slides/AGENTS.md](../slides/AGENTS.md) - LaTeX source files
- [docs/slides/AGENTS.md](slides/AGENTS.md) - Deployed slide assets
- [docs/slides/images/AGENTS.md](slides/images/AGENTS.md) - PNG slide images
