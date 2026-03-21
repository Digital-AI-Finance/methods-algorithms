# Plan: L05 PCA & t-SNE Ultra-Deep Top-20 Charts

## Context

### Original Request
Create `L05_pca_tsne_top20.tex` with 20 brand-new charts covering advanced, nuanced, and rarely-taught aspects of PCA and t-SNE. All charts use synthetic data. No duplication of the 22 existing charts.

### What Already Exists (DO NOT DUPLICATE)
22 charts already exist in `slides/L05_PCA_tSNE/`:
- 01_scree_plot: Eigenvalue bar chart (scree)
- 02_principal_components: PCA 2D projection scatter
- 03_reconstruction: Reconstruction error vs k
- 04a/b/c_tsne_perplexity_5/30/100: t-SNE at different perplexities
- 05a/b_pca/tsne_swiss_roll: Swiss roll comparison
- 06a/b/c_original/pca/tsne_cluster_projection: Cluster projection comparison
- 07_decision_flowchart: Method selection flowchart
- 08_high_dim_before_after: High-dim visualization
- 09_yield_curve_factors: Finance PCA application
- 10_pca_mini_example: PCA by hand (5 points)
- top10_09_cumulative_variance: Cumulative explained variance curve
- top10_10_pca_biplot: Biplot with loading arrows
- top10_11_scaling_effect: Scaled vs unscaled PCA
- top10_12_kernel_pca: Kernel PCA on non-linear data
- top10_13_tsne_iterations: t-SNE convergence snapshots
- top10_14_explained_var_heatmap: Loading heatmap
- top10_15_pca_denoising: PCA noise removal
- top10_16_tsne_distance_preservation: Original vs embedded distance scatter (Shepard-style)
- top10_17_pca_vs_tsne_runtime: Runtime scaling comparison
- top10_18_intrinsic_dimensionality: Elbow in explained variance
- top10_19_pca_whitening: PCA whitening effect
- top10_20_tsne_perplexity_grid: Perplexity grid comparison

### Reference Files
- Preamble: Copy exactly from `L05_pca_tsne_top10.tex` (lines 1-98)
- Chart pattern: See `top10_09_cumulative_variance/chart.py` for canonical structure
- Naming: `top20_XX_descriptive_name/chart.py` (numbering 21-40)
- XKCD images folder: `slides/L05_PCA_tSNE/images/`

### Critic Iteration 1 Feedback (ALL RESOLVED)
1. No subplots -- strict single-panel enforcement
2. Chart 21 eigenvalue spectrum cut (duplicates scree + intrinsic dim)
3. Chart 34 Shepard diagram cut (duplicates top10_16)
4. Chart 31 redesigned: sklearn-only (MDS, Isomap instead of UMAP)
5. Chart 32 KL trace replaced entirely with a different concept
6. Chart 26 progressive reconstruction cut (duplicates 03_reconstruction)
7. Section 4 redesigned with genuine finance synthetic data
8. Chart 37 dual-axis removed -- single y-axis only
9. Chart 35 continuity uses swapped-trustworthiness approximation (documented)
10. XKCD comics specified for opening and closing
11. Chart 30 crowding shows both problem AND t-distribution solution
12. Chart 40 vs 31 overlap resolved -- completely different concepts

---

## Work Objectives

### Core Objective
Deliver 20 new chart folders + 1 new .tex file covering advanced PCA/t-SNE topics that go beyond the introductory and intermediate material already covered.

### Deliverables
1. 20 chart folders: `top20_21_*` through `top20_40_*`, each containing `chart.py` that generates `chart.pdf`
2. 1 slide deck: `slides/L05_PCA_tSNE/L05_pca_tsne_top20.tex` (~30 slides)

### Definition of Done
- All 20 `chart.py` files run without error and produce `chart.pdf`
- `.tex` file compiles with `pdflatex` with zero Overfull warnings
- No chart duplicates any existing visualization
- Every chart uses synthetic data only (no external datasets)
- Every chart is a SINGLE figure with NO subplots

---

## Guardrails

### MUST Have
- `np.random.seed(42)` in every chart.py
- **EXACTLY ONE figure per chart -- NO subplots, NO multi-panel, NO fig.subplots(), NO axes arrays**
- `figsize=(10, 6)`, `dpi=150`, standard font sizes (14/14/16/13/13/13)
- ML color palette constants defined at top of each file
- `CHART_METADATA` dict with title, description, url
- URL watermark via `plt.figtext` bottom-right
- `chart.pdf` output via `plt.savefig(..., dpi=300, bbox_inches='tight')`
- Question-based slide titles
- `\bottomnote{}` on every slide
- Only numpy, scipy, sklearn, matplotlib, seaborn allowed
- Finance Section 4 must use finance-themed synthetic data (not relabeled blobs)

### MUST NOT Have
- Any chart that duplicates existing 22 charts
- External datasets (everything synthetic via numpy/sklearn generators)
- **Any subplots, multi-panel layouts, twinx(), or secondary axes**
- More than 30 total slides in the .tex file
- umap-learn or any non-sklearn dependency

---

## Chart Specifications (20 Charts in 4 Sections)

---

### SECTION 1: PCA Deep Mechanics (Charts 21-26)

---

