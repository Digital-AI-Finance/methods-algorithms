# Work Plan: L02 Logistic Regression Self-Study Document

## Context

### Original Request
Create a 5-page self-study LaTeX article (NOT Beamer) for Logistic Regression that MSc Data Science students can read independently. Compile to PDF and deploy to GitHub Pages.

### Research Findings

**Existing L02 Assets (verified):**
- `L02_overview.tex` (Beamer overview, ~17 slides)
- `L02_deepdive.tex` (Beamer deep dive, 41 frames + 8 appendix frames)
- `L02_logreg_mini.tex` (10-slide mini-lecture)
- `L02_logreg_full.tex` (31-frame full technical lecture)
- 7 chart PDFs in subfolders: `01_sigmoid_function/chart.pdf` through `07_decision_flowchart/chart.pdf`
- XKCD image: `images/1132_frequentist_bayesian.png` (NOT to be used in self-study)
- Instructor guide: `L02_instructor_guide.md`

**Content available in deepdive.tex for extraction/adaptation:**
- Full MLE derivation (likelihood, log-likelihood, gradient, chain rule)
- Odds and log-odds interpretation with worked example
- Statistical inference: Wald test, LRT, AIC/BIC, Hosmer-Lemeshow
- Regularization: L1/L2/Elastic Net with formulas
- Newton-Raphson / IRLS optimization
- Credit scoring: Basel PD, Gini coefficient, scorecards, WoE encoding
- Multiclass extension (softmax)

**GH Pages structure (verified):**
- PDFs live at: `docs/slides/pdf/*.pdf`
- L02 section in `docs/index.html` starts at line 163, contains a `cgrid` with cards for Overview PDF, Deep Dive PDF, Mini-Lecture PDF, Full Lecture PDF, Notebook, Dataset
- Card pattern: `<a class="ccard" href="slides/pdf/L02_*.pdf" download><div class="ccard-icon">PDF</div>Label<div class="ccard-label">Description</div></a>`

**Color palette (from existing .tex files):**
- mlpurple: RGB(51,51,178) = #3333B2
- mlblue: RGB(0,102,204) = #0066CC
- mlorange: RGB(255,127,14) = #FF7F0E
- mlgreen: RGB(44,160,44) = #2CA02C
- mlred: RGB(214,39,40) = #D62728

**Chart selection for self-study (4 charts, most pedagogically important):**
1. `01_sigmoid_function/chart.pdf` -- Essential: visualizes the core sigmoid function
2. `04_roc_curve/chart.pdf` -- Essential: key evaluation metric
3. `06_confusion_matrix/chart.pdf` -- Essential: foundation of all classification metrics
4. `03_log_loss/chart.pdf` -- Essential: visualizes the loss function being optimized

**Charts NOT included (to save space for 5-page limit):**
- `02_decision_boundary/chart.pdf` (useful but not critical for reading)
- `05_precision_recall/chart.pdf` (covered textually, ROC chart sufficient)
- `07_decision_flowchart/chart.pdf` (practice-oriented, not theory)

## Work Objectives

### Core Objective
Create `slides/L02_Logistic_Regression/L02_selfstudy.tex`, a self-contained 5-page LaTeX article document that covers logistic regression at MSc depth with mathematical derivations and a credit scoring worked example. Deploy compiled PDF to GitHub Pages.

### Deliverables
1. `slides/L02_Logistic_Regression/L02_selfstudy.tex` -- LaTeX source (article class)
2. `slides/L02_Logistic_Regression/L02_selfstudy.pdf` -- Compiled PDF (exactly 5 pages)
3. `docs/slides/pdf/L02_selfstudy.pdf` -- Copy for GH Pages
4. `docs/index.html` -- Updated with self-study card in L02 section

### Definition of Done
- [ ] LaTeX compiles with 0 errors and 0 Overfull warnings
- [ ] PDF is exactly 5 pages
- [ ] All 4 chart includes resolve correctly (paths relative to .tex location)
- [ ] Document is self-contained (readable without attending lecture)
- [ ] Contains full MLE derivation, gradient, and Newton-Raphson
- [ ] Contains credit scoring worked example with real numbers
- [ ] References section includes ISLR Ch.4, scikit-learn docs, Interpretable ML Book
- [ ] PDF deployed to `docs/slides/pdf/L02_selfstudy.pdf`
- [ ] Card added to `docs/index.html` L02 section

