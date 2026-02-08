<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-25 | Updated: 2026-02-07 -->

# L05_PCA_tSNE/

**Parent**: [../AGENTS.md](../AGENTS.md) (slides/)

## Purpose

Lesson 5 introduces dimensionality reduction with portfolio risk decomposition as the motivating finance case. Students learn PCA (linear), t-SNE (non-linear), and how to choose between them for visualization and feature engineering.

## Finance Case

**Problem**: Banks need to decompose portfolio risk into principal factors (market, sector, credit). PCA provides interpretable risk factors, while t-SNE visualizes high-dimensional asset relationships.

**Key Decision**: When to use PCA vs t-SNE for dimensionality reduction.

## Learning Objectives

1. **Understand**: Derive PCA from eigenvalue decomposition and variance maximization
2. **Apply**: Apply PCA and t-SNE for visualization and feature reduction
3. **Analyze**: Interpret principal components in finance context (e.g., PC1 = market factor)
4. **Evaluate**: Choose between PCA and t-SNE based on linearity and reproducibility needs

## Files

| File | Purpose | Slides |
|------|---------|--------|
| `L05_overview.tex` | Overview slides with 12 charts | ~17 |
| `L05_deepdive.tex` | Deep dive with eigenvector derivation | ~30 |
| `L05_instructor_guide.md` | Teaching guide with PMSP breakdown | - |

## Charts

All charts follow the naming convention `XX_descriptive_name/` and output `chart.pdf`:

| Chart | Directory | Description | Key Visual |
|-------|-----------|-------------|------------|
| 01 | `01_scree_plot/` | Variance explained | Bar chart showing variance per principal component |
| 02 | `02_principal_components/` | PC1 vs PC2 | Scatter plot in first 2 principal components |
| 03 | `03_reconstruction/` | PCA reconstruction | Original vs reconstructed data |
| 04a | `04a_tsne_perplexity_5/` | t-SNE (perplexity=5) | Low perplexity → local structure |
| 04b | `04b_tsne_perplexity_30/` | t-SNE (perplexity=30) | Medium perplexity → balanced |
| 04c | `04c_tsne_perplexity_100/` | t-SNE (perplexity=100) | High perplexity → global structure |
| 05a | `05a_pca_swiss_roll/` | PCA on Swiss roll | Fails to unroll non-linear manifold |
| 05b | `05b_tsne_swiss_roll/` | t-SNE on Swiss roll | Successfully unrolls manifold |
| 06a | `06a_original_clusters/` | 3D clustered data | Original high-dimensional clusters |
| 06b | `06b_pca_cluster_projection/` | PCA cluster projection | Linear projection may overlap clusters |
| 06c | `06c_tsne_cluster_projection/` | t-SNE cluster projection | Non-linear projection separates clusters |
| 07 | `07_decision_flowchart/` | When to use PCA/t-SNE | Flowchart for algorithm selection |

Note: Also includes `images/` subdirectory for XKCD cartoons and supporting visuals.

## CRITICAL: Chart Rewrite (Feb 2026)

**7 chart.py files were COMPLETELY REWRITTEN** in February 2026 to fix fabricated charts.

**Problem:** Original charts generated synthetic Gaussian blobs instead of running actual sklearn algorithms. They created visual mockups, not genuine algorithmic output.

**Solution:** All charts now:
- Use real sklearn TSNE/PCA on real datasets (load_digits, make_swiss_roll, make_blobs)
- Call `.fit_transform()` on actual data
- Use proper matplotlib settings (figsize=(10,6), dpi=150)
- Show genuine algorithm behavior, not synthetic mockups

**Affected Charts:**
- 04a_tsne_perplexity_5, 04b_tsne_perplexity_30, 04c_tsne_perplexity_100
- 05a_pca_swiss_roll, 05b_tsne_swiss_roll
- 06b_pca_cluster_projection, 06c_tsne_cluster_projection

## Chart Technical Details

**Standard settings** (same as L01-L04):
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
- MLRed: #D62728 (cluster 4, errors)

## Building Charts

```bash
# Build all charts for L05 (from project root)
python infrastructure/course_cli.py build charts --topic L05

# Build single chart manually
cd slides/L05_PCA_tSNE/01_scree_plot
python chart.py

# Verify all charts generated
python infrastructure/course_cli.py validate charts --topic L05
```

## LaTeX Compilation

```bash
# Compile overview slides (from L05 directory)
cd slides/L05_PCA_tSNE
pdflatex -interaction=nonstopmode L05_overview.tex

# Compile deep dive slides
pdflatex -interaction=nonstopmode L05_deepdive.tex

# Clean auxiliary files
mkdir temp 2>nul & move *.aux *.log *.nav *.out *.snm *.toc temp/

# Build via CLI (from project root)
python infrastructure/course_cli.py build slides --topic L05
```

## PMSP Structure

The instructor guide breaks down the 3-hour session:

