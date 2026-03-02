# Plan: Prerequisite Mini-Lectures (3 x 10 slides)

## Context

### Original Request
Create 3 standalone prerequisite mini-lecture slide decks (10 Beamer slides each) covering foundational knowledge from the German module description: "Lineare Algebra, Supervised / Unsupervised Learning, Klassifikation und Dekomposition von Daten."

### Codebase Facts
- 26 existing PDFs in `docs/slides/pdf/`
- Mini-lectures follow a strict pattern: lines 1-99 preamble from `L01_linreg_mini.tex`, then 10 `\begin{frame}` blocks
- Slide 1 = title page, Slide 2 = XKCD comic, Slides 3-9 = content, Slide 10 = summary
- XKCD images stored in `slides/LXX_Topic/images/` with `download_xkcd.py` script
- No `L00_Prerequisites/` folder exists yet -- must be created
- Footer: "Methods and Algorithms | MSc Data Science | page/total"
- All TikZ diagrams inline (no chart.py for prerequisites)
- GH Pages hero stats show `<b>26</b><small>PDFs</small>` -- must update to 29

---

## Work Objectives

### Core Objective
Produce 3 compilable, self-contained Beamer mini-lectures that cover prerequisite knowledge for the MSc Methods & Algorithms course.

### Deliverables
1. `slides/L00_Prerequisites/P01_linear_algebra_mini.tex` (10 slides)
2. `slides/L00_Prerequisites/P02_supervised_unsupervised_mini.tex` (10 slides)
3. `slides/L00_Prerequisites/P03_classification_decomposition_mini.tex` (10 slides)
4. `slides/L00_Prerequisites/images/download_xkcd.py` (download script for 3 XKCD images)
5. Updated `docs/index.html` (new Prerequisites section + hero count 26 -> 29)
6. 3 compiled PDFs in `docs/slides/pdf/`

### Definition of Done
- All 3 .tex files compile with `pdflatex` with 0 errors and 0 Overfull warnings
- Each file has exactly 10 `\begin{frame}` blocks
- Each file uses the exact preamble from L01_linreg_mini.tex (lines 1-99)
- XKCD images downloaded and present in images/ folder
- GH Pages updated with Prerequisites section and PDF count = 29
- All finance/banking examples are factually correct

---

## Must Have / Must NOT Have

### Must Have
- Exact same preamble as existing mini-lectures (lines 1-99 of L01_linreg_mini.tex)
- XKCD comic on slide 2 with CC BY-NC 2.5 attribution in `\bottomnote{}`
- Finance/banking application examples in each deck
- TikZ diagrams for visual concepts (inline, no chart.py)
- Max 3-4 bullets per slide
- Summary slide as slide 10

### Must NOT Have
- External chart.py files (all visuals via TikZ inline)
- German text (all content in English)
- Subplots or multi-panel figures
- More than 10 frames per file
- manifest.json changes (see note below)

### Content Depth Boundary

**DEFINITION-level only.** These prerequisite slides introduce terminology and concepts at the level of "what is X and why does it matter." They must NOT include:
- Worked numerical examples (those belong in L01-L06)
- Full derivations or proofs (those belong in L01-L06 deepdives)
- Model evaluation workflows beyond naming the metric (those belong in L01-L06)
- Hyperparameter tuning details (those belong in L01-L06)

Where P01/P03 content overlaps with L01-L06 topics (e.g., OLS formula in P01, classifiers in P03, K-Means in P03, PCA in P03), the prerequisite slides state the definition and one-sentence intuition only. The lectures provide the full treatment.

**P03 "Classification & Decomposition" note:** This deck functions as an orientation/terminology primer. It introduces vocabulary students will encounter in L01-L06 (classifier, clustering, dimensionality reduction, decomposition) so they are not seeing these terms for the first time during the lectures. It is NOT a course preview or a condensed version of L02/L03/L05.

### manifest.json -- NOT Modified