#### Chart 21: `top20_21_hotelling_t2_outlier`
- **Slide Title:** "Can PCA Detect Outliers? The Hotelling T-squared Statistic"
- **Visualization:** Single scatter plot of PC1 vs PC2 scores with points colored by their Hotelling T-squared value (continuous colormap `YlOrRd`). Draw 95% and 99% confidence ellipses as dashed curves. Points beyond 99% ellipse highlighted with red edge rings and annotated.
- **Synthetic Data:** 200 points from `np.random.multivariate_normal([0,0], [[3,1],[1,2]], 200)` plus 10 outliers at `mean=[6,6], cov=[[0.5,0],[0,0.5]]`. PCA on the combined set.
- **Teaching Point:** PCA scores follow a chi-squared distribution under normality. Hotelling T-squared measures Mahalanobis distance in PC space, enabling statistical outlier detection.
- **Python Approach:** Compute T-squared as sum of (score/sqrt(eigenvalue))^2 per point. Use `matplotlib.patches.Ellipse` for confidence ellipses at chi2.ppf(0.95,2) and chi2.ppf(0.99,2). Colorbar for T-squared values.
- **Bottomnote:** "Hotelling T-squared measures Mahalanobis distance in PC space---points beyond the 99\\% ellipse are statistically anomalous"
- **No duplication:** No existing chart shows outlier detection in PC space or confidence ellipses.

---

#### Chart 22: `top20_22_spe_q_residual`
- **Slide Title:** "What PCA Misses: The Q-Residual (SPE) Statistic"
- **Visualization:** Single bar chart showing SPE (Squared Prediction Error) values for each of ~50 samples (sorted descending for clarity). Horizontal dashed line at 95% confidence limit. Bars colored green (normal) vs red (exceeds threshold). Top-5 anomalous samples annotated with sample index.
- **Synthetic Data:** 200 normal points from 10D Gaussian with 3 true components. Inject 8 "sensor drift" anomalies by adding large values to features 7-10 only (features NOT captured by top 3 PCs). Show a random subset of 50 samples for visual clarity.
- **Teaching Point:** T-squared catches outliers IN the PC subspace; SPE/Q catches anomalies in the RESIDUAL subspace -- things that deviate in ways PCA doesn't model. Together they give complete monitoring.
- **Python Approach:** `PCA(n_components=3).fit(X_normal)`, compute residuals as `X - X_reconstructed`, SPE = sum of squared residuals per row. Threshold via chi-squared approximation.
- **Bottomnote:** "SPE detects anomalies invisible in PC space---deviations in directions PCA discards as noise"
- **No duplication:** No existing chart shows residual-space anomaly detection.

---

#### Chart 23: `top20_23_sparse_pca_loadings`
- **Slide Title:** "Sparse PCA: Can We Get Interpretable Components?"
- **Visualization:** Single horizontal bar chart showing PC1 loadings from Sparse PCA across 15 features. Bars colored by sign (positive = MLBlue, negative = MLOrange). Zero-loading features visually obvious. Feature names on y-axis (Feature_01 through Feature_15). Annotate which features are informative vs noise.
- **Synthetic Data:** 15 features, 500 samples. 5 features are informative (from `make_classification(n_informative=5, n_features=15)`), 10 are noise. StandardScaler applied.
- **Teaching Point:** Standard PCA loadings are dense and hard to interpret. Sparse PCA enforces an L1 penalty, producing components that load on few features -- much more interpretable for domain experts. The sparse loadings correctly identify the 5 informative features.
- **Python Approach:** `SparsePCA(n_components=1, alpha=1.0)` from sklearn.decomposition. `barh()` for loadings. Add a text annotation: "Standard PCA: all 15 features contribute. Sparse PCA: only informative features selected."
- **Bottomnote:** "Sparse PCA trades variance explained for interpretability---each component loads on only a handful of features"
- **No duplication:** No existing chart shows Sparse PCA or sparsity in loadings.

---

#### Chart 24: `top20_24_robust_pca_outlier_influence`
- **Slide Title:** "How Sensitive Is PCA to Outliers?"
- **Visualization:** Single 2D scatter plot with two sets of PC1 direction arrows overlaid: one computed from clean data (MLGreen arrow), one from contaminated data (MLRed arrow). Show the angular deviation as a labeled arc between the arrows. Outlier cluster visible in corner. Arrow length normalized for visibility. Legend with "Clean PC1" and "Contaminated PC1".
- **Synthetic Data:** 300 points from bivariate normal `cov=[[4,2],[2,1.5]]`. Add 15 outliers at `[8, -3]` with small spread `cov=0.3*I`. Run PCA on clean vs contaminated.
- **Teaching Point:** A small fraction of outliers can dramatically rotate the principal component directions. Robust PCA methods (or preprocessing) are needed when contamination is suspected.
- **Python Approach:** PCA on clean data, PCA on contaminated data. Draw PC1 direction as `ax.annotate` arrow from origin. Compute angle between the two PC1 vectors with `np.arccos(np.abs(dot_product))` and display as text.
- **Bottomnote:** "Just 5\\% contamination can rotate PC1 by 20+ degrees---always inspect for outliers before running PCA"
- **No duplication:** No existing chart shows outlier influence on PC directions.

---

