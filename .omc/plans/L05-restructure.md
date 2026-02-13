# L05 PCA & t-SNE: Three-Zone Restructure Plan

## Context

### Original Request
Restructure L05 PCA & t-SNE slides (overview + deepdive) using the slide creation skill v3 three-zone architecture with XKCD comics at opening and closing. Address all CRITICAL and MAJOR findings from the hostile review report (score: 37/100).

### Current State
- **L05_overview.tex**: 14 slides, 245 lines. No XKCD comics, LOs at wrong position (slide 3, before intro content), 7 charts dual-assigned with deepdive, no Zone comments, no \institute line. Missing finance applications entirely.
- **L05_deepdive.tex**: 30 slides, 659 lines. No XKCD comics, no \appendix section, LOs at wrong position (slide 3, before intro). Contains some MSc content (SVD-PCA equivalence, optimality proof, yield curve PCA, statistical inference, perplexity math) added during hostile-review fix phase, but structure does not follow three-zone pattern. 100% chart overlap with overview (7 of 7 charts shared).
- **Preamble**: Lines 1-92 identical in both files. MUST preserve byte-for-byte.

### Hostile Review Findings to Address
| ID | Severity | Issue | Status in Current Files |
|----|----------|-------|------------------------|
| C1 | CRITICAL | Missing yield curve PCA | FIXED in deepdive (lines 304-336), missing from overview |
| C2 | CRITICAL | "PCA assumes Gaussian" FALSE | FIXED in deepdive (line 354) |
| C3 | CRITICAL | Kaiser criterion unqualified | FIXED in deepdive (line 208) |
| C4 | CRITICAL | PCA centering implicit | PARTIALLY FIXED (deepdive formulas updated) |
| C5 | CRITICAL | Crowding problem missing | FIXED in deepdive (line 399 bottomnote) |
| C6 | CRITICAL | PCA optimality proof missing | FIXED in deepdive (lines 147-170) |
| C7 | CRITICAL | No statistical inference | FIXED in deepdive (lines 251-274) |
| M1 | MAJOR | No numerical finance example | FIXED in deepdive (lines 277-302) |
| M2 | MAJOR | Symmetrization missing | FIXED in deepdive (line 385) |
| M3 | MAJOR | SVD relationship absent | FIXED in deepdive (lines 172-191) |
| M4 | MAJOR | "Reversible" misleading | FIXED in deepdive (line 123) |
| M5 | MAJOR | Perplexity unexplained | FIXED in deepdive (line 428) |
| M6 | MAJOR | KL asymmetry missing | FIXED in deepdive (line 397) |

### Decisions Made
- **Chart allocation** (zero dual-assignment):
  - Overview (5 charts): 01_scree_plot, 05a_pca_swiss_roll, 05b_tsne_swiss_roll, 06c_tsne_cluster_projection, 07_decision_flowchart
  - Deepdive (7 charts): 02_principal_components, 03_reconstruction, 04a_tsne_perplexity_5, 04b_tsne_perplexity_30, 04c_tsne_perplexity_100, 06a_original_clusters, 06b_pca_cluster_projection
- **XKCD Opening**: #2048 "Curve Fitting" (images/2048_curve_fitting.png) -- both files
- **XKCD Closing**: #2400 "Statistics" text callback -- both files
- **Pattern source**: L03 restructure plan (24 slides overview, ~41 main + ~8 appendix deepdive)

### Key Pattern Rules (from L01/L02/L03)
1. Lines 1-92: Identical preamble -- DO NOT TOUCH
2. Add `\institute{MSc Data Science}` to title block
3. Zone comments: `% ZONE 1: INTRODUCTION (NO formulas, NO Greek letters)`, `% ZONE 2: CORE CONTENT (PMSP)`, `% ZONE 3: WRAP-UP`
4. Every slide gets a numbered comment header: `% SLIDE N: Title`
5. Every content slide gets `\bottomnote{...}`
6. XKCD opening at slide 3 (both files), closing before References
7. LOs placed AFTER intro section (slide 7 in overview, slide 4 in deepdive)
8. Charts: `\includegraphics[width=0.55\textwidth]` (with text) or `width=0.65\textwidth` (chart-only)
9. Deepdive gets `\appendix` + `\section*{Advanced Topics}` before appendix slides
10. Closing XKCD is a textual callback (quote + witty remark), NOT the image again
11. No pseudocode needed for PCA (closed-form computation, per instructor guide)

---

## Work Objectives

### Core Objective
Rewrite both L05 .tex files to match the three-zone pattern exactly, producing a 24-slide overview and ~40 main + ~8 appendix = ~48 slide deepdive, incorporating all hostile review fixes and eliminating chart dual-assignment.

### Deliverables
1. `L05_overview.tex` rewritten: 24 slides, 3 zones, 5 charts, XKCD open/close
2. `L05_deepdive.tex` rewritten: ~40 main + ~8 appendix slides, 7 charts, XKCD open/close, \appendix section
3. Both PDFs compiled with 0 errors and 0 Overfull warnings
4. Architect verification passed

### Definition of Done
- Preamble lines 1-92 byte-for-byte identical to current
- All slide numbering comments present and sequential
- Every content slide has \bottomnote{}
- Chart allocation: 5 to overview, 7 to deepdive, zero overlap
- XKCD #2048 at slide 3 (both files), XKCD #2400 callback at closing
- LOs at correct position (after intro, not slide 2)
- \institute{MSc Data Science} in title block
- Zone comments present
- All hostile review CRITICAL/MAJOR fixes preserved
- 0 LaTeX compilation errors
- 0 Overfull \hbox warnings
- Max 3-4 bullets per slide

---

## Must Have / Must NOT Have

### MUST Have
- Three-zone architecture (Intro / Core PMSP / Wrap-up)
- XKCD #2048 opening comic (slide 3, both files)
- XKCD #2400 closing callback (textual, both files)
- \institute{MSc Data Science} in title block
- \bottomnote{} on every content slide
- Slide number comments (% SLIDE N: Title)
- Zone boundary comments
- \appendix + \section*{Advanced Topics} in deepdive
- All hostile review fixes preserved:
  - Yield curve PCA (level/slope/curvature worked example)
  - PCA optimality proof (Lagrangian derivation)
  - SVD-PCA equivalence proof
  - t-SNE gradient and crowding problem explanation
  - Perplexity = 2^H definition
  - KL asymmetry discussion
  - Statistical inference for PCA (bootstrap CIs, parallel analysis)
  - Numerical portfolio example with loadings
  - Kaiser criterion qualified for correlation matrix
  - Centering explicit in all PCA formulas
- Finance applications: yield curve PCA, portfolio risk decomposition, market regime detection
- Bloom's Level 4-5 LOs

### MUST NOT Have
- Any modification to preamble (lines 1-92)
- Dual-assigned charts (each chart in exactly ONE file)
- LOs at slide 2 (must be after intro section)
- Subplots or multi-figure slides
- More than 4 bullets per slide
- Any slide without \bottomnote{}
- XKCD image reused at closing (use text callback only)
- "PCA assumes Gaussian" (corrected to "optimal for Gaussian but valid for any distribution")
- Unqualified Kaiser criterion (must state "correlation matrix only")
- Pseudocode blocks (PCA is closed-form; no pseudocode per instructor guide)

---

## Task Flow

```
Task 1 (Rewrite L05_overview.tex)
    |
    v
Task 2 (Rewrite L05_deepdive.tex)  [can run in PARALLEL with Task 1]
    |
    v
Task 3 (Compile both PDFs)  [depends on Tasks 1+2]
    |
    v
Task 4 (Architect verify)  [depends on Task 3]
```

---

## Task 1: Rewrite L05_overview.tex

**Target: 24 slides, 3 zones, 5 charts**

### Preamble (lines 1-92): PRESERVE UNCHANGED

### Title Block (line 93-97): Minor update
```latex
\title[L05: PCA \& t-SNE]{L05: PCA \& t-SNE}
\subtitle{Dimensionality Reduction for Visualization and Preprocessing}
\author{Methods and Algorithms}
\institute{MSc Data Science}       % <-- ADD THIS LINE
\date{Spring 2026}
```

### ZONE 1: INTRODUCTION (Slides 1-7, NO formulas, NO Greek letters)

```
SLIDE 1: Title Page
- Layout: \titlepage (standard)
- Content: Auto-generated from title block
- Chart: none
- \bottomnote: none (title page)
```

