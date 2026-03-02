# Plan: L03 Separate KNN and K-Means Notebooks

## Task
Create two simple, visual-heavy Jupyter notebooks:
1. `notebooks/L03_knn.ipynb` — KNN classification
2. `notebooks/L03_kmeans.ipynb` — K-Means clustering

Both should be simpler than the existing combined `L03_knn_kmeans.ipynb`, with emphasis on visuals.

### Existing Notebook Disposition
**Keep** `notebooks/L03_knn_kmeans.ipynb` as-is. It remains the "combined" reference notebook. The two new notebooks are focused, visual-heavy alternatives — not replacements. No archiving or deletion needed.

---

## Notebook 1: `notebooks/L03_knn.ipynb` — K-Nearest Neighbors

### Structure (~19 cells, minimum 8 visuals)

| # | Type | Content | Visual? |
|---|------|---------|---------|
| 1 | md | Title, Colab badge, objectives | - |
| 2 | code | Setup: imports (numpy, pandas, matplotlib, sklearn), seed, rcParams | - |
| 3 | md | "1. Generate Data" header | - |
| 4 | code | Create 2-class Iris-style dataset (make_classification or real Iris 2-feature) | - |
| 5 | code | **Visual 1**: Scatter plot of raw data (2 classes, colored) | Yes |
| 6 | md | "2. How KNN Works" header | - |
| 7 | code | **Visual 2**: Annotated plot showing a query point + its K=3 nearest neighbors with circles/lines | Yes |
| 8 | code | **Visual 3**: Side-by-side decision boundaries for K=1, K=5, K=15 (3-panel via `fig, axes = plt.subplots(1, 3, figsize=(18, 5))`) | Yes |
| 9 | md | "3. Feature Scaling Matters" header | - |
| 10 | code | **Visual 4**: Before/after scaling comparison — unscaled vs scaled distances (2 panels) | Yes |
| 11 | md | "4. Finding the Best K" header | - |
| 12 | code | **Visual 5**: Cross-validation accuracy curve (K=1..20), highlight best K | Yes |
| 13 | md | "5. Distance Metrics" header | - |
| 14 | code | **Visual 6**: Unit balls for Euclidean, Manhattan, Chebyshev (like chart 02) | Yes |
| 15 | md | "6. Final Model & Evaluation" header | - |
| 16 | code | Train best KNN, print accuracy, confusion matrix | - |
| 17 | code | **Visual 7**: Decision boundary with test points overlaid | Yes |
| 18 | code | **Visual 8**: Confusion matrix heatmap | Yes |
| 19 | md | Summary: key takeaways (3-4 bullets) | - |

### Colab Badge
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L03_knn.ipynb)
```

---

## Notebook 2: `notebooks/L03_kmeans.ipynb` — K-Means Clustering

### Structure (~19 cells, minimum 8 visuals)

| # | Type | Content | Visual? |
|---|------|---------|---------|
| 1 | md | Title, Colab badge, objectives | - |
| 2 | code | Setup: imports, seed, rcParams | - |
| 3 | md | "1. Generate Data" header | - |
| 4 | code | Create 3-cluster blob dataset (make_blobs) | - |
| 5 | code | **Visual 1**: Scatter plot of raw unlabeled data (single color — we don't know clusters yet!) | Yes |
| 6 | md | "2. How K-Means Works" header | - |
| 7 | code | **Visual 2**: 4-panel iteration plot (see implementation note below) | Yes |
| 8 | md | "3. Choosing K: Elbow Method" header | - |
| 9 | code | **Visual 3**: Elbow plot (WCSS vs K=1..10) with annotated elbow point | Yes |
| 10 | md | "4. Choosing K: Silhouette Analysis" header | - |
| 11 | code | **Visual 4**: Silhouette scores for K=2..8 | Yes |
| 12 | code | **Visual 5**: Silhouette plot (knife-shaped bars per cluster) for best K | Yes |
| 13 | md | "5. Final Clustering Result" header | - |
| 14 | code | **Visual 6**: Scatter plot with colored clusters + centroid markers + Voronoi overlay | Yes |
| 15 | md | "6. Customer Segmentation Example (RFM)" header | - |
| 16 | code | Generate simple RFM-like data (Recency, Frequency, Monetary) | - |
| 17 | code | **Visual 7**: 2D scatter of RFM clusters (Recency vs Monetary, colored by cluster) | Yes |
| 18 | code | **Visual 8**: Cluster profile bar chart (mean R, F, M per cluster) | Yes |
| 19 | md | Summary: key takeaways (3-4 bullets) | - |

### K-Means Iteration Animation (Visual 2) — Implementation Guide
Use manual K-Means implementation for pedagogical clarity:
```python
from sklearn.metrics import pairwise_distances_argmin

fig, axes = plt.subplots(1, 4, figsize=(20, 4))
# Initialize centroids randomly from data points
rng = np.random.RandomState(42)
centroids = X[rng.choice(len(X), 3, replace=False)]
titles = ['Init', 'Iteration 1', 'Iteration 2', 'Final (Converged)']
for i, ax in enumerate(axes):
    # Assign points to nearest centroid
    labels = pairwise_distances_argmin(X, centroids)
    ax.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=20, alpha=0.6)
    ax.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, edgecolors='black')
    ax.set_title(titles[i])
    ax.set_xticks([]); ax.set_yticks([])
    # Update centroids (mean of assigned points)
    centroids = np.array([X[labels == k].mean(axis=0) for k in range(3)])