#### Chart 25: `top20_25_pca_variance_vs_components`
- **Slide Title:** "How Does the Number of Components Affect Cluster Separability?"
- **Visualization:** Single line plot showing silhouette score (y-axis) vs number of PCA components k (x-axis, from 2 to 20). Horizontal dashed line showing silhouette score computed in the full original space. Shade the region where reduced-space silhouette exceeds the original (if applicable). Mark the optimal k with a star.
- **Synthetic Data:** 5 blobs in 30D, 600 samples, `cluster_std=2.0` so clusters partially overlap. True labels known.
- **Teaching Point:** Silhouette score measures cluster compactness and separation. For well-chosen k, PCA-reduced data can have HIGHER silhouette than the original because noise dimensions dilute cluster structure. The curve shows diminishing returns.
- **Python Approach:** `sklearn.metrics.silhouette_score(PCA(n_components=k).fit_transform(X), labels)` for k in range(2,21). Plot line vs horizontal reference line for full-space silhouette.
- **Bottomnote:** "Removing noise dimensions with PCA can improve clustering quality---reduced data sometimes has higher silhouette than the original"
- **No duplication:** No existing chart shows silhouette as a function of PCA components.

---

#### Chart 26: `top20_26_pca_condition_number`
- **Slide Title:** "Why Does Multicollinearity Break PCA?"
- **Visualization:** Single scatter plot showing condition number (log scale, y-axis) vs correlation strength (x-axis, from r=0.0 to r=0.99). Each dot represents one synthetic dataset with that correlation level. Horizontal dashed lines at condition_number=30 ("moderate collinearity") and condition_number=1000 ("severe collinearity"). Color points by severity: green < 30, orange 30-1000, red > 1000.
- **Synthetic Data:** For each correlation r in np.linspace(0, 0.99, 50): generate 500 samples of 5 features with pairwise correlation r (via Cholesky decomposition), compute PCA, record condition number (max eigenvalue / min eigenvalue).
- **Teaching Point:** As feature correlation increases, the covariance matrix becomes ill-conditioned, making PCA numerically unstable. Near-zero eigenvalues amplify noise. This is why scaling and regularization matter.
- **Python Approach:** For each r: construct correlation matrix with off-diags=r, Cholesky to generate data, PCA, compute `explained_variance_[0] / explained_variance_[-1]`.
- **Bottomnote:** "High correlation produces near-singular covariance matrices---PCA becomes numerically unstable with condition numbers above 1000"
- **No duplication:** No existing chart shows condition number or numerical stability issues.

---

### SECTION 2: t-SNE Deep Mechanics (Charts 27-32)

---

#### Chart 27: `top20_27_tsne_perplexity_vs_kl`
- **Slide Title:** "Which Perplexity Gives the Best Embedding?"
- **Visualization:** Single line plot showing final KL divergence (y-axis) vs perplexity value (x-axis, from 5 to 100 in steps of 5). Mark the optimal perplexity (lowest KL) with a star. Add a shaded "recommended range" band from perplexity 20-50.
- **Synthetic Data:** 5 Gaussian blobs in 20D, 500 samples, varying cluster sizes. Same dataset for all perplexity values.
- **Teaching Point:** KL divergence measures how well the embedding preserves the original neighborhood structure. There is typically a sweet spot -- too low means only nearest neighbors matter; too high blurs cluster boundaries. The recommended range of 5-50 is well-supported empirically.
- **Python Approach:** `TSNE(perplexity=p, random_state=42, n_iter=1000)` for p in range(5, 105, 5). Record `.kl_divergence_` attribute. Plot as line.
- **Bottomnote:** "KL divergence quantifies embedding quality---sweep perplexity values and pick the minimum for your dataset"
- **No duplication:** Existing perplexity charts (04a/b/c, top10_20) show spatial layout, not KL divergence as a function of perplexity.

---

#### Chart 28: `top20_28_tsne_learning_rate`
- **Slide Title:** "What Happens When You Change the t-SNE Learning Rate?"
- **Visualization:** Single scatter plot showing the t-SNE embedding at the DEFAULT learning rate (200) with good cluster separation. Annotate three text boxes around the plot: (1) "lr=10: compressed ball" with an inset arrow, (2) "lr=200: well-separated clusters (shown)", (3) "lr=2000: exploded/uniform scatter". The main plot demonstrates the good case; text annotations describe failure modes.
- **Synthetic Data:** 4 Gaussian blobs in 15D, 400 samples, well-separated (`cluster_std=1.0`). Color by cluster.
- **Teaching Point:** Learning rate controls step size in gradient descent. Too low = points stuck in local minimum. Too high = overshooting prevents fine structure. Default ~200 is usually good; sklearn auto-selects N/early_exaggeration.
- **Python Approach:** `TSNE(learning_rate=200, random_state=42, perplexity=30, n_iter=1000)`. Single scatter with cluster colors. Add `ax.text()` annotations for the failure modes.
- **Bottomnote:** "Learning rate too low: compressed blob. Too high: uniform scatter. Default (N/early\\_exaggeration or 200) is usually right"
- **No duplication:** No existing chart shows learning rate effects.

---