```
SLIDE 2: Outline
- Layout: \tableofcontents (standard)
- Content: Auto-generated section list
- Chart: none
- \bottomnote: none (outline page)
```

```
SLIDE 3: Opening Comic -- XKCD #2048
- Layout: Centered image, full-height
- Content:
  - Frame title: "The Curse of Too Many Dimensions"
  - \includegraphics[height=0.70\textheight]{images/2048_curve_fitting.png}
- Chart: none (XKCD image)
- \bottomnote{XKCD \#2048 ``Curve Fitting'' by Randall Munroe (CC BY-NC 2.5)}
```

```
SLIDE 4: The Dimensionality Problem
- Layout: Bullet list, no formulas
- Content:
  - A portfolio with 100 assets means working in 100-dimensional space
  - Humans cannot visualize anything beyond 3 dimensions
  - Many features are correlated and carry redundant information
  - We need methods that compress data while preserving structure
- Chart: none
- \bottomnote{Dimensionality reduction: see the forest for the trees in high-dimensional data}
```

```
SLIDE 5: Two Approaches to Reduction
- Layout: Two-column conceptual comparison (no math)
- Content:
  - PCA: Find the directions of greatest spread and project onto them
    - Like finding the best camera angle for a 3D object
    - Linear, fast, reversible (approximately)
  - t-SNE: Preserve which points are neighbors in a 2D map
    - Like seating friends close together at a wedding
    - Non-linear, visualization only
- Chart: none
- \bottomnote{PCA preserves global variance; t-SNE preserves local neighborhoods}
```

```
SLIDE 6: Why Banks Care About Dimensionality Reduction
- Layout: Bullet list, plain language
- Content:
  - Yield curves: 20+ maturities collapse to 3 meaningful factors
  - Portfolio risk: hundreds of assets decompose into a few risk drivers
  - Customer analytics: high-dimensional behavior data mapped to visual clusters
  - Market regimes: t-SNE reveals hidden groupings in trading patterns
- Chart: none
- \bottomnote{Dimensionality reduction is used daily in every major bank's risk management}
```

```
SLIDE 7: Learning Objectives
- Layout: Numbered list with Bloom's verbs
- Content:
  1. \textbf{Derive} PCA from the variance maximization principle and explain the SVD--PCA equivalence
  2. \textbf{Evaluate} dimensionality reduction methods (PCA vs.\ t-SNE vs.\ UMAP) for a given dataset
  3. \textbf{Analyze} the effect of hyperparameters (perplexity, learning rate) on t-SNE embeddings
  4. \textbf{Critique} PCA assumptions and limitations for nonlinear financial data (e.g., yield curves)
- Finance Application line: Portfolio risk decomposition, yield curve analysis, market regime detection
- Chart: none
- \bottomnote{Bloom's Level 4--5: Derive, Evaluate, Analyze, Critique}
```

### ZONE 2: CORE CONTENT -- PMSP (Slides 8-21)

**\section{Problem}**

```
SLIDE 8: The Business Problem
- Layout: Structured bullet list
- Content:
  - Curse of Dimensionality:
    - Portfolio with 100+ assets: impossible to visualize relationships
    - Customer data with dozens of features: redundant information
    - High dimensions cause sparsity, computational cost, and overfitting
  - Question: Can we find a lower-dimensional representation that preserves the important structure?
- Chart: none
- \bottomnote{Bellman (1961): ``curse of dimensionality'' -- data requirements grow exponentially with dimension}
```

```
SLIDE 9: Key Equations -- PCA
- Layout: Equation block with brief labels
- Content:
  - Covariance Matrix (from mean-centered data $X_c = X - \bar{X}$):
    $C = \frac{1}{n-1} X_c^\top X_c$
  - Eigendecomposition: $C\, v_k = \lambda_k\, v_k$
    (principal directions and variances)
  - Explained Variance Ratio:
    $\text{EVR}_k = \frac{\lambda_k}{\sum_{j=1}^{p} \lambda_j}$
- Chart: none
- \bottomnote{PCA: find orthogonal directions maximizing variance via eigendecomposition of the covariance matrix}
```

```
SLIDE 10: Key Equations -- t-SNE
- Layout: Equation block with brief labels
- Content:
  - High-Dimensional Similarity:
    $p_{j|i} = \frac{\exp(-\|x_i - x_j\|^2 / 2\sigma_i^2)}{\sum_{k \neq i}\exp(-\|x_i - x_k\|^2 / 2\sigma_i^2)}$
  - Low-Dimensional Similarity (t-distribution with 1 df):
    $q_{ij} = \frac{(1 + \|y_i - y_j\|^2)^{-1}}{\sum_{k \neq l} (1 + \|y_k - y_l\|^2)^{-1}}$
  - Objective: Minimize $KL(P\|Q) = \sum_{i \neq j} p_{ij} \log \frac{p_{ij}}{q_{ij}}$
- Chart: none
- \bottomnote{t-SNE: Gaussian similarities in high-D, t-distribution in low-D, minimize KL divergence}
```

**\section{Method}**

```
SLIDE 11: Scree Plot: Choosing Components (CHART)
- Layout: Full-width chart
- Content:
  - Brief text: "Plot eigenvalues (or cumulative variance) vs.\ component number; choose at the elbow"
  - \includegraphics[width=0.65\textwidth]{01_scree_plot/chart.pdf}
- Chart: 01_scree_plot/chart.pdf
- \bottomnote{Choose $k$ components capturing 80--95\% of variance, or at the ``elbow'' -- Kaiser criterion ($\lambda > 1$) valid for correlation matrix only}
```

```
SLIDE 12: PCA in Finance: Yield Curve Decomposition
- Layout: Bullet list with numerical values
- Content:
  - Yield curves (20+ maturities) decompose into ~3 principal components:
  - PC1 = \textbf{Level} (parallel shift): explains ~85\% variance
    - Loadings: approximately flat across all maturities
  - PC2 = \textbf{Slope} (steepening/flattening): explains ~10\% variance
    - Loadings: negative short end, positive long end
  - PC3 = \textbf{Curvature} (butterfly): explains ~3\% variance
    - Loadings: negative at ends, positive in middle
  - Together: 98\%+ of yield curve movements in 3 numbers
- Chart: none
- \bottomnote{Level/slope/curvature: industry-standard yield curve decomposition used in every bank}
```

```
SLIDE 13: PCA on Swiss Roll (CHART)
- Layout: Chart with brief text
- Content:
  - PCA projects onto directions of maximum variance
  - On non-linear manifolds, these directions miss the true structure
  - \includegraphics[width=0.65\textwidth]{05a_pca_swiss_roll/chart.pdf}
- Chart: 05a_pca_swiss_roll/chart.pdf
- \bottomnote{PCA (linear) cannot unroll the Swiss roll -- the projected structure overlaps}
```

```
SLIDE 14: t-SNE on Swiss Roll (CHART)
- Layout: Chart with brief text
- Content:
  - t-SNE preserves local neighborhoods and can unroll non-linear manifolds
  - Compare with the PCA projection on the previous slide
  - \includegraphics[width=0.65\textwidth]{05b_tsne_swiss_roll/chart.pdf}
- Chart: 05b_tsne_swiss_roll/chart.pdf
- \bottomnote{t-SNE (non-linear) successfully unrolls the manifold -- local structure preserved}
```

```
SLIDE 15: t-SNE: Cluster Preservation (CHART)
- Layout: Chart with brief text
- Content:
  - t-SNE excels at revealing cluster structure in high-dimensional data
  - Digit recognition (MNIST): 64 dimensions projected to 2D
  - \includegraphics[width=0.55\textwidth]{06c_tsne_cluster_projection/chart.pdf}
- Chart: 06c_tsne_cluster_projection/chart.pdf
- \bottomnote{t-SNE on MNIST digits: clear digit clusters in 2D -- PCA would show overlapping groups}
```

```
SLIDE 16: t-SNE Caveats: What NOT to Interpret
- Layout: Warning-style bullet list
- Content:
  - Cluster SIZES are not meaningful (artifact of density)
  - Distances BETWEEN clusters are not meaningful
  - Results are non-deterministic (run multiple times)
  - t-SNE is for visualization ONLY -- never cluster on t-SNE output
  - Best practice: Standardize -> PCA (30-50 dims) -> t-SNE (2D)
- Chart: none
- \bottomnote{t-SNE shows IF clusters exist, not HOW they relate -- always run multiple times}
```

**\section{Solution}**

