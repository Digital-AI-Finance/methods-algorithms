# L01 Ultra-Deep Review Plan - Version 2

**Created:** 2026-02-02
**Status:** CRITICAL FINDINGS - Template Deviations Identified

---

## Executive Summary

Previous analysis incorrectly claimed "100% template compliance". This deep audit reveals **27 specific deviations** from the authoritative template at `templates/beamer_template.tex`.

---

## 1. TEMPLATE DEVIATION AUDIT

### 1.1 Preamble Issues

#### Missing Comment
| Template Line | Template Has | L01_overview.tex Has | L01_deepdive.tex Has | Issue |
|---------------|--------------|----------------------|----------------------|-------|
| Line 16 | `% Custom colors (ML palette)` | `% Custom colors (ML palette)` | `% Custom colors` | **DEVIATION**: deepdive.tex line 16 uses abbreviated comment |

#### Package Order Deviation
| Template (lines 7-14) | L01_overview.tex (lines 7-14) | L01_deepdive.tex (lines 7-14) |
|----------------------|------------------------------|------------------------------|
| `inputenc, fontenc, amsmath, graphicx, booktabs, tikz, hyperref` | `inputenc, fontenc, amsmath, graphicx, booktabs, hyperref, tikz` | `inputenc, fontenc, amsmath, graphicx, booktabs, hyperref, tikz` |

**DEVIATION**: Both L01 files have `hyperref` before `tikz` (lines 13-14 swapped). Template has `tikz` at line 13, `hyperref` at line 14.

#### Footer Comment Deviation
| Template Line 28 | L01_overview.tex Line 28 | L01_deepdive.tex Line 28 |
|------------------|--------------------------|--------------------------|
| `% Footer customization` | `% Footer customization` | `% Footer` |

**DEVIATION**: deepdive.tex uses abbreviated comment "% Footer" instead of "% Footer customization"

#### Custom Commands Comment Deviation
| Template Line 47 | L01_overview.tex Line 47 | L01_deepdive.tex Line 46 |
|------------------|--------------------------|--------------------------|
| `% Custom commands` | `% Custom commands` | `% Commands` |

**DEVIATION**: deepdive.tex uses abbreviated comment "% Commands" instead of "% Custom commands"

#### Title Comment Deviation
| Template Line 52 | L01_overview.tex | L01_deepdive.tex Line 51 |
|------------------|------------------|--------------------------|
| `% Title information` | `% Title information` | `% Title` |

**DEVIATION**: deepdive.tex uses abbreviated "% Title" instead of "% Title information"

### 1.2 Author Field Deviation

| Template Line 55 | Both L01 Files Line 55/54 |
|------------------|---------------------------|
| `\author{Methods and Algorithms}` | `\author{Methods and Algorithms -- MSc Data Science}` |

**DEVIATION**: Both files add "-- MSc Data Science" to author field which is redundant since `\institute{MSc Data Science}` already exists.

### 1.3 Date Field Deviation

| Template Line 57 | Both L01 Files |
|------------------|----------------|
| `\date{Spring 2026}` | `\date{}` |

**DEVIATION**: Both files use empty date instead of "Spring 2026".

### 1.4 Missing Structural Elements

#### Missing Outline Slide in Overview
| Template | L01_overview.tex |
|----------|------------------|
| Has `\begin{frame}{Outline} \tableofcontents \end{frame}` at lines 66-69 | **MISSING** - No outline/tableofcontents slide |

**CRITICAL DEVIATION**: L01_overview.tex does not have a `\tableofcontents` slide after title. Template requires this.

#### Missing PMSP Section Organization in Overview
| Template Sections | L01_overview.tex Sections |
|-------------------|---------------------------|
| Problem, Method, Solution, Practice, Decision Framework, Summary | **NO SECTIONS DEFINED** |

**CRITICAL DEVIATION**: L01_overview.tex has NO `\section{}` commands. Template explicitly requires PMSP sections with comments like:
```latex
% ============================================
% SECTION: Problem (PMSP)
% ============================================
\section{Problem}
```