#### Chart 29: `top20_29_early_exaggeration`
- **Slide Title:** "Why Does t-SNE Use Early Exaggeration?"
- **Visualization:** Single scatter showing t-SNE result with early_exaggeration=1 (NO exaggeration). Points are colored by cluster but clusters overlap poorly. Annotate: "Without early exaggeration, clusters remain tangled. Default (12x) pushes clusters apart in first 250 iterations, creating room for fine structure." Draw dashed circles around tangled regions.
- **Synthetic Data:** 5 blobs in 20D, 500 samples, moderate separation. Color by cluster.
- **Teaching Point:** Early exaggeration multiplies p_ij values in the first 250 iterations, forcing clusters apart early. This creates "room" for fine-grained structure to emerge later. Without it, clusters get stuck overlapping.
- **Python Approach:** `TSNE(early_exaggeration=1, random_state=42, n_iter=1000)`. Single scatter. Add text annotations explaining why this looks worse than the default.
- **Bottomnote:** "Early exaggeration (default 12x) forces clusters apart in the first 250 iterations---without it, clusters remain entangled"
- **No duplication:** No existing chart addresses early exaggeration.

---

#### Chart 30: `top20_30_crowding_problem`
- **Slide Title:** "The Crowding Problem: Why t-SNE Uses a t-Distribution"
- **Visualization:** Single plot showing two overlaid curves (NOT histograms): the Gaussian kernel q_ij (dashed, MLBlue, labeled "Gaussian q_ij") and the Student-t kernel q_ij (solid, MLOrange, labeled "Student-t q_ij") as a function of pairwise distance in the embedding space (x-axis: 0 to 5). The t-distribution has heavier tails, giving moderate-distance points more probability mass. Annotate the "crowding zone" (distance 1-3) where the Gaussian drops to near-zero but the t-distribution still has mass.
- **Synthetic Data:** Not needed -- this is a mathematical comparison. Generate x = np.linspace(0, 5, 200) and compute both kernel functions directly.
- **Teaching Point:** When mapping from high-D to 2D, moderate distances collapse together (crowding). The t-distribution's heavy tails give moderately distant points more room than a Gaussian would, solving the crowding problem. This is the key innovation that makes t-SNE (with the "t") superior to SNE.
- **Python Approach:** Gaussian: `q_gauss = np.exp(-x**2) / sum`. Student-t: `q_t = (1 + x**2)**(-1) / sum`. Normalize both. Plot as two curves on same axes. Fill the region between them in the tail.
- **Bottomnote:** "The t-distribution's heavy tails give moderately distant points more room---this is the key insight that makes t-SNE superior to SNE"
- **No duplication:** No existing chart shows the kernel comparison or the mathematical crowding mechanism.

---

#### Chart 31: `top20_31_tsne_vs_mds_vs_isomap`
- **Slide Title:** "t-SNE vs MDS vs Isomap: Which Preserves What?"
- **Visualization:** Single grouped bar chart with 3 groups (t-SNE, MDS, Isomap) and 2 bars per group: trustworthiness score (MLBlue) and runtime in seconds (MLOrange, log scale on secondary... NO -- single axis). Use trustworthiness only (single metric) on y-axis (0 to 1). Label each bar with exact value. Add runtime as text annotation above each bar (e.g., "0.3s", "1.2s", "5.1s").
- **Synthetic Data:** Two interlocking half-moons (`make_moons(n_samples=600, noise=0.05)`) embedded in 10D by adding 8 noise dimensions. Same dataset for all methods.
- **Teaching Point:** t-SNE excels at local structure (highest trustworthiness) but is slowest. MDS preserves global distances but struggles with non-linear manifolds. Isomap follows geodesic distances along the manifold. The right choice depends on data structure and what you need to preserve.
- **Python Approach:** `TSNE(random_state=42)`, `MDS(n_components=2, random_state=42)`, `Isomap(n_components=2)`. Compute `trustworthiness(X, X_emb, n_neighbors=10)` for each. Time each with `time.time()`. Bar chart with `ax.bar()`.
- **Bottomnote:** "t-SNE preserves local structure best; MDS preserves global distances; Isomap follows geodesic paths along the manifold"
- **No duplication:** No existing chart compares these three sklearn methods quantitatively.

---

#### Chart 32: `top20_32_tsne_n_iter_effect`
- **Slide Title:** "How Many Iterations Does t-SNE Actually Need?"
- **Visualization:** Single line plot showing trustworthiness score (y-axis, 0.7 to 1.0) vs n_iter (x-axis: 100, 200, 300, 500, 750, 1000, 1500, 2000). Mark the "diminishing returns" point where trustworthiness plateaus. Add a shaded "recommended" band at n_iter 500-1000.
- **Synthetic Data:** 4 blobs in 15D, 400 samples.
- **Teaching Point:** t-SNE quality improves with iterations but plateaus. Running 250 iterations (the sklearn default) is often insufficient for complex data. 1000 iterations is a good default. Beyond that, returns diminish rapidly.
- **Python Approach:** For each n_iter value: `TSNE(n_iter=n, random_state=42)`, compute `trustworthiness(X, X_emb, n_neighbors=10)`. Plot as line with markers.
- **Bottomnote:** "t-SNE quality plateaus around 500--1000 iterations---the default 1000 is usually sufficient, but always verify"
- **No duplication:** Existing top10_13_tsne_iterations shows spatial snapshots; this shows quality as a quantitative metric vs iteration count.

---

### SECTION 3: Practical Diagnostics (Charts 33-36)

---

