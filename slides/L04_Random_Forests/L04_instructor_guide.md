# Instructor Guide: L04 - Random Forests

## Session Overview

| Aspect | Details |
|--------|---------|
| **Duration** | 3 hours |
| **Topic** | Random Forests and Ensemble Learning |
| **Finance Case** | Fraud detection with feature importance |
| **Prerequisites** | L01-L03, decision tree basics |

## Learning Objectives

By the end of this session, students will be able to:

1. Explain how decision trees partition feature space using Gini/entropy
2. Implement Random Forests with bootstrap and feature randomization
3. Interpret feature importance and OOB error
4. Apply ensemble methods to fraud detection problems

## PMSP Structure

### Problem Phase (15 min)

**Motivation**: Present fraud detection as a real-world problem requiring both accuracy and interpretability.

**Key Questions to Ask**:
- Why might a single decision tree be unreliable?
- What does "ensemble" mean in the context of ML?
- Why do banks need to explain fraud flags?

**Discussion Points**:
- Connect to "wisdom of crowds" - many weak learners become strong
- Contrast with black-box models (neural networks)
- Business requirement: regulatory compliance needs explainability

### Method Phase (45 min)

**Core Concepts to Cover**:

1. **Decision Tree Foundations**
   - Gini impurity and entropy
   - Recursive partitioning algorithm
   - Stopping criteria

2. **Bootstrap Aggregating (Bagging)**
   - Sampling with replacement
   - 63.2% unique samples per tree
   - Out-of-bag samples (~37%)

3. **Random Forest Innovations**
   - Feature randomization at each split
   - sqrt(p) for classification, p/3 for regression
   - Decorrelating trees for variance reduction

4. **Feature Importance**
   - Mean Decrease in Impurity (MDI)
   - Permutation importance

**Common Misconceptions**:
- "More trees = overfitting" - FALSE, more trees never hurts
- "Random Forest is uninterpretable" - FALSE, feature importance helps
- "OOB error is biased" - FALSE, it's unbiased like CV

### Solution Phase (45 min)

**Implementation Walkthrough**:

1. **Single Tree Demo**
   - Show overfitting on training data
   - Demonstrate high variance with different samples

2. **Building the Forest**
   - Bootstrap sampling visualization
   - Feature randomization effect
   - OOB error convergence

3. **Feature Importance**
   - MDI vs permutation importance
   - Business interpretation of top features

**Live Coding Tips**:
- Show tree variance by training on different random states
- Visualize OOB error vs number of trees
- Compare RF accuracy to single tree

### Practice Phase (75 min)

**Hands-on Notebook**:
- Students work through L04_random_forests.ipynb
- Fraud detection exercise with real feature interpretation

**Exercise Difficulty Progression**:
1. Train RF and compare to single tree (guided)
2. Tune hyperparameters using OOB error (semi-guided)
3. Interpret feature importance for business decisions (open-ended)

## Key Equations

### Gini Impurity
$$G = 1 - \sum_{k=1}^{K} p_k^2$$

### Information Gain
$$IG = H(\text{parent}) - \sum_{j} \frac{n_j}{n} H(\text{child}_j)$$

### Variance Reduction (Averaging)
$$\text{Var}\left(\frac{1}{B}\sum_{b=1}^{B} \hat{f}_b\right) = \rho\sigma^2 + \frac{1-\rho}{B}\sigma^2$$

## Decision Framework

### When to Use Random Forests

| Use RF When | Consider Alternatives When |
|-------------|---------------------------|
| Tabular data | Very sparse high-dimensional data |
| Non-linear patterns | Need full interpretability |
| Feature importance needed | Extrapolation required |
| Out-of-the-box performance | Fastest prediction needed |

## Materials Checklist

- [ ] Slides: L04_overview.pdf
- [ ] Slides: L04_deepdive.pdf
- [ ] Notebook: L04_random_forests.ipynb
- [ ] Dataset: transactions_synthetic.csv
- [ ] All 7 charts compiled

## Timing Guide

| Phase | Duration | Notes |
|-------|----------|-------|
| Problem | 15 min | Fraud detection motivation |
| Method | 45 min | Trees → Bagging → RF |
| Solution | 45 min | Live coding with sklearn |
| **Break** | 15 min | |
| Practice | 60 min | Fraud detection project |
| Q&A | 15 min | Preview PCA/t-SNE |

## Common Student Questions

**Q: How many trees should I use?**
A: Start with 100. More is always better (just slower). Use OOB error to check convergence - if still decreasing, add more trees.

**Q: What's the difference between Gini and entropy?**
A: Both measure impurity. Gini is faster to compute. Entropy produces slightly more balanced trees. In practice, results are nearly identical.

**Q: Why use feature randomization instead of just bagging?**
A: Bagging alone doesn't decorrelate trees enough. If one feature is very strong, all bagged trees will use it at the root. Feature randomization forces diversity.

**Q: Can Random Forests extrapolate?**
A: No. Trees can only predict values seen in training data. For extrapolation, use parametric models (linear regression, neural networks).

**Q: How do I handle imbalanced classes?**
A: Use class_weight='balanced' or class_weight='balanced_subsample'. Alternatively, use stratified bootstrap sampling.

## Assessment Connection

This topic is assessed in:
- **Quiz**: Quiz 2 (questions 8-14)
- **Presentations**: Topics 7-9 (XGBoost, SHAP, Imbalanced Classification)
- **Capstone**: Fraud detection or feature importance projects

## Additional Resources

- ISLR Chapter 8: Tree-Based Methods
- Breiman (2001) Random Forests paper
- scikit-learn ensemble documentation
- SHAP library for advanced feature importance

## Post-Session Notes

*Space for instructor notes after delivering the session*

---

*Last updated: 2026-01-07*