These prerequisite mini-lectures are supplementary materials, same category as the L03 notebooks and L02-L04 mini-lectures added previously. The established project pattern for supplementary materials is: do NOT add them to manifest.json. Reason: the manifest schema is consumed by 8+ infrastructure Python files (`assets.get("notebook", {})` etc.), and adding new asset types risks breaking the CLI validators, builders, and auditors. The prerequisite PDFs are tracked by git and discoverable via `docs/index.html`.

---

## Title Block Convention

The existing mini-lectures have two conventions:
- **L01:** `\author{Methods \& Algorithms}` + `\date{MSc Data Science -- Spring 2026}`
- **L02, L04:** `\author{Methods and Algorithms}` + `\institute{MSc Data Science}` + `\date{}`

**Decision: Use the L02/L04 convention** (newer, used by more files). All 3 prerequisite decks use:

```latex
\author{Methods and Algorithms}
\institute{MSc Data Science}
\date{}
```

This avoids the ampersand escape (`\&`) and keeps a clean empty date (the semester info is already in the footer preamble).

---

## Task Flow

```
T1: Create folder structure
 |
T2: Create download_xkcd.py + download images
 |
T3: Create P01_linear_algebra_mini.tex
T4: Create P02_supervised_unsupervised_mini.tex
T5: Create P03_classification_decomposition_mini.tex
 |  (T3, T4, T5 are independent of each other)
 |
T6: Compile all 3 PDFs, fix any overflow/errors
 |
T7: Copy PDFs to docs/slides/pdf/
 |
T8: Update docs/index.html
 |
T9: Final verification
```

---

## Detailed TODOs

### T1: Create Folder Structure

```bash
mkdir -p slides/L00_Prerequisites/images
```

**Acceptance:** Folder `slides/L00_Prerequisites/images/` exists.

---

### T2: Download XKCD Images

Create `slides/L00_Prerequisites/images/download_xkcd.py` with these 3 comics:

| Deck | XKCD # | Title | Filename | Rationale |
|------|--------|-------|----------|-----------|
| P01 | #1838 | "Machine Learning" | `1838_machine_learning.png` | "Pour the data into this pile of linear algebra" -- directly references linear algebra as ML foundation. Reused from L03/L06 intentionally: prerequisites are a separate context (pre-course vs in-course) and the joke is uniquely apt for linear algebra motivation. |
| P02 | #1425 | "Tasks" | `1425_tasks.png` | "In CS, it can be hard to explain the difference between easy and virtually impossible" -- fits the supervised (tractable) vs unsupervised (harder) paradigm distinction. |
| P03 | #2173 | "Trained a Neural Net" | `2173_trained_a_neural_net.png` | "I trained a neural net and it works but I have no idea why" -- classification/ML humor. If download fails, replace slide 2 with a TikZ comic (existing mini-lectures have TikZ comic examples in overview.tex files). |

**Do NOT put raw URLs in the plan.** The download_xkcd.py script constructs URLs from comic numbers using the standard `https://imgs.xkcd.com/comics/{slug}.png` pattern. The executor should verify each download succeeds and handle failures with a TikZ fallback.

**Acceptance:** download_xkcd.py exists and all 3 images download successfully (or TikZ fallback specified for failures).

---

### T3: P01 -- Linear Algebra for ML (10 slides)

**File:** `slides/L00_Prerequisites/P01_linear_algebra_mini.tex`

**Preamble:** Copy lines 1-99 exactly from `slides/L01_Introduction_Linear_Regression/L01_linreg_mini.tex`

**Title block:**
```latex
\title[Linear Algebra Mini-Lecture]{Linear Algebra for Machine Learning}
\subtitle{Mini-Lecture: The Mathematical Foundation}
\author{Methods and Algorithms}
\institute{MSc Data Science}
\date{}
```

**Slide-by-slide content:**

