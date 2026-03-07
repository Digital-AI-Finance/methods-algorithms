# Plan: PCA Simple Narrative Lecture

## Context

### Original Request
Create a simple, narrative-driven PCA-only Beamer lecture for MSc Data Science. Emphasis: "as simple as possible, narrative-driven, start with charts." Every concept introduced via a chart BEFORE the explanation. All new charts use synthetic data with `np.random.seed(42)`.

### Research Findings
- **Existing files:** L05_overview.tex, L05_deepdive.tex, L05_pca_full.tex (24 frames, full rigor), L05_pca_mini.tex (10 frames, PCA+t-SNE), L05_pca_tsne_top10.tex
- **Available XKCD:** `images/2048_curve_fitting.png` (opening), `images/2400_statistics.png` (closing)
- **Reusable charts (already have chart.pdf):** 01_scree_plot, 02_principal_components, 03_reconstruction, 06b_pca_cluster_projection, top10_09_cumulative_variance, top10_10_pca_biplot, top10_11_scaling_effect
- **Preamble:** Copy from L05_pca_mini.tex (self-contained, includes dfteal/dfred, Madrid 8pt 16:9, all ML colors, TikZ libs, pgfplots)
- **Target:** `slides/L05_PCA_tSNE/L05_pca_simple.tex`

### Design Decisions
- **Framework:** Option D (Custom) with narrative sections matching the 3-act story
- **Audience:** MSc (22-28 slides, Greek from slide 2 OK, 1+ derivation, 1+ worked example)
- **PCA only:** Zero t-SNE content -- this is a standalone PCA lecture
- **Chart-first pedagogy:** Every section OPENS with showing a chart, THEN explains

---

## Work Objectives

### Core Objective
A 25-slide standalone Beamer deck telling the PCA story in three acts: (1) the problem of too many dimensions, (2) how PCA solves it, (3) evaluating how well it worked. Every concept is introduced via a chart first, explanation second.

### Deliverables
1. `slides/L05_PCA_tSNE/L05_pca_simple.tex` -- 25 frames, self-contained preamble
2. 2 new chart.py files (new folders with chart.py + chart.pdf)
3. 6 reused existing charts (no new chart.py needed)

### Definition of Done
- [ ] 25 frames compile with 0 errors, 0 Overfull
- [ ] 8 charts total (1 per 3.1 slides > 1 per 4 minimum)
- [ ] 2 XKCD comics (opening + closing) with attribution
- [ ] 1 derivation (eigenvalue problem)
- [ ] 1 worked numerical example (2D-to-1D projection)
- [ ] 1 finance application (yield curve PCA)
- [ ] 8+ distinct layout patterns used
- [ ] Bottomnote on every content slide
- [ ] Question-based slide titles on all content slides

---

## Guardrails

