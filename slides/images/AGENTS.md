<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-25 | Updated: 2026-01-25 -->

# PNG Slide Images

**Parent:** [../AGENTS.md](../AGENTS.md)
**Generated:** 2026-01-25
**Type:** Output/Deployment Directory

## Purpose

This directory contains **PNG images of individual slides** extracted from compiled Beamer PDFs. These images are embedded in the Reveal.js HTML presentations for web viewing.

**Why PNG instead of LaTeX?**
- Avoids LaTeX parsing issues (LaTeX → HTML conversion is complex and error-prone)
- Preserves exact PDF rendering (fonts, spacing, math formulas)
- Faster loading in browsers (pre-rendered images vs. on-the-fly LaTeX)
- Works on all devices (no MathJax/KaTeX dependencies)

**Trade-offs:**
- Larger file sizes (~100-200 KB per slide vs. ~10 KB for HTML)
- Not searchable or copy-paste friendly (text is in images)
- Requires PDF recompilation for any content changes

## Structure

```
images/
├── L01_overview/                # L01 overview slides (10 slides)
│   ├── slide_01.png            # Title slide
│   ├── slide_02.png            # Problem slide
│   ├── slide_03.png            # Method slide 1
│   ├── ...
│   └── slide_10.png            # Summary slide
├── L01_deepdive/                # L01 deep dive slides (35 slides)
│   ├── slide_01.png
│   ├── slide_02.png
│   ├── ...
│   └── slide_35.png
├── L01_Introduction_Linear_Regression/  # Chart images (8 charts)
│   ├── 01_simple_regression.png
│   ├── 02_multiple_regression_3d.png
│   ├── 03_residual_plots.png
│   ├── 04_gradient_descent.png
│   ├── 05_learning_curves.png
│   ├── 06_regularization_comparison.png
│   ├── 07_bias_variance.png
│   └── 08_decision_flowchart.png
├── L02_overview/                # L02 overview slides
├── L02_deepdive/                # L02 deep dive slides
├── L02_Logistic_Regression/     # L02 chart images (7 charts)
├── L03_overview/
├── L03_deepdive/
├── L03_KNN_KMeans/              # L03 chart images (7 charts)
├── L04_overview/
├── L04_deepdive/
├── L04_Random_Forests/          # L04 chart images (7 charts)
├── L05_overview/
├── L05_deepdive/
├── L05_PCA_tSNE/                # L05 chart images (7 charts)
├── L06_overview/
├── L06_deepdive/
└── L06_Embeddings_RL/           # L06 chart images (7 charts)
```

## Image Types

### Slide Images (L0X_overview/, L0X_deepdive/)

**Purpose:** Individual slide renderings from Beamer PDFs

**Naming convention:** `slide_XX.png` (where XX is zero-padded slide number)

**Generation process:**
1. Compile LaTeX source to PDF: `pdflatex L01_overview.tex`
2. Extract PDF pages to PNG: `pdf2image.convert_from_path(pdf, dpi=150)`
3. Save with sequential naming: `slide_01.png`, `slide_02.png`, etc.

**Specifications:**
- **Format:** PNG (lossless compression, optimized)
- **DPI:** 150 (good balance of quality and file size)
- **Dimensions:** ~2000×1125 pixels (16:9 aspect ratio at 150 DPI)
- **Size:** ~100-200 KB per slide (depends on content complexity)
- **Color depth:** 24-bit RGB (no alpha channel needed)

**Typical counts per lecture:**
- **Overview:** 10-17 slides (quick intro to topic)
- **Deep dive:** 24-35 slides (full mathematical treatment)

### Chart Images (L0X_Topic/)

**Purpose:** Standalone Python-generated charts embedded in slides

**Naming convention:** `XX_descriptive_name.png` (matches source folder name)

**Generation process:**
1. Run Python script: `python slides/L01.../01_simple_regression/chart.py`
2. Script outputs: `chart.pdf` (vector graphics)
3. PDF embedded in LaTeX, rendered in final PDF
4. Extracted from PDF or copied directly as PNG