## Must Have / Must NOT Have

### MUST HAVE
- LaTeX `article` document class (NOT beamer)
- Course color palette (mlpurple, mlblue, mlorange, mlgreen, mlred) used for headings and accent
- Geometry package for margin control to hit 5-page target
- Numbered sections with clear hierarchy
- Mathematical content at MSc depth:
  - Sigmoid function definition and properties
  - MLE derivation: likelihood -> log-likelihood -> gradient -> matrix form
  - Newton-Raphson / IRLS update formula
  - Odds ratios and coefficient interpretation
  - Statistical inference: Wald test, LRT (formulas)
  - Regularization: L1/L2 penalty formulas
- Credit scoring worked example:
  - Concrete feature values (income, debt ratio, employment years)
  - Fitted coefficients with actual numbers
  - Odds ratio interpretation with numbers
  - PD calculation for a sample applicant
  - Basel/Gini connection
- 4 chart figures included via `\includegraphics`
- Evaluation metrics: confusion matrix, ROC/AUC, Gini
- References section (not BibTeX -- inline for simplicity)
- Clean article typography: 10pt or 11pt, reasonable margins

### MUST NOT HAVE
- Beamer documentclass or any slide-like formatting
- XKCD images or comic references
- Code listings or Python snippets
- BibTeX compilation requirement (use inline references)
- More than 5 pages
- Overfull hbox/vbox warnings
- Relative paths that break (all chart paths relative to .tex file location)
- Table of contents (wastes space on a 5-page document)

## Task Flow

```
Task 1 (LaTeX document)
    |
    v
Task 2 (Compile + verify)
    |
    v
Task 3 (Deploy to GH Pages + update index.html)
```

All tasks are sequential -- each depends on the previous.

## Detailed Tasks

