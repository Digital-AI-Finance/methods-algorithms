# Plan: L05 Full Lecture Decks + Visual-Heavy Notebooks

## Task
Bring L05 (PCA & t-SNE) to parity with L03/L04 by creating:
1. t-SNE mini-lecture (L05_tsne_mini.tex, 10 slides)
2. PCA full technical lecture (L05_pca_full.tex, ~25 slides)
3. t-SNE full technical lecture (L05_tsne_full.tex, ~25 slides)
4. PCA visual-heavy notebook (L05_pca.ipynb, ~18 cells, ~8 visuals)
5. t-SNE visual-heavy notebook (L05_tsne.ipynb, ~18 cells, ~8 visuals)

Plus: compile, deploy PDFs, update GH Pages + manifest, commit + push.

## Current State

### Existing L05 Assets
| File | Frames | Charts | Status |
|------|--------|--------|--------|
| L05_overview.tex | 24 | 7 | committed |
| L05_deepdive.tex | 48 | 8 | committed |
| L05_pca_mini.tex | 10 | 3 | committed |
| L05_pca_tsne.ipynb | 32 cells, 10 visuals | — | committed (combined) |

### Missing (vs L03/L04 pattern)
| Asset | L03 Equivalent | L04 Equivalent |
|-------|---------------|----------------|
| L05_tsne_mini.tex | L03_kmeans_mini.tex | L04_rf_mini.tex |
| L05_pca_full.tex | L03_knn_full.tex | L04_dt_full.tex |
| L05_tsne_full.tex | L03_kmeans_full.tex | L04_rf_full.tex |
| L05_pca.ipynb | L03_knn.ipynb | L04_dt.ipynb |
| L05_tsne.ipynb | L03_kmeans.ipynb | L04_rf.ipynb |

### Chart Folders (12 total)
| ID | Content | PCA? | t-SNE? |
|----|---------|------|--------|
| 01_scree_plot | Variance explained per component | ✓ | |
| 02_principal_components | PC1/PC2 scatter with loadings | ✓ | |
| 03_reconstruction | Original vs reconstructed data | ✓ | |
| 04a_tsne_perplexity_5 | t-SNE with perplexity=5 | | ✓ |
| 04b_tsne_perplexity_30 | t-SNE with perplexity=30 | | ✓ |
| 04c_tsne_perplexity_100 | t-SNE with perplexity=100 | | ✓ |
| 05a_pca_swiss_roll | PCA on Swiss roll (fails) | ✓ | |
| 05b_tsne_swiss_roll | t-SNE on Swiss roll (succeeds) | | ✓ |
| 06a_original_clusters | High-dim clusters before reduction | ✓ | ✓ |
| 06b_pca_cluster_projection | PCA projection of clusters | ✓ | |
| 06c_tsne_cluster_projection | t-SNE projection of clusters | | ✓ |
| 07_decision_flowchart | When to use PCA vs t-SNE | | ✓ |

### XKCD Images
| Image | File | Use |
|-------|------|-----|
| #2048 curve_fitting | images/2048_curve_fitting.png | PCA full closing |
| #2400 statistics | images/2400_statistics.png | t-SNE full closing |

---

## Deck Architecture & Chart Reuse Policy

### Relationship Between Slide Decks

L05 follows the same multi-deck architecture as L03 and L04:

| Deck Type | Purpose | Audience | Standalone? |
|-----------|---------|----------|-------------|
| **Overview** (L05_overview.tex) | Course-level intro covering BOTH PCA and t-SNE | All students, first exposure | Yes — uses charts from both topics |
| **Deepdive** (L05_deepdive.tex) | Course-level theory covering BOTH PCA and t-SNE | All students, detailed theory | Yes — uses charts from both topics |
| **PCA Mini** (L05_pca_mini.tex) | 10-slide BSc-accessible PCA overview | Students needing gentle intro | Yes — 2 PCA charts only |
| **t-SNE Mini** (L05_tsne_mini.tex) | 10-slide BSc-accessible t-SNE overview | Students needing gentle intro | Yes — 2 t-SNE charts only |
| **PCA Full** (L05_pca_full.tex) | Deep standalone PCA lecture | Students wanting PCA-only depth | Yes — 6 PCA charts only |
| **t-SNE Full** (L05_tsne_full.tex) | Deep standalone t-SNE lecture | Students wanting t-SNE-only depth | Yes — 6 t-SNE charts only |