L01_overview.tex just has individual frames without section organization.

### 1.5 Deepdive Section Naming Deviations

| Template Section Names | L01_deepdive.tex Section Names |
|------------------------|--------------------------------|
| Problem | Mathematical Foundations |
| Method | Gradient Descent |
| Solution | Model Evaluation |
| Practice | Regularization |
| Decision Framework | Bias-Variance Tradeoff |
| Summary | Decision Framework, Summary |

**DEVIATION**: L01_deepdive.tex uses custom section names instead of PMSP framework. While sections exist, they don't follow the Problem-Method-Solution-Practice structure mandated by template.

### 1.6 Frame Title Style Deviations

| Template Pattern | L01 Files Pattern |
|------------------|-------------------|
| `\begin{frame}[t]{Title}` | Mixed - some have `[t]`, some don't |

**Finding**: Both files consistently use `[t]` option - this is CORRECT.

### 1.7 Missing References Frame Structure

| Template Line 215-221 | L01_overview.tex | L01_deepdive.tex |
|-----------------------|------------------|------------------|
| Dedicated `\section{References}` implied | No separate section | No separate section |
| `\footnotesize` for reference text | Uses `\footnotesize` | Uses `\footnotesize` |

**Finding**: References are embedded in Key Takeaways frame in overview, separate frame in deepdive. Template has standalone References frame - structure differs.

---

## 2. CHART WIDTH AUDIT

### Template Requirements (from CLAUDE.md):
- **0.55\textwidth**: Charts WITH accompanying text on same slide
- **0.65\textwidth**: Chart-ONLY slides (no text except bottomnote)

### L01_overview.tex Chart Widths

| Chart | Current Width | Slide Has Text? | Correct Width | STATUS |
|-------|---------------|-----------------|---------------|--------|
| 01_simple_regression/chart.pdf | 0.50\textwidth | Yes (bottomnote only) | 0.65\textwidth | **WRONG** |
| 02_multiple_regression_3d/chart.pdf | 0.42\textwidth | Yes (bottomnote only) | 0.65\textwidth | **WRONG** |
| images/1725_linear_regression.png | 0.55\textwidth | Yes (bottomnote) | 0.65\textwidth | **WRONG** |
| 04_gradient_descent/chart.pdf | 0.45\textwidth | Yes (bottomnote only) | 0.65\textwidth | **WRONG** |
| 03_residual_plots/chart.pdf | 0.50\textwidth | Yes (bottomnote only) | 0.65\textwidth | **WRONG** |
| 05_learning_curves/chart.pdf | 0.50\textwidth | Yes (bottomnote only) | 0.65\textwidth | **WRONG** |
| images/2048_curve_fitting.png | 0.32\textwidth | Yes (bottomnote) | 0.65\textwidth | **WRONG** |
| 06_regularization_comparison/chart.pdf | 0.50\textwidth | Yes (bottomnote only) | 0.65\textwidth | **WRONG** |
| 07_bias_variance/chart.pdf | 0.50\textwidth | Yes (bottomnote only) | 0.65\textwidth | **WRONG** |
| images/605_extrapolating.png | 0.50\textwidth | Yes (bottomnote) | 0.65\textwidth | **WRONG** |
| 08_decision_flowchart/chart.pdf | 0.45\textwidth | Yes (bottomnote only) | 0.65\textwidth | **WRONG** |

**CRITICAL FINDING**: ALL 11 charts in L01_overview.tex use incorrect widths. Chart-only slides (with just bottomnote) should use 0.65\textwidth.

### L01_deepdive.tex Chart Widths

