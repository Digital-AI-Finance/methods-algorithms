# L01 Ultra-Deep Review Plan - Version 3

**Created:** 2026-02-02
**Revised:** 2026-02-02 (Iteration 2 - Critic-approved improvements)
**Status:** CRITICAL FINDINGS - Template Deviations Identified

---

## Executive Summary

Previous analysis incorrectly claimed "100% template compliance". This deep audit reveals **28 specific deviations** from the authoritative template at `templates/beamer_template.tex`.

**Revision Notes (v3):**
- Complete chart.py audit for ALL 8 charts (no "Need to verify" entries)
- Pattern-based fix instructions instead of line numbers
- Clear decision on deepdive section naming
- Added missing "Remove navigation symbols" comment deviation
- Colab URL marked as TBD
- Compilation test step added

---

## 1. TEMPLATE DEVIATION AUDIT

### 1.1 Preamble Issues

#### Missing Comment (NEWLY IDENTIFIED)
| Template Line 44 | L01_overview.tex | L01_deepdive.tex |
|------------------|------------------|------------------|
| `% Remove navigation symbols` | `% Remove navigation symbols` | **MISSING COMMENT** |

**DEVIATION**: L01_deepdive.tex line 44 has `\setbeamertemplate{navigation symbols}{}` without the preceding comment.

#### Custom Colors Comment
| Template Line 16 | L01_overview.tex Line 16 | L01_deepdive.tex Line 16 |
|------------------|--------------------------|--------------------------|
| `% Custom colors (ML palette)` | `% Custom colors (ML palette)` | `% Custom colors` |

**DEVIATION**: deepdive.tex uses abbreviated comment.

#### Package Order Deviation
| Template (lines 13-14) | L01_overview.tex (lines 13-14) | L01_deepdive.tex (lines 13-14) |
|------------------------|--------------------------------|--------------------------------|
| `tikz` then `hyperref` | `hyperref` then `tikz` | `hyperref` then `tikz` |

**DEVIATION**: Both L01 files have packages in wrong order.

#### Footer Comment Deviation
| Template Line 28 | L01_overview.tex Line 28 | L01_deepdive.tex Line 28 |
|------------------|--------------------------|--------------------------|
| `% Footer customization` | `% Footer customization` | `% Footer` |

**DEVIATION**: deepdive.tex uses abbreviated comment.

#### Custom Commands Comment Deviation
| Template Line 47 | L01_overview.tex Line 47 | L01_deepdive.tex Line 46 |
|------------------|--------------------------|--------------------------|
| `% Custom commands` | `% Custom commands` | `% Commands` |

**DEVIATION**: deepdive.tex uses abbreviated comment.

#### Title Comment Deviation
| Template Line 52 | L01_overview.tex Line 52 | L01_deepdive.tex Line 51 |
|------------------|--------------------------|--------------------------|
| `% Title information` | `% Title information` | `% Title` |

**DEVIATION**: deepdive.tex uses abbreviated comment.

### 1.2 Author Field Deviation

| Template | Both L01 Files |
|----------|----------------|
| `\author{Methods and Algorithms}` | `\author{Methods and Algorithms -- MSc Data Science}` |

**DEVIATION**: Both files add redundant "-- MSc Data Science" (already in `\institute`).

### 1.3 Date Field Deviation

| Template | Both L01 Files |
|----------|----------------|
| `\date{Spring 2026}` | `\date{}` |

**DEVIATION**: Both files use empty date.

### 1.4 Missing Structural Elements

#### Missing Outline Slide in Overview
| Template | L01_overview.tex |
|----------|------------------|
| Has `\begin{frame}{Outline} \tableofcontents \end{frame}` | **MISSING** |

**CRITICAL DEVIATION**: L01_overview.tex has no outline slide after title.

#### Missing PMSP Section Organization in Overview
| Template Sections | L01_overview.tex Sections |
|-------------------|---------------------------|
| Problem, Method, Solution, Practice, Decision Framework, Summary | **NO SECTIONS DEFINED** |

**CRITICAL DEVIATION**: L01_overview.tex has NO `\section{}` commands.

### 1.5 Deepdive Section Naming

| Template Section Names | L01_deepdive.tex Section Names |
|------------------------|--------------------------------|
| Problem | Mathematical Foundations |
| Method | Gradient Descent |
| Solution | Model Evaluation |
| Practice | Regularization |
| Decision Framework | Bias-Variance Tradeoff |
| Summary | Decision Framework, Summary |