| Slide | Title | Content | Visual Type |
|-------|-------|---------|-------------|
| 1 | Title Page | `\titlepage` | -- |
| 2 | XKCD Opening | "Pour the data into this pile of linear algebra" | XKCD #1838 image, `\bottomnote{XKCD \#1838 by Randall Munroe (CC BY-NC 2.5)}` |
| 3 | Vectors: Direction and Magnitude | - A vector $\mathbf{x} \in \mathbb{R}^n$ represents a data point with $n$ features; - Example: a loan applicant = [income, age, debt\_ratio, credit\_score]; - Dot product $\mathbf{a} \cdot \mathbf{b} = \sum a_i b_i$ measures similarity; - Norm $\|\mathbf{x}\| = \sqrt{\sum x_i^2}$ measures magnitude | **TikZ**: 2D vector diagram showing two vectors, angle between them, and projection |
| 4 | Matrices: Data as a Table | - A matrix $X \in \mathbb{R}^{n \times p}$: $n$ observations, $p$ features; - Each row = one customer, each column = one feature; - Matrix-vector product $X\boldsymbol{\beta}$ = all predictions at once; - Finance: portfolio of 500 stocks x 10 risk factors = $500 \times 10$ matrix | **Text/formula only**: matrix notation with labeled dimensions, $X\boldsymbol{\beta} = \hat{\mathbf{y}}$ equation block |
| 5 | Key Matrix Operations | - Transpose: $X^T$ flips rows and columns; - Inverse: $A^{-1}$ such that $AA^{-1} = I$ (exists only for square, non-singular matrices); - $X^TX$ = covariance-like matrix (definition only -- OLS derivation is in L01); - Determinant: $\det(A) = 0$ means matrix is singular (not invertible) | **Text/formula only**: definition list with formulas |
| 6 | Eigenvalues and Eigenvectors | - $A\mathbf{v} = \lambda\mathbf{v}$: the matrix $A$ only scales $\mathbf{v}$, does not change direction; - $\lambda$ = eigenvalue (how much), $\mathbf{v}$ = eigenvector (which direction); - PCA uses eigenvectors of the covariance matrix (details in L05); - Finance: eigenvalues of a correlation matrix reveal independent risk factors | **TikZ**: Vector before and after transformation, showing eigenvector stays on same line, non-eigenvector rotates |
| 7 | Linear Transformations | - Matrix multiplication = linear transformation (rotation, scaling, projection); - ML models apply transformations: $\hat{y} = X\boldsymbol{\beta}$ transforms feature space to prediction space; - Rank of $X$ determines how many independent features exist; - If $\text{rank}(X) < p$, features are linearly dependent (multicollinearity) | **Text/formula only**: transformation notation with rank definition |
| 8 | Norms and Distance Metrics | - L2 norm (Euclidean): $\|\mathbf{x}\|_2 = \sqrt{\sum x_i^2}$ -- used in Ridge regression; - L1 norm (Manhattan): $\|\mathbf{x}\|_1 = \sum |x_i|$ -- used in Lasso regression; - Frobenius norm for matrices: $\|A\|_F = \sqrt{\sum_{i,j} a_{ij}^2}$; - Finance: portfolio tracking error = L2 norm of return differences | **TikZ**: Unit circles for L1 (diamond) and L2 (circle) norms, labeled |
| 9 | Finance Application: Covariance and Risk | - Covariance matrix $\Sigma$: $\Sigma_{ij} = \text{Cov}(R_i, R_j)$; - Portfolio variance: $\sigma_p^2 = \mathbf{w}^T \Sigma \mathbf{w}$ where $\mathbf{w}$ = weights; - Eigendecomposition of $\Sigma$ reveals principal risk factors; - Cholesky decomposition $\Sigma = LL^T$ used in Monte Carlo simulation | **Text/formula only**: formula block with labeled components |
| 10 | Summary: Linear Algebra in 4 Takeaways | 1. Vectors represent data points; matrices represent datasets; 2. Matrix operations ($X^TX$, inverse, transpose) power regression and regularization; 3. Eigenvalues/eigenvectors decompose variance and identify risk factors; 4. Norms (L1, L2) measure distance and drive regularization penalties. Next: these tools appear in every lecture L01-L06. | -- |