| Chart | Current Width | Slide Has Text? | Correct Width | STATUS |
|-------|---------------|-----------------|---------------|--------|
| 01_simple_regression/chart.pdf | 0.55\textwidth | Yes (bottomnote only) | 0.65\textwidth | **WRONG** |
| 02_multiple_regression_3d/chart.pdf | 0.42\textwidth | Yes (bottomnote only) | 0.65\textwidth | **WRONG** |
| 04_gradient_descent/chart.pdf | 0.55\textwidth | Yes (bottomnote only) | 0.65\textwidth | **WRONG** |
| 03_residual_plots/chart.pdf | 0.55\textwidth | Yes (bottomnote only) | 0.65\textwidth | **WRONG** |
| 05_learning_curves/chart.pdf | 0.55\textwidth | Yes (bottomnote only) | 0.65\textwidth | **WRONG** |
| 06_regularization_comparison/chart.pdf | 0.55\textwidth | Yes (bottomnote only) | 0.65\textwidth | **WRONG** |
| 07_bias_variance/chart.pdf | 0.55\textwidth | Yes (bottomnote only) | 0.65\textwidth | **WRONG** |
| 08_decision_flowchart/chart.pdf | 0.50\textwidth | Yes (bottomnote only) | 0.65\textwidth | **WRONG** |

**CRITICAL FINDING**: ALL 8 charts in L01_deepdive.tex use incorrect widths.

---

## 3. CHART.PY TEMPLATE COMPLIANCE

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

### Chart.py Audit

| Chart | Has spines.top: False? | Has spines.right: False? | Has GitHub URL? | STATUS |
|-------|------------------------|--------------------------|-----------------|--------|
| 01_simple_regression | NO | NO | NO | **MISSING SETTINGS** |
| 02_multiple_regression_3d | NO | NO | NO | **MISSING SETTINGS** |
| 03_residual_plots | Need to verify | Need to verify | Need to verify | CHECK |
| 04_gradient_descent | Need to verify | Need to verify | Need to verify | CHECK |
| 05_learning_curves | Need to verify | Need to verify | Need to verify | CHECK |
| 06_regularization_comparison | Need to verify | Need to verify | Need to verify | CHECK |
| 07_bias_variance | Need to verify | Need to verify | Need to verify | CHECK |
| 08_decision_flowchart | NO | NO | NO | **MISSING SETTINGS** (also uses font.size: 11 instead of 14) |

**DEVIATION FOUND**:
1. Chart 01 and 02 are missing `axes.spines.top: False` and `axes.spines.right: False`
2. Chart 01 and 02 are missing the GitHub URL text annotation in bottom-right
3. Chart 08 uses `font.size: 11` instead of template's `font.size: 14`

---

## 4. CHART COUNT AUDIT

### Expected (from CLAUDE.md): 7-8 charts per topic

| Deck | Generated Charts (.py) | External Images | Total Visuals |
|------|------------------------|-----------------|---------------|
| L01_overview.tex | 8 used | 3 XKCD images | 11 total |
| L01_deepdive.tex | 8 used | 0 | 8 total |

**FINDING**: Chart count is adequate (8 charts). However, some charts are reused between overview and deepdive.

### Chart Reuse Analysis

| Chart | Used in Overview? | Used in Deepdive? |
|-------|-------------------|-------------------|
| 01_simple_regression | Yes | Yes |
| 02_multiple_regression_3d | Yes | Yes |
| 03_residual_plots | Yes | Yes |
| 04_gradient_descent | Yes | Yes |
| 05_learning_curves | Yes | Yes |
| 06_regularization_comparison | Yes | Yes |
| 07_bias_variance | Yes | Yes |
| 08_decision_flowchart | Yes | Yes |

**OBSERVATION**: All 8 charts are reused in both decks. This may be intentional for reinforcement but reduces unique content per deck.

---

## 5. MSc LEVEL CONTENT AUDIT

### Prerequisites Check

| Topic | Assumes Prior Knowledge? | Appropriate for No Prerequisites? |
|-------|--------------------------|-----------------------------------|
| Matrix notation | Yes - Linear algebra | **CONCERN**: May need brief intro |
| Calculus (derivatives) | Yes | **CONCERN**: Gradient derivation assumes calculus |
| Statistics basics | Yes - means, variance | Acceptable for MSc |
| Programming | No explicit code shown | OK |

### Depth Assessment

| Aspect | Level | Assessment |
|--------|-------|------------|
| Mathematical rigor | High | Appropriate for MSc |
| Derivations shown | Complete | Excellent |
| Practical applications | Good | Finance examples present |
| Conceptual explanations | Good | But could explain matrix operations |