### Task 1: Create L02_selfstudy.tex
**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L02_Logistic_Regression\L02_selfstudy.tex`
**Agent:** executor-high (opus) -- complex LaTeX document with mathematical content
**Priority:** HIGH

**Acceptance Criteria:**
- Article document class, 10pt or 11pt font
- Geometry package: margins tuned for exactly 5 pages (start with 1in margins, adjust if needed)
- Color definitions matching existing .tex files (mlpurple, mlblue, mlorange, mlgreen, mlred)
- Section headings colored in mlpurple
- Custom `\highlight{}` command using mlorange (matching existing convention)

**Document Structure (5 pages):**

**Page 1: Introduction + Mathematical Model**
- Title block: "Logistic Regression: A Self-Study Guide" / "Methods and Algorithms -- MSc Data Science" / "L02 Self-Study Document"
- Brief 2-3 sentence intro: why logistic regression matters, what this document covers
- Section 1: The Logistic Model
  - The classification problem: predict P(y=1|x) in [0,1]
  - Sigmoid function: definition, key properties, derivative
  - Chart: `01_sigmoid_function/chart.pdf` (width ~0.45\textwidth, wrapped with text)
  - Odds and log-odds: formulas, coefficient interpretation as odds ratios

**Page 2: Maximum Likelihood Estimation**
- Section 2: Parameter Estimation
  - Likelihood function construction
  - Log-likelihood transformation
  - Binary cross-entropy equivalence
  - Chart: `03_log_loss/chart.pdf` (width ~0.45\textwidth)
  - Gradient derivation via chain rule (single-sample then matrix form)
  - Newton-Raphson / IRLS: Hessian formula, update rule, quadratic convergence note

**Page 3: Statistical Inference + Regularization**
- Section 3: Inference and Model Selection
  - Standard errors from Hessian inverse
  - Wald test: z-statistic formula, decision rule
  - Likelihood Ratio Test: formula, chi-squared distribution
  - AIC/BIC: formulas, when to use which
- Section 4: Regularization
  - L2 (Ridge) and L1 (Lasso) penalty formulas
  - Elastic Net combination
  - Cross-validation for lambda selection (brief)

**Page 4: Evaluation Metrics + Credit Scoring Application**
- Section 5: Evaluation Metrics
  - Confusion matrix: TP, FP, TN, FN definitions
  - Chart: `06_confusion_matrix/chart.pdf` (width ~0.40\textwidth)
  - Precision, recall, F1-score formulas (compact, in-line or small table)
  - ROC curve and AUC interpretation
  - Chart: `04_roc_curve/chart.pdf` (width ~0.40\textwidth)
  - Gini coefficient: Gini = 2*AUC - 1, banking standard benchmarks
- Section 6: Application -- Credit Scoring (start here, continue to page 5)
  - Worked example: 5 features (income, debt_ratio, employment_years, credit_history, delinquencies)
  - Fitted coefficients table (e.g., beta_income = 0.42, beta_debt = -1.15, etc.)

**Page 5: Credit Scoring (continued) + Summary + References**
- Worked example continued:
  - Sample applicant: concrete values for all 5 features
  - Step-by-step PD calculation: z = w^T x + b -> sigma(z) -> PD
  - Odds ratio interpretation: "Each additional year of employment multiplies odds of repayment by e^{0.35} = 1.42"
  - Basel context: PD feeds into Expected Loss = PD * LGD * EAD, Gini benchmark
- Section 7: Summary
  - 5-6 bullet point recap of key takeaways
  - When to use logistic regression vs. alternatives (brief)
- References
  - James, Witten, Hastie, Tibshirani (2021). Introduction to Statistical Learning, 2nd ed. Chapter 4.
  - Hastie, Tibshirani, Friedman (2009). Elements of Statistical Learning. Chapter 4.
  - Molnar, C. (2022). Interpretable Machine Learning. https://christophm.github.io/interpretable-ml-book/
  - scikit-learn User Guide: Logistic Regression. https://scikit-learn.org/stable/modules/linear_model.html

**LaTeX Specifics:**
- Use `\usepackage[margin=0.85in]{geometry}` as starting point (tune for 5 pages)
- Use `\usepackage{amsmath,amssymb}` for math
- Use `\usepackage{graphicx}` for charts
- Use `\usepackage{booktabs}` for the coefficient table
- Use `\usepackage{wrapfig}` for wrapping text around charts (saves space)
- Use `\usepackage{enumitem}` with `\setlist{nosep}` for compact lists
- Use `\usepackage[colorlinks=true,linkcolor=mlblue,urlcolor=mlblue]{hyperref}` for links
- Use `\usepackage{xcolor}` with named colors
- Section headings: `\titleformat` from titlesec package to color headings mlpurple
- Paragraphs: `\setlength{\parskip}{0.4em}` and `\setlength{\parindent}{0em}` for readability
- Compact math: use `align*` environments, avoid excess vertical spacing
- Font: leave as default Computer Modern (clean, professional)
- DO NOT include `\tableofcontents` -- wastes space

**Chart inclusion pattern:**
```latex
\begin{wrapfigure}{r}{0.45\textwidth}
  \centering
  \vspace{-1em}
  \includegraphics[width=0.43\textwidth]{01_sigmoid_function/chart.pdf}
  \caption{The sigmoid function maps $\mathbb{R} \to (0,1)$.}
  \vspace{-1em}
