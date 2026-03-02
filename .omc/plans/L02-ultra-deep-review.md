# L02 Ultra Deep Review Plan

## Executive Summary

This plan documents all template deviations found in L02 (Logistic Regression) slides and charts, with pattern-based fix instructions. Analysis covers both overview and deepdive slides, all 7 chart.py files, and content-level assessment.

---

## PART 1: TEMPLATE DEVIATIONS FOUND

### 1.1 L02_overview.tex Deviations

| # | Deviation | Template Requires | L02 Has | Severity |
|---|-----------|-------------------|---------|----------|
| 1 | **Comment: Title information** | `% Title information` | `% Title` | LOW |
| 2 | **Author field suffix** | `\author{Methods and Algorithms}` | `\author{Methods and Algorithms -- MSc Data Science}` | MEDIUM |
| 3 | **Date field empty** | `\date{Spring 2026}` | `\date{}` | MEDIUM |
| 4 | **Missing Outline slide** | Must have `\begin{frame}{Outline}\n  \tableofcontents\n\end{frame}` after title frame | Missing entirely | HIGH |
| 5 | **Missing PMSP sections** | Must have `\section{Problem}`, `\section{Method}`, `\section{Solution}`, `\section{Practice}`, `\section{Decision Framework}`, `\section{Summary}` | Missing all `\section{}` declarations | HIGH |
| 6 | **Missing Practice frame with Colab** | Template requires hands-on exercise frame with Colab link | Missing Practice section entirely | HIGH |
| 7 | **Missing References frame** | Template has References frame at end | Missing | MEDIUM |
| 8 | **Chart width inconsistency** | 0.65\textwidth for chart-only, 0.55\textwidth with text | Uses 0.48\textwidth (ROC), 0.6\textwidth (PR, Confusion) | MEDIUM |

### 1.2 L02_deepdive.tex Deviations

| # | Deviation | Template Requires | L02 Has | Severity |
|---|-----------|-------------------|---------|----------|
| 1 | **Comment: Title information** | `% Title information` | `% Title` | LOW |
| 2 | **Author field suffix** | `\author{Methods and Algorithms}` | `\author{Methods and Algorithms -- MSc Data Science}` | MEDIUM |
| 3 | **Date field empty** | `\date{Spring 2026}` | `\date{}` | MEDIUM |
| 4 | **Missing Outline slide** | Must have `\begin{frame}{Outline}\n  \tableofcontents\n\end{frame}` after title frame | Missing entirely | HIGH |
| 5 | **Missing template PMSP sections** | Must have `\section{Problem}`, `\section{Practice}`, `\section{Decision Framework}` | Has: Mathematical Foundations, Decision Boundaries, Evaluation Metrics, Regularization, Implementation, Practical Considerations, Summary - but missing Problem, Practice, Decision Framework as distinct sections | MEDIUM |
| 6 | **Missing Practice frame with Colab** | Template requires hands-on exercise frame with Colab link | Missing Practice section entirely | HIGH |
| 7 | **Extra packages** | Template has specific package list | Has extra: `\usepackage{algorithm}`, `\usepackage{algorithmic}` | LOW (acceptable) |
| 8 | **Chart width inconsistency** | 0.65\textwidth for chart-only, 0.55\textwidth with text | Uses 0.45\textwidth (ROC), 0.6\textwidth (Decision flowchart) | MEDIUM |

### 1.3 Chart.py Deviations (ALL 7 FILES)

| Chart | Missing `axes.spines.top/right: False` | Missing URL figtext | Font size issue |
|-------|---------------------------------------|---------------------|-----------------|
| 01_sigmoid_function | YES | YES | OK (14) |
| 02_decision_boundary | YES | YES | OK (14) |
| 03_log_loss | YES | YES | OK (14) |
| 04_roc_curve | YES | YES | OK (14) |
| 05_precision_recall | YES | YES | OK (14) |
| 06_confusion_matrix | YES | YES | OK (14) |
| 07_decision_flowchart | YES | YES | OK (14) |

**Common Chart.py Deviations:**

1. **Missing spine removal in rcParams**: All charts missing:
   ```python
   'axes.spines.top': False,
   'axes.spines.right': False,
   ```

2. **Missing URL annotation**: All charts missing the figtext URL annotation:
   ```python
   plt.figtext(0.99, 0.01, CHART_METADATA['url'],
               fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
   ```
   - Note: Some charts use `ax.text()` with transform but not in the template's figtext style