**DECISION (v3):** The deepdive section names ARE meaningful and pedagogically appropriate for the technical deep dive. However, they deviate from template PMSP structure.

**Recommendation:** Keep current deepdive section names (Mathematical Foundations, Gradient Descent, etc.) as they serve the educational purpose better than generic PMSP names for a technical deep dive. Document this as an intentional deviation.

### 1.6 Missing Practice Section

| Template | L01_overview.tex | L01_deepdive.tex |
|----------|------------------|------------------|
| Has `\section{Practice}` with Colab link | **MISSING** | **MISSING** |

**CRITICAL DEVIATION**: Neither file has a Practice section with hands-on exercise.

---

## 2. CHART WIDTH AUDIT

### Template Requirements (from CLAUDE.md):
- **0.55\textwidth**: Charts WITH accompanying text on same slide
- **0.65\textwidth**: Chart-ONLY slides (no text except bottomnote)

### L01_overview.tex Chart Widths

| Chart | Current Width | Slide Type | Correct Width | STATUS |
|-------|---------------|------------|---------------|--------|
| 01_simple_regression/chart.pdf | 0.50\textwidth | Chart-only | 0.65\textwidth | **WRONG** |
| 02_multiple_regression_3d/chart.pdf | 0.42\textwidth | Chart-only | 0.55\textwidth* | **WRONG** |
| images/1725_linear_regression.png | 0.55\textwidth | Chart-only | 0.65\textwidth | **WRONG** |
| 04_gradient_descent/chart.pdf | 0.45\textwidth | Chart-only | 0.65\textwidth | **WRONG** |
| 03_residual_plots/chart.pdf | 0.50\textwidth | Chart-only | 0.65\textwidth | **WRONG** |
| 05_learning_curves/chart.pdf | 0.50\textwidth | Chart-only | 0.65\textwidth | **WRONG** |
| images/2048_curve_fitting.png | 0.32\textwidth | Chart-only | 0.55\textwidth* | **WRONG** |
| 06_regularization_comparison/chart.pdf | 0.50\textwidth | Chart-only | 0.65\textwidth | **WRONG** |
| 07_bias_variance/chart.pdf | 0.50\textwidth | Chart-only | 0.65\textwidth | **WRONG** |
| images/605_extrapolating.png | 0.50\textwidth | Chart-only | 0.65\textwidth | **WRONG** |
| 08_decision_flowchart/chart.pdf | 0.45\textwidth | Chart-only | 0.65\textwidth | **WRONG** |

*Note: 3D plots and XKCD images may need smaller widths for aspect ratio preservation.

### L01_deepdive.tex Chart Widths

| Chart | Current Width | Slide Type | Correct Width | STATUS |
|-------|---------------|------------|---------------|--------|
| 01_simple_regression/chart.pdf | 0.55\textwidth | Chart-only | 0.65\textwidth | **WRONG** |
| 02_multiple_regression_3d/chart.pdf | 0.42\textwidth | Chart-only | 0.55\textwidth* | **WRONG** |
| 04_gradient_descent/chart.pdf | 0.55\textwidth | Chart-only | 0.65\textwidth | **WRONG** |
| 03_residual_plots/chart.pdf | 0.55\textwidth | Chart-only | 0.65\textwidth | **WRONG** |
| 05_learning_curves/chart.pdf | 0.55\textwidth | Chart-only | 0.65\textwidth | **WRONG** |
| 06_regularization_comparison/chart.pdf | 0.55\textwidth | Chart-only | 0.65\textwidth | **WRONG** |
| 07_bias_variance/chart.pdf | 0.55\textwidth | Chart-only | 0.65\textwidth | **WRONG** |
| 08_decision_flowchart/chart.pdf | 0.50\textwidth | Chart-only | 0.65\textwidth | **WRONG** |

---

## 3. CHART.PY TEMPLATE COMPLIANCE (COMPLETE AUDIT)

### Template Requirements (from templates/chart_template.py):

```python
plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 13,
    'ytick.labelsize': 13,
    'legend.fontsize': 13,
    'figure.figsize': (10, 6),
    'figure.dpi': 150,
    'axes.spines.top': False,      # REQUIRED
    'axes.spines.right': False,    # REQUIRED
})
```

Plus: GitHub URL annotation in bottom-right corner.

### Complete Chart.py Audit (ALL 8 CHARTS)