### Chart Reuse Policy

**The "one chart per file" rule applies within a TIER, not across tiers.** Charts are shared across deck types because each deck serves a different pedagogical purpose:

- **Overview + Deepdive** = course-level files covering both PCA and t-SNE together (existing)
- **Mini-lectures** = topic-specific BSc-accessible introductions (existing PCA, new t-SNE)
- **Full lectures** = topic-specific deep technical standalone decks (new)

All 12 charts are already used in the existing overview and/or deepdive files. The full-deck files intentionally reuse the same charts in a topic-focused context. This is the same pattern used in L03 (where knn_full and kmeans_full share charts with L03_overview and L03_deepdive) and L04 (where dt_full and rf_full share charts with L04_overview and L04_deepdive).

**Within-tier constraint**: No chart appears in BOTH pca_full AND tsne_full. No chart appears in BOTH pca_mini AND tsne_mini. This is enforced by the allocation table below.

### XKCD Image Reuse

XKCD images are shared across decks (same pattern as L03/L04):
- **#2048 curve_fitting**: Used in L05_overview (opening comic), L05_pca_mini (closing), AND L05_pca_full (closing). Intentional — it's the canonical PCA image.
- **#2400 statistics**: Used in L05_overview (closing) AND L05_tsne_full (closing). Intentional — it's the canonical dimensionality reduction image.

---

## Chart Allocation

### PCA Full (~25 slides): 6 charts
01_scree_plot, 02_principal_components, 03_reconstruction, 05a_pca_swiss_roll, 06a_original_clusters, 06b_pca_cluster_projection
→ Density: 25/6 = 1:4.2 ✓

### t-SNE Full (~25 slides): 6 charts
04a_tsne_perplexity_5, 04b_tsne_perplexity_30, 04c_tsne_perplexity_100, 05b_tsne_swiss_roll, 06c_tsne_cluster_projection, 07_decision_flowchart
→ Density: 25/6 = 1:4.2 ✓

### t-SNE Mini (10 slides): 2 charts
04b_tsne_perplexity_30, 06c_tsne_cluster_projection
→ Matches L03/L04 mini pattern (2 charts per mini)

---

## Deliverable 1: L05_tsne_mini.tex (10 slides)

### Design
- Follow L05_pca_mini.tex pattern exactly (same preamble, 10-slide WHY-FEEL-WHAT-CASE-HOW-RISK-WHERE-IMPACT-SO_WHAT-ACT)
- BSc accessible: plain English, no jargon without definition
- TikZ comics: opening (slide 1) + risk (slide 6) + closing (slide 10)
- 2 charts: 04b_tsne_perplexity_30 (slide 4), 06c_tsne_cluster_projection (slide 5)
- Finance domain: detecting market regime changes by visualizing high-dimensional trading data

### Slide-by-Slide

| # | Section | Title | Content |
|---|---------|-------|---------|
| 1 | WHY | "Why Can't We See 50 Variables at Once?" | TikZ comic: analyst with 50 stock screens, thought bubble "What if I could see ALL of this on ONE scatter plot?" |
| 2 | FEEL | "You Have 1000 Stocks and 50 Features — How Would You Visualize Them?" | Reflection: students realize 50D scatter plot is impossible. Build intuition for needing dimensionality reduction. |
| 3 | WHAT | "What IS t-SNE?" | Plain English: "An algorithm that squeezes high-dimensional data into 2D while preserving which points are neighbors." Key terms: embedding, perplexity, neighborhood. |
| 4 | CASE | "How Does t-SNE Reveal Hidden Structure?" | Use 04b_tsne_perplexity_30/chart. Show how 50D stock data collapses into clear clusters: tech stocks, banks, energy. |
| 5 | HOW | "How Does t-SNE Preserve Neighborhoods?" | Use 06c_tsne_cluster_projection/chart. Explain: "Points that are close in 50D stay close in 2D. Points that are far apart are pushed further." |
| 6 | RISK | "What Can Go Wrong with t-SNE?" | TikZ comic: two identical-looking maps with different parameters → completely different clusters! Punchline: "t-SNE is sensitive to perplexity — always try multiple values." |
| 7 | WHERE | "Where Do Quants Use t-SNE?" | Market regime detection, portfolio visualization, anomaly detection (outlier stocks), customer segmentation visualization. |
| 8 | IMPACT | "Why Does Visualization Change Decisions?" | Before t-SNE: "We have 50 risk factors, trust us." After: "Look — these 3 clusters ARE your portfolio." Stakeholder impact: traders, risk managers, regulators. |
| 9 | SO WHAT | "When Should You Use t-SNE vs PCA?" | PCA: when you need a new coordinate system, interpretable axes, preprocessing for ML. t-SNE: when you need to SEE clusters, explore data, present to non-technical audience. |
| 10 | ACT | "Can You Spot the Regime Change?" | Exercise: given a t-SNE plot with timestamps colored by date, identify when clusters shift. Closing TikZ comic: stick figure saying "I can see 50 dimensions!" |