---

## PART 2: SPECIFIC FIX INSTRUCTIONS

### 2.1 L02_overview.tex Fixes

**Fix 1: Comment - Title information**
```
OLD: % Title
NEW: % Title information
```

**Fix 2: Author field**
```
OLD: \author{Methods and Algorithms -- MSc Data Science}
NEW: \author{Methods and Algorithms}
```

**Fix 3: Date field**
```
OLD: \date{}
NEW: \date{Spring 2026}
```

**Fix 4: Add Outline slide after title frame**
Insert after `\end{frame}` of title slide (after line 62):
```latex
% Outline
\begin{frame}{Outline}
  \tableofcontents
\end{frame}
```

**Fix 5: Add PMSP section declarations**
The content needs to be reorganized into PMSP structure:
- Add `\section{Problem}` before "Why Logistic Regression?" frame
- Add `\section{Method}` before "The Sigmoid Function" frame
- Add `\section{Solution}` before "ROC Curve and AUC" frame
- Add `\section{Practice}` and create new Practice frame with Colab link
- Add `\section{Decision Framework}` before "When to Use Logistic Regression" frame
- Add `\section{Summary}` at end

**Fix 6: Add Practice frame**
Insert before Decision Framework section:
```latex
\section{Practice}

\begin{frame}[t]{Hands-on Exercise}
  \textbf{Open the Colab Notebook}

  \begin{itemize}
    \item Exercise 1: Implement logistic regression from scratch
    \item Exercise 2: Train model on credit scoring data
    \item Exercise 3: Evaluate with ROC curve and confusion matrix
  \end{itemize}

  \vspace{1em}
  \textbf{Link:} \url{https://colab.research.google.com/...}
\end{frame}
```

**Fix 7: Add References frame**
Add before `\end{document}`:
```latex
\begin{frame}[t]{References}
  \footnotesize
  \begin{itemize}
    \item James et al. (2021). \textit{Introduction to Statistical Learning}. \url{https://www.statlearning.com/}
    \item Hastie et al. (2009). \textit{Elements of Statistical Learning}. \url{https://hastie.su.domains/ElemStatLearn/}
  \end{itemize}
\end{frame}
```

**Fix 8: Standardize chart widths**
```
OLD: \includegraphics[width=0.48\textwidth]{04_roc_curve/chart.pdf}
NEW: \includegraphics[width=0.65\textwidth]{04_roc_curve/chart.pdf}

OLD: \includegraphics[width=0.6\textwidth]{05_precision_recall/chart.pdf}
NEW: \includegraphics[width=0.65\textwidth]{05_precision_recall/chart.pdf}

OLD: \includegraphics[width=0.6\textwidth]{06_confusion_matrix/chart.pdf}
NEW: \includegraphics[width=0.65\textwidth]{06_confusion_matrix/chart.pdf}
```

### 2.2 L02_deepdive.tex Fixes

**Fix 1: Comment - Title information**
```
OLD: % Title
NEW: % Title information
```

**Fix 2: Author field**
```
OLD: \author{Methods and Algorithms -- MSc Data Science}
NEW: \author{Methods and Algorithms}
```

**Fix 3: Date field**
```
OLD: \date{}
NEW: \date{Spring 2026}
```

**Fix 4: Add Outline slide after title frame**
Insert after `\end{frame}` of title slide (after line 64):
```latex
% Outline
\begin{frame}{Outline}
  \tableofcontents
\end{frame}
```

**Fix 5: Restructure sections to include Problem and Practice**
The deepdive has good topical sections but needs:
- Rename/restructure first section to include Problem context
- Add Practice section with Colab exercises
- Ensure Decision Framework section exists (currently in "Practical Considerations")

**Fix 6: Add Practice section**
Insert before Summary section:
```latex
\section{Practice}

\begin{frame}[t]{Hands-on Exercises}
  \textbf{Open the Colab Notebook}

  \begin{itemize}
    \item Exercise 1: Implement gradient descent for logistic regression
    \item Exercise 2: Compare L1, L2, and Elastic Net regularization
    \item Exercise 3: Build credit scoring model with threshold optimization
    \item Exercise 4: Generate ROC and PR curves, interpret results
  \end{itemize}

  \vspace{1em}
  \textbf{Link:} \url{https://colab.research.google.com/...}
\end{frame}
```