```
SLIDE 17: PCA vs t-SNE: Head-to-Head Comparison
- Layout: Comparison table (tabular with booktabs)
- Content:
  | Aspect       | PCA               | t-SNE              |
  | Type         | Linear            | Non-linear          |
  | Speed        | Fast $O(np^2)$    | Slow $O(n^2)$      |
  | Deterministic| Yes               | No                  |
  | Preserves    | Global variance   | Local neighbors     |
  | Reversible   | Lossy if $k<p$    | No                  |
  | Use for ML   | Yes (preprocess)  | No                  |
  | Visualization| Adequate          | Excellent           |
- Chart: none
- \bottomnote{Use PCA for preprocessing and feature extraction; t-SNE for visualization only}
```

```
SLIDE 18: Finance Application: Portfolio Risk Decomposition
- Layout: Bullet list with concrete example
- Content:
  - PC1 often = "market factor" (loadings ~uniform across assets)
  - PC2-3 = sector or style factors (e.g., tech vs banks)
  - Higher PCs = idiosyncratic risk
  - Practical use: reduce 100-asset portfolio to 3-5 risk factors
  - Applications: risk attribution, hedging, noise reduction in signals
- Chart: none
- \bottomnote{PCA on asset returns reveals latent factor structure -- foundation of factor investing}
```

```
SLIDE 19: Finance Application: Market Regime Detection with t-SNE
- Layout: Bullet list
- Content:
  - Input: daily feature vectors (volatility, volume, spreads, correlations)
  - t-SNE projection reveals natural clusters of "market states"
  - Typical findings: calm/trending, volatile/stressed, transition periods
  - Use: regime-conditional trading strategies, risk limits
  - Warning: always validate with domain knowledge and out-of-sample testing
- Chart: none
- \bottomnote{t-SNE for regime detection: exploratory only -- combine with formal clustering methods}
```

```
SLIDE 20: Decision Framework (CHART)
- Layout: Chart with brief text
- Content:
  - Use columns: text left (0.42), chart right (0.55)
  - Left: When to use PCA (preprocessing, linear structure, speed, reversibility needed) vs t-SNE (visualization, cluster discovery, non-linear manifolds, exploratory analysis)
  - \includegraphics[width=\textwidth]{07_decision_flowchart/chart.pdf}
- Chart: 07_decision_flowchart/chart.pdf
- \bottomnote{Start with PCA for preprocessing; add t-SNE when you need to see structure}
```

**\section{Practice}**

```
SLIDE 21: Hands-on Exercise
- Layout: Numbered exercise list
- Content:
  - Exercise 1: Apply PCA to financial returns data, interpret the scree plot, choose k
  - Exercise 2: Visualize clusters with t-SNE at perplexity 5, 30, 50
  - Exercise 3: Compare PCA vs t-SNE projections side by side
  - Link: See course materials on GitHub
- Chart: none
- \bottomnote{Estimated time: 45--60 minutes for all three exercises}
```

### ZONE 3: WRAP-UP (Slides 22-24)

**\section{Summary}**

```
SLIDE 22: Key Takeaways
- Layout: Two-part summary
- Content:
  - PCA: linear, fast, (approximately) reversible; use for preprocessing and feature extraction; choose k by scree plot or 80-95\% variance rule
  - t-SNE: non-linear, slow, visualization-only; excellent for exploring cluster structure; don't interpret distances or sizes
  - Common pipeline: Standardize -> PCA (30-50) -> t-SNE (2D)
  - Finance: yield curve = level/slope/curvature; portfolio risk = factor decomposition
- Chart: none
- \bottomnote{Both are foundational: PCA for compression, t-SNE for visual exploration}
```

```
SLIDE 23: Closing Comic -- XKCD #2400 Callback
- Layout: Centered text, italic quote
- Content:
  - Frame title: "Until Next Time..."
  - Italic quote referencing XKCD #2400 "Statistics":
    *"We reduced our 100-dimensional portfolio to 3 principal components. The fourth component? That's just noise... probably."*
  - "Now you can compress with PCA and visualize with t-SNE."
  - Next Session: L06 -- Embeddings and Reinforcement Learning
- Chart: none
- \bottomnote{XKCD \#2400 ``Statistics'' callback by Randall Munroe (CC BY-NC 2.5) -- not all variance is signal}
```

```
SLIDE 24: References
- Layout: \footnotesize bullet list
- Content:
  - Jolliffe, I.T. (2002). Principal Component Analysis. Springer.
  - van der Maaten, L. \& Hinton, G. (2008). Visualizing Data using t-SNE. JMLR.
  - James et al. (2021). ISLR, Chapter 12. https://www.statlearning.com/
  - Hastie et al. (2009). ESL, Chapter 14.
  - McInnes et al. (2018). UMAP: Uniform Manifold Approximation and Projection.
- Chart: none
- \bottomnote{Primary textbooks: ISLR Ch.~12, ESL Ch.~14}
```

### Acceptance Criteria -- Task 1
- [ ] Exactly 24 slides
- [ ] Preamble lines 1-92 unchanged
- [ ] \institute{MSc Data Science} present
- [ ] Zone comments present (3 zones)
- [ ] XKCD #2048 at slide 3
- [ ] XKCD #2400 callback at slide 23
- [ ] LOs at slide 7 (after intro section)
- [ ] 5 charts used: 01, 05a, 05b, 06c, 07
- [ ] No charts from deepdive set (02, 03, 04a, 04b, 04c, 06a, 06b)
- [ ] Every content slide has \bottomnote{}
- [ ] Every slide has numbered comment header
- [ ] Max 3-4 bullets per itemize
- [ ] No formulas in Zone 1 (slides 1-7)
- [ ] Bloom's Level 4-5 in LOs
- [ ] Yield curve PCA included (slide 12)
- [ ] Finance regime detection included (slide 19)
- [ ] Kaiser criterion qualified (slide 11 bottomnote)

---

## Task 2: Rewrite L05_deepdive.tex

**Target: ~40 main slides + ~8 appendix slides = ~48 total, 7 charts**

### Preamble (lines 1-92): PRESERVE UNCHANGED

### Title Block (line 93-97): Update
```latex
\title[L05: PCA \& t-SNE Deep Dive]{L05: PCA \& t-SNE}
\subtitle{Deep Dive: Theory, Derivations, and Financial Applications}
\author{Methods and Algorithms}
\institute{MSc Data Science}       % <-- ADD THIS LINE
\date{Spring 2026}
```

### Main Slides (1-40)

```
SLIDE 1: Title Page
- Layout: \titlepage (standard)
- Content: Auto-generated from title block
- Chart: none
- \bottomnote: none (title page)
```

```
SLIDE 2: Outline
- Layout: \tableofcontents (standard)
- Content: Auto-generated section list
- Chart: none
- \bottomnote: none (outline page)
```

```
SLIDE 3: Opening Comic -- XKCD #2048
- Layout: Centered image
- Content:
  - Frame title: "Finding Signal in the Noise"
  - \includegraphics[height=0.65\textheight]{images/2048_curve_fitting.png}
- Chart: none (XKCD image)
- \bottomnote{XKCD \#2048 ``Curve Fitting'' by Randall Munroe (CC BY-NC 2.5) -- ``The data points are pretty sparse...let's fit all the models''}
```

```
SLIDE 4: Learning Objectives
- Layout: Numbered list
- Content:
  1. \textbf{Derive} PCA from the variance maximization principle via Lagrangian optimization and prove the SVD--PCA equivalence
  2. \textbf{Evaluate} dimensionality reduction methods using quantitative criteria (variance explained, silhouette, trustworthiness)
  3. \textbf{Analyze} the t-SNE gradient, crowding problem, and perplexity--entropy relationship
  4. \textbf{Critique} PCA limitations for nonlinear data and apply yield curve decomposition with numerical interpretation
- Finance Applications: Yield curve PCA, portfolio risk decomposition, market regime detection
- Chart: none
- \bottomnote{Bloom's Level 4--5: Derive, Evaluate, Analyze, Critique}
```

#### Section 1: PCA Foundations (~8 slides)

**\section{PCA Foundations}**

```
SLIDE 5: PCA: Variance Maximization
- Layout: Structured bullets
- Content:
  - Goal: find orthogonal directions of maximum variance
  - Input: mean-centered data $X_c = X - \bar{X}$ (centering is REQUIRED)
  - Key properties:
    - Linear transformation
    - Components are uncorrelated (orthogonal)
    - Partially reversible (lossy reconstruction when $k < p$)
  - PCA does NOT require Gaussian data -- optimal for Gaussian, valid for any distribution
- Chart: none
- \bottomnote{PCA is a second-moment method based on covariance -- no distributional assumption required}
```