---

## Deliverable 2: L05_pca_full.tex (~25 slides)

### Design
- Three-zone architecture: INTRO (1-5, no formulas) → CORE (6-19, formulas) → CLOSING (20-25)
- 6 charts (01, 02, 03, 05a, 06a, 06b)
- TikZ comic opening (slide 2), XKCD #2048 closing (slide 25)
- Finance domain: portfolio risk decomposition, yield curve analysis
- Question-style frame titles, max 3-4 bullets per slide
- At least 8 distinct layout patterns

### Slide-by-Slide

**INTRO (slides 1-5, no formulas)**

| # | Title | Layout | Content |
|---|-------|--------|---------|
| 1 | Title Page | Title | "Principal Component Analysis: Seeing Through the Noise" |
| 2 | "A Portfolio Manager Tracks 500 Stocks with 50 Risk Factors — How?" | TikZ comic | SCQ: too many variables to analyze. TikZ: overwhelmed trader with screens. |
| 3 | Learning Objectives | LO list | 4 LOs at Bloom 4+: (1) Derive PCA as variance maximization via eigendecomposition, (2) Analyze scree plots and reconstruction error to select components, (3) Evaluate PCA's linear assumption using Swiss roll and non-linear alternatives, (4) Apply PCA to yield curve decomposition and portfolio risk |
| 4 | "What Is PCA in Plain English?" | Two-column | Left: "Find new axes that capture the most spread in the data." Analogy: rotating a camera to see the widest view. Right: key terms. |
| 5 | "Why Reduce Dimensions?" | Three reasons | (1) Visualization: 50D→2D, (2) Noise reduction: discard low-variance directions, (3) Speed: fewer features = faster ML. |

**CORE — METHOD (slides 6-14)**

| # | Title | Layout | Content |
|---|-------|--------|---------|
| 6 | "What Does the Data Look Like Before Reduction?" | Full-size chart | 06a_original_clusters. High-dimensional data (shown as parallel coordinates or multi-panel). |
| 7 | "How Does PCA Find the Best Axes?" | Chart + text | 02_principal_components. PC1 = direction of maximum variance. PC2 = perpendicular direction of next most variance. Geometric intuition with loadings. |
| 8 | "The Variance Maximization Objective" | Definition block | Maximize $\text{Var}(\mathbf{w}^T \mathbf{X}) = \mathbf{w}^T \mathbf{S} \mathbf{w}$ subject to $\|\mathbf{w}\| = 1$. Where $\mathbf{S}$ = covariance matrix. Solution: eigenvectors of $\mathbf{S}$. |
| 9 | "Worked Example: 2D→1D by Hand" | Worked example | 5 data points in 2D, compute mean, center, covariance matrix, eigenvalues/vectors. Show projection onto PC1. All numerical values explicit. |
| 10 | "How Much Variance Does Each Component Explain?" | Chart + text | 01_scree_plot. Explained variance ratio. Cumulative sum. "How many PCs to keep? → 90% threshold rule." |
| 11 | "Reconstruction: Going Back to Original Space" | Chart + text | 03_reconstruction. $\hat{\mathbf{X}} = \mathbf{Z} \mathbf{W}^T + \boldsymbol{\mu}$. Show original vs reconstructed. Reconstruction error = discarded variance. |
| 12 | "SVD and PCA: Two Paths, One Answer" | Formula reference | SVD: $\mathbf{X} = \mathbf{U} \boldsymbol{\Sigma} \mathbf{V}^T$. Right singular vectors V = eigenvectors of $\mathbf{X}^T\mathbf{X}$. "sklearn uses SVD (faster, numerically stable)." |
| 13 | "When Does PCA Fail?" | Chart + text | 05a_pca_swiss_roll. PCA on Swiss roll = disaster. "PCA only captures LINEAR structure." Bridge to t-SNE. |
| 14 | "PCA Projection Preserves Linear Clusters" | Full-size chart | 06b_pca_cluster_projection. When clusters are linearly separable, PCA projection works well. |