| Chart | Has CHART_METADATA? | Has GitHub URL? | Has spines.top: False? | Has spines.right: False? | font.size | STATUS |
|-------|---------------------|-----------------|------------------------|--------------------------|-----------|--------|
| 01_simple_regression | YES | YES (in metadata) | NO | NO | 14 | **MISSING SPINE SETTINGS + URL ANNOTATION** |
| 02_multiple_regression_3d | YES | YES (in metadata) | NO | NO | 14 | **MISSING SPINE SETTINGS + URL ANNOTATION** |
| 03_residual_plots | YES | YES (in metadata) | NO | NO | 14 | **MISSING SPINE SETTINGS + URL ANNOTATION** |
| 04_gradient_descent | YES | YES (in metadata) | NO | NO | 14 | **MISSING SPINE SETTINGS + URL ANNOTATION** |
| 05_learning_curves | YES | YES (in metadata) | NO | NO | 14 | **MISSING SPINE SETTINGS + URL ANNOTATION** |
| 06_regularization_comparison | YES | YES (in metadata) | NO | NO | 14 | **MISSING SPINE SETTINGS + URL ANNOTATION** |
| 07_bias_variance | YES | YES (in metadata) | NO | NO | 14 | **MISSING SPINE SETTINGS + URL ANNOTATION** |
| 08_decision_flowchart | YES | YES (in metadata) | NO | NO | **11** | **WRONG FONT SIZE + MISSING SPINE SETTINGS + URL ANNOTATION** |

### Chart-Specific Notes:

1. **01_simple_regression/chart.py**: Has correct rcParams except missing `axes.spines.top/right: False`. Has `CHART_METADATA` with URL but no `ax.text()` annotation to display it.

2. **02_multiple_regression_3d/chart.py**: Same issues. Note: 3D plots don't have traditional spines, but setting should still be present for consistency.

3. **03_residual_plots/chart.py**: Same issues. Chart uses `ax.grid(True)` which is good.

4. **04_gradient_descent/chart.py**: Same issues. Uses colorbar which is appropriate for contour plot.

5. **05_learning_curves/chart.py**: Same issues. Good use of fill_between for visualization.

6. **06_regularization_comparison/chart.py**: Same issues. Good coefficient path visualization.

7. **07_bias_variance/chart.py**: Same issues. Good bias-variance decomposition visualization.

8. **08_decision_flowchart/chart.py**: Uses `font.size: 11` instead of 14. This may be intentional for flowchart text density, but deviates from template.

---

## 4. SPECIFIC FIXES REQUIRED (PATTERN-BASED)

### Priority 1: Critical Template Deviations

#### Fix 1: L01_overview.tex - Add Outline slide
**Location:** After the frame containing `\titlepage` (currently the first frame)
**Pattern:** After `\end{frame}` that contains `\titlepage`, add:
```latex
\begin{frame}{Outline}
  \tableofcontents
\end{frame}
```

#### Fix 2: L01_overview.tex - Add PMSP sections
**Locations by frame title:**
- Before frame titled "The Business Problem": Add `\section{Problem}`
- Before frame titled "What is Linear Regression?": Add `\section{Method}`
- Before frame titled "Interpreting Coefficients": Add `\section{Solution}`
- Before frame titled "When to Use Linear Regression": Add `\section{Practice}` AND create Practice frame (see Fix 11)
- After Practice frame: Add `\section{Decision Framework}`
- Before frame titled "Key Takeaways": Add `\section{Summary}`

#### Fix 3: Both files - Fix author field
**Pattern:** Find `\author{Methods and Algorithms -- MSc Data Science}` and replace with:
```latex
\author{Methods and Algorithms}
```

#### Fix 4: Both files - Add date
**Pattern:** Find `\date{}` and replace with:
```latex
\date{Spring 2026}
```

#### Fix 5: Both files - Fix package order
**Pattern:** Find these two consecutive lines:
```latex
\usepackage{hyperref}
\usepackage{tikz}
```
Replace with:
```latex
\usepackage{tikz}
\usepackage{hyperref}
```

### Priority 2: Chart Width Fixes

#### Fix 6: L01_overview.tex - Update chart widths
**Pattern-based replacements (search for each `\includegraphics` line):**