**RECOMMENDATION**: Add 1-2 slides on "Matrix Notation Refresher" in deepdive for students rusty on linear algebra.

---

## 6. SLIDE PURPOSE AUDIT

### L01_overview.tex - Slide-by-Slide

| Slide # | Title | Purpose Clear? | Serves Learning Objective? | Issues |
|---------|-------|----------------|---------------------------|--------|
| 1 | Title | Yes | N/A | - |
| 2 | Learning Objectives | Yes | Sets expectations | - |
| 3 | The Art of Fitting Lines (XKCD) | **WEAK** | Humor but no learning value | Consider moving to end |
| 4 | The Business Problem | Yes | Motivates topic | - |
| 5 | What is Linear Regression? | Yes | Core concept | - |
| 6 | Simple Linear Regression | Yes | Visualization | - |
| 7 | Multiple Linear Regression | Yes | Extension | - |
| 8 | The Optimization Problem | Yes | Math foundation | - |
| 9 | Two Solution Approaches | Yes | Methods | - |
| 10 | Gradient Descent in Action | Yes | Visualization | - |
| 11 | Interpreting Coefficients | Yes | Business relevance | - |
| 12 | Model Evaluation | Yes | Metrics | - |
| 13 | Residual Diagnostics | Yes | Model validation | - |
| 14 | Learning Curves | Yes | Overfitting detection | - |
| 15 | When to Use Linear Regression | Yes | Decision framework | - |
| 16 | The Danger of Overfitting (XKCD) | **WEAK** | Humor, disrupts flow | Consider integrating with regularization |
| 17 | Regularization: Ridge vs Lasso | Yes | Advanced technique | - |
| 18 | Bias-Variance Tradeoff | Yes | Core concept | - |
| 19 | A Word of Caution (XKCD) | **WEAK** | Humor at end | Appropriate position |
| 20 | Decision Framework | Yes | Summary flowchart | - |
| 21 | Key Takeaways | Yes | Wrap-up | - |

**ISSUES IDENTIFIED**:
1. XKCD slides (3, 16, 19) break pedagogical flow
2. No Outline slide (template requires one)
3. No Practice section with hands-on exercise (template requires this)
4. No clear PMSP structure

### L01_deepdive.tex - Slide-by-Slide

| Slide # | Title | Purpose | Issues |
|---------|-------|---------|--------|
| 1-2 | Title, Outline | Setup | **HAS OUTLINE - GOOD** |
| 3-6 | Matrix Notation through Normal Eq | Math Foundation | Excellent |
| 7-8 | Visualizations | Reinforcement | - |
| 9-16 | Gradient Descent section | Algorithm details | Excellent |
| 17-23 | Model Evaluation | Metrics deep dive | Good |
| 24-30 | Regularization | Advanced methods | Good |
| 31-34 | Bias-Variance | Theory | Good |
| 35-38 | Decision Framework, Summary | Wrap-up | Good |

**ISSUES IDENTIFIED**:
1. No Practice section with Colab link (template requires this)
2. Section names don't follow PMSP

---

## 7. SPECIFIC FIXES REQUIRED

### Priority 1: Critical Template Deviations

1. **L01_overview.tex - Add Outline slide after title** (lines 65-68)
   ```latex
   \begin{frame}{Outline}
     \tableofcontents
   \end{frame}
   ```

2. **L01_overview.tex - Add PMSP sections**
   - Add `\section{Problem}` before "The Business Problem"
   - Add `\section{Method}` before "What is Linear Regression?"
   - Add `\section{Solution}` before "Interpreting Coefficients"
   - Add `\section{Practice}` - CREATE NEW PRACTICE SECTION
   - Add `\section{Decision Framework}` before "When to Use"
   - Add `\section{Summary}` before "Key Takeaways"

3. **Both files - Fix author field**
   ```latex
   \author{Methods and Algorithms}  % Remove "-- MSc Data Science"
   ```