**CORE — SOLUTION (slides 15-19)**

| # | Title | Layout | Content |
|---|-------|--------|---------|
| 15 | "Yield Curve PCA: The Canonical Finance Example" | Two-column | Left: yield curve = 10+ maturities. Right: PC1 = level (parallel shift), PC2 = slope (steepening), PC3 = curvature. "3 PCs explain ~98% of yield curve variance." |
| 16 | "Portfolio Risk Decomposition" | Step-by-step | Apply PCA to 50-stock return matrix. PC1 = market factor. PC2 = sector rotation. "Reduce 50 risk factors to 5 interpretable principal portfolios." |
| 17 | "Choosing the Number of Components" | Two-column | Methods: (1) Scree plot elbow, (2) Kaiser criterion (eigenvalue > 1), (3) Cumulative variance threshold (90-95%), (4) Cross-validation on downstream task. |
| 18 | "PCA as Preprocessing for ML" | Code example [fragile] | sklearn Pipeline: StandardScaler → PCA(n_components=0.95) → LogisticRegression. "PCA speeds up training and fights overfitting." |
| 19 | "Interpreting Principal Components" | Two-column | Loadings matrix: which original features load heavily on each PC? Example: if PC1 has high loadings on all stocks → market factor. If PC2 has positive tech, negative energy → sector rotation. |

**CLOSING (slides 20-25)**

| # | Title | Layout | Content |
|---|-------|--------|---------|
| 20 | "When to Use PCA — and When Not To" | Pros/Cons | Pros: interpretable, fast, preserves global structure, preprocessing. Cons: linear only, sensitive to scaling, loses local structure. |
| 21 | "PCA vs Factor Analysis vs Autoencoders" | Comparison table | Linearity, interpretability, number of components selection, computational cost, non-linear capability. |
| 22 | "Hands-on: Decompose Portfolio Risk" | Code [fragile] | sklearn PCA on stock returns. Scree plot + biplot code. Link to L05_pca.ipynb. |
| 23 | "Key Takeaways" | Summary | Left: concepts (eigenvectors, variance, reconstruction, scree). Right: practice (scale first, check scree, interpret loadings, Swiss roll test). |
| 24 | "What's Next: t-SNE for Visualization" | Bridge | "PCA finds global axes. t-SNE finds local neighborhoods. Next: when the data is non-linear." |
| 25 | "Closing Thought" | XKCD #2048 | Image + quote about dimensionality reduction revealing hidden structure. |

---

## Deliverable 3: L05_tsne_full.tex (~25 slides)

### Design
- Three-zone architecture: INTRO (1-5) → CORE (6-19) → CLOSING (20-25)
- 6 charts (04a, 04b, 04c, 05b, 06c, 07)
- TikZ comic opening (slide 2), XKCD #2400 closing (slide 25)
- Finance domain: market regime detection, anomaly visualization
- Question-style titles, max 3-4 bullets

### Slide-by-Slide

**INTRO (slides 1-5, no formulas)**

| # | Title | Layout | Content |
|---|-------|--------|---------|
| 1 | Title Page | Title | "t-SNE: Visualizing High-Dimensional Data" |
| 2 | "How Do You Spot a Market Crash in 100 Variables?" | TikZ comic | Analyst drowning in dimensions. "What if I could SEE all 100 variables in one picture?" |
| 3 | Learning Objectives | LO list | 4 LOs: (1) Derive t-SNE's KL divergence objective and understand the gradient, (2) Analyze how perplexity controls the balance between local and global structure, (3) Evaluate t-SNE's limitations vs PCA and UMAP, (4) Apply t-SNE to detect market regimes and financial anomalies |
| 4 | "What Is t-SNE in Plain English?" | Two-column | "Convert pairwise distances in high-D to probabilities. Find a 2D layout where those probabilities are preserved." Analogy: seating dinner guests so friends sit together. |
| 5 | "Why Not Just Use PCA?" | Chart comparison | Show PCA on Swiss roll fails (reference 05a), t-SNE succeeds. "PCA captures linear variance. t-SNE captures LOCAL neighborhood structure." |