plt.suptitle('K-Means Algorithm: Step by Step', fontsize=16)
plt.tight_layout()
```

### RFM Visual Decision: 2D Scatter
Use **2D scatter** (Recency vs Monetary, colored by cluster) instead of 3D. Rationale:
- 2D is cleaner and easier to interpret in a notebook
- 3D rotatable plots don't render in Colab static output
- Students can change axes to explore other pairs (R-F, F-M)

### Colab Badge
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L03_kmeans.ipynb)
```

---

## Shared Conventions (from existing notebook)

- `np.random.seed(42)` for reproducibility
- `plt.rcParams['figure.figsize'] = (10, 6)` and `plt.rcParams['font.size'] = 12`
- ML color palette: `#3333B2` (purple), `#0066CC` (blue), `#FF7F0E` (orange), `#2CA02C` (green), `#D62728` (red)
- Finance domain examples (customer data, transactions)
- Simple code — no complex abstractions, each cell does one thing
- Every visual has: title, axis labels, legend (where applicable), `plt.grid(True, alpha=0.3)`

---

## GH Pages Integration

### Update `docs/index.html`

**Line 119** — Update hero notebook count from `6` to `8`:
```html
<span><b>8</b><small>Notebooks</small></span>
```

**Line 205** — Replace the single combined notebook card with two separate cards:

Replace:
```html
<a class="ccard" href="https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L03_knn_kmeans.ipynb" target="_blank"><div class="ccard-icon">NB</div>Colab Notebook<div class="ccard-label">Open in Colab</div></a>
```

With:
```html
<a class="ccard" href="https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L03_knn_kmeans.ipynb" target="_blank"><div class="ccard-icon">NB</div>Combined Notebook<div class="ccard-label">KNN + K-Means</div></a>
<a class="ccard" href="https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L03_knn.ipynb" target="_blank"><div class="ccard-icon">NB</div>KNN Notebook<div class="ccard-label">Visual-heavy KNN</div></a>
<a class="ccard" href="https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L03_kmeans.ipynb" target="_blank"><div class="ccard-icon">NB</div>K-Means Notebook<div class="ccard-label">Visual-heavy K-Means</div></a>
```

---

## manifest.json Update

**No changes to manifest.json.** The existing `"notebook"` key for L03 points to `notebooks/L03_knn_kmeans.ipynb` and must remain as-is. Reason: 8+ infrastructure Python files (`notebook_builder.py`, `notebook_validator.py`, `colab_deployer.py`, `guide_generator.py`, `build_report.py`, `coverage_report.py`, `html_dashboard.py`) all access `assets.get("notebook", {})` with the singular key. Changing the key or its structure would silently break all infrastructure tooling.

The two new notebooks are supplementary visual-heavy alternatives discovered via the GH Pages site and Colab badges, not tracked in the infrastructure manifest.

---

## Verification

### How to verify notebooks run top-to-bottom
Run each notebook with `nbconvert --execute`:
```bash
jupyter nbconvert --to notebook --execute notebooks/L03_knn.ipynb --output /dev/null 2>&1 && echo "KNN: PASS" || echo "KNN: FAIL"
jupyter nbconvert --to notebook --execute notebooks/L03_kmeans.ipynb --output /dev/null 2>&1 && echo "K-Means: PASS" || echo "K-Means: FAIL"
```

If `jupyter` is not available, use Python directly:
```bash
python -c "import nbformat; from nbconvert.preprocessors import ExecutePreprocessor; nb=nbformat.read('notebooks/L03_knn.ipynb',4); ep=ExecutePreprocessor(timeout=120); ep.preprocess(nb); print('KNN: PASS')"
python -c "import nbformat; from nbconvert.preprocessors import ExecutePreprocessor; nb=nbformat.read('notebooks/L03_kmeans.ipynb',4); ep=ExecutePreprocessor(timeout=120); ep.preprocess(nb); print('K-Means: PASS')"
```

### Checklist
- [ ] `notebooks/L03_knn.ipynb` exists with 8+ visuals
- [ ] `notebooks/L03_kmeans.ipynb` exists with 8+ visuals
- [ ] Both execute top-to-bottom without errors
- [ ] Both use `np.random.seed(42)`
- [ ] Both use course color palette and rcParams
- [ ] `docs/index.html` hero count = 8 notebooks
- [ ] `docs/index.html` L03 section has 3 notebook cards
- [ ] `manifest.json` is untouched (no schema changes)
- [ ] Existing `L03_knn_kmeans.ipynb` is untouched

---

## Acceptance Criteria

1. `notebooks/L03_knn.ipynb` exists with minimum 8 visual-producing code cells
2. `notebooks/L03_kmeans.ipynb` exists with minimum 8 visual-producing code cells
3. Both notebooks run without errors (verified via nbconvert --execute or equivalent)
4. Both use `np.random.seed(42)` for reproducibility
5. Both use course color palette and rcParams
6. KNN notebook covers: scatter, KNN neighbors illustration, decision boundaries (multiple K), scaling, CV curve, distance metrics, confusion matrix
7. K-Means notebook covers: unlabeled scatter, iteration 4-panel, elbow, silhouette, final clusters with centroids, RFM 2D scatter + bar chart
8. Both have Colab badges with correct GitHub URLs
9. Code is simple — no unnecessary abstractions, suitable for MSc students to follow
10. `docs/index.html` updated (hero count + L03 notebook cards)
11. `manifest.json` untouched (no schema changes — infrastructure tooling preserved)
12. Existing `notebooks/L03_knn_kmeans.ipynb` remains untouched

---

PLAN_READY: .omc/plans/L03-notebooks.md