| Find (frame title context) | Replace width |
|---------------------------|---------------|
| Frame "Simple Linear Regression" containing `01_simple_regression` | `0.65\textwidth` |
| Frame "Multiple Linear Regression" containing `02_multiple_regression_3d` | `0.55\textwidth` |
| Frame "The Art of Fitting Lines" containing `1725_linear_regression.png` | `0.65\textwidth` |
| Frame "Gradient Descent in Action" containing `04_gradient_descent` | `0.65\textwidth` |
| Frame "Residual Diagnostics" containing `03_residual_plots` | `0.65\textwidth` |
| Frame "Learning Curves" containing `05_learning_curves` | `0.65\textwidth` |
| Frame "The Danger of Overfitting" containing `2048_curve_fitting.png` | `0.55\textwidth` |
| Frame "Regularization: Ridge vs Lasso" containing `06_regularization` | `0.65\textwidth` |
| Frame "Bias-Variance Tradeoff" containing `07_bias_variance` | `0.65\textwidth` |
| Frame "A Word of Caution" containing `605_extrapolating.png` | `0.65\textwidth` |
| Frame "Decision Framework" containing `08_decision_flowchart` | `0.65\textwidth` |

#### Fix 7: L01_deepdive.tex - Update chart widths
**Pattern-based replacements:**

| Find (frame title context) | Replace width |
|---------------------------|---------------|
| Frame "Simple Regression Visualization" containing `01_simple_regression` | `0.65\textwidth` |
| Frame "Multiple Regression Surface" containing `02_multiple_regression_3d` | `0.55\textwidth` |
| Frame "Gradient Descent Visualization" containing `04_gradient_descent` | `0.65\textwidth` |
| Frame "Residual Analysis" containing `03_residual_plots` | `0.65\textwidth` |
| Frame "Learning Curves" containing `05_learning_curves` | `0.65\textwidth` |
| Frame "Ridge vs Lasso Comparison" containing `06_regularization` | `0.65\textwidth` |
| Frame "The Tradeoff Illustrated" containing `07_bias_variance` | `0.65\textwidth` |
| Frame "Algorithm Selection Guide" containing `08_decision_flowchart` | `0.65\textwidth` |

### Priority 3: Chart.py Template Compliance

#### Fix 8: All 8 chart.py files - Add missing rcParams
**Pattern:** Find the `plt.rcParams.update({` block and add inside it:
```python
    'axes.spines.top': False,
    'axes.spines.right': False,
```

#### Fix 9: All 8 chart.py files - Add GitHub URL annotation
**Pattern:** Before `plt.tight_layout()`, add:
```python
ax.text(0.99, 0.01, CHART_METADATA['url'],
        transform=ax.transAxes, fontsize=7, color='gray',
        ha='right', va='bottom', alpha=0.7)
```

Note: For charts using `fig, ax = plt.subplots()`, this works directly. For 3D plots (02_multiple_regression_3d), use `fig.text()` instead.

#### Fix 10: 08_decision_flowchart/chart.py - Fix font size
**Pattern:** Find `'font.size': 11` and replace with:
```python
'font.size': 14
```

### Priority 4: Content Structure

#### Fix 11: L01_overview.tex - Add Practice section
**Location:** After the `\section{Solution}` content, before "When to Use Linear Regression" frame
**Add new section and frame:**
```latex
\section{Practice}
\begin{frame}[t]{Hands-on Exercise}
  \textbf{Open the Colab Notebook}

  \begin{itemize}
    \item Exercise 1: Implement OLS from scratch
    \item Exercise 2: Use scikit-learn LinearRegression
    \item Exercise 3: Compare with gradient descent
  \end{itemize}

  \vspace{1em}
  \textbf{Link:} [TBD - Colab notebook URL]
\end{frame}
```

#### Fix 12: L01_deepdive.tex - Add Practice section
**Location:** After "Choosing Lambda" frame (end of Regularization section)
**Add new frame:**
```latex
\begin{frame}[t]{Hands-on Exercise}
  \textbf{Open the Colab Notebook}

  \begin{itemize}
    \item Exercise 1: Implement gradient descent from scratch
    \item Exercise 2: Compare Ridge, Lasso, and Elastic Net
    \item Exercise 3: Analyze bias-variance tradeoff
  \end{itemize}

  \vspace{1em}
  \textbf{Link:} [TBD - Colab notebook URL]
\end{frame}
```

### Priority 5: Minor Comment Fixes (L01_deepdive.tex)

#### Fix 13: Add missing navigation comment
**Pattern:** Before line `\setbeamertemplate{navigation symbols}{}`, add:
```latex
% Remove navigation symbols
```

