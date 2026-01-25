<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-25 | Updated: 2026-01-25 -->

# L03_KNN_KMeans/

**Parent**: [../AGENTS.md](../AGENTS.md) (slides/)

## Purpose

Lesson 3 introduces instance-based learning (KNN) and clustering (K-Means) with customer segmentation as the motivating finance case. Students learn distance metrics, the curse of dimensionality, and cluster quality evaluation.

## Finance Case

**Problem**: Banks need to segment customers for targeted marketing and anomaly detection (fraud). KNN provides non-parametric classification, while K-Means identifies customer archetypes without labels.

**Key Decision**: When to use KNN vs parametric models, and how to choose optimal K.

## Learning Objectives

1. **Understand**: Explain distance metrics (Euclidean, Manhattan, Minkowski) and their properties
2. **Apply**: Implement KNN and K-Means from scratch (NumPy)
3. **Analyze**: Interpret cluster quality using silhouette scores
4. **Evaluate**: Select optimal K using elbow method and silhouette analysis

## Files

| File | Purpose | Slides |
|------|---------|--------|
| `L03_overview.tex` | Overview slides with 7 charts | ~17 |
| `L03_deepdive.tex` | Deep dive with distance metrics | ~30 |
| `L03_instructor_guide.md` | Teaching guide with PMSP breakdown | - |

## Charts

All charts follow the naming convention `XX_descriptive_name/` and output `chart.pdf`:

| Chart | Directory | Description | Key Visual |
|-------|-----------|-------------|------------|
| 01 | `01_knn_boundaries/` | Decision boundaries | KNN decision regions with k=1, k=5, k=15 |
| 02 | `02_distance_metrics/` | Distance comparison | Euclidean vs Manhattan distance visualization |
| 03 | `03_kmeans_iteration/` | K-Means convergence | Step-by-step centroid updates |
| 04 | `04_elbow_method/` | Optimal K selection | Within-cluster sum of squares (WCSS) vs K |
| 05 | `05_silhouette/` | Cluster quality | Silhouette scores for different K values |
| 06 | `06_voronoi/` | Voronoi diagram | Partition of space by nearest centroids |
| 07 | `07_decision_flowchart/` | When to use KNN/K-Means | Flowchart for algorithm selection |

## Chart Technical Details

**Standard settings** (same as L01-L02):
```python
plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150
})
```

**Color palette**:
- MLPurple: #3333B2 (structure)
- MLBlue: #0066CC (cluster 1)
- MLOrange: #FF7F0E (cluster 2)
- MLGreen: #2CA02C (cluster 3)
- MLRed: #D62728 (anomalies, errors)

## Building Charts

```bash
# Build all charts for L03 (from project root)
python infrastructure/course_cli.py build charts --topic L03

# Build single chart manually
cd slides/L03_KNN_KMeans/01_knn_boundaries
python chart.py

# Verify all charts generated
python infrastructure/course_cli.py validate charts --topic L03
```

## LaTeX Compilation

```bash
# Compile overview slides (from L03 directory)
cd slides/L03_KNN_KMeans
pdflatex -interaction=nonstopmode L03_overview.tex

# Compile deep dive slides
pdflatex -interaction=nonstopmode L03_deepdive.tex

# Clean auxiliary files
mkdir temp 2>nul & move *.aux *.log *.nav *.out *.snm *.toc temp/

# Build via CLI (from project root)
python infrastructure/course_cli.py build slides --topic L03
```

## PMSP Structure

The instructor guide breaks down the 3-hour session:

| Phase | Duration | Content |
|-------|----------|---------|
| **Problem** | 15 min | Customer segmentation motivation, fraud detection use case |
| **Method** | 45 min | Distance metrics, KNN algorithm, K-Means convergence |
| **Solution** | 45 min | NumPy implementation, sklearn comparison, elbow/silhouette |
| **Practice** | 75 min | Jupyter notebook `L03_knn_kmeans.ipynb` with customer data |

## Key Concepts

- **Distance Metrics**: Euclidean (L2), Manhattan (L1), Minkowski (Lp norm)
- **KNN Algorithm**: No training phase, lazy learning, majority vote for classification
- **K-Means Algorithm**: Lloyd's algorithm, minimizes within-cluster variance
- **Elbow Method**: Plot WCSS vs K, look for "elbow" where improvement slows
- **Silhouette Score**: Measures how similar points are to own cluster vs neighbors (-1 to +1)
- **Curse of Dimensionality**: Distance metrics become less meaningful in high dimensions

## Decision Framework

**When to use KNN**:
- Non-parametric (no assumptions about distribution)
- Small to medium datasets (slow on large data)
- Irregular decision boundaries
- No training time acceptable

**When to use K-Means**:
- Customer segmentation, market baskets
- Spherical clusters expected
- Fast clustering needed
- Number of clusters can be estimated

**When NOT to use**:
- High-dimensional data (curse of dimensionality)
- Large datasets (KNN slow at prediction)
- Non-spherical clusters (K-Means fails)
- Unknown K (try hierarchical clustering)

## Common Pitfalls

1. **Feature Scaling**: ALWAYS standardize features (distance-based methods)
2. **Choosing K**: Use cross-validation for KNN, elbow+silhouette for K-Means
3. **Initialization**: K-Means sensitive to initial centroids (use k-means++ or multiple runs)
4. **Imbalanced Classes**: KNN can be biased toward majority class

## Testing Checklist

- [ ] All 7 chart.py scripts generate chart.pdf
- [ ] L03_overview.tex compiles without errors
- [ ] L03_deepdive.tex compiles without errors
- [ ] ZERO "Overfull \hbox" warnings in LaTeX output
- [ ] KNN boundaries show smoothing with increasing K
- [ ] K-Means elbow plot shows clear inflection point

## Related Assets

- **Notebook**: `notebooks/L03_knn_kmeans.ipynb`
- **Dataset**: `datasets/customers_synthetic.csv` (features: age, income, spending; for clustering)
- **Quiz**: `quizzes/quiz2_topics_3_4.xml` (covers L03 + L04)
- **Template**: `templates/beamer_template.tex`, `templates/chart_template.py`

## Prerequisites

Students should know:
- L01 (gradient descent for comparison)
- Distance metrics (Euclidean vs Manhattan)
- Basic NumPy (array operations, broadcasting)

## Next Lesson

→ [L04_Random_Forests/AGENTS.md](../L04_Random_Forests/AGENTS.md) - Ensemble methods and feature importance