\end{wrapfigure}
```

### Task 2: Compile and Verify
**Agent:** executor (sonnet) -- straightforward compilation task
**Priority:** HIGH
**Depends on:** Task 1

**Steps:**
1. `cd D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L02_Logistic_Regression`
2. `pdflatex -interaction=nonstopmode L02_selfstudy.tex` (run twice for references)
3. `pdflatex -interaction=nonstopmode L02_selfstudy.tex` (second pass)
4. Verify: 0 errors in log
5. Verify: 0 "Overfull" warnings in log (grep for "Overfull")
6. Verify: PDF page count is exactly 5
7. Move aux files: `mkdir temp 2>nul & move L02_selfstudy.aux L02_selfstudy.log L02_selfstudy.out temp\`

**Acceptance Criteria:**
- 0 LaTeX errors
- 0 Overfull hbox/vbox warnings
- PDF exists and is exactly 5 pages
- All charts render (no missing file errors)

**If page count is wrong:**
- If 4 pages: reduce margins slightly, add more content to credit scoring example
- If 6 pages: increase margins, tighten vertical spacing, reduce paragraph spacing
- If Overfull warnings: reduce chart widths, rephrase long lines, use `\allowbreak` or `\sloppy` locally

### Task 3: Deploy to GitHub Pages
**File 1:** `D:\Joerg\Research\slides\Methods_and_Algorithms\docs\slides\pdf\L02_selfstudy.pdf`
**File 2:** `D:\Joerg\Research\slides\Methods_and_Algorithms\docs\index.html`
**Agent:** executor (sonnet)
**Priority:** MEDIUM
**Depends on:** Task 2

**Steps:**

**3a. Copy PDF:**
```
copy "slides\L02_Logistic_Regression\L02_selfstudy.pdf" "docs\slides\pdf\L02_selfstudy.pdf"
```

**3b. Add card to index.html L02 section:**

Find this block (line ~172, after the Full Lecture PDF card):
```html
<a class="ccard" href="slides/pdf/L02_logreg_full.pdf" download><div class="ccard-icon">PDF</div>Full Lecture PDF<div class="ccard-label">31-slide technical</div></a>
```

Insert AFTER it (before the Colab Notebook card):
```html
<a class="ccard" href="slides/pdf/L02_selfstudy.pdf" download><div class="ccard-icon">PDF</div>Self-Study Guide<div class="ccard-label">5-page reading</div></a>
```

**Also update the hero stats:** Change `<b>12</b><small>PDFs</small>` to `<b>13</b><small>PDFs</small>` (line ~116).

**Acceptance Criteria:**
- `docs/slides/pdf/L02_selfstudy.pdf` exists and is identical to source
- Card appears in L02 section of index.html between "Full Lecture PDF" and "Colab Notebook"
- Card follows exact same HTML pattern as sibling cards
- Hero stats updated to reflect new PDF count
- Page loads correctly in browser (no broken HTML)

## Commit Strategy

**Single commit** after all 3 tasks complete:

```
Add L02 self-study guide: 5-page logistic regression reading

Create a self-contained LaTeX article for independent study covering
MLE derivation, statistical inference, regularization, evaluation
metrics, and a credit scoring worked example with Basel context.
Deploy compiled PDF to GitHub Pages.

New files:
- slides/L02_Logistic_Regression/L02_selfstudy.tex
- slides/L02_Logistic_Regression/L02_selfstudy.pdf
- docs/slides/pdf/L02_selfstudy.pdf

Modified files:
- docs/index.html (add self-study card to L02 section)
```

## Success Criteria

| Criterion | Measurement |
|-----------|-------------|
| Compiles cleanly | 0 errors, 0 Overfull warnings in pdflatex log |
| Correct length | PDF is exactly 5 pages |
| Self-contained | A student can read it without lecture context |
| MSc depth | Contains MLE derivation, Hessian, Wald test, LRT formulas |
| Finance application | Credit scoring example with concrete numbers |
| Charts included | 4 charts render correctly in PDF |
| GH Pages deployed | PDF accessible at `docs/slides/pdf/L02_selfstudy.pdf` |
| Index updated | Card visible in L02 section of index.html |
| References present | ISLR Ch.4, scikit-learn docs, Interpretable ML Book cited |

## Risk Mitigations

| Risk | Mitigation |
|------|------------|
| Page count wrong | Geometry margins are the primary tuning knob; parskip as secondary |
| Overfull hbox from equations | Use `\allowbreak`, split long equations across lines, or use `\small` locally |
| Chart paths broken | Paths verified: `01_sigmoid_function/chart.pdf` etc. relative to .tex location |
| wrapfig spacing issues | Fall back to centered `figure` environment if wrapfig causes problems |
| 5 pages too tight for all content | Prioritize: MLE + credit scoring are non-negotiable; trim inference section if needed |