**Fix 7: Standardize chart widths**
```
OLD: \includegraphics[width=0.45\textwidth]{04_roc_curve/chart.pdf}
NEW: \includegraphics[width=0.65\textwidth]{04_roc_curve/chart.pdf}

OLD: \includegraphics[width=0.6\textwidth]{07_decision_flowchart/chart.pdf}
NEW: \includegraphics[width=0.65\textwidth]{07_decision_flowchart/chart.pdf}
```

### 2.3 Chart.py Fixes (Apply to ALL 7 files)

**Fix 1: Add spine removal to rcParams**
In every chart.py, change:
```python
plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150
})
```
TO:
```python
plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False,
})
```

**Fix 2: Add URL figtext annotation**
In every chart.py, add before `plt.tight_layout()`:
```python
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
```

**Affected files:**
1. `slides/L02_Logistic_Regression/01_sigmoid_function/chart.py`
2. `slides/L02_Logistic_Regression/02_decision_boundary/chart.py`
3. `slides/L02_Logistic_Regression/03_log_loss/chart.py`
4. `slides/L02_Logistic_Regression/04_roc_curve/chart.py`
5. `slides/L02_Logistic_Regression/05_precision_recall/chart.py`
6. `slides/L02_Logistic_Regression/06_confusion_matrix/chart.py`
7. `slides/L02_Logistic_Regression/07_decision_flowchart/chart.py`

---

## PART 3: CHART AUDIT

### 3.1 Chart Inventory

| # | Chart Name | Purpose | Used in Overview | Used in Deepdive |
|---|------------|---------|------------------|------------------|
| 1 | 01_sigmoid_function | Logistic activation function visualization | Yes (0.55) | Yes (0.55) |
| 2 | 02_decision_boundary | Linear decision boundary with contours | Yes (0.65) | Yes (0.55) |
| 3 | 03_log_loss | Cross-entropy loss curves | Yes (0.55) | Yes (0.55) |
| 4 | 04_roc_curve | ROC curves comparison | Yes (0.48 - WRONG) | Yes (0.45 - WRONG) |
| 5 | 05_precision_recall | PR curves for imbalanced data | Yes (0.6 - WRONG) | Yes (0.55) |
| 6 | 06_confusion_matrix | Classification results heatmap | Yes (0.6 - WRONG) | Yes (0.55) |
| 7 | 07_decision_flowchart | When to use logistic regression | Yes (0.65) | Yes (0.6 - WRONG) |

### 3.2 Chart Width Summary

**Overview widths that need fixing:**
- 04_roc_curve: 0.48 -> 0.65 (chart-only slide)
- 05_precision_recall: 0.6 -> 0.65 (chart-only slide)
- 06_confusion_matrix: 0.6 -> 0.65 (chart-only slide)

**Deepdive widths that need fixing:**
- 04_roc_curve: 0.45 -> 0.65 (chart-only slide)
- 07_decision_flowchart: 0.6 -> 0.65 (chart-only slide)

### 3.3 Chart Count Assessment

- **Total charts available:** 7
- **Overview uses:** 7 charts
- **Deepdive uses:** 7 charts
- **Assessment:** ADEQUATE - matches expectations for ~7-8 charts per topic

---

## PART 4: CONTENT LEVEL AUDIT

### 4.1 MSc Level Assessment

| Criterion | Status | Notes |
|-----------|--------|-------|
| **Mathematical rigor** | EXCELLENT | Proper notation, MLE derivation, gradient formulas |
| **Theoretical depth** | EXCELLENT | Log-odds interpretation, convexity of loss, calibration |
| **Practical application** | EXCELLENT | Credit scoring, fraud detection, regulatory compliance |
| **No prerequisites assumed** | GOOD | Explains basic probability concepts, builds from linear regression |
| **Industry relevance** | EXCELLENT | Basel compliance, interpretability requirements |

### 4.2 Missing Prerequisite Explanations

The content assumes familiarity with:
1. **Matrix notation** - Used without explanation (acceptable for MSc)
2. **Gradient descent basics** - Referenced from L01 (appropriate)
3. **Basic probability** - P(y=1|x) notation introduced clearly

**Assessment:** Content is MSc-appropriate. Builds appropriately on L01 (linear regression) foundation.

### 4.3 Finance/Banking Application Coverage