#### Chart 33: `top20_33_pca_then_tsne_pipeline`
- **Slide Title:** "The PCA-then-t-SNE Pipeline: Why Pre-Reduce to 50D?"
- **Visualization:** Single scatter plot showing the t-SNE embedding AFTER PCA pre-reduction to 50D. Clean, well-separated clusters. Add a text box with: "Direct t-SNE on 500D: noisy, 45s. PCA(50) + t-SNE: clean clusters, 3s." Show runtime speedup as "15x faster" annotation.
- **Synthetic Data:** 5 blobs at 500D, 800 samples. Only 10 informative features; 490 are noise columns (`np.hstack([make_blobs(..., n_features=10)[0], np.random.randn(800, 490)])`).
- **Teaching Point:** t-SNE on very high-D data is slow and suffers from the curse of dimensionality (distances become less meaningful). Pre-reducing with PCA to ~50D removes noise dimensions and speeds up t-SNE dramatically.
- **Python Approach:** PCA(n_components=50) then TSNE(random_state=42). Time PCA+t-SNE pipeline. Also time raw t-SNE (but only show the clean result). Add annotation with both runtimes.
- **Bottomnote:** "Pre-reducing to 50D with PCA removes noise dimensions and can speed up t-SNE by 10x or more"
- **No duplication:** No existing chart shows the PCA pre-reduction pipeline.

---

#### Chart 34: `top20_34_trustworthiness_vs_k`
- **Slide Title:** "How Does Neighborhood Size Affect Embedding Quality?"
- **Visualization:** Single line plot showing trustworthiness (y-axis, 0.7 to 1.0) vs k (number of neighbors, x-axis: 5, 10, 15, 20, 30, 50, 75, 100). Three lines on same axes: t-SNE (MLPurple), PCA (MLBlue), Isomap (MLGreen). Legend in upper-right.
- **Synthetic Data:** 5 blobs in 20D, 500 samples. Same dataset for all methods.
- **Teaching Point:** Trustworthiness measures "are nearby points in the embedding truly nearby in the original?" The k parameter controls the neighborhood size for evaluation. t-SNE typically dominates at small k (local) but may lose ground at large k (global). PCA is more stable across k values.
- **Python Approach:** For each k and each method: `trustworthiness(X, X_emb, n_neighbors=k)`. Plot three lines. Use sklearn's trustworthiness function.
- **Bottomnote:** "Trustworthiness at small k measures local fidelity; at large k it measures global fidelity---t-SNE excels locally, PCA globally"
- **No duplication:** top10_16 shows a distance scatter; this shows trustworthiness as a function of k, which is a completely different diagnostic.

---

#### Chart 35: `top20_35_explained_var_vs_accuracy`
- **Slide Title:** "More Variance Explained = Better Predictions?"
- **Visualization:** Single plot with ONE y-axis showing logistic regression accuracy (5-fold CV, y-axis 0.5-1.0) vs number of PCA components k (x-axis, 2-25). Add a secondary annotation track: for each k, show cumulative variance ratio as text labels at select points (k=5, 10, 15, 20, 25) positioned as small labels above the curve. Mark the accuracy plateau with a dashed horizontal line. Mark the "95% variance" k with a vertical dashed line.
- **Synthetic Data:** Binary classification, 30 features, 8 informative (`make_classification(n_samples=800, n_features=30, n_informative=8, random_state=42)`).
- **Teaching Point:** Explained variance is an unsupervised criterion. Downstream task performance often saturates at fewer components than the 95% variance rule suggests. Always validate with the actual task metric, not just cumulative variance.
- **Python Approach:** For k in range(2,26): `PCA(n_components=k)`, then `cross_val_score(LogisticRegression(), X_pca, y, cv=5).mean()`. Single line plot. Add variance ratio text annotations at select k values. NO twinx() or dual axis.
- **Bottomnote:** "The 95\\% variance rule is a useful heuristic but not gospel---downstream accuracy often saturates much earlier"
- **No duplication:** No existing chart links PCA components to downstream classification performance.

---

#### Chart 36: `top20_36_pca_correlation_effect`
- **Slide Title:** "Why Does Correlation Determine PCA's Usefulness?"
- **Visualization:** Single plot: two overlaid eigenvalue decay curves on same axes (semilogy). Curve 1 (MLPurple, solid): eigenvalues from highly correlated features (off-diag r=0.7) -- sharp drop. Curve 2 (MLOrange, dashed): eigenvalues from uncorrelated features -- flat line. X-axis: component index (1-10). Annotate curve 1 as "Correlated (compressible)" and curve 2 as "Uncorrelated (incompressible)".
- **Synthetic Data:** Correlated: 10 features with correlation matrix off-diag=0.7 + diag=1.0 (via Cholesky), 500 samples. Uncorrelated: 10 independent standard normals, 500 samples.
- **Teaching Point:** PCA is most useful when features are correlated -- it concentrates variance into few components. With uncorrelated features, all eigenvalues are similar and PCA offers no compression. This explains why PCA works well on financial returns (assets are correlated through common factors).
- **Python Approach:** Construct correlation matrix, Cholesky decompose, generate data. PCA on both. Plot `explained_variance_` as two lines on semilogy scale. Color: MLPurple solid, MLOrange dashed.
- **Bottomnote:** "PCA compresses correlated data efficiently---uncorrelated features yield flat eigenvalues where no component can be dropped"
- **No duplication:** Existing scree plot (01) shows one dataset; existing intrinsic_dim (top10_18) shows elbow detection. This uniquely contrasts correlated vs uncorrelated eigenvalue spectra to explain WHY PCA works.