```
SLIDE 6: Mathematical Foundation
- Layout: Equation block
- Content:
  - Covariance Matrix (from mean-centered data):
    $\Sigma = \frac{1}{n-1} X_c^\top X_c$ where $X_c = X - \bar{X}$
  - Eigendecomposition:
    $\Sigma v = \lambda v$
    where $v$ = eigenvector (principal direction), $\lambda$ = eigenvalue (variance captured)
  - Projection onto $k$ components:
    $Z = X_c W_k$ where $W_k = [v_1, \ldots, v_k]$ (centered data required)
- Chart: none
- \bottomnote{Eigenvalues $\lambda_k$ are the variance captured by each component; eigenvectors $v_k$ are the directions}
```

```
SLIDE 7: Why Eigenvectors? The Optimality Proof
- Layout: Derivation sequence
- Content:
  - Find direction $w$ maximizing projected variance:
    $\max_{w} w^\top \Sigma w$ subject to $\|w\| = 1$
  - Lagrangian: $L = w^\top \Sigma w - \lambda(w^\top w - 1)$
  - First-order condition:
    $\nabla_w L = 2\Sigma w - 2\lambda w = 0$
  - Result: $\Sigma w = \lambda w$ (eigenvalue equation!)
  - Maximum variance = largest eigenvalue $\lambda_1$; direction = corresponding eigenvector $v_1$
- Chart: none
- \bottomnote{Constrained optimization proves eigenvectors are the optimal projection directions}
```

```
SLIDE 8: SVD--PCA Equivalence
- Layout: Proof steps
- Content:
  - Theorem: PCA principal components = right singular vectors of $X_c$
  - Proof sketch:
    1. SVD: $X_c = U S V^\top$
    2. Then: $X_c^\top X_c = V S^2 V^\top$
    3. Covariance: $C = \frac{1}{n-1} V S^2 V^\top$
    4. Therefore: columns of $V$ are eigenvectors of $C$
  - Eigenvalues: $\lambda_k = s_k^2 / (n-1)$
  - Why SVD? Numerically more stable (avoids squaring condition number)
- Chart: none
- \bottomnote{scikit-learn uses truncated SVD internally -- never forms the covariance matrix explicitly}
```

```
SLIDE 9: Variance Explained and Component Selection
- Layout: Equations + bullet list
- Content:
  - Explained Variance Ratio: $\text{EVR}_k = \frac{\lambda_k}{\sum_{j=1}^{p} \lambda_j}$
  - Cumulative Variance: $\text{Cum}_k = \sum_{i=1}^{k} \text{EVR}_i$
  - Rules for choosing $k$:
    - Keep 80--95\% of total variance
    - Scree plot "elbow" method
    - Kaiser criterion: $\lambda > 1$ (\textbf{valid for correlation matrix / standardized data ONLY})
    - Parallel analysis (compare to random data)
- Chart: none
- \bottomnote{Kaiser criterion on raw covariance matrix is meaningless -- always standardize first or use parallel analysis}
```

```
SLIDE 10: Principal Components Visualization (CHART)
- Layout: Chart with brief text
- Content:
  - PC1 captures the dominant trend (highest variance direction)
  - PC2 captures the next-best orthogonal direction
  - \includegraphics[width=0.55\textwidth]{02_principal_components/chart.pdf}
- Chart: 02_principal_components/chart.pdf
- \bottomnote{PC1 and PC2 are orthogonal: they capture independent patterns in the data}
```

```
SLIDE 11: Reconstruction from k Components
- Layout: Equations + text
- Content:
  - Reconstruction formula: $\hat{X} = Z W_k^\top + \bar{X}$ (add mean back!)
  - Reconstruction Error:
    $\|X - \hat{X}\|_F^2 = \sum_{i=k+1}^{p} \lambda_i$
  - Error = sum of discarded eigenvalues
  - More components -> lower error, but diminishing returns
- Chart: none
- \bottomnote{Reconstruction error is exactly the sum of the eigenvalues you threw away}
```

```
SLIDE 12: Reconstruction Error vs Components (CHART)
- Layout: Full-width chart
- Content:
  - \includegraphics[width=0.65\textwidth]{03_reconstruction/chart.pdf}
- Chart: 03_reconstruction/chart.pdf
- \bottomnote{Adding more components always reduces error -- but the first few components capture most of the signal}
```

#### Section 2: PCA in Finance (~5 slides)

**\section{PCA in Finance}**

```
SLIDE 13: Yield Curve PCA: The Canonical Example
- Layout: Bullet list with numerical values
- Content:
  - Yield curves (20+ maturities) decompose into ~3 principal components
  - PC1 = \textbf{Level} (parallel shift): ~85\% variance
    - Loadings approximately flat across maturities
  - PC2 = \textbf{Slope} (steepening/flattening): ~10\% variance
    - Negative short end, positive long end
  - PC3 = \textbf{Curvature} (butterfly): ~3\% variance
    - Negative at ends, positive in middle
  - Together: 98\%+ of all yield curve movements
- Chart: none
- \bottomnote{Level/slope/curvature: used daily in every bank's fixed-income risk management}
```

```
SLIDE 14: Yield Curve PCA: Worked Example
- Layout: Numerical table + interpretation
- Content:
  - Example: 5 maturities (1Y, 2Y, 5Y, 10Y, 30Y)
  - Table showing PC1, PC2, PC3 loadings (numerical):
    | Maturity | PC1 (Level) | PC2 (Slope) | PC3 (Curvature) |
    | 1Y       | 0.42        | -0.58       | 0.50            |
    | 2Y       | 0.44        | -0.37       | -0.20           |
    | 5Y       | 0.46        | 0.06        | -0.62           |
    | 10Y      | 0.45        | 0.41        | -0.10           |
    | 30Y      | 0.43        | 0.60        | 0.56            |
  - Reading: PC1 shifts all rates similarly; PC2 moves short and long in opposite directions
- Chart: none
- \bottomnote{Trading: duration hedging (PC1), curve trades (PC2), butterfly spreads (PC3)}
```

```
SLIDE 15: Portfolio Risk Decomposition
- Layout: Bullet list with numerical example
- Content:
  - Apply PCA to daily returns of n assets:
  - PC1 loadings ~uniform: "market factor" (~60\% variance for equities)
  - PC2: sector rotation (e.g., tech positive, banks negative)
  - PC3+: style factors or idiosyncratic noise
  - Example: 10-stock portfolio, PC1 explains 62\%, first 3 PCs explain 81\%
  - Use: risk attribution, factor-neutral hedging, noise filtering for signals
- Chart: none
- \bottomnote{PCA on asset returns: empirical foundation of statistical factor models}
```

```
SLIDE 16: Statistical Inference for PCA
- Layout: Structured bullet list
- Content:
  - Bootstrap Confidence Intervals for loadings:
    - Resample data B times, recompute PCA, track loading stability
  - Parallel Analysis for choosing k:
    - Compare eigenvalues to random data; keep $\lambda_{data} > \lambda_{random}$
  - Cross-Validation:
    - Split data, train PCA, measure reconstruction error on holdout
  - For t-SNE: run multiple times with different seeds; unstable clusters are artifacts
- Chart: none
- \bottomnote{MSc-level: always quantify uncertainty -- bootstrap CIs and parallel analysis are standard}
```

```
SLIDE 17: PCA Limitations
- Layout: Two-column: limitations + solutions
- Content:
  - When PCA falls short:
    - Non-linear relationships (curved manifolds)
    - Cluster structure not aligned with variance direction
    - Outliers heavily influence results (leverage on covariance)
  - Alternatives:
    - Kernel PCA: implicit non-linear mapping via kernel trick
    - Robust PCA: decompose into low-rank + sparse (for outliers)
    - t-SNE/UMAP: for visualization of non-linear structure
- Chart: none
- \bottomnote{PCA is optimal for Gaussian data; for non-Gaussian, it still works but may miss non-linear structure}
```

#### Section 3: t-SNE Theory (~8 slides)

**\section{t-SNE Theory}**