| Application | Covered | Location |
|-------------|---------|----------|
| Credit default prediction | YES | Throughout |
| Fraud detection | YES | Threshold selection, imbalanced classes |
| Regulatory compliance (interpretability) | YES | Model interpretation, coefficient analysis |
| Cost-sensitive classification | YES | FP vs FN costs, threshold tuning |

---

## PART 5: PURPOSE AUDIT

### 5.1 L02_overview.tex Slide Purposes

| Slide | Frame Title | Purpose | Verdict |
|-------|-------------|---------|---------|
| 1 | Title | Course identification | OK |
| 2 | Learning Objectives | Set expectations | OK |
| 3 | Why Logistic Regression? | Motivation, business context | OK |
| 4 | The Sigmoid Function | Core mathematical concept | OK |
| 5 | Decision Boundary | Visual understanding of classification | OK |
| 6 | Binary Cross-Entropy Loss | Why this loss function | OK |
| 7 | ROC Curve and AUC | Model evaluation | OK |
| 8 | Precision-Recall Trade-off | Imbalanced data handling | OK |
| 9 | Confusion Matrix | Results interpretation | OK |
| 10 | When to Use Logistic Regression | Decision framework | OK |

**Missing critical slides:**
- Outline slide (navigation)
- Practice slide (hands-on learning)
- References slide (academic integrity)

### 5.2 L02_deepdive.tex Slide Purposes

| Section | Slides | Purpose | Verdict |
|---------|--------|---------|---------|
| Mathematical Foundations | 7 | Deep math understanding | OK |
| Decision Boundaries | 4 | Feature engineering, multiclass | OK |
| Evaluation Metrics | 8 | Comprehensive metrics coverage | OK |
| Regularization | 4 | Overfitting prevention | OK |
| Implementation | 5 | Practical coding guidance | OK |
| Practical Considerations | 4 | Production deployment | OK |
| Summary | 2 | Key takeaways, references | OK |

**Missing critical sections/slides:**
- Outline slide (navigation)
- Problem section (PMSP framework)
- Practice section with Colab exercises

### 5.3 Redundancy Check

**Potential redundancies between overview and deepdive:**
- Sigmoid function appears in both (acceptable - overview intro, deepdive details)
- Decision boundary appears in both (acceptable - overview visual, deepdive math)
- ROC curve appears in both (acceptable - overview intro, deepdive interpretation)

**Assessment:** No problematic redundancy. Deepdive appropriately expands on overview concepts.

---

## PART 6: DEVIATION SUMMARY

### Total Deviations by Category

| Category | Count | Critical |
|----------|-------|----------|
| LaTeX Template (Overview) | 8 | 3 (Outline, Sections, Practice) |
| LaTeX Template (Deepdive) | 8 | 2 (Outline, Practice) |
| Chart.py Template | 14 (2 per file x 7 files) | 0 |
| **TOTAL** | **30** | **5** |

### Priority Fix Order

1. **CRITICAL - Structural:**
   - Add Outline slides to both files
   - Add PMSP section declarations to overview
   - Add Practice section with Colab to both files

2. **MEDIUM - Metadata:**
   - Fix author field in both files
   - Fix date field in both files
   - Standardize chart widths in both files

3. **LOW - Formatting:**
   - Fix "% Title" comments to "% Title information"
   - Add spine removal to all chart.py rcParams
   - Add URL figtext to all chart.py files

---

## PART 7: TASK LIST

### Phase 1: LaTeX Structural Fixes (Critical)

- [ ] **TASK-1**: Add Outline slide to L02_overview.tex after title frame
- [ ] **TASK-2**: Add PMSP section declarations to L02_overview.tex
- [ ] **TASK-3**: Add Practice frame with Colab link to L02_overview.tex
- [ ] **TASK-4**: Add References frame to L02_overview.tex
- [ ] **TASK-5**: Add Outline slide to L02_deepdive.tex after title frame
- [ ] **TASK-6**: Add Practice frame with Colab link to L02_deepdive.tex

### Phase 2: LaTeX Metadata Fixes (Medium)

- [ ] **TASK-7**: Fix author field in L02_overview.tex (remove "-- MSc Data Science")
- [ ] **TASK-8**: Fix date field in L02_overview.tex (add "Spring 2026")
- [ ] **TASK-9**: Fix author field in L02_deepdive.tex (remove "-- MSc Data Science")
- [ ] **TASK-10**: Fix date field in L02_deepdive.tex (add "Spring 2026")