---

### SECTION 4: Finance Applications (Charts 37-40)

**ALL charts in this section use finance-themed synthetic data -- not generic blobs with financial labels.**

---

#### Chart 37: `top20_37_yield_curve_factor_loadings`
- **Slide Title:** "What Do Yield Curve PCA Factors Actually Look Like?"
- **Visualization:** Single line plot showing PC1, PC2, PC3 loading vectors (y-axis: loading magnitude) across 10 maturities (x-axis: 3M, 6M, 1Y, 2Y, 3Y, 5Y, 7Y, 10Y, 20Y, 30Y). Three colored lines: PC1 (MLPurple, "Level"), PC2 (MLBlue, "Slope"), PC3 (MLOrange, "Curvature"). Classic yield curve factor shape patterns.
- **Synthetic Data:** Generate realistic yield curve data: base curve via Nelson-Siegel model `y(tau) = b0 + b1*(1-exp(-tau/lambda))/(tau/lambda) + b2*((1-exp(-tau/lambda))/(tau/lambda) - exp(-tau/lambda))`. Generate 500 daily observations by adding noise to b0 (level shifts ~ N(0,0.3)), b1 (slope ~ N(0,0.2)), b2 (curvature ~ N(0,0.1)), plus small iid noise.
- **Teaching Point:** In fixed income, PCA on yield curve changes consistently reveals three factors: Level (parallel shift, ~85% variance), Slope (steepening/flattening, ~10%), and Curvature (butterfly, ~3%). These are the fundamental risk factors for bond portfolios.
- **Python Approach:** Generate yields at 10 maturities using Nelson-Siegel with varying parameters. PCA(n_components=3). Plot `components_` as 3 lines across maturities. Label with financial interpretation.
- **Bottomnote:** "PCA on yield curves reveals Level, Slope, and Curvature---three factors that explain 98\\% of interest rate movements"
- **No duplication:** Existing 09_yield_curve_factors shows PC scores over time; this uniquely shows the loading shapes (level/slope/curvature pattern) across maturities.

---

#### Chart 38: `top20_38_portfolio_factor_decomposition`
- **Slide Title:** "Can PCA Reveal Hidden Factors in a Stock Portfolio?"
- **Visualization:** Single horizontal bar chart showing PC1 loadings (x-axis: loading magnitude) across 12 synthetic stocks (y-axis: labeled as sector tickers -- "BANK_A", "BANK_B", "TECH_A", "TECH_B", "OIL_A", "OIL_B", etc.). Bars colored by sector (3 sectors, 4 stocks each). PC1 loadings cluster by sector, revealing the market factor with sector tilts.
- **Synthetic Data:** Generate 12-stock daily returns using a 3-factor model: `r_i = beta_i1 * F_market + beta_i2 * F_sector + epsilon_i`. Stocks in same sector share F_sector exposure. 500 daily returns. Correlations within sector ~ 0.6-0.8, across sectors ~ 0.2-0.4.
- **Teaching Point:** PCA on portfolio returns reveals latent risk factors without needing predefined factor models. PC1 is typically the "market factor" (all stocks load positively). PC2/PC3 reveal sector/style rotations. This is the empirical basis for factor investing.
- **Python Approach:** Generate factor returns (3 factors), assign sector betas, construct returns. PCA(n_components=1). Plot `components_[0]` as barh. Color by known sector membership.
- **Bottomnote:** "PCA on returns reveals the market factor (PC1) and sector rotations---the empirical foundation of factor investing"
- **No duplication:** No existing chart shows PCA applied to stock return factor structure.

---

