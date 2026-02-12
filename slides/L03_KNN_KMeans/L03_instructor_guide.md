# Instructor Guide: L03 - KNN & K-Means

## Session Overview

| Aspect | Details |
|--------|---------|
| **Duration** | 3 hours |
| **Topic** | K-Nearest Neighbors and K-Means Clustering |
| **Finance Case** | Customer segmentation, fraud detection |
| **Prerequisites** | L01-L02, basic statistics |

## Learning Objectives

By the end of this session, students will be able to:

1. Apply KNN for classification with appropriate K selection
2. Implement K-Means clustering and evaluate cluster quality
3. Compare distance metrics and their effects on results
4. Distinguish between supervised (KNN) and unsupervised (K-Means)

## PMSP Structure

### Problem Phase (15 min)

**Motivation**: Present customer segmentation and fraud detection as dual problems.

**Key Questions to Ask**:
- What's the difference between classification and clustering?
- When do we have labels vs when do we need to discover structure?
- Why might a bank want to segment customers?

**Discussion Points**:
- Connect KNN to human intuition: "similar things are similar"
- K-Means as discovering hidden patterns in data

### Method Phase (45 min)

**Core Concepts to Cover**:

1. **KNN Fundamentals**
   - Distance metrics (Euclidean, Manhattan)
   - Effect of K on decision boundary
   - Curse of dimensionality

2. **K-Means Algorithm**
   - Iterative assignment and update
   - K-Means++ initialization
   - Choosing K: elbow, silhouette

3. **Key Distinction**
   - Supervised vs unsupervised
   - "K" means different things!

**Common Misconceptions**:
- "KNN and K-Means are the same" - completely different algorithms
- "Higher K is always better" - bias-variance tradeoff applies
- "K-Means always finds optimal clusters" - only local optimum

### Solution Phase (45 min)

**Implementation Walkthrough**:

1. **KNN Implementation**
   - Feature scaling importance
   - Cross-validation for K selection
   - Weighted vs uniform voting

2. **K-Means Implementation**
   - Running multiple initializations
   - Interpreting cluster centers
   - Profiling clusters for business insights

**Live Coding Tips**:
- Show decision boundary changing with K
- Visualize K-Means iteration by iteration
- Compare elbow and silhouette methods

### Practice Phase (75 min)

**Hands-on Notebook**:
- Students work through L03_knn_kmeans.ipynb
- Customer segmentation exercise with interpretation

**Exercise Difficulty Progression**:
1. Apply KNN to synthetic data, vary K (guided)
2. Segment customers with K-Means, profile clusters (semi-guided)
3. Compare different K selection methods (open-ended)

## Decision Framework

### KNN vs K-Means

| Aspect | KNN | K-Means |
|--------|-----|---------|
| Task | Classification | Clustering |
| Input | Labeled data | Unlabeled data |
| K meaning | Neighbors | Clusters |
| Output | Class label | Cluster ID |

## Materials Checklist

- [ ] Slides: L03_overview.pdf
- [ ] Slides: L03_deepdive.pdf
- [ ] Notebook: L03_knn_kmeans.ipynb
- [ ] Dataset: customers_synthetic.csv
- [ ] All 7 charts compiled

## Timing Guide

| Phase | Duration | Notes |
|-------|----------|-------|
| Problem | 15 min | Dual problem motivation |
| Method | 45 min | Clear KNN vs K-Means distinction |
| Solution | 45 min | Live coding both algorithms |
| **Break** | 15 min | |
| Practice | 60 min | Customer segmentation focus |
| Q&A | 15 min | Preview random forests |

## Common Student Questions

**Q: How do I choose between KNN and logistic regression?**
A: Logistic regression for interpretable coefficients and linear boundaries. KNN for complex, non-linear patterns and when similar examples argument helps.

**Q: What if K-Means gives different results each time?**
A: Use n_init parameter (default 10) to run multiple times with different initializations. Also set random_state for reproducibility.

**Q: How do I know if clusters are "good"?**
A: No ground truth in unsupervised learning. Use silhouette score, and most importantly, do clusters make business sense?

## Assessment Connection

This topic is assessed in:
- **Quiz**: Quiz 2 (questions 1-7)
- **Presentations**: Topics 4-6 (Distance Metrics, K-Means++, DBSCAN)
- **Capstone**: Customer analytics projects

## Additional Resources

- ISLR Chapters 2 (KNN), 12 (Clustering)
- scikit-learn clustering documentation
- Arthur & Vassilvitskii (2007) K-Means++ paper

## Slide Build Specification

### Required Content
- Intro key visual: Nearest neighbor intuition (show k=1,3,7 effect)
- Must-have derivations: Distance metric proofs, K-Means convergence, curse of dimensionality
- Must-have pseudocode: KNN with tie-breaking, K-Means with empty cluster handling

### Chart Requirements
- KNN boundaries (overview)
- Distance heatmap (deepdive)
- K-Means iteration (overview)
- Elbow plot (overview)
- Silhouette plot (deepdive)
- Voronoi diagram (deepdive)

### Domain Applications
- Customer segmentation (RFM) (worked example)
- Fraud anomaly detection via clustering

### Appendix Content
- Distance metric proofs
- K-Means convergence proof
- Empty cluster handling edge cases

## Post-Session Notes

*Space for instructor notes after delivering the session*

---

*Last updated: 2026-01-07*
