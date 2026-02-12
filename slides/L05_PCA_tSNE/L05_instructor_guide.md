# Instructor Guide: L05 - PCA & t-SNE

## Session Overview

| Aspect | Details |
|--------|---------|
| **Duration** | 3 hours |
| **Topic** | Dimensionality Reduction: PCA and t-SNE |
| **Finance Case** | Portfolio risk decomposition, asset visualization |
| **Prerequisites** | L01-L04, linear algebra basics |

## Learning Objectives

By the end of this session, students will be able to:

1. Apply PCA for dimensionality reduction and feature extraction
2. Interpret variance explained and choose number of components
3. Use t-SNE for visualization of high-dimensional data
4. Compare linear (PCA) vs non-linear (t-SNE) methods

## PMSP Structure

### Problem Phase (15 min)

**Motivation**: Present the curse of dimensionality in portfolio analysis.

**Key Questions to Ask**:
- How do you visualize a portfolio with 100 assets?
- What does "dimensionality reduction" mean?
- Why can't we just pick the 2 most important features?

**Discussion Points**:
- High-dimensional data is hard to visualize and analyze
- Features are often correlated (redundant information)
- We want to compress while preserving important structure

### Method Phase (45 min)

**Core Concepts to Cover**:

1. **PCA Fundamentals**
   - Covariance matrix and eigendecomposition
   - Principal components as orthogonal directions
   - Variance explained and scree plots

2. **Choosing Number of Components**
   - 80-95% variance rule
   - Elbow method
   - Kaiser criterion

3. **t-SNE Basics**
   - Probabilistic neighbor preservation
   - Perplexity parameter
   - KL divergence optimization

4. **Comparison**
   - Linear vs non-linear
   - Speed and scalability
   - Use cases

**Common Misconceptions**:
- "t-SNE cluster sizes are meaningful" - FALSE
- "t-SNE distances between clusters are meaningful" - FALSE
- "PCA always loses important information" - Not if variance is preserved

### Solution Phase (45 min)

**Implementation Walkthrough**:

1. **PCA Demo**
   - Show scree plot interpretation
   - Visualize principal components
   - Demonstrate reconstruction

2. **t-SNE Demo**
   - Show perplexity effect
   - Compare multiple runs
   - Highlight non-determinism

**Live Coding Tips**:
- Always standardize before PCA
- Show side-by-side PCA vs t-SNE
- Run t-SNE multiple times with different seeds

### Practice Phase (60 min)

**Hands-on Notebook**:
- Students work through L05_pca_tsne.ipynb
- Portfolio decomposition exercise

**Exercise Difficulty Progression**:
1. Apply PCA, plot scree, choose k (guided)
2. Compare PCA vs t-SNE visualizations (semi-guided)
3. Interpret PCA loadings for business insights (open-ended)

## Key Equations

### PCA
$$\Sigma = \frac{1}{n-1} X^T X$$
$$\Sigma v = \lambda v$$

### Variance Explained
$$\text{Explained Variance}_i = \frac{\lambda_i}{\sum_j \lambda_j}$$

## Materials Checklist

- [ ] Slides: L05_overview.pdf
- [ ] Slides: L05_deepdive.pdf
- [ ] Notebook: L05_pca_tsne.ipynb
- [ ] Dataset: portfolio_synthetic.csv
- [ ] All 7 charts compiled

## Timing Guide

| Phase | Duration | Notes |
|-------|----------|-------|
| Problem | 15 min | Curse of dimensionality |
| Method | 45 min | PCA math, t-SNE intuition |
| Solution | 45 min | Live coding both methods |
| **Break** | 15 min | |
| Practice | 45 min | Portfolio analysis |
| Q&A | 15 min | Preview embeddings/RL |

## Common Student Questions

**Q: Should I always use PCA before t-SNE?**
A: Generally yes, especially for large datasets. PCA to 30-50 dimensions speeds up t-SNE significantly.

**Q: How do I choose perplexity?**
A: Start with 30 (default). Try 5, 30, 50 to see how structure changes. Should be smaller than dataset size.

**Q: Can I use t-SNE for clustering?**
A: Only for visualization/exploration. Don't cluster on t-SNE output - cluster in original space.

**Q: What about UMAP?**
A: UMAP is often preferred now - faster, better global structure, can embed new points. Consider teaching as alternative.

## Assessment Connection

This topic is assessed in:
- **Quiz**: Quiz 3 (questions 1-7)
- **Presentations**: Topics 10-12 (UMAP, PCA in Finance, Autoencoders)
- **Capstone**: Dimensionality reduction for any project

## Slide Build Specification

### Required Content
- Intro key visual: 3D to 2D projection
- Must-have derivations: Eigenvalue derivation from covariance matrix, SVD connection, t-SNE gradient, perplexity math
- No pseudocode needed (PCA is a closed-form computation)

### Chart Requirements
- Scree plot (overview)
- PC loadings (deepdive)
- Reconstruction visualization (deepdive)
- t-SNE perplexity comparison (deepdive)
- Swiss roll projection (overview)

### Domain Applications
- Yield curve PCA: first 3 PCs = level/slope/curvature (worked example)
- Portfolio risk decomposition
- t-SNE for market regime detection

### Appendix Content
- Full eigenvalue derivation
- SVD-PCA equivalence proof
- t-SNE gradient derivation

## Post-Session Notes

*Space for instructor notes after delivering the session*

---

*Last updated: 2026-01-07*