**TikZ diagrams (3 total) -- explicit slide mapping:**
1. Slide 3: 2D vector with projection (simple axes + two arrows + dashed projection line)
2. Slide 6: Eigenvector visualization (vector scaled but not rotated)
3. Slide 8: L1 vs L2 unit circles (diamond vs circle)

**Slides WITHOUT TikZ (text/formula/table only):** 1, 2, 4, 5, 7, 9, 10

**Content overlap notes:** Slide 5 mentions OLS formula $\hat{\beta} = (X^TX)^{-1}X^Ty$ as a definition/example of where $X^TX$ appears -- no derivation (that is in L01). Slide 8 names Ridge/Lasso norms as definitions -- no regularization path or lambda tuning (that is in L01).

**Finance examples:** Loan applicant feature vector (slide 3), portfolio risk matrix (slide 4), stock correlation eigenvalues (slide 6), portfolio tracking error (slide 8), covariance-based risk (slide 9).

**Acceptance:**
- 10 frames exactly
- Compiles with 0 errors, 0 Overfull
- All 3 TikZ diagrams render correctly
- Formulas are typeset properly

---

### T4: P02 -- Supervised vs Unsupervised Learning (10 slides)

**File:** `slides/L00_Prerequisites/P02_supervised_unsupervised_mini.tex`

**Preamble:** Copy lines 1-99 exactly from `slides/L01_Introduction_Linear_Regression/L01_linreg_mini.tex`

**Title block:**
```latex
\title[ML Paradigms Mini-Lecture]{Supervised \& Unsupervised Learning}
\subtitle{Mini-Lecture: Two Paradigms of Machine Learning}
\author{Methods and Algorithms}
\institute{MSc Data Science}
\date{}
```

**Slide-by-slide content:**

| Slide | Title | Content | Visual Type |
|-------|-------|---------|-------------|
| 1 | Title Page | `\titlepage` | -- |
| 2 | XKCD Opening | "In CS, it can be hard to explain the difference between easy and virtually impossible" | XKCD #1425 image (or TikZ fallback), `\bottomnote{XKCD \#1425 by Randall Munroe (CC BY-NC 2.5)}` |
| 3 | What Is Machine Learning? | - Learning patterns from data instead of explicit programming; - Three core paradigms: supervised, unsupervised, reinforcement; - This course focuses on supervised (L01-L04) and unsupervised (L03, L05); - Finance: predict defaults (supervised), segment customers (unsupervised) | **TikZ**: Three-box diagram: Supervised / Unsupervised / Reinforcement, with brief labels |
| 4 | Supervised Learning: Learn from Labels | - Training data has input-output pairs: $(X, y)$; - Goal: learn a function $f: X \to y$ that generalizes to unseen data; - Regression: $y$ is continuous (predict house price, stock return); - Classification: $y$ is categorical (default/no-default, fraud/not-fraud) | **Text/formula only**: $f: X \to y$ equation, bullet definitions of regression vs classification |
| 5 | The ML Workflow | - Split data: Train (70%) / Validation (15%) / Test (15%); - Train: fit model parameters on training set; - Validate: tune hyperparameters on validation set; - Test: evaluate final performance on held-out test set; - NEVER use test data during training (data leakage) | **TikZ**: Horizontal bar split into 3 colored segments (train/val/test), arrows showing workflow |
| 6 | Bias-Variance Trade-off | - Underfitting (high bias): model too simple, misses patterns; - Overfitting (high variance): model memorizes noise, fails on new data; - Sweet spot: enough complexity to capture signal, not noise; - Finance: a model that perfectly predicts past stock prices but fails on tomorrow's is overfitting | **TikZ**: Three small plots -- underfitting (straight line through curved data), good fit, overfitting (wiggly line through every point) |
| 7 | Unsupervised Learning: Find Hidden Structure | - No labels -- only input data $X$; - Clustering: group similar observations (K-Means, hierarchical); - Dimensionality reduction: compress features while preserving structure (PCA, t-SNE); - Finance: segment customers by spending behavior, reduce 100 risk factors to 5 principal components | **Text/formula only**: bullet list with named methods (no algorithm details -- those are in L03/L05) |
| 8 | Key Terminology | Table format: Term / Meaning / Example: Features ($X$) / Input variables / Income, age, credit score; Target ($y$) / Output to predict / Default (yes/no); Hyperparameter / Tuning knob not learned from data / K in KNN, learning rate; Cross-validation / Rotate train/val splits / 5-fold CV; Metric / Measures model quality / Accuracy, RMSE, AUC | **Text only**: `tabular` or `block` environment, no TikZ |
| 9 | Finance Application: Supervised vs Unsupervised | Two-column comparison: Supervised examples: credit scoring, stock price forecasting, fraud detection; Unsupervised examples: customer segmentation, portfolio risk decomposition, anomaly detection; Key insight: most real projects combine both | **TikZ**: Two-column split diagram with labeled examples |
| 10 | Summary: Two Paradigms in 4 Takeaways | 1. Supervised learning: labeled data, predict $y$ from $X$ (regression or classification); 2. Unsupervised learning: no labels, find structure (clustering, dimensionality reduction); 3. The ML workflow: train/validate/test split prevents overfitting; 4. Finance uses both: predict defaults (supervised) and segment customers (unsupervised). Next: L01-L06 deep-dive into specific algorithms. | -- |