4. **Both files - Add date**
   ```latex
   \date{Spring 2026}
   ```

5. **Both files - Fix package order** (lines 13-14)
   ```latex
   \usepackage{tikz}
   \usepackage{hyperref}
   ```

### Priority 2: Chart Width Fixes

6. **L01_overview.tex - Update all chart-only slides to 0.65\textwidth**
   - Line 86: `0.55\textwidth` -> `0.65\textwidth`
   - Line 139: `0.50\textwidth` -> `0.65\textwidth`
   - Line 149: `0.42\textwidth` -> `0.65\textwidth` (or `0.55\textwidth` for 3D)
   - Line 221: `0.45\textwidth` -> `0.65\textwidth`
   - Line 273: `0.50\textwidth` -> `0.65\textwidth`
   - Line 283: `0.50\textwidth` -> `0.65\textwidth`
   - Line 332: `0.32\textwidth` -> `0.55\textwidth` (XKCD may be smaller)
   - Line 342: `0.50\textwidth` -> `0.65\textwidth`
   - Line 352: `0.50\textwidth` -> `0.65\textwidth`
   - Line 362: `0.50\textwidth` -> `0.65\textwidth`
   - Line 372: `0.45\textwidth` -> `0.65\textwidth`

7. **L01_deepdive.tex - Update all chart-only slides to 0.65\textwidth**

### Priority 3: Chart.py Template Compliance

8. **All 8 chart.py files - Add missing rcParams**
   ```python
   'axes.spines.top': False,
   'axes.spines.right': False,
   ```

9. **All 8 chart.py files - Add GitHub URL annotation**
   ```python
   ax.text(0.99, 0.01, CHART_METADATA['url'],
           transform=ax.transAxes, fontsize=7, color='gray',
           ha='right', va='bottom', alpha=0.7)
   ```

10. **08_decision_flowchart/chart.py - Fix font size**
    ```python
    'font.size': 14,  # Not 11
    ```

### Priority 4: Content Structure

11. **L01_overview.tex - Add Practice section** with Colab notebook link
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
      \textbf{Link:} \url{https://colab.research.google.com/...}
    \end{frame}
    ```

12. **L01_deepdive.tex - Add Practice section** similarly

### Priority 5: Minor Comment Fixes (deepdive.tex)

13. Line 16: `% Custom colors` -> `% Custom colors (ML palette)`
14. Line 28: `% Footer` -> `% Footer customization`
15. Line 46: `% Commands` -> `% Custom commands`
16. Line 51: `% Title` -> `% Title information`

---

## 8. SUMMARY OF DEVIATIONS

| Category | Count | Severity |
|----------|-------|----------|
| Missing Outline slide | 1 | HIGH |
| Missing PMSP sections (overview) | 1 | HIGH |
| Wrong chart widths | 19 | MEDIUM |
| Package order wrong | 2 | LOW |
| Author field redundant | 2 | LOW |
| Date field empty | 2 | LOW |
| Comment abbreviations | 4 | LOW |
| Missing chart.py settings | 8+ | MEDIUM |
| Missing Practice section | 2 | HIGH |

**TOTAL DEVIATIONS: 27+**

---

## 9. RECOMMENDED ACTION SEQUENCE

1. Fix L01_overview.tex PMSP structure and Outline slide
2. Add Practice sections to both files
3. Update all chart widths in both files
4. Fix author/date fields in both files
5. Fix package order in both files
6. Update all chart.py files with missing rcParams and URLs
7. Fix comment abbreviations in deepdive.tex
8. Recompile all charts and slides
9. Run LaTeX validator with --strict flag

---

## 10. VERIFICATION COMMANDS

```bash
# Validate LaTeX after fixes
python infrastructure/course_cli.py validate latex --strict

# Rebuild all charts
python infrastructure/course_cli.py build charts --topic L01

# Rebuild slides
python infrastructure/course_cli.py build slides --topic L01

# Full audit
python run_audit.py
```

---

**Plan Status:** Ready for execution
**Estimated Fix Time:** 2-3 hours
**Risk Level:** Low (cosmetic and structural changes only)