**Specifications:**
- **Format:** PNG (converted from PDF)
- **DPI:** 150 (matches slide DPI)
- **Dimensions:** ~1500×900 pixels (10×6 inches at 150 DPI)
- **Size:** ~50-150 KB per chart (simpler than full slides)
- **Colors:** MLPurple (#3333B2), MLBlue (#0066CC), MLOrange (#FF7F0E)

**Typical counts per lecture:**
- **7-8 charts** per topic (defined in manifest.json)

**Chart categories:**
- Regression plots (scatter + fitted lines)
- 3D surfaces (multiple regression)
- Loss curves (gradient descent, learning curves)
- Decision boundaries (classification)
- Confusion matrices (model evaluation)
- Tree diagrams (random forests)
- Scatter plots (PCA, t-SNE)

## For AI Agents

### DO NOT Edit Directly

This is an **OUTPUT DIRECTORY**. All PNG images are generated from source files:

| Image Type | Source | Generator |
|------------|--------|-----------|
| `L0X_overview/slide_XX.png` | `slides/L0X_Topic/L0X_overview.pdf` | `pdf_to_revealjs.py` → `pdf2image` |
| `L0X_deepdive/slide_XX.png` | `slides/L0X_Topic/L0X_deepdive.pdf` | `pdf_to_revealjs.py` → `pdf2image` |
| `L0X_Topic/XX_chart.png` | `slides/L0X_Topic/XX_chart/chart.pdf` | Manual copy or PDF extraction |

**Never edit PNG files directly. Always regenerate from source PDFs/scripts.**

### Regeneration Workflow

**Regenerate slide images for one lecture:**

```bash
# 1. Compile LaTeX to PDF (if source changed)
cd slides/L01_Introduction_Linear_Regression
pdflatex -interaction=nonstopmode L01_overview.tex

# 2. Convert PDF to PNG images
cd ../..
python infrastructure/pdf_to_revealjs.py
# This will:
# - Extract pages from L01_overview.pdf
# - Save as docs/slides/images/L01_overview/slide_01.png, slide_02.png, ...
# - Generate docs/slides/L01_overview.html with image references
```

**Regenerate all slide images:**

```bash
# Build all PDFs first
python infrastructure/course_cli.py build slides --topic all

# Convert all to images
python infrastructure/pdf_to_revealjs.py
# Processes all L0X_overview.pdf and L0X_deepdive.pdf files
# Outputs to docs/slides/images/L0X_overview/, L0X_deepdive/
```

**Regenerate chart images:**

```bash
# Option 1: Rebuild all charts
python infrastructure/course_cli.py build charts --topic all
# Runs all chart.py scripts, outputs to slides/L0X_Topic/XX_chart/chart.pdf

# Option 2: Rebuild charts for one topic
python infrastructure/course_cli.py build charts --topic L01

# Option 3: Rebuild single chart
cd slides/L01_Introduction_Linear_Regression/01_simple_regression
python chart.py  # Outputs chart.pdf in same directory

# Then copy/convert to PNG for docs/
# (Usually done automatically by pdf_to_revealjs.py when processing full PDFs)
```

**Change image resolution:**

Edit `infrastructure/pdf_to_revealjs.py`:
```python
# Line ~29: Change DPI parameter
images = convert_from_path(str(pdf_path), dpi=150)  # Increase for higher quality
```

Higher DPI = better quality but larger files:
- 150 DPI: ~100-200 KB per slide (current default, good for web)
- 200 DPI: ~200-400 KB per slide (better for print/zoom)
- 300 DPI: ~500-800 KB per slide (print quality, slow loading)

### Dependencies

**Python libraries:**
- `pdf2image` - Converts PDF pages to PIL Image objects
- `Pillow (PIL)` - Image processing and PNG optimization
- `poppler` - PDF rendering engine (system dependency for pdf2image)

**Install poppler:**
- **Windows:** Download from https://github.com/oschwartz10612/poppler-windows/releases/
- **Linux:** `sudo apt-get install poppler-utils`
- **macOS:** `brew install poppler`

**Verify installation:**
```bash
python -c "from pdf2image import convert_from_path; print('OK')"
```

### Common Tasks

**Add images for new lecture (L07):**
1. Compile LaTeX: `slides/L07_NewTopic/L07_overview.pdf`
2. Run converter: `python infrastructure/pdf_to_revealjs.py`
3. Verify output: `docs/slides/images/L07_overview/` exists
4. Check slide count: `ls docs/slides/images/L07_overview/ | wc -l`

**Fix missing or corrupted images:**
1. Check source PDF exists: `slides/L01.../L01_overview.pdf`
2. Verify PDF opens correctly (not corrupted)
3. Delete corrupted images: `rm -rf docs/slides/images/L01_overview/`
4. Regenerate: `python infrastructure/pdf_to_revealjs.py`
5. Verify: `ls docs/slides/images/L01_overview/`

**Optimize image file sizes:**
- Images are already optimized by PIL's `save(..., optimize=True)`
- For further compression, use tools like `pngquant` or `optipng`:
  ```bash
  pngquant --quality=80-95 docs/slides/images/L01_overview/*.png
  optipng -o7 docs/slides/images/L01_overview/*.png
  ```
- Trade-off: Smaller files but slightly lower quality

**Convert chart.pdf to PNG manually:**
```bash
# Using ImageMagick
convert -density 150 chart.pdf chart.png

# Using pdf2image
python -c "from pdf2image import convert_from_path; \
           img = convert_from_path('chart.pdf', dpi=150)[0]; \
           img.save('chart.png', 'PNG', optimize=True)"
```

### File Organization

**By lecture type:**
- **Overview images:** L0X_overview/ (10-17 slides each, 6 lectures = ~60-100 images)
- **Deep dive images:** L0X_deepdive/ (24-35 slides each, 6 lectures = ~150-200 images)
- **Chart images:** L0X_Topic/ (7-8 charts each, 6 lectures = ~45-50 images)

**Total counts:**
- Slide images: ~250-300 files (overview + deep dive)
- Chart images: ~45-50 files
- Total: ~295-350 PNG files in images/
- Total size: ~30-50 MB (all images combined)

**Naming consistency:**
- Slide images: `slide_01.png`, `slide_02.png`, ... (zero-padded)
- Chart images: `01_chart_name.png`, `02_chart_name.png`, ... (matches source folder)

### Quality Checks

**Verify image generation:**
```bash
# Count slides per lecture (should match PDF page count)
ls docs/slides/images/L01_overview/ | wc -l  # Should be ~10
ls docs/slides/images/L01_deepdive/ | wc -l  # Should be ~35

# Check file sizes (all should be 50-500 KB)
du -h docs/slides/images/L01_overview/

# Verify dimensions (should be consistent)
file docs/slides/images/L01_overview/*.png | head -5
```

**Test in Reveal.js:**
1. Open HTML: `docs/slides/L01_overview.html`
2. Check all slides load (no broken images)
3. Verify image quality (readable text, sharp charts)
4. Test on mobile (images scale correctly)

**Common issues:**
- **Blank slides:** PDF rendering failed (check poppler installation)
- **Fuzzy text:** DPI too low (increase from 150 to 200)
- **Slow loading:** File sizes too large (optimize or reduce DPI)
- **Missing slides:** PDF has fewer pages than expected (LaTeX compilation error)

## Related Documentation

- [../AGENTS.md](../AGENTS.md) - Deployed slide assets overview
- [../../AGENTS.md](../../AGENTS.md) - GitHub Pages deployment
- [../../../slides/AGENTS.md](../../../slides/AGENTS.md) - LaTeX source files
- [../../../infrastructure/AGENTS.md](../../../infrastructure/AGENTS.md) - Build tools