```
SLIDE 18: t-SNE: Core Idea
- Layout: Bullet list
- Content:
  - t-Distributed Stochastic Neighbor Embedding (van der Maaten \& Hinton, 2008)
  - Core idea: convert pairwise distances to probabilities
  - In high-D: Gaussian kernel -> conditional similarities $p_{j|i}$
  - In low-D: Student t-distribution (1 df) -> similarities $q_{ij}$
  - Objective: minimize KL divergence between P and Q
  - Result: low-D embedding that preserves local neighborhood structure
- Chart: none
- \bottomnote{t-SNE: a visualization method -- NOT for preprocessing or as ML input features}
```

```
SLIDE 19: t-SNE Mathematical Formulation
- Layout: Equation sequence
- Content:
  - High-dimensional conditional similarity:
    $p_{j|i} = \frac{\exp(-\|x_i - x_j\|^2 / 2\sigma_i^2)}{\sum_{k \neq i} \exp(-\|x_i - x_k\|^2 / 2\sigma_i^2)}$
  - Symmetrize to joint probability:
    $p_{ij} = \frac{p_{j|i} + p_{i|j}}{2n}$
  - Low-dimensional similarity (Student-t, 1 df):
    $q_{ij} = \frac{(1 + \|y_i - y_j\|^2)^{-1}}{\sum_{k \neq l} (1 + \|y_k - y_l\|^2)^{-1}}$
- Chart: none
- \bottomnote{Symmetrization ensures each point contributes equally regardless of local density}
```

```
SLIDE 20: The Crowding Problem and t-Distribution
- Layout: Explanation + rationale
- Content:
  - The crowding problem: in high-D, moderate distances are common; when projected to low-D, these moderate distances collapse to small values
  - Result with Gaussian in low-D: all points crowd into the center of the map
  - Solution: use heavy-tailed t-distribution (1 df) in low-D
    - Nearby points: t-distribution and Gaussian are similar (neighborhoods preserved)
    - Distant points: t-distribution has heavier tails (allows them to spread apart)
  - This is the key innovation of t-SNE over the original SNE
- Chart: none
- \bottomnote{The t-distribution solves crowding: nearby pairs attract, distant pairs can repel via heavy tails}
```

```
SLIDE 21: KL Divergence and the Gradient
- Layout: Equations + interpretation
- Content:
  - Objective: $KL(P\|Q) = \sum_{i \neq j} p_{ij} \log \frac{p_{ij}}{q_{ij}}$
  - KL is asymmetric: penalizes large $p_{ij}$ with small $q_{ij}$ more than the reverse
  - Consequence: nearby points MUST stay nearby (preserves local structure)
  - Distant points CAN end up anywhere (global structure not guaranteed)
  - Gradient: $\frac{\partial KL}{\partial y_i} = 4 \sum_j (p_{ij} - q_{ij})(y_i - y_j)(1 + \|y_i - y_j\|^2)^{-1}$
- Chart: none
- \bottomnote{Attractive force ($p_{ij} > q_{ij}$): pull together; Repulsive force ($p_{ij} < q_{ij}$): push apart}
```

```
SLIDE 22: Perplexity: Low (CHART)
- Layout: Full-width chart
- Content:
  - Perplexity = $2^H$ where $H$ is entropy of conditional distribution
  - Roughly the effective number of neighbors considered
  - Low perplexity (5): focus on very local structure
  - \includegraphics[width=0.55\textwidth]{04a_tsne_perplexity_5/chart.pdf}
- Chart: 04a_tsne_perplexity_5/chart.pdf
- \bottomnote{Perplexity 5: tight clusters, only nearest 5 neighbors matter -- may fragment true clusters}
```

```
SLIDE 23: Perplexity: Default (CHART)
- Layout: Full-width chart
- Content:
  - Default perplexity (30): balanced local and global structure
  - Good starting point for most datasets
  - \includegraphics[width=0.55\textwidth]{04b_tsne_perplexity_30/chart.pdf}
- Chart: 04b_tsne_perplexity_30/chart.pdf
- \bottomnote{Perplexity 30: balanced -- the default in scikit-learn and a good starting point}
```

```
SLIDE 24: Perplexity: High (CHART)
- Layout: Full-width chart
- Content:
  - High perplexity (100): more global structure preserved
  - Clusters may merge; structure becomes more diffuse
  - \includegraphics[width=0.55\textwidth]{04c_tsne_perplexity_100/chart.pdf}
- Chart: 04c_tsne_perplexity_100/chart.pdf
- \bottomnote{Perplexity 100: global view -- individual clusters less distinct, large-scale relationships visible}
```

```
SLIDE 25: Perplexity Guidelines
- Layout: Structured bullets
- Content:
  - Perplexity = $2^H$ = effective number of neighbors
  - Low (5--10): very local structure, may fragment clusters
  - Medium (30--50): balanced (default), good for most data
  - High (100+): more global, clusters may merge
  - Guidelines:
    - Must be smaller than number of points
    - Larger datasets tolerate higher perplexity
    - Always run multiple perplexities to validate findings
- Chart: none
- \bottomnote{No single perplexity is ``correct'' -- results that persist across perplexities are more trustworthy}
```

#### Section 4: Comparison (~5 slides)

**\section{PCA vs t-SNE Comparison}**

```
SLIDE 26: Cluster Preservation: Original Data (CHART)
- Layout: Full-width chart
- Content:
  - MNIST digits: 64-dimensional pixel data
  - In raw space, classes overlap heavily
  - \includegraphics[width=0.55\textwidth]{06a_original_clusters/chart.pdf}
- Chart: 06a_original_clusters/chart.pdf
- \bottomnote{MNIST digits (64 dims): digit classes overlap when viewed in any two raw pixel dimensions}
```

```
SLIDE 27: Cluster Preservation: PCA Projection (CHART)
- Layout: Full-width chart
- Content:
  - PCA finds maximum-variance directions
  - Some digit separation, but significant overlap
  - \includegraphics[width=0.55\textwidth]{06b_pca_cluster_projection/chart.pdf}
- Chart: 06b_pca_cluster_projection/chart.pdf
- \bottomnote{PCA finds max-variance directions -- partial digit separation but linear projection has limits}
```

```
SLIDE 28: t-SNE Caveats (Detailed)
- Layout: Bullet list
- Content:
  - Non-deterministic: different random seeds give different layouts
  - O($n^2$) naive; O($n \log n$) with Barnes-Hut approximation (default in scikit-learn)
  - Cannot embed new points without re-running
  - Hyperparameter sensitive: perplexity, learning rate, early exaggeration
  - Best practices:
    - Use PCA first to reduce to 30--50 dims (speeds up t-SNE)
    - Run 3--5 times with different seeds
    - Structures present in all runs are real
- Chart: none
- \bottomnote{t-SNE shows IF clusters exist, not HOW they relate -- always verify with domain knowledge}
```

```
SLIDE 29: UMAP: Modern Alternative
- Layout: Bullet list
- Content:
  - Uniform Manifold Approximation and Projection (McInnes et al., 2018)
  - Advantages over t-SNE:
    - Faster (especially for large datasets)
    - Better preserves global structure
    - Can embed new points (transform method)
  - Hyperparameters: n_neighbors (~perplexity), min_dist (cluster tightness)
  - Increasingly the default choice for large-scale visualization
- Chart: none
- \bottomnote{UMAP often preferred in practice -- see McInnes et al.\ (2018) for formal comparison}
```

```
SLIDE 30: When to Use Which
- Layout: Two-part recommendation
- Content:
  - Use PCA when:
    - Preprocessing for ML (reduce features before model)
    - Linear relationships expected
    - Need reversibility (reconstruction)
    - Speed matters (large n, large p)
  - Use t-SNE/UMAP when:
    - Visualizing high-dimensional data
    - Looking for cluster structure
    - Non-linear manifolds expected
    - Exploratory analysis
- Chart: none
- \bottomnote{Often use both: PCA first to 30--50 dims, then t-SNE/UMAP for 2D visualization}
```

#### Section 5: Finance Applications (~3 slides)

**\section{Finance Applications}**

```
SLIDE 31: Market Regime Detection with t-SNE
- Layout: Structured description
- Content:
  - Input: daily rolling feature vectors (realized vol, volume ratios, credit spreads, correlation changes)
  - Pipeline: standardize features -> PCA (15-20 dims) -> t-SNE (2D)
  - Typical regime clusters: low-vol trending, high-vol mean-reverting, crisis
  - Validation: color points by VIX level or drawdown magnitude
  - Warning: exploratory only; use HMMs or formal methods for production
- Chart: none
- \bottomnote{t-SNE regime detection: great for hypothesis generation, not for automated trading signals}
```