**CORE — METHOD (slides 6-14)**

| # | Title | Layout | Content |
|---|-------|--------|---------|
| 6 | "How Does t-SNE Preserve Neighborhoods?" | Full-size chart | 05b_tsne_swiss_roll. t-SNE unrolls the Swiss roll. "Points near each other in 100D stay near each other in 2D." |
| 7 | "Step 1: Compute Pairwise Similarities in High-D" | Definition block | $p_{j|i} = \frac{\exp(-\|x_i - x_j\|^2 / 2\sigma_i^2)}{\sum_{k \neq i}\exp(-\|x_i - x_k\|^2 / 2\sigma_i^2)}$. Symmetrize: $p_{ij} = (p_{j|i} + p_{i|j}) / 2n$. "Gaussian kernel → closer points get higher probability." |
| 8 | "Step 2: Compute Similarities in Low-D (Student-t Kernel)" | Definition + reason | $q_{ij} = \frac{(1 + \|y_i - y_j\|^2)^{-1}}{\sum_{k \neq l}(1 + \|y_k - y_l\|^2)^{-1}}$. "Heavy-tailed t-distribution → far-apart points pushed further → prevents crowding." |
| 9 | "Step 3: Minimize KL Divergence" | Formula + intuition | $\text{KL}(P\|Q) = \sum_i \sum_j p_{ij} \log \frac{p_{ij}}{q_{ij}}$. "Penalizes keeping nearby high-D points far apart in low-D. Does NOT penalize pushing far points together." Asymmetry matters! |
| 10 | "The Crowding Problem: Why Student-t?" | Two-column | Left: Gaussian in low-D → moderate-distance points forced to overlap (crowding). Right: Student-t → heavier tails → room for moderate distances. Worked example: 10 equidistant points in circle. |
| 11 | "What Does Perplexity Do?" | Three charts side-by-side | 04a (perplexity=5), 04b (perplexity=30), 04c (perplexity=100). "Perplexity ≈ number of effective neighbors. Low → tight local clusters. High → global structure." |
| 12 | "Perplexity Guidelines" | Table | Perplexity 5-10: very local, risk of fragments. 30-50: typical default (sklearn=30). 100+: global focus, risk of merging clusters. Rule: n/3 < perplexity, always try 3+ values. |
| 13 | "t-SNE Caveats: What You Cannot Infer" | Two-column | (1) Cluster sizes don't mean anything, (2) Distances between clusters don't mean anything, (3) Axis orientation is random, (4) Different runs may produce different layouts. "t-SNE is for EXPLORATION, not measurement." |
| 14 | "How Does Cluster Preservation Compare?" | Full-size chart | 06c_tsne_cluster_projection. Show t-SNE separating clusters that PCA merges. |

**CORE — SOLUTION (slides 15-19)**

| # | Title | Layout | Content |
|---|-------|--------|---------|
| 15 | "Market Regime Detection with t-SNE" | Two-column | Apply t-SNE to daily return vectors of 50 stocks over 5 years. Color by date → clusters = market regimes (bull, bear, crisis). "2008 points cluster together, separate from 2005 points." |
| 16 | "Anomaly Detection: Spotting Outliers Visually" | Two-column | Points far from any cluster in the t-SNE map = potential anomalies. Example: rogue trading days, flash crashes. "Complement to statistical outlier tests." |
| 17 | "UMAP: The Modern Alternative" | Comparison | UMAP = faster, preserves more global structure, deterministic. Same idea: find a low-D layout preserving neighborhoods. "UMAP is often preferred for large datasets (>10K points)." |
| 18 | "t-SNE vs PCA vs UMAP: Decision Framework" | Chart + table | 07_decision_flowchart. Table: speed, global structure, local structure, interpretability, reproducibility. |
| 19 | "The t-SNE Gradient" | Formula [optional depth] | $\frac{\partial C}{\partial y_i} = 4\sum_j (p_{ij} - q_{ij})(y_i - y_j)(1 + \|y_i - y_j\|^2)^{-1}$. "Attractive force (p>q) pulls neighbors together. Repulsive force (p<q) pushes non-neighbors apart." |