### Phase 3: Chart Width Standardization (Medium)

- [ ] **TASK-11**: Fix ROC curve width in L02_overview.tex (0.48 -> 0.65)
- [ ] **TASK-12**: Fix PR curve width in L02_overview.tex (0.6 -> 0.65)
- [ ] **TASK-13**: Fix confusion matrix width in L02_overview.tex (0.6 -> 0.65)
- [ ] **TASK-14**: Fix ROC curve width in L02_deepdive.tex (0.45 -> 0.65)
- [ ] **TASK-15**: Fix decision flowchart width in L02_deepdive.tex (0.6 -> 0.65)

### Phase 4: LaTeX Comment Fixes (Low)

- [ ] **TASK-16**: Fix "% Title" to "% Title information" in L02_overview.tex
- [ ] **TASK-17**: Fix "% Title" to "% Title information" in L02_deepdive.tex

### Phase 5: Chart.py Fixes (Low)

- [ ] **TASK-18**: Add `'axes.spines.top': False, 'axes.spines.right': False` to 01_sigmoid_function/chart.py
- [ ] **TASK-19**: Add `'axes.spines.top': False, 'axes.spines.right': False` to 02_decision_boundary/chart.py
- [ ] **TASK-20**: Add `'axes.spines.top': False, 'axes.spines.right': False` to 03_log_loss/chart.py
- [ ] **TASK-21**: Add `'axes.spines.top': False, 'axes.spines.right': False` to 04_roc_curve/chart.py
- [ ] **TASK-22**: Add `'axes.spines.top': False, 'axes.spines.right': False` to 05_precision_recall/chart.py
- [ ] **TASK-23**: Add `'axes.spines.top': False, 'axes.spines.right': False` to 06_confusion_matrix/chart.py
- [ ] **TASK-24**: Add `'axes.spines.top': False, 'axes.spines.right': False` to 07_decision_flowchart/chart.py
- [ ] **TASK-25**: Add URL figtext annotation to 01_sigmoid_function/chart.py
- [ ] **TASK-26**: Add URL figtext annotation to 02_decision_boundary/chart.py
- [ ] **TASK-27**: Add URL figtext annotation to 03_log_loss/chart.py
- [ ] **TASK-28**: Add URL figtext annotation to 04_roc_curve/chart.py
- [ ] **TASK-29**: Add URL figtext annotation to 05_precision_recall/chart.py
- [ ] **TASK-30**: Add URL figtext annotation to 06_confusion_matrix/chart.py
- [ ] **TASK-31**: Add URL figtext annotation to 07_decision_flowchart/chart.py

### Phase 6: Regeneration & Validation

- [ ] **TASK-32**: Regenerate all chart PDFs after chart.py fixes
- [ ] **TASK-33**: Compile L02_overview.tex and verify no overflow warnings
- [ ] **TASK-34**: Compile L02_deepdive.tex and verify no overflow warnings
- [ ] **TASK-35**: Run full validation: `python infrastructure/course_cli.py validate --all`

---

## Acceptance Criteria

1. Both .tex files have correct `\author{Methods and Algorithms}` (no suffix)
2. Both .tex files have `\date{Spring 2026}`
3. Both .tex files have Outline slide with `\tableofcontents`
4. L02_overview.tex has all 6 PMSP sections declared
5. Both .tex files have Practice frame with Colab link placeholder
6. All chart widths follow 0.55/0.65 rule consistently
7. All 7 chart.py files have spine removal in rcParams
8. All 7 chart.py files have URL figtext annotation
9. LaTeX compilation produces zero overflow warnings
10. All chart PDFs regenerated successfully

---

## Commit Strategy

**Commit 1: LaTeX structural fixes**
- Add Outline slides
- Add section declarations
- Add Practice and References frames
Message: "L02: Add missing PMSP structure, Outline, Practice, References"

**Commit 2: LaTeX metadata fixes**
- Fix author, date, comments
- Fix chart widths
Message: "L02: Fix template metadata and chart widths"

**Commit 3: Chart.py fixes**
- Add spine removal to all charts
- Add URL figtext to all charts
Message: "L02: Add template-compliant rcParams and URL annotations to charts"

**Commit 4: Regeneration**
- Regenerate all chart PDFs
- Recompile LaTeX
Message: "L02: Regenerate charts and compile slides"

---

**PLAN_READY: .omc/plans/L02-ultra-deep-review.md**