```
SLIDE 32: PCA Preprocessing for ML Pipelines
- Layout: Bullet list
- Content:
  - Common pipeline: StandardScaler -> PCA(0.95) -> Classifier
  - Benefits: faster training, reduced overfitting, removed multicollinearity
  - Caution: PCA is unsupervised -- may discard features that are low-variance but predictive
  - Alternative: Supervised feature selection (mutual information, L1 regularization)
  - scikit-learn: Pipeline(StandardScaler(), PCA(n_components=0.95), LogisticRegression())
- Chart: none
- \bottomnote{PCA as preprocessing: always cross-validate the full pipeline, not PCA in isolation}
```

```
SLIDE 33: Comparison Table: Dimensionality Reduction Methods
- Layout: Tabular comparison (5 methods)
- Content:
  | Method    | Type      | Speed     | New Points | Best For            |
  | PCA       | Linear    | Fast      | Yes        | Preprocessing       |
  | Kernel PCA| Non-linear| Moderate  | Yes        | Non-linear features |
  | t-SNE     | Non-linear| Slow      | No         | Visualization       |
  | UMAP      | Non-linear| Moderate  | Yes        | Visualization+      |
  | Autoencoder| Non-linear| Slow (train)| Yes     | Complex patterns    |
- Chart: none
- \bottomnote{Choose method by task: preprocessing (PCA), visualization (t-SNE/UMAP), complex features (autoencoder)}
```

#### Section 6: Implementation (~3 slides)

**\section{Implementation}**

```
SLIDE 34: PCA in scikit-learn
- Layout: Code-style bullet list
- Content:
  - PCA(n_components=k): keep k components
  - PCA(n_components=0.95): keep 95\% variance (auto-selects k)
  - Attributes: explained_variance_ratio_, components_ (loadings)
  - pca.inverse_transform(): reconstruct (add mean back automatically)
  - Note: sklearn uses truncated SVD internally (more stable than eigendecomposition)
- Chart: none
- \bottomnote{Always \texttt{StandardScaler()} before PCA -- otherwise high-variance features dominate}
```

```
SLIDE 35: t-SNE and UMAP in scikit-learn
- Layout: Code-style bullet list
- Content:
  - TSNE(n_components=2, perplexity=30, random_state=42)
  - Key params: perplexity, learning_rate, n_iter, early_exaggeration
  - UMAP: umap.UMAP(n_neighbors=15, min_dist=0.1)
  - Best practice: PCA to 30-50 dims first, then t-SNE/UMAP
  - Always set random_state for reproducibility
- Chart: none
- \bottomnote{Normalize data before t-SNE/UMAP; consider PCA preprocessing for speed}
```

#### Section 7: Practice + Summary (~5 slides)

**\section{Practice}**

```
SLIDE 36: Hands-on Exercise
- Layout: Numbered exercise list
- Content:
  - Exercise 1: Apply PCA to yield curve data, identify level/slope/curvature, interpret loadings
  - Exercise 2: Compare PCA vs t-SNE on stock return data -- which reveals sector structure better?
  - Exercise 3: Vary perplexity (5, 30, 100) on customer transaction data, document how clusters change
  - Link: See course materials for Colab notebook
- Chart: none
- \bottomnote{Exercises use real financial data -- connect theory to practice}
```

**\section{Summary}**

```
SLIDE 37: Key Takeaways
- Layout: Structured summary
- Content:
  - PCA: variance maximization via eigendecomposition; SVD for computation; yield curve = level/slope/curvature
  - t-SNE: probability-based neighbor embedding; crowding problem solved by t-distribution; visualization only
  - Finance: yield curve PCA (daily in banks), portfolio factors, regime detection
  - Pipeline: Standardize -> PCA (30-50) -> t-SNE (2D) for visualization
- Chart: none
- \bottomnote{PCA and t-SNE are complementary: PCA for compression and preprocessing, t-SNE for seeing structure}
```

```
SLIDE 38: Closing Comic -- XKCD #2400 Callback
- Layout: Centered text, italic quote
- Content:
  - Frame title: "Until Next Time..."
  - Italic quote referencing XKCD #2400 "Statistics":
    *"After reducing 200 dimensions to 3, the risk manager asked: 'But which 197 dimensions did we lose?' The answer: 'The ones that were just noise... statistically speaking.'"*
  - "You can now derive PCA, interpret its components, and visualize structure with t-SNE."
  - Next Session: L06 -- Embeddings and Reinforcement Learning
- Chart: none
- \bottomnote{XKCD \#2400 ``Statistics'' callback by Randall Munroe (CC BY-NC 2.5) -- dimensionality reduction is the art of knowing what to throw away}
```

```
SLIDE 39: References (Textbooks)
- Layout: \footnotesize two-section list
- Content:
  - Textbooks:
    - Jolliffe, I.T. (2002). Principal Component Analysis. Springer.
    - James et al. (2021). ISLR, Chapter 12: Unsupervised Learning.
    - Hastie et al. (2009). ESL, Chapter 14: Unsupervised Learning.
  - Original Papers:
    - Pearson (1901). On Lines and Planes of Closest Fit.
    - van der Maaten \& Hinton (2008). Visualizing Data using t-SNE. JMLR.
    - McInnes et al. (2018). UMAP.
- Chart: none
- \bottomnote{Primary textbooks: ISLR Ch.~12, ESL Ch.~14; t-SNE paper is one of the most cited in visualization}
```

```
SLIDE 40: References (Documentation and Resources)
- Layout: \footnotesize bullet list
- Content:
  - Documentation:
    - scikit-learn: sklearn.decomposition.PCA
    - scikit-learn: sklearn.manifold.TSNE
    - UMAP documentation: umap-learn.readthedocs.io
  - Further Reading:
    - Litterman \& Scheinkman (1991). Common factors affecting bond returns. Journal of Fixed Income.
    - Wattenberg et al. (2016). How to Use t-SNE Effectively. Distill.
- Chart: none
- \bottomnote{Wattenberg et al.\ (2016) Distill article: essential reading for t-SNE interpretation}
```

### APPENDIX (Slides 41-48)

**\appendix**
**\section*{Advanced Topics}**

```
APPENDIX SLIDE 1: Section Divider
- Layout: Centered beamercolorbox
- Content:
  - "Appendix: Advanced Topics and Proofs"
  - Subtitle: "These slides are supplementary material for self-study"
- Chart: none
- \bottomnote: none (divider)
```

```
APPENDIX SLIDE 2: Full Eigenvalue Derivation
- Layout: Extended derivation
- Content:
  - Problem: max $w^\top \Sigma w$ s.t. $\|w\|=1$
  - Full Lagrangian setup: $L = w^\top \Sigma w - \lambda(w^\top w - 1)$
  - Gradient: $\frac{\partial L}{\partial w} = 2\Sigma w - 2\lambda w = 0$
  - Second component: max $w_2^\top \Sigma w_2$ s.t. $\|w_2\|=1$ AND $w_2^\top w_1 = 0$
  - Lagrangian with two constraints: $L_2 = w_2^\top \Sigma w_2 - \lambda_2(w_2^\top w_2 - 1) - \mu(w_2^\top w_1)$
  - Result: $w_2$ is eigenvector for second-largest eigenvalue
- Chart: none
- \bottomnote{Each successive PC maximizes variance orthogonal to all previous -- proof by induction}
```

```
APPENDIX SLIDE 3: SVD-PCA Equivalence: Full Proof
- Layout: Step-by-step proof
- Content:
  - Given: $X_c = U S V^\top$ (SVD of mean-centered data, $n \times p$)
  - Step 1: $X_c^\top X_c = (U S V^\top)^\top (U S V^\top) = V S^\top U^\top U S V^\top = V S^2 V^\top$
  - Step 2: Covariance $C = \frac{1}{n-1} X_c^\top X_c = \frac{1}{n-1} V S^2 V^\top$
  - Step 3: $C V = V \frac{S^2}{n-1}$, so columns of $V$ are eigenvectors of $C$
  - Step 4: Eigenvalues $\lambda_k = s_k^2 / (n-1)$
  - Computational note: SVD avoids forming $X^\top X$ (condition number $\kappa(X^\top X) = \kappa(X)^2$)
- Chart: none
- \bottomnote{SVD is THE standard computational approach -- eigendecomposition of $\Sigma$ is for theory only}
```