| Phase | Duration | Content |
|-------|----------|---------|
| **Problem** | 15 min | Portfolio risk decomposition, curse of dimensionality |
| **Method** | 45 min | PCA derivation (eigendecomposition), t-SNE algorithm |
| **Solution** | 45 min | NumPy PCA implementation, sklearn comparison, perplexity tuning |
| **Practice** | 75 min | Jupyter notebook `L05_pca_tsne.ipynb` with portfolio data |

## Key Concepts

- **PCA Algorithm**: Center data (X→X_c) → compute covariance → eigendecomposition → project
- **Variance Maximization**: PCA finds directions of maximum variance
- **Scree Plot**: Elbow method to select number of components
- **t-SNE**: Non-linear method using Student's t-distribution
- **Perplexity**: t-SNE parameter balancing local vs global structure (typical: 5-50)
- **Curse of Dimensionality**: Distance metrics become less meaningful in high dimensions

## Major Additions (Feb 2026 Hostile Review Remediation)

This topic received **MAJOR MSc-level enhancements** in February 2026:

### New Content Blocks
1. **SVD-PCA Equivalence Proof**:
   - 5-step mathematical proof showing X = UΣV^T leads to same PCs
   - Shows covariance matrix C = VΣ²V^T/n
   - Explains computational efficiency of SVD approach

2. **PCA Optimality Proof**:
   - Lagrangian derivation of variance maximization
   - Shows PCs are eigenvectors of covariance matrix
   - Formal constraint: ||w|| = 1

3. **Yield Curve PCA** (2 frames):
   - Finance application: decomposing interest rate curves
   - PC1 = level (parallel shift), PC2 = slope, PC3 = curvature
   - Interpretation for risk management

4. **Statistical Inference**:
   - Bootstrap confidence intervals for explained variance
   - Permutation tests for component significance
   - Cross-validation for component selection

5. **Centering Correction**:
   - All formulas now show explicit centering: X → X_c
   - Mean-centering as prerequisite step before covariance computation
   - Impact on reconstruction quality

### Corrections
- **Centering**: Added explicit X→X_c notation throughout
- **EVR Formula**: Added explicit definition of explained variance ratio
- **Learning Objectives**: Rewritten to Bloom's Level 4-5 (Derive, Evaluate, Analyze, Critique)

### New Slides
- **Key Equations Frame** (Overview): Covariance matrix, eigendecomposition, EVR, t-SNE similarity formulas

## Mathematical Details

**PCA Objective**:
```
max_w w^T Σ w  subject to ||w|| = 1
```
where Σ is covariance matrix, w is principal component.

**t-SNE Objective**:
```
min KL(P || Q)
```
where P is high-dimensional similarities, Q is low-dimensional similarities.

## Decision Framework

**When to use PCA**:
- Linear relationships expected
- Interpretable components needed (e.g., risk factors)
- New data must be projected (transform available)
- Reproducible results required

**When to use t-SNE**:
- Non-linear manifold structure
- Visualization only (2D/3D)
- Local structure more important than global
- Stochastic results acceptable

**When NOT to use**:
- PCA: Non-linear structure (use kernel PCA or t-SNE)
- t-SNE: Need reproducibility, new data projection, or interpretability

## Common Pitfalls

1. **Feature Scaling**: ALWAYS standardize features before PCA (variance-based)
2. **Number of Components**: Use scree plot or cumulative variance threshold (e.g., 95%)
3. **t-SNE Perplexity**: Too low → fragmented clusters, too high → blob
4. **t-SNE Initialization**: Multiple runs with different seeds (non-deterministic)
5. **Interpretation**: t-SNE distances NOT meaningful (only cluster separation)

## Hyperparameter Tuning

**PCA**:
- `n_components`: Based on scree plot or variance threshold
- No other major hyperparameters

**t-SNE**:
| Parameter | Effect | Typical Range |
|-----------|--------|---------------|
| `perplexity` | Local vs global balance | 5-50 |
| `n_iter` | Convergence quality | 1000-5000 |
| `learning_rate` | Optimization speed | 10-1000 |

## Testing Checklist

- [ ] All 12 chart.py scripts generate chart.pdf
- [ ] L05_overview.tex compiles without errors
- [ ] L05_deepdive.tex compiles without errors
- [ ] ZERO "Overfull \hbox" warnings in LaTeX output
- [ ] Scree plot shows clear elbow
- [ ] PCA variance explained sums to 1.0
- [ ] t-SNE perplexity comparison shows different structures

## Related Assets

- **Notebook**: `notebooks/L05_pca_tsne.ipynb`
- **Dataset**: `datasets/portfolio_synthetic.csv` (features: 20 asset returns)
- **Quiz**: `quizzes/quiz3_topics_5_6.xml` (covers L05 + L06)
- **Template**: `templates/beamer_template.tex`, `templates/chart_template.py`

## Prerequisites

Students should know:
- L01 (linear regression for PCA connection)
- Linear algebra (eigenvalues, eigenvectors, matrix multiplication)
- Covariance and correlation

## Next Lesson

→ [L06_Embeddings_RL/AGENTS.md](../L06_Embeddings_RL/AGENTS.md) - Representation learning and sequential decision making