**CLOSING (slides 20-25)**

| # | Title | Layout | Content |
|---|-------|--------|---------|
| 20 | "When to Use t-SNE — and When Not To" | Pros/Cons | Pros: reveals clusters, handles non-linear, stunning visualizations. Cons: slow O(n²), non-reproducible, can't project new points, uninterpretable axes. |
| 21 | "t-SNE vs Logistic Regression Feature Space" | Comparison | When PCA+LR fails (non-linear boundary), t-SNE visualization shows WHY — classes overlap in linear projection. |
| 22 | "Hands-on: Detect Market Regimes" | Code [fragile] | sklearn TSNE on return vectors. Multi-perplexity comparison. Link to L05_tsne.ipynb. |
| 23 | "Key Takeaways" | Summary | Left: concepts (KL divergence, perplexity, crowding, Student-t). Right: practice (try 3 perplexities, don't read distances, use for exploration, UMAP for speed). |
| 24 | "What's Next: Embeddings and RL" | Bridge | "t-SNE visualizes learned features. Next: how neural networks LEARN those features — word embeddings, representation learning." |
| 25 | "Closing Thought" | XKCD #2400 | Image + quote. |

---

## Deliverable 4: L05_pca.ipynb (~18 cells, ~8 visuals)

### Pattern
Follow L04_dt.ipynb exactly: markdown headers + code cells, ML color palette, no exercises.

**rcParams note:** Notebooks use `font.size=12` (matching L04_dt.ipynb convention), NOT `font.size=14` (which is the CLAUDE.md chart.py standard). This is intentional — notebook inline plots use smaller fonts than standalone chart.pdf files.

### Dataset
```python
from sklearn.datasets import load_iris  # 4D, 3 classes — perfect for PCA demo
X, y = load_iris(return_X_y=True)
feature_names = load_iris().feature_names
```
(Iris is standard for PCA — 4 features, 3 clearly separable classes, interpretable loadings.)

### Cell Structure

| # | Type | Content | Visual? |
|---|------|---------|---------|
| 1 | MD | Title + Colab badge + 4 LOs | — |
| 2 | Code | Setup: imports (PCA, StandardScaler), ML palette, rcParams, seed | — |
| 3 | MD | "1. Load and Explore Data" | — |
| 4 | Code | Load Iris, print shape/feature names, scatter matrix or pairplot of 4 features (2×2 grid with colored classes) | Visual 1: Feature pair scatter |
| 5 | MD | "2. PCA: Finding Principal Axes" | — |
| 6 | Code | StandardScaler → PCA(n_components=4), plot explained variance ratio bar chart + cumulative line | Visual 2: Scree plot |
| 7 | Code | Scatter of PC1 vs PC2, colored by class, with arrows for loadings | Visual 3: Biplot |
| 8 | MD | "3. How Many Components?" | — |
| 9 | Code | Cumulative variance curve with 90%/95% thresholds marked | Visual 4: Variance threshold |
| 10 | Code | Reconstruction error vs n_components (1 to 4) | Visual 5: Reconstruction error |
| 11 | MD | "4. PCA on High-Dimensional Data" | — |
| 12 | Code | Generate make_classification(n_features=20, n_informative=5), PCA(n_components=2), scatter colored by class | Visual 6: High-D reduction |
| 13 | MD | "5. PCA Limitation: Non-Linear Data" | — |
| 14 | Code | make_swiss_roll, PCA(n_components=2) — show it fails (colors interleaved) | Visual 7: Swiss roll PCA failure |
| 15 | MD | "6. PCA as Preprocessing" | — |
| 16 | Code | Compare accuracy: raw features vs PCA(n_components=2) → LogisticRegression. Bar chart of accuracies. | Visual 8: Preprocessing comparison |
| 17 | MD | Summary: 4 bullets | — |

### Colab Badge URL
`https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L05_pca.ipynb`

---

## Deliverable 5: L05_tsne.ipynb (~19 cells, ~8 visuals)

### Dataset
```python
from sklearn.datasets import load_digits  # 64D, 10 classes — ideal for t-SNE
X, y = load_digits(return_X_y=True)
```
(Digits has 1797 samples, 64 features, 10 classes — t-SNE shines here.)

### Cell Structure

| # | Type | Content | Visual? |
|---|------|---------|---------|
| 1 | MD | Title + Colab badge + 4 LOs | — |
| 2 | Code | Setup: imports (TSNE, PCA), ML palette, rcParams, seed | — |
| 3 | MD | "1. Load High-Dimensional Data" | — |
| 4 | Code | Load digits, show 10 sample images in a row (2x5 grid), print shape (1797, 64) | Visual 1: Sample digit images |
| 5 | MD | "2. PCA First — Does It Separate Classes?" | — |
| 6 | Code | PCA(n_components=2), scatter colored by digit class (10 colors) — shows overlap | Visual 2: PCA projection |
| 7 | MD | "3. t-SNE Reveals Hidden Clusters" | — |
| 8 | Code | TSNE(n_components=2, perplexity=30, random_state=42), scatter colored by digit — shows clear clusters | Visual 3: t-SNE projection |
| 9 | Code | Side-by-side: PCA vs t-SNE | Visual 4: PCA vs t-SNE comparison |
| 10 | MD | "4. Effect of Perplexity" | — |
| 11 | Code | 3-panel: perplexity=5, 30, 100 | Visual 5: Perplexity comparison |
| 12 | MD | "5. What t-SNE Distances Mean (and Don't Mean)" | — |
| 13 | Code | Show that cluster size and inter-cluster distance are NOT meaningful. Two metrics: trustworthiness + silhouette. Print values for different perplexities. | Visual 6: Metric comparison |
| 14 | MD | "6. t-SNE on a Simple Dataset" | — |
| 15 | Code | make_classification(n_features=20, n_informative=5, n_classes=4, n_clusters_per_class=1), t-SNE colored by class. Annotate "Class 0", etc. | Visual 7: Synthetic data t-SNE |
| 16 | MD | "7. UMAP Comparison" | — |
| 17 | Code | If umap available: run UMAP + t-SNE side-by-side. If not: just note UMAP is faster. Fall back to PCA vs t-SNE timing comparison. | Visual 8: Speed/quality comparison |
| 18 | MD | Summary: 4 bullets | — |

**Note:** Cell 17 should have a `try/except ImportError` for umap-learn since it may not be installed in all environments. If umap not available, compare PCA vs t-SNE execution times instead.

### Colab Badge URL
`https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L05_tsne.ipynb`

---

## GH Pages Updates

### docs/index.html changes

1. **Hero stat** (line 126): `<b>33</b>` → `<b>36</b>` (PDFs: +3 for tsne_mini + pca_full + tsne_full)
2. **Hero stat**: `<b>10</b><small>Notebooks</small>` → `<b>12</b><small>Notebooks</small>` (+2 split notebooks)
3. **L05 section** (around line 299-302): Add new PDF cards after existing Mini-Lecture:
```html
<a class="ccard" href="slides/pdf/L05_tsne_mini.pdf" download><div class="ccard-icon">PDF</div>t-SNE Mini-Lecture<div class="ccard-label">10-slide t-SNE overview</div></a>
<a class="ccard" href="slides/pdf/L05_pca_full.pdf" download><div class="ccard-icon">PDF</div>PCA Full Lecture<div class="ccard-label">25-slide PCA theory</div></a>
<a class="ccard" href="slides/pdf/L05_tsne_full.pdf" download><div class="ccard-icon">PDF</div>t-SNE Full Lecture<div class="ccard-label">25-slide t-SNE theory</div></a>
```
4. **Relabel existing notebook**: "Colab Notebook" → "Combined Notebook" with label "PCA + t-SNE Combined"
5. **Add 2 new notebook cards**:
```html
<a class="ccard" href="https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L05_pca.ipynb" target="_blank"><div class="ccard-icon">NB</div>PCA Notebook<div class="ccard-label">Visual-heavy PCA</div></a>
<a class="ccard" href="https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L05_tsne.ipynb" target="_blank"><div class="ccard-icon">NB</div>t-SNE Notebook<div class="ccard-label">Visual-heavy t-SNE</div></a>
```

### manifest.json changes

Add to L05 assets (after existing entries). Also add the missing `pca_mini_slides` entry which was never tracked:
```json
"pca_mini_slides": {
    "file": "slides/L05_PCA_tSNE/L05_pca_mini.tex",
    "status": "complete"
},
"tsne_mini_slides": {
    "file": "slides/L05_PCA_tSNE/L05_tsne_mini.tex",
    "status": "complete"
},
"pca_full_slides": {
    "file": "slides/L05_PCA_tSNE/L05_pca_full.tex",
    "status": "complete"
},
"tsne_full_slides": {
    "file": "slides/L05_PCA_tSNE/L05_tsne_full.tex",
    "status": "complete"
},
"notebook_pca": {
    "file": "notebooks/L05_pca.ipynb",
    "status": "complete"
},
"notebook_tsne": {
    "file": "notebooks/L05_tsne.ipynb",
    "status": "complete"
}
```

---

## Implementation Steps

### Step 0: Verify all chart.pdf files exist
- Run `python infrastructure/course_cli.py build charts --topic L05` or manually verify all 12 chart.pdf files are present and current
- If any chart.pdf is missing, regenerate it before proceeding to LaTeX compilation

### Step 1: Create L05_tsne_mini.tex
- Copy preamble from L05_pca_mini.tex
- 10 slides as specified above
- 2 charts, 3 TikZ comics, finance domain

### Step 2: Create L05_pca_full.tex
- Copy preamble from L05_pca_mini.tex, adjust title
- ~25 slides as specified above
- 6 charts, TikZ opening, XKCD #2048 closing

### Step 3: Create L05_tsne_full.tex
- Same preamble
- ~25 slides as specified above
- 6 charts, TikZ opening, XKCD #2400 closing

### Step 4: Compile all 3 tex files
- `pdflatex -interaction=nonstopmode` (2 passes each)
- Verify 0 Overfull warnings

### Step 5: Create L05_pca.ipynb
- ~18 cells, ~8 visuals
- Iris dataset for main demo
- ML color palette, figsize=(10,6), font.size=12

### Step 6: Create L05_tsne.ipynb
- ~19 cells, ~8 visuals
- Digits dataset for main demo
- ML color palette, same rcParams

### Step 7: Test both notebooks
- `jupyter nbconvert --execute` for each

### Step 8: Deploy to GH Pages
- Copy 3 PDFs to docs/slides/pdf/
- Update docs/index.html (hero stats, L05 section)
- Update manifest.json

### Step 9: Commit and push

---

## Acceptance Criteria

1. `L05_tsne_mini.tex` exists with 10 slides, 3 TikZ comics, 2 charts
2. `L05_pca_full.tex` exists with ~25 slides, 6 charts (01, 02, 03, 05a, 06a, 06b), TikZ + XKCD #2048
3. `L05_tsne_full.tex` exists with ~25 slides, 6 charts (04a, 04b, 04c, 05b, 06c, 07), TikZ + XKCD #2400
4. All 3 tex files compile with 0 errors, 0 Overfull warnings
5. `L05_pca.ipynb` exists with ~18 cells, ~8 visuals, Iris dataset
6. `L05_tsne.ipynb` exists with ~19 cells, ~8 visuals, Digits dataset
7. Both notebooks execute without errors
8. docs/index.html hero stats: 36 PDFs, 12 notebooks
9. docs/index.html L05 section: 6 PDF cards + 3 notebook cards (Combined, PCA, t-SNE)
10. manifest.json: 6 new entries (pca_mini [backfill], tsne_mini, pca_full, tsne_full, notebook_pca, notebook_tsne)
11. All PDFs deployed to docs/slides/pdf/
12. Changes committed and pushed to master

---

## Risk Assessment

| Risk | Mitigation |
|------|------------|
| t-SNE is slow on large datasets | Use digits (n=1797) or subsample. Set random_state=42 for reproducibility. |
| UMAP not installed in all environments | Use try/except ImportError in notebook. Fall back to timing comparison. |
| Swiss roll PCA may look OK in some views | Use 3D Swiss roll data with clear coloring to show interleaving. |
| t-SNE notebooks produce different results each run | Always set random_state=42 and n_iter=1000. |
| Perplexity comparison takes 3x compute time | Use subset of digits (n=500) for the 3-panel perplexity demo. |
| TikZ comics cause Overfull warnings | Keep comics simple (stick figures, speech bubbles). Test each frame individually. |
| chart.pdf files missing or stale | Step 0 verifies all 12 chart.pdf files exist before LaTeX compilation. |

---

PLAN_READY: .omc/plans/l05-full-decks-notebooks.md