**TikZ diagrams (4 total) -- explicit slide mapping:**
1. Slide 3: Three-paradigm box diagram
2. Slide 5: Train/Validation/Test split bar
3. Slide 6: Underfit/Good fit/Overfit trio
4. Slide 9: Two-column supervised vs unsupervised split

**Slides WITHOUT TikZ (text/formula/table only):** 1, 2, 4, 7, 8, 10

**Finance examples:** Credit scoring (slide 4), stock prediction overfitting (slide 6), customer segmentation (slide 7), comprehensive comparison (slide 9).

**Acceptance:**
- 10 frames exactly
- Compiles with 0 errors, 0 Overfull
- All 4 TikZ diagrams render correctly
- Terminology table fits on one slide without overflow

---

### T5: P03 -- Classification and Data Decomposition (10 slides)

**File:** `slides/L00_Prerequisites/P03_classification_decomposition_mini.tex`

**Preamble:** Copy lines 1-99 exactly from `slides/L01_Introduction_Linear_Regression/L01_linreg_mini.tex`

**Title block:**
```latex
\title[Classification \& Decomposition Mini-Lecture]{Classification \& Data Decomposition}
\subtitle{Mini-Lecture: Sorting, Grouping, and Compressing Data}
\author{Methods and Algorithms}
\institute{MSc Data Science}
\date{}
```

**Orientation note:** This deck is a terminology primer. It introduces vocabulary and high-level concepts (classifier, clustering, dimensionality reduction, decomposition) that students will encounter repeatedly in L01-L06. Each topic is covered at DEFINITION level only -- one-sentence intuition, no worked examples, no evaluation workflows, no hyperparameter tuning. The full treatment of each algorithm is in its respective lecture.

**Slide-by-slide content:**