```
APPENDIX SLIDE 4: t-SNE Gradient Derivation
- Layout: Derivation
- Content:
  - KL objective: $C = \sum_{i \neq j} p_{ij} \log \frac{p_{ij}}{q_{ij}}$
  - $q_{ij} = \frac{(1 + \|y_i - y_j\|^2)^{-1}}{Z}$ where $Z = \sum_{k \neq l} (1 + \|y_k - y_l\|^2)^{-1}$
  - Taking $\frac{\partial C}{\partial y_i}$:
  - $\frac{\partial C}{\partial y_i} = 4 \sum_j (p_{ij} - q_{ij})(y_i - y_j)(1 + \|y_i - y_j\|^2)^{-1}$
  - Interpretation: attractive force from $p_{ij} > q_{ij}$, repulsive from $p_{ij} < q_{ij}$
- Chart: none
- \bottomnote{Barnes-Hut approximation computes repulsive forces via quadtree -- reduces $O(n^2)$ to $O(n \log n)$}
```

```
APPENDIX SLIDE 5: Perplexity, Entropy, and Sigma
- Layout: Mathematical relationship
- Content:
  - Perplexity definition: $\text{Perp}(P_i) = 2^{H(P_i)}$ where $H(P_i) = -\sum_j p_{j|i} \log_2 p_{j|i}$
  - Perplexity is the effective number of neighbors each point "considers"
  - $\sigma_i$ is set via binary search so that $\text{Perp}(P_i)$ matches the user-specified value
  - Each point gets its OWN $\sigma_i$ -- adaptive to local density
  - Dense regions: small $\sigma_i$ (tight Gaussian); sparse regions: large $\sigma_i$ (broad Gaussian)
- Chart: none
- \bottomnote{Adaptive $\sigma_i$ is what makes t-SNE work across varying densities -- a key design choice}
```

```
APPENDIX SLIDE 6: Kernel PCA
- Layout: Concept explanation
- Content:
  - Standard PCA: eigendecomposition of $X^\top X$ (or SVD of $X$)
  - Kernel PCA: eigendecomposition of kernel matrix $K_{ij} = k(x_i, x_j)$
  - Common kernels: polynomial $k(x,y) = (x^\top y + c)^d$, RBF $k(x,y) = \exp(-\gamma\|x-y\|^2)$
  - Advantage: non-linear feature extraction without explicitly computing features
  - Disadvantage: $O(n^2)$ space and time (kernel matrix is $n \times n$)
- Chart: none
- \bottomnote{Kernel PCA: when linear PCA misses non-linear structure but you still need reversible features}
```

```
APPENDIX SLIDE 7: Trustworthiness and Continuity Metrics
- Layout: Formulas + interpretation
- Content:
  - Trustworthiness: do points that are neighbors in low-D also neighbors in high-D?
  - Continuity: do points that are neighbors in high-D also neighbors in low-D?
  - $T(k) = 1 - \frac{2}{nk(2n-3k-1)} \sum_i \sum_{j \in U_k(i)} (r(i,j) - k)$
  - High T: embedded neighbors are real; High C: no real neighbors lost
  - Use to compare t-SNE runs and parameter choices quantitatively
- Chart: none
- \bottomnote{Trustworthiness and continuity give objective quality metrics for dimensionality reduction}
```

```
APPENDIX SLIDE 8: References and Further Reading
- Layout: Two-column \footnotesize
- Content:
  - Left: Advanced Theory
    - Jolliffe \& Cadima (2016). Principal component analysis: a review. Phil.\ Trans.\ R.\ Soc.\ A.
    - Linderman \& Steinerberger (2019). Clustering with t-SNE, provably. SIAM.
    - Kobak \& Berens (2019). The art of using t-SNE for single-cell transcriptomics. Nature Comms.
  - Right: Finance Applications
    - Litterman \& Scheinkman (1991). Common factors affecting bond returns.
    - Alexander (2001). Market Models: A Guide to Financial Data Analysis. Ch.\ 7.
    - Lopez de Prado (2018). Advances in Financial Machine Learning. Ch.\ 8.
- Chart: none
- \bottomnote{Primary finance reference: Litterman \& Scheinkman (1991) for yield curve PCA}
```

### Acceptance Criteria -- Task 2
- [ ] ~40 main slides (38-42 acceptable range)
- [ ] ~8 appendix slides (6-9 acceptable range)
- [ ] Preamble lines 1-92 unchanged
- [ ] \institute{MSc Data Science} present
- [ ] XKCD #2048 at slide 3
- [ ] XKCD #2400 callback at slide 38 (or last main slide before references)
- [ ] LOs at slide 4 (after opening comic)
- [ ] 7 charts used: 02, 03, 04a, 04b, 04c, 06a, 06b
- [ ] No charts from overview set (01, 05a, 05b, 06c, 07)
- [ ] \appendix + \section*{Advanced Topics} present
- [ ] Appendix divider slide present
- [ ] All hostile review CRITICAL fixes preserved:
  - [ ] PCA optimality proof (slide 7)
  - [ ] SVD-PCA equivalence (slide 8)
  - [ ] Kaiser criterion qualified (slide 9)
  - [ ] Centering explicit in all formulas (slides 5, 6, 11)
  - [ ] Yield curve PCA (slides 13-14)
  - [ ] Crowding problem (slide 20)
  - [ ] KL asymmetry (slide 21)
  - [ ] t-SNE symmetrization (slide 19)
  - [ ] Perplexity = 2^H (slide 22, 25)
  - [ ] Statistical inference (slide 16)
  - [ ] Numerical portfolio example (slide 15)
  - [ ] "PCA does NOT require Gaussian" (slide 5)
- [ ] Every content slide has \bottomnote{}
- [ ] Every slide has numbered comment header
- [ ] Max 3-4 bullets per itemize
- [ ] No pseudocode (PCA is closed-form per instructor guide)
- [ ] Appendix includes: full eigenvalue derivation, SVD-PCA proof, t-SNE gradient derivation

---

## Task 3: Compile Both PDFs

**Depends on**: Tasks 1 and 2