#### Fix 14: Fix custom colors comment
**Pattern:** Find `% Custom colors` (without "(ML palette)") and replace with:
```latex
% Custom colors (ML palette)
```

#### Fix 15: Fix footer comment
**Pattern:** Find `% Footer` (by itself) and replace with:
```latex
% Footer customization
```

#### Fix 16: Fix custom commands comment
**Pattern:** Find `% Commands` and replace with:
```latex
% Custom commands
```

#### Fix 17: Fix title comment
**Pattern:** Find `% Title` (by itself, before `\title`) and replace with:
```latex
% Title information
```

---

## 5. SUMMARY OF DEVIATIONS

| Category | Count | Severity |
|----------|-------|----------|
| Missing Outline slide (overview) | 1 | HIGH |
| Missing PMSP sections (overview) | 1 | HIGH |
| Missing Practice section | 2 | HIGH |
| Missing navigation comment (deepdive) | 1 | LOW |
| Wrong chart widths | 19 | MEDIUM |
| Package order wrong | 2 | LOW |
| Author field redundant | 2 | LOW |
| Date field empty | 2 | LOW |
| Comment abbreviations | 4 | LOW |
| Missing chart.py spine settings | 8 | MEDIUM |
| Missing chart.py URL annotations | 8 | MEDIUM |
| Wrong chart.py font size | 1 | MEDIUM |

**TOTAL DEVIATIONS: 28**

---

## 6. RECOMMENDED ACTION SEQUENCE

1. **L01_overview.tex structural fixes** (Fixes 1, 2, 11)
   - Add Outline slide
   - Add PMSP sections
   - Add Practice section

2. **Both tex files - metadata fixes** (Fixes 3, 4, 5)
   - Fix author field
   - Add date
   - Fix package order

3. **Both tex files - chart width fixes** (Fixes 6, 7)
   - Update all chart widths per table

4. **L01_deepdive.tex - comment fixes** (Fixes 13-17)
   - Add missing navigation comment
   - Fix abbreviated comments

5. **All chart.py files - template compliance** (Fixes 8, 9, 10)
   - Add spine settings
   - Add URL annotations
   - Fix font size in flowchart

6. **Recompile and validate** (see verification commands)

---

## 7. VERIFICATION COMMANDS (MANDATORY)

### Step 1: Compile slides to verify fixes
```bash
cd slides/L01_Introduction_Linear_Regression
pdflatex -interaction=nonstopmode L01_overview.tex
pdflatex -interaction=nonstopmode L01_deepdive.tex
```

Check for errors in the output. Both compilations must succeed.

### Step 2: Rebuild all charts
```bash
python infrastructure/course_cli.py build charts --topic L01
```

### Step 3: Validate LaTeX (strict mode)
```bash
python infrastructure/course_cli.py validate latex --strict
```

**MUST PASS**: Zero overflow warnings.

### Step 4: Full audit
```bash
python run_audit.py
```

### Step 5: Visual verification
Open the compiled PDFs and verify:
- [ ] Outline slide appears after title in overview
- [ ] Sections appear in both slide navigation and tableofcontents
- [ ] Chart widths look appropriate (not too small or stretched)
- [ ] Practice sections have placeholder Colab links
- [ ] Charts show GitHub URL in bottom-right corner

---

## 8. NOTES AND DECISIONS

### Section Naming in Deepdive (INTENTIONAL DEVIATION)
The L01_deepdive.tex uses custom section names (Mathematical Foundations, Gradient Descent, etc.) instead of generic PMSP names. This is an **intentional deviation** because:
- Deep dive content is more technical and benefits from specific section names
- Students can navigate to specific topics more easily
- The overview file should use PMSP structure for consistency

### Colab Notebook URLs
Currently marked as **[TBD]**. Need to:
1. Create the L01 Colab notebook if not exists
2. Upload to course Google Drive
3. Generate shareable link
4. Update both tex files with actual URL

### 3D Plot and XKCD Image Widths
Using 0.55\textwidth instead of 0.65\textwidth for:
- 02_multiple_regression_3d (3D aspect ratio preservation)
- XKCD images (original image aspect ratios)

This is a justified deviation from the standard chart width.

---

**Plan Status:** Ready for execution
**Estimated Fix Time:** 2-3 hours
**Risk Level:** Low (cosmetic and structural changes only)
**Compilation Test:** MANDATORY before declaring complete