| Slide | Title | Content | Visual Type |
|-------|-------|---------|-------------|
| 1 | Title Page | `\titlepage` | -- |
| 2 | XKCD Opening | Use XKCD #2173 "Trained a Neural Net" or TikZ comic fallback | XKCD image, `\bottomnote{XKCD \#2173 by Randall Munroe (CC BY-NC 2.5)}` |
| 3 | Classification: Assigning Labels | - Given features $X$, predict a discrete class $y \in \{0, 1, \ldots, K\}$; - Binary: spam/not-spam, default/no-default; - Multiclass: which sector does this company belong to?; - The decision boundary separates classes in feature space | **TikZ**: 2D scatter plot with two classes (circles vs crosses) and a decision boundary line |
| 4 | How Classifiers Decide | - Logistic regression: probability $P(y=1|X)$, threshold at 0.5; - KNN: majority vote among $k$ nearest neighbors; - Decision tree: if-then splits on features; - Each creates a different decision boundary shape | **Text only**: bullet list naming each classifier with one-sentence description (no formulas, no boundary details -- those are in L02/L03/L04) |
| 5 | Evaluating Classifiers | - Accuracy alone is misleading (99% accuracy on 1% fraud rate = useless); - Confusion matrix: TP, FP, TN, FN; - Precision = TP/(TP+FP): "of predicted positives, how many correct?"; - Recall = TP/(TP+FN): "of actual positives, how many found?" | **TikZ**: 2x2 confusion matrix grid with TP/FP/FN/TN labeled, colored cells |
| 6 | Clustering: Grouping Without Labels | - Partition $n$ observations into $K$ groups based on similarity; - K-Means: assign to nearest centroid, update centroids, repeat (definition only -- full algorithm in L03); - Evaluate via inertia or silhouette score; - Finance: segment bank customers into spending profiles | **TikZ**: Three clusters with centroids marked as stars, points colored by cluster |
| 7 | Dimensionality Reduction: Compressing Data | - High-dimensional data ($p$ features) is hard to visualize and model; - PCA: project onto directions of maximum variance (definition only -- derivation in L05); - t-SNE: preserve local neighborhoods in 2D (visualization only); - Goal: reduce $p$ features to $k \ll p$ while retaining most information | **TikZ**: 3D point cloud with an arrow projecting down to a 2D plane |
| 8 | The Decomposition Perspective | - "Decomposition" = breaking data into interpretable components; - SVD: $X \approx U \Sigma V^T$ (truncated); - Factor analysis decomposes correlations into latent factors; - Finance: decompose portfolio returns into market, sector, and idiosyncratic components | **Text/formula only**: formula block showing $X = U\Sigma V^T$ with labels |
| 9 | Finance Application: Putting It All Together | - Classification: credit scoring (approve/deny), fraud detection (flag/pass); - Clustering: customer segmentation, regime detection in markets; - Decomposition: PCA on 50 stock returns to find 3 principal risk factors; - Real workflow: decompose (PCA) -> cluster -> classify | **TikZ**: Pipeline diagram: Raw Data -> PCA -> K-Means -> Classifier -> Decision |
| 10 | Summary: Classification & Decomposition in 4 Takeaways | 1. Classification assigns discrete labels -- evaluate with precision/recall, not just accuracy; 2. Clustering finds natural groups without labels -- K-Means is the workhorse; 3. Dimensionality reduction (PCA, t-SNE) compresses features while preserving structure; 4. Finance combines all three: decompose returns, cluster clients, classify risk. Next: L01-L06 cover each algorithm in depth. | -- |

**TikZ diagrams (5 total) -- explicit slide mapping:**
1. Slide 3: 2D scatter with decision boundary
2. Slide 5: Confusion matrix grid
3. Slide 6: Three clusters with centroids
4. Slide 7: 3D-to-2D projection
5. Slide 9: Pipeline flow diagram

**Slides WITHOUT TikZ (text/formula/table only):** 1, 2, 4, 8, 10

**Content overlap notes:** Slides 4 (classifiers) and 6 (K-Means) name algorithms at definition level only -- no logistic regression sigmoid derivation (L02), no KNN distance computation (L03), no K-Means convergence proof (L03). Slide 7 names PCA/t-SNE without eigenvalue computation (L05).

**Finance examples:** Credit scoring (slide 3), fraud detection accuracy paradox (slide 5), customer segmentation (slide 6), portfolio return decomposition (slide 8), combined workflow (slide 9).

**Acceptance:**
- 10 frames exactly
- Compiles with 0 errors, 0 Overfull
- All 4 TikZ diagrams render correctly
- SVD formula is typeset correctly

---

### T6: Compile All 3 PDFs