#### Chart 39: `top20_39_credit_risk_tsne`
- **Slide Title:** "Can t-SNE Reveal Structure in Credit Risk Features?"
- **Visualization:** Single t-SNE scatter plot of credit risk applicants. Points colored by credit class: green="Good", orange="Borderline", red="Default". Use different marker sizes to encode loan amount (small=low, large=high). Add a text annotation box listing the 6 features used.
- **Synthetic Data:** Generate 600 credit applicants with 6 correlated features: `annual_income` (log-normal, mean=11, std=0.5), `debt_to_income` (beta distribution, shape varies by class), `credit_utilization` (uniform 0-1, skewed by class), `months_employed` (exponential, mean varies), `num_late_payments` (Poisson, lambda varies by class), `loan_amount` (log-normal). Good borrowers: low debt ratio, few late payments. Default: high debt, many late payments. Borderline: intermediate values with overlap.
- **Teaching Point:** t-SNE on credit features reveals natural clusters that align with (but don't perfectly match) credit classes. The borderline region shows where simple rules fail. This motivates more sophisticated classification approaches.
- **Python Approach:** Generate each feature with class-dependent parameters. StandardScaler. TSNE(random_state=42, perplexity=30). Color by class, size by loan_amount.
- **Bottomnote:** "t-SNE on credit features reveals natural risk clusters---the borderline region shows where classification is genuinely difficult"
- **No duplication:** No existing chart applies t-SNE to finance-themed features.

---

#### Chart 40: `top20_40_portfolio_risk_pca_monitoring`
- **Slide Title:** "PCA for Portfolio Risk Monitoring: Detecting Regime Changes"
- **Visualization:** Single time-series line plot showing the rolling explained variance ratio of PC1 (y-axis: 0.3 to 0.9) over a 250-day window (x-axis: trading days 250-1000). Two regimes visible: "Normal" period (PC1 explains ~40-50%) and "Crisis" period (PC1 explains ~70-85% -- correlations spike). Shade the crisis period in light red. Add horizontal dashed lines at 50% and 70% thresholds. Annotate "Normal: diversified risk" and "Crisis: single-factor dominance".
- **Synthetic Data:** Generate 1000 days of 10-stock returns. Days 1-500 and 750-1000: normal regime (moderate correlations, off-diag ~0.3). Days 500-750: crisis regime (high correlations, off-diag ~0.8, higher volatility). Rolling PCA with 250-day window.
- **Teaching Point:** During financial crises, asset correlations spike and PC1 absorbs most variance ("everything goes down together"). Monitoring the rolling PC1 explained variance ratio is a practical early-warning indicator for portfolio risk managers. When PC1 share jumps above 70%, diversification is breaking down.
- **Python Approach:** Generate returns with regime-switching correlations. Rolling window: for each day t >= 250, PCA on returns[t-250:t], record `explained_variance_ratio_[0]`. Plot as time series. `ax.axhspan` for crisis period.
- **Bottomnote:** "When PC1's share spikes above 70\\%, correlations are rising and diversification is breaking down---a crisis early-warning signal"
- **No duplication:** No existing chart shows rolling PCA variance monitoring or regime detection.

---

## Slide Deck Structure: `L05_pca_tsne_top20.tex`

### XKCD Comics
- **Opening:** XKCD #2048 "Curve Fitting" (already in images folder, used by top10 deck -- reuse is fine since it's a different slide deck)
- **Closing:** XKCD #2400 "Statistics" (already in images folder -- reuse is fine since it's a different slide deck)

### Slide Flow (~30 slides)
1. Title page
2. Opening XKCD #2048 with SCQ hook
3. Learning Objectives (4 items, Bloom's 4-5)
4. Outline (table of contents)
5. **Section 1: PCA Deep Mechanics** (6 chart slides: Charts 21-26)
6. Transition slide: "From PCA to t-SNE"
7. **Section 2: t-SNE Deep Mechanics** (6 chart slides: Charts 27-32)
8. Transition slide: "From Theory to Practice"
9. **Section 3: Practical Diagnostics** (4 chart slides: Charts 33-36)
10. Transition slide: "From Theory to Finance"
11. **Section 4: Finance Applications** (4 chart slides: Charts 37-40)
12. Summary checklist (20 charts listed)
13. Closing XKCD #2400

**Total: ~30 slides** (1 title + 1 XKCD + 1 LO + 1 outline + 20 charts + 3 transitions + 1 summary + 1 closing + 1 closing XKCD = 30)

---

## Task Flow

### Phase 1: Create 20 chart folders and chart.py files (TODOs 1-20)
Each chart.py must follow the canonical pattern from `top10_09_cumulative_variance/chart.py`:
- Module docstring
- CHART_METADATA dict
- rcParams update with standard font sizes
- Color constants (MLPurple, MLBlue, MLOrange, MLGreen, MLRed, MLLavender)
- Synthetic data generation with `np.random.seed(42)`
- Single figure creation with `plt.figure(figsize=(10, 6))`
- NO plt.subplots(), NO fig.add_subplot(), NO axes arrays
- URL watermark via `plt.figtext`
- Save to chart.pdf with `dpi=300, bbox_inches='tight'`

### Phase 2: Create L05_pca_tsne_top20.tex (TODO 21)
- Copy preamble from L05_pca_tsne_top10.tex exactly (lines 1-93)
- Update title to "PCA & t-SNE: Ultra-Deep Visuals"
- Update subtitle to "20 Advanced Charts for the Curious Data Scientist"
- Structure: Title + XKCD + LOs + Outline + 4 sections + Summary checklist + closing XKCD
- Reference chart paths as `top20_XX_descriptive_name/chart.pdf`

### Phase 3: Build and validate (TODO 22)
- Run all 20 chart.py files
- Compile .tex with pdflatex
- Check for Overfull warnings

---

## Detailed TODOs

### TODO 1: Create `top20_21_hotelling_t2_outlier/chart.py`
- **Acceptance:** File exists, runs without error, produces chart.pdf showing T-squared colored scatter with confidence ellipses. SINGLE figure, no subplots.

### TODO 2: Create `top20_22_spe_q_residual/chart.py`
- **Acceptance:** File exists, runs without error, produces chart.pdf with SPE bar chart and threshold line. SINGLE figure, no subplots.

### TODO 3: Create `top20_23_sparse_pca_loadings/chart.py`
- **Acceptance:** File exists, runs without error, produces chart.pdf with horizontal bar chart of sparse loadings. SINGLE figure, no subplots.

### TODO 4: Create `top20_24_robust_pca_outlier_influence/chart.py`
- **Acceptance:** File exists, runs without error, produces chart.pdf showing PC1 direction shift from outliers. SINGLE figure, no subplots.

### TODO 5: Create `top20_25_pca_variance_vs_components/chart.py`
- **Acceptance:** File exists, runs without error, produces chart.pdf with silhouette vs k line plot. SINGLE figure, no subplots.

### TODO 6: Create `top20_26_pca_condition_number/chart.py`
- **Acceptance:** File exists, runs without error, produces chart.pdf showing condition number vs correlation strength. SINGLE figure, no subplots.

### TODO 7: Create `top20_27_tsne_perplexity_vs_kl/chart.py`
- **Acceptance:** File exists, runs without error, produces chart.pdf with KL divergence vs perplexity line plot. SINGLE figure, no subplots.

### TODO 8: Create `top20_28_tsne_learning_rate/chart.py`
- **Acceptance:** File exists, runs without error, produces chart.pdf with single scatter showing good lr=200 result plus text annotations for failure modes. SINGLE figure, no subplots.

### TODO 9: Create `top20_29_early_exaggeration/chart.py`
- **Acceptance:** File exists, runs without error, produces chart.pdf with single scatter showing poor result without exaggeration. SINGLE figure, no subplots.

### TODO 10: Create `top20_30_crowding_problem/chart.py`
- **Acceptance:** File exists, runs without error, produces chart.pdf with overlaid Gaussian vs t-distribution kernel curves showing both the problem and the solution. SINGLE figure, no subplots.

### TODO 11: Create `top20_31_tsne_vs_mds_vs_isomap/chart.py`
- **Acceptance:** File exists, runs without error, produces chart.pdf with grouped bar chart comparing trustworthiness across 3 sklearn methods. SINGLE figure, no subplots. NO umap-learn.

### TODO 12: Create `top20_32_tsne_n_iter_effect/chart.py`
- **Acceptance:** File exists, runs without error, produces chart.pdf with trustworthiness vs n_iter line plot. SINGLE figure, no subplots.

### TODO 13: Create `top20_33_pca_then_tsne_pipeline/chart.py`
- **Acceptance:** File exists, runs without error, produces chart.pdf showing PCA+t-SNE pipeline result with runtime annotations. SINGLE figure, no subplots.

### TODO 14: Create `top20_34_trustworthiness_vs_k/chart.py`
- **Acceptance:** File exists, runs without error, produces chart.pdf with 3 lines (t-SNE, PCA, Isomap) showing trustworthiness vs k. SINGLE figure, no subplots.

### TODO 15: Create `top20_35_explained_var_vs_accuracy/chart.py`
- **Acceptance:** File exists, runs without error, produces chart.pdf with single-axis accuracy vs k plot with variance annotations. SINGLE figure, no subplots, NO twinx().

### TODO 16: Create `top20_36_pca_correlation_effect/chart.py`
- **Acceptance:** File exists, runs without error, produces chart.pdf with two overlaid eigenvalue decay curves. SINGLE figure, no subplots.

### TODO 17: Create `top20_37_yield_curve_factor_loadings/chart.py`
- **Acceptance:** File exists, runs without error, produces chart.pdf showing Level/Slope/Curvature loading patterns. SINGLE figure, no subplots. Uses Nelson-Siegel synthetic yield data.

### TODO 18: Create `top20_38_portfolio_factor_decomposition/chart.py`
- **Acceptance:** File exists, runs without error, produces chart.pdf with horizontal bar chart of PC1 loadings colored by sector. SINGLE figure, no subplots. Uses synthetic multi-factor stock returns.

### TODO 19: Create `top20_39_credit_risk_tsne/chart.py`
- **Acceptance:** File exists, runs without error, produces chart.pdf with t-SNE scatter colored by credit class. SINGLE figure, no subplots. Uses synthetic credit features with realistic distributions.

### TODO 20: Create `top20_40_portfolio_risk_pca_monitoring/chart.py`
- **Acceptance:** File exists, runs without error, produces chart.pdf with rolling PC1 variance time series showing regime change. SINGLE figure, no subplots. Uses synthetic regime-switching stock returns.

### TODO 21: Create `slides/L05_PCA_tSNE/L05_pca_tsne_top20.tex`
- **Acceptance:** File exists with correct preamble (copy lines 1-93 from L05_pca_tsne_top10.tex), 20 chart slides with question titles and bottomnotes, ~30 slides total, all chart paths correct. Opening XKCD #2048, closing XKCD #2400.

### TODO 22: Build and validate all charts and the .tex file
- **Acceptance:** All 20 chart.pdf files exist. pdflatex compiles L05_pca_tsne_top20.tex with zero Overfull warnings. All charts are single-panel (no subplots).

---

## Commit Strategy

1. **Commit 1:** All 20 chart.py files + L05_pca_tsne_top20.tex
2. **Commit 2:** Generated chart.pdf files + compiled L05_pca_tsne_top20.pdf

---

## Success Criteria

- [ ] 20 new chart folders exist under `slides/L05_PCA_tSNE/top20_21_*` through `top20_40_*`
- [ ] Each chart.py runs without error and produces chart.pdf
- [ ] **Every chart is a SINGLE figure -- zero subplots, zero multi-panel, zero twinx()**
- [ ] L05_pca_tsne_top20.tex compiles with zero Overfull warnings
- [ ] No chart duplicates any of the 22 existing charts
- [ ] All charts use synthetic data only (numpy/scipy/sklearn generators)
- [ ] Every slide has a question-based title and bottomnote
- [ ] .tex preamble matches L05_pca_tsne_top10.tex exactly (lines 1-93)
- [ ] Section 4 charts use genuine finance-themed synthetic data (not relabeled blobs)
- [ ] Only numpy, scipy, sklearn, matplotlib, seaborn used (no umap-learn)
