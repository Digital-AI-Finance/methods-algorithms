# Instructor Guide: L02 - Logistic Regression

## Session Overview

| Aspect | Details |
|--------|---------|
| **Duration** | 3 hours |
| **Topic** | Logistic Regression for Classification |
| **Finance Case** | Credit default prediction, loan approval |
| **Prerequisites** | L01 Linear Regression, probability basics |

## Learning Objectives

By the end of this session, students will be able to:

1. Explain how logistic regression models binary outcomes
2. Derive the maximum likelihood estimation for logistic regression
3. Interpret classification metrics (precision, recall, AUC)
4. Apply logistic regression for credit scoring decisions

## PMSP Structure (Problem-Method-Solution-Practice)

### Problem Phase (15 min)

**Motivation**: Present credit scoring as motivating example.

**Key Questions to Ask**:
- Why can't we use linear regression for yes/no outcomes?
- What does a bank need: prediction or probability?
- Why do regulators require interpretable models?

**Discussion Points**:
- Cost of false positives vs false negatives in lending
- Basel regulations on model interpretability
- Real-world impact of credit decisions

### Method Phase (45 min)

**Core Concepts to Cover**:

1. **From Linear to Logistic**
   - Sigmoid function intuition
   - Odds and log-odds interpretation
   - Why cross-entropy, not MSE?

2. **Maximum Likelihood Estimation**
   - Likelihood function construction
   - Log-likelihood transformation
   - Gradient derivation

3. **Decision Boundaries**
   - Linear boundary in feature space
   - Threshold selection based on costs
   - Multiclass extension (softmax)

**Common Misconceptions**:
- "Logistic regression is for continuous outputs between 0 and 1" - it outputs probabilities
- "Higher accuracy always means better model" - explain class imbalance
- "Coefficients show feature importance" - need to standardize first

### Solution Phase (45 min)

**Implementation Walkthrough**:

1. **From Scratch (NumPy)**
   - Sigmoid function
   - Cross-entropy loss
   - Gradient descent loop

2. **Using Libraries (scikit-learn)**
   - LogisticRegression()
   - predict_proba() for probabilities
   - classification_report()

**Live Coding Tips**:
- Start with 2D data for visual decision boundary
- Show effect of regularization on boundary
- Demonstrate threshold tuning

### Practice Phase (75 min)

**Hands-on Notebook**:
- Students work through L02_logistic_regression.ipynb
- Focus on interpreting coefficients in credit context

**Exercise Difficulty Progression**:
1. Fit logistic regression on synthetic credit data (guided)
2. Evaluate model with confusion matrix, ROC curve (semi-guided)
3. Handle class imbalance with different techniques (open-ended)

## Decision Framework

### When to Use Logistic Regression

| Use When | Don't Use When |
|----------|----------------|
| Binary classification | Multi-class with >3 classes |
| Probability estimates needed | Complex non-linear patterns |
| Interpretability required | Very high-dimensional (use regularized) |
| Baseline model needed | Image/text data without features |

## Materials Checklist

- [ ] Slides: L02_overview.pdf
- [ ] Slides: L02_deepdive.pdf
- [ ] Notebook: L02_logistic_regression.ipynb
- [ ] Dataset: credit_synthetic.csv
- [ ] All 7 charts compiled

## Timing Guide

| Phase | Duration | Notes |
|-------|----------|-------|
| Problem | 15 min | Credit scoring motivation |
| Method | 45 min | Don't rush MLE derivation |
| Solution | 45 min | Live coding, threshold selection |
| **Break** | 15 min | |
| Practice | 60 min | Hands-on notebook work |
| Q&A | 15 min | Discuss vs. L01, preview KNN |

## Common Student Questions

**Q: Why not just round linear regression predictions to 0/1?**
A: Linear regression can predict values outside [0,1], and rounding loses the probability interpretation. Logistic regression is designed for classification with proper probability outputs.

**Q: How do I choose the threshold?**
A: Default is 0.5, but optimal threshold depends on costs. Plot precision-recall curve, find threshold that maximizes F1 or meets business constraint (e.g., max 5% FPR).

**Q: When should I use AUC vs F1?**
A: AUC is threshold-independent, good for model comparison. F1 is for a specific threshold, use when you need to pick one operating point.

## Assessment Connection

This topic is assessed in:
- **Quiz**: Quiz 1 (questions 8-15)
- **Presentations**: Topics 2, 3 (Logistic Regression in Healthcare, Feature Engineering)
- **Capstone**: Credit scoring projects

## Additional Resources

- ISLR Chapter 4: Classification
- scikit-learn Logistic Regression User Guide
- Interpretable ML Book: Logistic Regression chapter

## Post-Session Notes

*Space for instructor notes after delivering the session*

---

*Last updated: 2026-01-07*