For each .tex file, run from the `slides/L00_Prerequisites/` directory:

```bash
cd slides/L00_Prerequisites
pdflatex -interaction=nonstopmode P01_linear_algebra_mini.tex
pdflatex -interaction=nonstopmode P02_supervised_unsupervised_mini.tex
pdflatex -interaction=nonstopmode P03_classification_decomposition_mini.tex
```

Then check for errors:
```bash
grep -c "^!" P01_linear_algebra_mini.log P02_supervised_unsupervised_mini.log P03_classification_decomposition_mini.log
grep -c "Overfull" P01_linear_algebra_mini.log P02_supervised_unsupervised_mini.log P03_classification_decomposition_mini.log
```

**Fix any overflow:** Reduce bullet text, use `\scriptsize`, or adjust TikZ scale.

**Acceptance:** 0 errors AND 0 Overfull warnings across all 3 log files.

---

### T7: Copy PDFs to docs/

```bash
cp slides/L00_Prerequisites/P01_linear_algebra_mini.pdf docs/slides/pdf/P01_linear_algebra_mini.pdf
cp slides/L00_Prerequisites/P02_supervised_unsupervised_mini.pdf docs/slides/pdf/P02_supervised_unsupervised_mini.pdf
cp slides/L00_Prerequisites/P03_classification_decomposition_mini.pdf docs/slides/pdf/P03_classification_decomposition_mini.pdf
```

**Acceptance:** 3 new PDFs exist in `docs/slides/pdf/`, total PDF count = 29.

---

### T8: Update docs/index.html

Two changes required:

**Change 1: Hero stats PDF count**

Update line 119:
```html
<!-- OLD -->
<span><b>26</b><small>PDFs</small></span>
<!-- NEW -->
<span><b>29</b><small>PDFs</small></span>
```

**Change 2: Add Prerequisites section**

Insert a new Prerequisites section BEFORE the existing "Lecture Card Grids" section (before line 123 `<!-- Lecture Card Grids -->`). Also add Prerequisites to the sidebar navigation.

**Sidebar addition** (insert before the "Quizzes" details block, around line 94):
```html
<details style="border-bottom:1px solid #f0f0f0"><summary style="border-left:3px solid #586069">Prerequisites</summary><ul>
<li><a href="#prerequisites">Linear Algebra</a></li>
<li><a href="#prerequisites">ML Paradigms</a></li>
<li><a href="#prerequisites">Classification & Decomposition</a></li>
</ul></details>
```

**Main content addition** (insert before line 123 `<!-- Lecture Card Grids -->`):
```html
<!-- Prerequisites Section -->
<section class="section" id="prerequisites">
<div class="section-head" style="border-color:#586069"><span style="background:#586069">P</span><h2>Prerequisites</h2></div>
<div style="background:#fff;border:1px solid #e1e4e8;border-radius:6px;padding:12px;margin-bottom:12px">
<div style="font-size:11px;color:#24292e;margin-bottom:8px"><b>Foundational Knowledge</b> -- Review these mini-lectures before starting the course. They cover linear algebra, ML paradigms, and classification/decomposition concepts assumed throughout L01-L06.</div>
<div class="cgrid" style="grid-template-columns:repeat(3,1fr)">
<a class="ccard" href="slides/pdf/P01_linear_algebra_mini.pdf" download><div class="ccard-icon">PDF</div>Linear Algebra<div class="ccard-label">10-slide prerequisite</div></a>
<a class="ccard" href="slides/pdf/P02_supervised_unsupervised_mini.pdf" download><div class="ccard-icon">PDF</div>Supervised & Unsupervised<div class="ccard-label">10-slide prerequisite</div></a>
<a class="ccard" href="slides/pdf/P03_classification_decomposition_mini.pdf" download><div class="ccard-icon">PDF</div>Classification & Decomposition<div class="ccard-label">10-slide prerequisite</div></a>
</div>
</div>
</section>
```