### Steps
1. Navigate to `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L05_PCA_tSNE\`
2. Compile overview:
   ```
   pdflatex -interaction=nonstopmode L05_overview.tex
   pdflatex -interaction=nonstopmode L05_overview.tex
   ```
3. Compile deepdive:
   ```
   pdflatex -interaction=nonstopmode L05_deepdive.tex
   pdflatex -interaction=nonstopmode L05_deepdive.tex
   ```
4. Move aux files:
   ```
   mkdir temp 2>nul
   move *.aux *.log *.nav *.out *.snm *.toc temp/
   ```

### Verification
- Check compilation output for "0 errors"
- Grep output for "Overfull": must be 0 occurrences
- Verify PDF page count: overview ~24 pages, deepdive ~48 pages

### Acceptance Criteria -- Task 3
- [ ] L05_overview.pdf exists and is valid
- [ ] L05_deepdive.pdf exists and is valid
- [ ] 0 LaTeX errors in both compilations
- [ ] 0 Overfull \hbox warnings in both compilations
- [ ] Overview PDF: ~24 pages
- [ ] Deepdive PDF: ~48 pages

---

## Task 4: Architect Verification

**Depends on**: Task 3

### 18-Point Checklist

| # | Check | Target |
|---|-------|--------|
| 1 | Preamble integrity | Lines 1-92 byte-identical in both files |
| 2 | \institute line | Present in both files |
| 3 | Zone comments | 3 zones marked in overview; zone-style sections in deepdive |
| 4 | Slide count | Overview: 24; Deepdive: ~40 main + ~8 appendix |
| 5 | XKCD opening | Slide 3 in both files, XKCD #2048, CC BY-NC 2.5 attribution |
| 6 | XKCD closing | Text callback to #2400 in both files (not image reuse) |
| 7 | LO placement | After intro (slide 7 overview, slide 4 deepdive), NOT slide 2 |
| 8 | Chart allocation | Overview: 01,05a,05b,06c,07; Deepdive: 02,03,04a,04b,04c,06a,06b; zero overlap |
| 9 | \bottomnote coverage | Every content slide has one |
| 10 | Slide numbering comments | Sequential % SLIDE N: headers throughout |
| 11 | Bullet discipline | Max 3-4 per itemize/enumerate |
| 12 | \appendix section | Present in deepdive with \section*{Advanced Topics} |
| 13 | Content preservation | All hostile review CRITICAL/MAJOR fixes preserved |
| 14 | Compilation | 0 errors, 0 Overfull warnings |
| 15 | Bloom's LOs | Level 4-5 verbs in both files |
| 16 | Yield curve PCA | Present in overview (slide 12) and deepdive (slides 13-14) |
| 17 | PCA Gaussian claim | States "does NOT require Gaussian" (not the incorrect "assumes Gaussian") |
| 18 | Kaiser criterion | Qualified as "correlation matrix / standardized data ONLY" |

### Acceptance Criteria -- Task 4
- [ ] All 18 checks pass
- [ ] Written verification report

---

## Chart Allocation Table (Final)

| Chart | File | Slide # | Full Path |
|-------|------|---------|-----------|
| 01_scree_plot | Overview | 11 | 01_scree_plot/chart.pdf |
| 02_principal_components | Deepdive | 10 | 02_principal_components/chart.pdf |
| 03_reconstruction | Deepdive | 12 | 03_reconstruction/chart.pdf |
| 04a_tsne_perplexity_5 | Deepdive | 22 | 04a_tsne_perplexity_5/chart.pdf |
| 04b_tsne_perplexity_30 | Deepdive | 23 | 04b_tsne_perplexity_30/chart.pdf |
| 04c_tsne_perplexity_100 | Deepdive | 24 | 04c_tsne_perplexity_100/chart.pdf |
| 05a_pca_swiss_roll | Overview | 13 | 05a_pca_swiss_roll/chart.pdf |
| 05b_tsne_swiss_roll | Overview | 14 | 05b_tsne_swiss_roll/chart.pdf |
| 06a_original_clusters | Deepdive | 26 | 06a_original_clusters/chart.pdf |
| 06b_pca_cluster_projection | Deepdive | 27 | 06b_pca_cluster_projection/chart.pdf |
| 06c_tsne_cluster_projection | Overview | 15 | 06c_tsne_cluster_projection/chart.pdf |
| 07_decision_flowchart | Overview | 20 | 07_decision_flowchart/chart.pdf |

**Totals:** Overview = 5 charts, Deepdive = 7 charts, Overlap = 0

---

## MUST HAVE Checklist

### Derivations and Formulas
- [ ] Eigenvalue derivation from covariance matrix (deepdive slide 7)
- [ ] SVD-PCA connection (deepdive slide 8, appendix slide 3)
- [ ] t-SNE gradient formula (deepdive slide 21, appendix slide 4)
- [ ] Perplexity = 2^H entropy relationship (deepdive slides 22, 25, appendix slide 5)
- [ ] KL divergence asymmetry explained (deepdive slide 21)
- [ ] Crowding problem motivation for t-distribution (deepdive slide 20)
- [ ] t-SNE symmetrization step (deepdive slide 19)
- [ ] Kaiser criterion qualified for correlation matrix (deepdive slide 9, overview slide 11 bottomnote)

### Finance Applications
- [ ] Yield curve PCA: level/slope/curvature worked example (overview slide 12, deepdive slides 13-14)
- [ ] Portfolio risk decomposition (overview slide 18, deepdive slide 15)
- [ ] Market regime detection with t-SNE (overview slide 19, deepdive slide 31)
- [ ] Numerical loadings table for yield curve (deepdive slide 14)

### Appendix Content
- [ ] Full eigenvalue derivation (appendix slide 2)
- [ ] SVD-PCA equivalence full proof (appendix slide 3)
- [ ] t-SNE gradient derivation (appendix slide 4)
- [ ] Perplexity/entropy/sigma relationship (appendix slide 5)
- [ ] Kernel PCA explanation (appendix slide 6)
- [ ] Trustworthiness/continuity metrics (appendix slide 7)

### Correctness
- [ ] PCA stated as NOT requiring Gaussian (deepdive slide 5)
- [ ] Centering explicit in all PCA formulas (deepdive slides 5, 6, 11)
- [ ] "Reversible" qualified as "lossy when k < p" (deepdive slide 5)

---

## Deliverables Summary

| Deliverable | Path | Description |
|-------------|------|-------------|
| L05_overview.tex | slides/L05_PCA_tSNE/L05_overview.tex | 24-slide overview, 3 zones, 5 charts |
| L05_deepdive.tex | slides/L05_PCA_tSNE/L05_deepdive.tex | ~40 main + ~8 appendix slides, 7 charts |
| L05_overview.pdf | slides/L05_PCA_tSNE/L05_overview.pdf | Compiled overview |
| L05_deepdive.pdf | slides/L05_PCA_tSNE/L05_deepdive.pdf | Compiled deepdive |

---

## Acceptance Criteria (Global)

1. Both files follow three-zone pattern
2. Chart allocation is clean: 5 overview, 7 deepdive, 0 overlap
3. XKCD #2048 opening and #2400 text callback closing in both files
4. All hostile review CRITICAL fixes preserved (C1-C7)
5. All hostile review MAJOR fixes preserved (M1-M6)
6. Yield curve PCA present in both files
7. No "PCA assumes Gaussian" anywhere
8. Kaiser criterion always qualified
9. Centering explicit in all PCA formulas
10. Compilation clean: 0 errors, 0 Overfull
11. Architect verification passes all 18 checks

---

## Verification Steps

1. **Preamble diff**: Compare lines 1-92 of both new files against current versions (must be byte-identical)
2. **Chart grep**: Search both files for `\includegraphics` -- verify allocation matches table
3. **XKCD grep**: Search for "2048" (opening) and "2400" (closing) in both files
4. **Bottomnote count**: Count `\bottomnote` occurrences vs content slide count
5. **Bullet count**: No `\item` block should have > 4 items
6. **Zone comments**: Grep for "% ZONE" in overview
7. **\institute**: Grep for `\institute{MSc Data Science}` in both files
8. **\appendix**: Grep for `\appendix` in deepdive
9. **Gaussian check**: Grep for "assumes Gaussian" -- must return 0 results
10. **Kaiser check**: Grep for "Kaiser" -- must include "correlation" or "standardized" qualifier
11. **Compile**: Run pdflatex twice on each file, check for 0 errors and 0 Overfull
12. **Page count**: Overview ~24, deepdive ~48

---

## Risks

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| Overfull \hbox from dense equation slides | MEDIUM | Keep max 2 display equations per slide; use \small for tables |
| XKCD images not found at path | LOW | Verify images/2048_curve_fitting.png exists before compile |
| Appendix pushes total past 50 slides | LOW | Appendix is 8 slides; 40+8=48 is within budget |
| Yield curve loadings table too wide | MEDIUM | Use \small or \footnotesize; 5 columns fits in 16:9 |
| t-SNE gradient equation too long for slide | MEDIUM | Split across two lines with align environment |
| Hostile review fixes lost during rewrite | HIGH | Explicitly list each fix in acceptance criteria; verify with grep |

---

## Commit Strategy

### Single Commit After All Tasks Pass
```
Restructure L05 PCA & t-SNE slides with three-zone architecture

- Rewrite L05_overview.tex: 24 slides, 3 zones, XKCD #2048 open/#2400 close
- Rewrite L05_deepdive.tex: ~40 main + ~8 appendix slides, XKCD open/close
- Fix chart dual-assignment: 5 to overview, 7 to deepdive, zero overlap
- Move LOs after intro section (was slide 3)
- Add \institute{MSc Data Science} to both files
- Add \appendix + \section*{Advanced Topics} to deepdive
- Preserve all hostile review fixes (yield curve PCA, optimality proof, SVD,
  crowding problem, Kaiser qualification, Gaussian correction, inference)
```

### Files Changed
- `slides/L05_PCA_tSNE/L05_overview.tex`
- `slides/L05_PCA_tSNE/L05_deepdive.tex`
- `slides/L05_PCA_tSNE/L05_overview.pdf`
- `slides/L05_PCA_tSNE/L05_deepdive.pdf`

---

## Success Criteria

1. Both files follow three-zone pattern exactly
2. Chart allocation is clean (no dual-assignment)
3. XKCD comics at opening and closing in both files
4. All hostile review CRITICAL and MAJOR fixes preserved
5. Yield curve PCA worked example with numerical loadings
6. All derivations present (eigenvalue, SVD, t-SNE gradient, perplexity)
7. Finance applications concrete and quantitative
8. Compilation clean (0 errors, 0 Overfull)
9. Architect verification passes all 18 checks

---

**Plan Created:** 2026-02-13
**Plan Status:** READY FOR EXECUTION
**Estimated Execution Time:** 90-120 minutes (Tasks 1+2 parallel, Task 3+4 sequential)
**Parallel Execution:** Tasks 1 and 2 can run concurrently
