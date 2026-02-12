# Instructor Guide: L01 - Introduction & Linear Regression

## Session Overview

| Aspect | Details |
|--------|---------|
| **Duration** | 3 hours |
| **Topic** | Introduction & Linear Regression |
| **Finance Case** | House price prediction, factor models |
| **Prerequisites** | Python, Statistics, Linear Algebra |

## Learning Objectives

By the end of this session, students will be able to:

1. Derive the OLS estimator using matrix calculus
2. Implement gradient descent for linear regression
3. Interpret regression coefficients in business contexts

## PMSP Structure (Problem-Method-Solution-Practice)

### Problem Phase (15 min)

**Motivation**: Present house price prediction as motivating example.

**Key Questions to Ask**:
- Why do banks need accurate property valuations?
- What makes this problem suitable for linear regression?
- Why is interpretability important for mortgage decisions?

**Discussion Points**:
- Connect to students' understanding of mortgages and real estate
- Highlight that coefficients have direct business interpretation

### Method Phase (45 min)

**Core Concepts to Cover**:

1. **Mathematical Foundation**
   - Matrix notation: y = Xb + e
   - Design matrix structure
   - OLS assumptions (linearity, exogeneity, homoscedasticity)

2. **Algorithm Steps**
   - Normal equation derivation
   - Gradient descent as alternative
   - Learning rate selection

3. **Assumptions & Limitations**
   - When linearity assumption fails
   - Multicollinearity issues

**Common Misconceptions**:
- "R-squared always increases means model improves" - explain adjusted R2
- "Large coefficients mean important features" - need to standardize

### Solution Phase (45 min)

**Implementation Walkthrough**:

1. **From Scratch (NumPy)**
   - Normal equation: beta = (X'X)^-1 X'y
   - Gradient descent loop

2. **Using Libraries (scikit-learn)**
   - LinearRegression()
   - Ridge(), Lasso() for regularization

**Live Coding Tips**:
- Start with 1D case (simple regression)
- Show residual plot to check assumptions
- Demonstrate overfitting with polynomial features

### Practice Phase (75 min)

**Hands-on Notebook**:
- Students work through L01_linear_regression.ipynb
- Circulate to help with NumPy operations

**Exercise Difficulty Progression**:
1. Fit simple linear regression (guided)
2. Implement gradient descent (semi-guided)
3. Compare Ridge vs Lasso on housing data (open-ended)

## Decision Framework

### When to Use Linear Regression

| Use When | Don't Use When |
|----------|----------------|
| Continuous target variable | Target is categorical |
| Linear relationships expected | Strong non-linear patterns |
| Interpretability required | Pure prediction accuracy goal |

## Materials Checklist

- [ ] Slides: L01_overview.pdf
- [ ] Slides: L01_deepdive.pdf
- [ ] Notebook: L01_linear_regression.ipynb
- [ ] Dataset: housing_synthetic.csv
- [ ] All 8 charts compiled

## Timing Guide

| Phase | Duration | Notes |
|-------|----------|-------|
| Problem | 15 min | Keep engaging, connect to finance |
| Method | 45 min | Don't rush matrix derivation |
| Solution | 45 min | Live coding, encourage questions |
| **Break** | 15 min | |
| Practice | 60 min | Hands-on notebook work |
| Q&A | 15 min | Wrap-up, preview logistic regression |

## Common Student Questions

**Q: When should I use the normal equation vs gradient descent?**
A: Normal equation for small-medium data (n, p < 10000). Gradient descent for larger datasets or when memory is limited.

**Q: How do I choose between Ridge and Lasso?**
A: Lasso for feature selection (sparse models). Ridge when all features likely relevant. Use cross-validation to select lambda.

**Q: Why do we need to standardize features for gradient descent?**
A: Features with different scales cause gradient descent to oscillate. Standardization ensures all features contribute equally to the learning process.

**Q: What does a negative coefficient mean?**
A: A negative coefficient indicates an inverse relationship - as the feature increases, the target decreases (e.g., age of house reducing price).

**Q: How do I know if my model is overfitting?**
A: Compare training and validation errors. Large gap = overfitting. Use learning curves and cross-validation to diagnose.

## Assessment Connection

This topic is assessed in:
- **Quiz**: Quiz 1 (questions 1-7)
- **Presentations**: Topics 1-3 (Ridge vs Lasso, Feature Engineering)
- **Capstone**: Foundation for all regression-based projects

## Additional Resources

- ISLR Chapter 3: Linear Regression
- ESL Chapter 3: Linear Methods for Regression
- 3Blue1Brown: Linear Algebra series

## Slide Build Specification

### Required Content
- Intro key formula: `y = a + bx` (then switch to beta notation)
- Must-have derivations: OLS normal equation, gradient descent gradient computation
- Must-have inference: t-test for coefficients, F-test for model

### Chart Requirements
- Regression surfaces (deepdive)
- QQ-plot (deepdive)
- Confidence bands (deepdive)
- CV error curve (deepdive)

### Domain Applications
- House price valuation for banks (worked numerical example)
- CAPM beta estimation

### Appendix Content
- Gauss-Markov proof
- MLE connection
- Convergence theory

## Post-Session Notes

*Space for instructor notes after delivering the session*

---

*Last updated: 2026-01-20*