**Sidebar links note:** All 3 links point to `#prerequisites` since it is a single section with all 3 PDFs. This is acceptable.

**Acceptance:**
- Hero shows 29 PDFs
- New "Prerequisites" section visible on page
- All 3 PDF download links work
- Sidebar has Prerequisites navigation

---

### T9: Final Verification

Run these checks:

1. **Frame count:** `grep -c "begin{frame}" slides/L00_Prerequisites/P0*_mini.tex` -- each must show 10
2. **Error count:** `grep -c "^!" slides/L00_Prerequisites/*.log` -- each must show 0
3. **Overfull count:** `grep -c "Overfull" slides/L00_Prerequisites/*.log` -- each must show 0
4. **PDF existence:** `ls -la docs/slides/pdf/P0*` -- 3 files must exist
5. **Hero count:** `grep "PDFs" docs/index.html` -- must show 29
6. **Preamble match:** Diff lines 1-99 of each P0X file against L01_linreg_mini.tex -- must be identical
7. **Title block convention:** grep each .tex for `\author{Methods and Algorithms}` and `\institute{MSc Data Science}` and `\date{}` -- all 3 must match

**Acceptance:** All 7 checks pass.

---

## Commit Strategy

Single commit after all tasks complete:

```
Add 3 prerequisite mini-lectures (Linear Algebra, ML Paradigms, Classification & Decomposition)

- P01: Linear algebra for ML (vectors, matrices, eigenvalues, norms)
- P02: Supervised vs unsupervised learning (workflow, bias-variance, terminology)
- P03: Classification and data decomposition (classifiers, clustering, PCA/SVD)
- Each: 10 Beamer slides, TikZ diagrams, finance examples, XKCD comic
- GH Pages: new Prerequisites section, PDF count 26 -> 29
```

Files to stage:
- `slides/L00_Prerequisites/P01_linear_algebra_mini.tex`
- `slides/L00_Prerequisites/P02_supervised_unsupervised_mini.tex`
- `slides/L00_Prerequisites/P03_classification_decomposition_mini.tex`
- `slides/L00_Prerequisites/images/download_xkcd.py`
- `slides/L00_Prerequisites/images/*.png` (3 XKCD images)
- `docs/slides/pdf/P01_linear_algebra_mini.pdf`
- `docs/slides/pdf/P02_supervised_unsupervised_mini.pdf`
- `docs/slides/pdf/P03_classification_decomposition_mini.pdf`
- `docs/index.html`

Do NOT stage: `manifest.json` (not modified -- see rationale above).

---

## Success Criteria

| Criterion | How to Verify |
|-----------|---------------|
| 3 .tex files exist | `ls slides/L00_Prerequisites/P0*_mini.tex` |
| 10 frames each | `grep -c "begin{frame}" <file>` = 10 for each |
| 0 compile errors | `grep -c "^!" <logfile>` = 0 for each |
| 0 Overfull warnings | `grep -c "Overfull" <logfile>` = 0 for each |
| Preamble matches L01 | `diff <(head -99 P01_*.tex) <(head -99 ../L01_*/L01_linreg_mini.tex)` = no diff |
| Title block uses L02/L04 convention | grep confirms `\author{Methods and Algorithms}` in all 3 |
| XKCD images present | `ls slides/L00_Prerequisites/images/*.png` = 3 files |
| PDFs in docs/ | `ls docs/slides/pdf/P0*` = 3 files |
| GH Pages hero = 29 | grep confirms `<b>29</b>` |
| Prerequisites section in HTML | grep confirms `id="prerequisites"` |
| Finance examples in each deck | Manual check: at least 2 finance references per .tex file |
| manifest.json unchanged | `git diff manifest.json` shows no changes |
| TikZ count matches plan | P01: 3 TikZ (slides 3,6,8); P02: 4 TikZ (slides 3,5,6,9); P03: 5 TikZ (slides 3,5,6,7,9) |
| Content depth = DEFINITION only | No worked examples, no derivations, no evaluation workflows beyond naming |