### MUST Have
- Chart appears BEFORE its explanation in every section
- Narrative arc: problem --> method --> evaluation (3 acts)
- Minimal notation: only X, mu, Sigma, lambda, v, k used
- Opening XKCD (#2048) and closing XKCD (#2400)
- Self-contained preamble (copied from L05_pca_mini.tex)
- Every chart slide has 2-3 interpretive bullets
- All new chart.py files follow the boilerplate (rcParams, CHART_METADATA, seed=42, ML palette)

### MUST NOT Have
- t-SNE content (this is PCA-only)
- Matrix calculus or Lagrange multiplier derivation (too heavy for "simple")
- More than 6 notation symbols
- Subplots in any chart.py (one figure, one ax)
- Definition-first slides (always problem/visual first)
- Slides with >4 bullets per column

---

## Notation Table

| Symbol | Meaning | Where Used |
|--------|---------|------------|
| X | Data matrix (n x p) | Throughout |
| mu | Column means for centering | Centering step |
| Sigma | Covariance matrix | Eigenvalue derivation |
| lambda_k | k-th eigenvalue (variance of PC_k) | Scree plot, explained variance |
| v_k | k-th eigenvector (direction of PC_k) | Principal components |
| k | Number of components retained | Scree/reconstruction |

No other Greek letters. No lambda/alpha collisions. All symbols defined at first use.

---

## Narrative Arc

### ACT 1: "Your Data Has Too Many Dimensions" (slides 2-7)
Hook: Show a messy high-D dataset. The student FEELS the problem before hearing the term "dimensionality reduction."

### ACT 2: "PCA Finds the Directions That Matter" (slides 8-18)
Mechanism: Show the PC arrows on correlated data. The student SEES variance maximization before the formula. Then one clean derivation, one worked example, one practical gotcha (scaling).

### ACT 3: "How Well Did It Work?" (slides 19-24)
Evaluation: Show reconstruction error curve. The student JUDGES the quality before hearing rules of thumb. Finance application grounds the theory.

### CLOSING (slide 25)
Summary + closing XKCD.

---

## Chart Allocation Table

| # | Chart | Folder | Status | Used In Slide | Type (taxonomy) |
|---|-------|--------|--------|---------------|-----------------|
| C1 | Correlated 2D scatter with PC arrows | `02_principal_components/` | REUSE | 8 | Scatter + Fit |
| C2 | Scree plot (individual + cumulative) | `01_scree_plot/` | REUSE | 19 | Metric Curves |
| C3 | Reconstruction error curve | `03_reconstruction/` | REUSE | 21 | Metric Curves |
| C4 | PCA cluster projection (MNIST digits) | `06b_pca_cluster_projection/` | REUSE | 16 | Dimensionality Reduction |
| C5 | Scaling effect side-by-side | `top10_11_scaling_effect/` | REUSE | 15 | Comparison |
| C6 | High-D data blob before/after PCA | `08_high_dim_before_after/` | **NEW** | 4 | Dimensionality Reduction |
| C7 | Yield curve PCA factor loadings | `09_yield_curve_factors/` | **NEW** | 22 | Bar/Distribution |
| C8 | PCA biplot (loadings + scores) | `top10_10_pca_biplot/` | REUSE | 14 | Dimensionality Reduction |

**8 charts in 25 slides = 1 chart per 3.1 slides (exceeds 1:4 minimum).**

No chart dual-assignment. Each chart appears in exactly one slide.

---

## NEW Chart Specifications

### C6: High-D Before/After PCA (`08_high_dim_before_after/chart.py`)

**What it plots:** Single scatter showing PCA 2D projection of a 10-feature synthetic dataset with 3 colored clusters. One ax, one figure.

**Spec:**
- Generate 10-feature data with `make_blobs(n_samples=300, n_features=10, centers=3, random_state=42)`
- `StandardScaler().fit_transform(X)`
- `PCA(n_components=2).fit_transform(X_scaled)`
- Scatter `X_pca` colored by cluster label (MLBLUE, MLORANGE, MLGREEN for 3 clusters)
- Title: "10 Features Compressed to 2 Components"
- Annotation box: "Original: 10 features | After PCA: 2 components | Variance kept: {var:.0f}%"
- x-axis: "PC1 ({var1:.1f}% variance)", y-axis: "PC2 ({var2:.1f}% variance)"

**Synthetic data:** `sklearn.datasets.make_blobs`, seed 42
**sklearn calls:** `StandardScaler`, `PCA(n_components=2)`

### C7: Yield Curve Factor Loadings (`09_yield_curve_factors/chart.py`)

**What it plots:** Bar chart showing the loadings (eigenvector values) of the first 3 PCA components across 5 maturities (1Y, 2Y, 5Y, 10Y, 30Y). Three grouped bars per maturity. PC1 loadings are flat (level), PC2 loadings slope upward (slope), PC3 loadings are U-shaped (curvature).

**Synthetic data:**
- Construct a 5-maturity synthetic covariance matrix that mimics real yield curve behavior
- Generate 500 daily yield changes using `np.random.multivariate_normal`
- Run `PCA(n_components=3)` on the data
- Plot `pca.components_` as grouped bars

**Detailed construction:**
```python
np.random.seed(42)  # MANDATORY: reproducible synthetic data
maturities = ['1Y', '2Y', '5Y', '10Y', '30Y']
# Correlation matrix mimicking yield curve behavior
corr = np.array([
    [1.0, 0.95, 0.85, 0.75, 0.65],
    [0.95, 1.0, 0.92, 0.82, 0.72],
    [0.85, 0.92, 1.0, 0.93, 0.83],
    [0.75, 0.82, 0.93, 1.0, 0.94],
    [0.65, 0.72, 0.83, 0.94, 1.0],
])
# Vols decrease with maturity (basis points)
vols = np.array([0.08, 0.07, 0.06, 0.05, 0.04])
cov = np.outer(vols, vols) * corr
X = np.random.multivariate_normal(np.zeros(5), cov, 500)
```
- Grouped bar: x = maturities, 3 bars per maturity (PC1=MLPURPLE, PC2=MLORANGE, PC3=MLGREEN)
- Annotate PC1 as "Level", PC2 as "Slope", PC3 as "Curvature"
- Title: "Yield Curve PCA: What the Three Factors Look Like"

**sklearn calls:** `PCA(n_components=3)`

---

## Slide-by-Slide Specification

### ACT 0: Title + Opening

| Slide | Title | Layout | Content | Chart | Bottomnote |
|-------|-------|--------|---------|-------|------------|
| 1 | Title page | `[plain] \titlepage` | "PCA: Seeing Through the Noise" / "A Simple Guide to Principal Component Analysis" | -- | -- |
| 2 | When You Have Too Many Dimensions to Plot | Layout 8 (mixed media) | XKCD #2048 (0.55\textwidth) + 2 framing bullets: "Your dataset has 50 columns. You can only plot 2 axes. What do you do?" | XKCD #2048 | XKCD #2048 by Randall Munroe (CC BY-NC 2.5). This is the problem we solve today. |

### ACT 1: "Your Data Has Too Many Dimensions" (The Problem)

| Slide | Title | Layout | Content | Chart | Bottomnote |
|-------|-------|--------|---------|-------|------------|
| 3 | What Happens When You Have 50 Features? | Layout 7 (full width text) | Concrete scenario: "A bank tracks 50 risk metrics for each portfolio. A data scientist needs to visualize risk clusters. Plotting 50 axes is impossible. Dropping features loses information. What if there were directions that capture most of the variation?" 3 bullets + exampleblock. | -- | High-dimensional data is everywhere: genomics (20k genes), NLP (50k words), finance (hundreds of factors). |
| 4 | **[CHART FIRST]** What Does Compressed Data Look Like? | Layout 22 (chart + explanations) | Show chart C6 (10D -> 2D PCA). Below: 3 bullets interpreting: (1) "Each dot was originally described by 10 numbers," (2) "PCA compressed it to just 2 numbers," (3) "The clusters are still visible." | C6 (NEW) | PCA found the 2 directions that preserve the most spread in the data -- no human picked them. |
| 5 | Why Not Just Pick Two Features? | Layout 10 (comparison) | Left column: "Cherry-picking" -- pick features 1 and 2, lose info from features 3-10. Right column: "PCA" -- combine ALL features into 2 new axes, keep maximum info. Block: "PCA does not discard features -- it blends them." | -- | Selecting features = supervised (you choose). PCA = unsupervised (the data chooses). |
| 6 | What Does "Variance" Mean Here? | Layout 4 (two cols math) | Left: simple formula `Var(x) = (1/n) * sum((x_i - mean)^2)`. Right: TikZ mini-diagram showing a cloud of points with a wide spread along one axis and narrow spread along another. "High variance = lots of information. Low variance = mostly noise." | -- | In PCA, "variance" and "information" are treated as synonyms. This is an assumption, not a fact. |
| 7 | Road Map: Three Steps of PCA | Layout 11 (step-by-step) | Three numbered steps across two columns: (1) Center the data, (2) Find the directions of maximum variance, (3) Project onto those directions. Block: "That is the entire algorithm." | -- | We will see each step visually before we see any formulas. |

### ACT 2: "PCA Finds the Directions That Matter" (The Method)

| Slide | Title | Layout | Content | Chart | Bottomnote |
|-------|-------|--------|---------|-------|------------|
| 8 | **[CHART FIRST]** Which Direction Captures the Most Spread? | Layout 22 (chart + explanations) | Show chart C1 (PC arrows on correlated scatter). Below: (1) "The red arrow (PC1) points along the main cloud -- maximum spread," (2) "The orange arrow (PC2) is perpendicular -- remaining spread," (3) "Together they form new coordinate axes." | C1 (REUSE) | PCA is a rotation: it does not distort your data, it views it from a better angle. |
| 9 | Step 1: Center the Data | Layout 9 (definition-example) | Left: formula `X_c = X - mu` where mu is the column mean vector. Right: worked numerical mini-example: 4 data points, subtract mean, show shifted cloud. Block insight. | -- | Centering ensures PC1 passes through the origin. Without centering, the mean dominates the first component. |
| 10 | Step 2: The Covariance Matrix | Layout 4 (two cols math) | Left: formula `Sigma = (1/(n-1)) * X_c^T X_c`. Right: interpretation -- diagonal = variance of each feature, off-diagonal = how features move together. "Large off-diagonal = redundancy = PCA can compress." | -- | If all off-diagonals were zero, PCA would do nothing -- the features are already independent. |
| 11 | Step 3: Eigenvalues and Eigenvectors (The Key Equation) | Layout 9 (definition-example) | Left: `Sigma v = lambda v`. "An eigenvector v is a direction that the covariance matrix only stretches, never rotates. The eigenvalue lambda tells you how much it stretches." Right: intuition -- "Imagine pulling a rubber sheet. The eigenvectors are the directions that only stretch, not twist." | -- | This is the ONLY equation you need to remember. Everything else follows from it. |
| 12 | Derivation: Why Does PCA Maximize Variance? | Layout 7 (full width text) | 4-step derivation: (1) We want direction v that maximizes Var(X_c v) = v^T Sigma v, (2) subject to ||v||=1, (3) Lagrangian: L = v^T Sigma v - lambda(v^T v - 1), (4) dL/dv = 0 gives Sigma v = lambda v. "The eigenvectors of Sigma are the principal components. The eigenvalues are their variances." | -- | Pearson (1901) and Hotelling (1933). The constrained optimization is standard Lagrange multipliers. |
| 13 | Worked Example: 2D to 1D by Hand | Layout 7 (full width text) | Full numerical walkthrough: 5 data points in 2D, center, compute Sigma (2x2), solve eigenvalue equation, project onto PC1. Show numbers at each step. Final: "We reduced 2D to 1D and kept 82% of the variance." | -- | Try this yourself: change the correlation and watch how the PC direction rotates. |
| 14 | How Do You Read a Biplot? | Layout 22 (chart + explanations) | Show biplot chart (top10_10_pca_biplot/chart.pdf). Below: (1) "Dots = data points in PC space," (2) "Arrows = original features. Long arrow = feature contributes strongly," (3) "Arrows pointing the same direction = correlated features." | top10_10_pca_biplot (REUSE) | Biplots are the main diagnostic tool for interpreting what PCA did. Always plot one. |
| 15 | **[CHART FIRST]** What Happens If You Forget to Scale? | Layout 22 (chart + explanations) | Show chart C5 (scaling effect). Below: (1) "Left: feature 1 is in thousands, dominates PC1 alone," (2) "Right: after scaling, all features contribute fairly," (3) "Always standardize unless features share the same units." | C5 (REUSE) | StandardScaler (zero mean, unit variance) is the default. Skip it only when features are already on the same scale. |
| 16 | **[CHART FIRST]** Can PCA Separate Clusters? | Layout 22 (chart + explanations) | Show chart C4 (MNIST digits PCA). Below: (1) "Each color is a digit class (0-9). PCA separates some but not all," (2) "Digits 0 and 1 are easy to tell apart. Digits 4 and 9 overlap," (3) "PCA is linear -- it cannot untangle nonlinear structure." | C4 (REUSE) | For better cluster separation on complex data, consider t-SNE (visualization) or UMAP. |
| 17 | When Does PCA Fail? | Layout 18 (pros/cons) | [+] Linear relationships, correlated features, preprocessing for ML, interpretable. [-] Nonlinear structure (swiss roll), outlier sensitivity, all features must be numeric, components are linear combinations (not single features). | -- | PCA assumes linear relationships. If your data lives on a curved surface, PCA will cut through it. |
| 18 | PCA as Preprocessing: The 95% Rule | Layout 7 (full width text) | Practical recipe: (1) StandardScaler, (2) PCA(n_components=0.95), (3) Feed into classifier/regressor. "sklearn's PCA can auto-select k to hit a variance threshold." Pseudo-code snippet using \code{}. | -- | PCA before KNN or logistic regression often improves speed AND accuracy by removing noise dimensions. |

### ACT 3: "How Well Did It Work?" (Evaluation)

| Slide | Title | Layout | Content | Chart | Bottomnote |
|-------|-------|--------|---------|-------|------------|
| 19 | **[CHART FIRST]** How Many Components Do We Keep? | Layout 22 (chart + explanations) | Show chart C2 (scree plot). Below: (1) "Blue bars = variance explained by each PC. The first 3 tower over the rest," (2) "Red line = cumulative. It crosses 80% at PC3," (3) "The elbow at PC3 says: keep 3, discard the rest." | C2 (REUSE) | Named after geological "scree" (rubble at a cliff base). You stop where the cliff flattens into rubble. |
| 20 | Rules of Thumb for Choosing k | Layout 6 (three-way split) | Three columns: (1) "Elbow method" -- look at scree plot, (2) "Threshold method" -- keep enough for 90-95% variance, (3) "Cross-validation" -- pick k that maximizes downstream task performance. Each with 2 bullets. | -- | No single rule is always best. In practice, try 2-3 methods and see if they agree. |
| 21 | **[CHART FIRST]** Reconstruction Error: What Did We Lose? | Layout 22 (chart + explanations) | Show chart C3 (reconstruction error curve). Below: (1) "Error drops steeply for the first few components," (2) "After k=5, adding components barely helps," (3) "The gap between k=3 and k=20 is only a few percent." | C3 (REUSE) | Reconstruction: X_approx = X_pca @ V_k^T + mu. The error is ||X - X_approx||^2. |
| 22 | **[CHART FIRST]** Finance Application: Yield Curve PCA | Layout 22 (chart + explanations) | Show chart C7 (yield curve factor loadings). Below: (1) "PC1 (flat bars) = all maturities move together = 'level'," (2) "PC2 (sloped bars) = short and long rates diverge = 'slope'," (3) "PC3 (U-shaped bars) = belly moves differently = 'curvature'." | C7 (NEW) | Litterman & Scheinkman (1991): 3 PCA factors explain >98% of US Treasury yield curve movements. |
| 23 | Yield Curve PCA: The Worked Numbers | Layout 9 (definition-example) | Left: portfolio risk formula `Delta P ~ D1*Delta PC1 + D2*Delta PC2 + D3*Delta PC3`. Right: worked example with numbers: "If level shifts +10bp (PC1=+10), slope steepens (PC2=+5), curvature unchanged (PC3=0), and D1=0.8, D2=0.3, D3=0.1, then Delta P ~ 0.8*10 + 0.3*5 = 9.5bp." | -- | 3 numbers replace 5+ maturity exposures. This is why every fixed income desk uses PCA. |
| 24 | PCA Decision Checklist | Layout 13 (summary) | Left column: "Use PCA when..." (correlated features, too many dimensions, preprocessing, interpretable compression). Right column: "Skip PCA when..." (few features already, nonlinear structure, need original feature names, categorical data). | -- | The simplest test: if your correlation matrix has large off-diagonal entries, PCA will help. |

### CLOSING

| Slide | Title | Layout | Content | Chart | Bottomnote |
|-------|-------|--------|---------|-------|------------|
| 25 | PCA in Four Sentences | Layout 8 (mixed media) | Left column: (1) "High-D data is hard to visualize and model," (2) "PCA finds orthogonal directions of maximum variance," (3) "Keep k components that explain 90-95% of variance," (4) "In finance, 3 PCA factors explain nearly all yield curve movement." Right column: XKCD #2400 (0.42\textwidth). | XKCD #2400 | XKCD #2400 by Randall Munroe (CC BY-NC 2.5). Next: explore t-SNE for nonlinear visualization in the deep dive. |

**Total: 25 slides (1 title + 2 INTRO + 5 ACT1 + 11 ACT2 + 6 ACT3/CLOSING)**

---

## Layout Diversity Audit

| Layout | Slide Numbers | Count |
|--------|---------------|-------|
| Layout 7 (full width text) | 3, 12, 13, 18 | 4 |
| Layout 22 (chart + explanations) | 4, 8, 14, 15, 16, 19, 21, 22 | 8 |
| Layout 8 (mixed media / image) | 2, 25 | 2 |
| Layout 4 (two cols math) | 6, 10 | 2 |
| Layout 9 (definition-example) | 9, 11, 23 | 3 |
| Layout 10 (comparison) | 5 | 1 |
| Layout 11 (step-by-step) | 7 | 1 |
| Layout 18 (pros/cons) | 17 | 1 |
| Layout 6 (three-way split) | 20 | 1 |
| Layout 13 (summary) | 24 | 1 |

**10 distinct layout patterns (exceeds 8 minimum).**

---

## Slide Title Audit (question-based preferred)

| Slide | Title | Question? |
|-------|-------|-----------|
| 2 | When You Have Too Many Dimensions to Plot | Implied |
| 3 | What Happens When You Have 50 Features? | YES |
| 4 | What Does Compressed Data Look Like? | YES |
| 5 | Why Not Just Pick Two Features? | YES |
| 6 | What Does "Variance" Mean Here? | YES |
| 7 | Road Map: Three Steps of PCA | Declarative (OK for roadmap) |
| 8 | Which Direction Captures the Most Spread? | YES |
| 9 | Step 1: Center the Data | Process step |
| 10 | Step 2: The Covariance Matrix | Process step |
| 11 | Step 3: Eigenvalues and Eigenvectors | Process step |
| 12 | Derivation: Why Does PCA Maximize Variance? | YES |
| 13 | Worked Example: 2D to 1D by Hand | Declarative (example) |
| 14 | How Do You Read a Biplot? | YES |
| 15 | What Happens If You Forget to Scale? | YES |
| 16 | Can PCA Separate Clusters? | YES |
| 17 | When Does PCA Fail? | YES |
| 18 | PCA as Preprocessing: The 95% Rule | Declarative |
| 19 | How Many Components Do We Keep? | YES |
| 20 | Rules of Thumb for Choosing k | Declarative |
| 21 | Reconstruction Error: What Did We Lose? | YES |
| 22 | Finance Application: Yield Curve PCA | Declarative (application) |
| 23 | Yield Curve PCA: The Worked Numbers | Declarative (example) |
| 24 | PCA Decision Checklist | Declarative (checklist) |
| 25 | PCA in Four Sentences | Declarative (summary) |

**13/23 content slides have question titles (57%). Process steps, examples, and summaries are appropriately declarative.**

---

## Deliberately Dropped Content

| Content | Why Dropped | Where It Lives Instead |
|---------|-------------|------------------------|
| SVD connection | "Simple as possible" -- eigendecomposition is enough | L05_pca_full.tex slide 16 |
| Kernel PCA | Nonlinear PCA is scope creep | top10_12_kernel_pca chart, L05_deepdive.tex |
| PCA whitening | Specialized preprocessing, not core | top10_19_pca_whitening chart |
| PCA denoising | Application, not core concept | top10_15_pca_denoising chart |
| Formal proof of variance maximality | Lagrange sketch is included; full proof is in deepdive | L05_deepdive.tex |
| PCA vs Factor Analysis vs Autoencoders | Comparison is in full deck | L05_pca_full.tex slide 20 |

---

## Task Flow

### Task 1: Create new chart C6 (`08_high_dim_before_after/chart.py`)
- Create folder `slides/L05_PCA_tSNE/08_high_dim_before_after/`
- Write chart.py per spec above
- Run chart.py, verify chart.pdf generated
- **Acceptance:** chart.pdf exists, shows 3 colored clusters in 2D, title mentions "10 Features", annotation shows variance percentage

### Task 2: Create new chart C7 (`09_yield_curve_factors/chart.py`)
- Create folder `slides/L05_PCA_tSNE/09_yield_curve_factors/`
- Write chart.py per spec above
- Run chart.py, verify chart.pdf generated
- **Acceptance:** chart.pdf exists, shows grouped bars for 5 maturities x 3 PCs, PC1 loadings visibly flat, PC2 visibly sloped, PC3 visibly curved

### Task 3: Write `L05_pca_simple.tex`
- Copy preamble from L05_pca_mini.tex (lines 1-106, up to `\begin{document}`)
- Change title/subtitle/date
- Write all 25 frames per the slide-by-slide spec
- All chart references use relative paths: `XX_name/chart.pdf`
- Every content frame has `[t]` alignment and `\bottomnote{}`
- **Acceptance:** 25 `\begin{frame}` / `\end{frame}` pairs, 8 chart `\includegraphics` + 2 XKCD images = 10 total

### Task 4: Compile and verify
- Run `pdflatex -interaction=nonstopmode L05_pca_simple.tex` (twice)
- `grep -c "^!" L05_pca_simple.log` == 0
- `grep -c "Overfull" L05_pca_simple.log` == 0
- Verify page count == 25
- **Acceptance:** clean compile, 0 errors, 0 Overfull, 25 pages

### Task 5: Update manifest.json
- Add L05_pca_simple.tex to L05 topic entry
- Add new chart folders 08_high_dim_before_after and 09_yield_curve_factors
- **Acceptance:** manifest.json valid JSON, new entries present

### Dependencies
```
Task 1 ──┐
          ├──> Task 3 ──> Task 4 ──> Task 5
Task 2 ──┘
```
Tasks 1 and 2 are independent (can run in parallel). Task 3 depends on both charts existing. Task 4 depends on Task 3. Task 5 depends on Task 4.

---

## Commit Strategy

Single commit after all tasks complete:
```
Add simple narrative PCA lecture (L05_pca_simple.tex)

- 25-slide chart-first narrative covering PCA fundamentals
- 2 new charts: high-D before/after PCA, yield curve factor loadings
- 6 reused existing charts from L05 chart library
- Opening XKCD #2048, closing XKCD #2400
- Self-contained preamble, standalone compilation

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
```

Files to stage:
- `slides/L05_PCA_tSNE/L05_pca_simple.tex`
- `slides/L05_PCA_tSNE/08_high_dim_before_after/chart.py`
- `slides/L05_PCA_tSNE/08_high_dim_before_after/chart.pdf`
- `slides/L05_PCA_tSNE/09_yield_curve_factors/chart.py`
- `slides/L05_PCA_tSNE/09_yield_curve_factors/chart.pdf`
- `manifest.json`

---

## Success Criteria

| Criterion | Verification |
|-----------|-------------|
| Compiles clean | 0 errors, 0 Overfull in log |
| 25 slides | `pdflatex` output says "25 pages" |
| 8 charts | `grep -c "chart.pdf" L05_pca_simple.tex` == 8 |
| 2 XKCDs | `grep -c "images/" L05_pca_simple.tex` == 2 |
| 10 total includegraphics | `grep -c "includegraphics" L05_pca_simple.tex` == 10 (8 charts + 2 XKCDs) |
| Chart-first pedagogy | Slides 4, 8, 14, 15, 16, 19, 21, 22 all have chart ABOVE explanation |
| Narrative arc | Sections follow problem -> method -> evaluation |
| Minimal notation | Only 6 symbols: X, mu, Sigma, lambda, v, k |
| 10 layout patterns | Layout audit table shows 10 distinct |
| Bottomnotes everywhere | `grep -c "bottomnote" L05_pca_simple.tex` >= 23 |
| Finance application | Slides 22-23 cover yield curve PCA with worked numbers |
| Derivation present | Slide 12 has 4-step variance maximization |
| Worked example present | Slide 13 has 2D-to-1D numerical walkthrough |
