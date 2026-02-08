<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-25 | Updated: 2026-02-07 -->

# L01_Introduction_Linear_Regression/

**Parent**: [../AGENTS.md](../AGENTS.md) (slides/)

## Purpose

Lesson 1 introduces linear regression with house price prediction as the motivating finance case. Students learn OLS estimation, gradient descent, regularization techniques, and the bias-variance tradeoff.

## Finance Case

**Problem**: Banks need accurate property valuations for mortgage lending. Linear regression provides interpretable coefficients (e.g., "$2000 per sqm") that regulators and underwriters can understand.

**Key Decision**: When to use linear regression vs tree-based models for valuation.

## Learning Objectives

1. **Understand**: Derive the OLS estimator mathematically using matrix calculus
2. **Apply**: Implement gradient descent from scratch (NumPy)
3. **Analyze**: Interpret regression coefficients in business context (e.g., "Each additional sqm adds $2000 to price")
4. **Evaluate**: Choose between Ridge and Lasso regularization based on feature count

## Files

| File | Purpose | Slides |
|------|---------|--------|
| `L01_overview.tex` | Overview slides with 7 charts | ~17 |
| `L01_overview.pdf` | Compiled overview slides | - |
| `L01_deepdive.tex` | Deep dive with mathematical derivations | ~45 frames |
| `L01_deepdive.pdf` | Compiled deep dive slides | - |
| `L01_instructor_guide.md` | Teaching guide with PMSP breakdown | - |

## Charts

All charts follow the naming convention `XX_descriptive_name/` and output `chart.pdf`:

| Chart | Directory | Description | Key Visual |
|-------|-----------|-------------|------------|
| 01 | `01_simple_regression/` | Scatter plot with fitted line | House price vs size with OLS line |
| 02 | `02_multiple_regression_3d/` | 3D surface plot | Price vs (size, location) |
| 03 | `03_residual_plots/` | Residual diagnostics | Residuals vs fitted values |
| 04 | `04_gradient_descent/` | Optimization trajectory | Contour plot with descent path |
| 05 | `05_learning_curves/` | Training vs validation curves | Detect overfitting/underfitting |
| 06 | `06_regularization_comparison/` | Ridge vs Lasso coefficients | Coefficient paths as lambda varies |
| 07 | `07_bias_variance/` | Bias-variance decomposition | Model complexity vs error |
| 08 | `08_decision_flowchart/` | When to use linear regression | Flowchart for algorithm selection |

## Chart Technical Details

**Standard settings** (defined in each chart.py):
```python
plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150
})
```

**Color palette**:
- MLPurple: #3333B2 (primary structure color)
- MLBlue: #0066CC (data points)
- MLOrange: #FF7F0E (fitted lines, highlights)
- MLGreen: #2CA02C (positive indicators)
- MLRed: #D62728 (errors, warnings)

## Building Charts

```bash
# Build all charts for L01 (from project root)
python infrastructure/course_cli.py build charts --topic L01

# Build single chart manually
cd slides/L01_Introduction_Linear_Regression/01_simple_regression
python chart.py

# Verify all charts generated
python infrastructure/course_cli.py validate charts --topic L01
```

## LaTeX Compilation

```bash
# Compile overview slides (from L01 directory)
cd slides/L01_Introduction_Linear_Regression
pdflatex -interaction=nonstopmode L01_overview.tex

# Compile deep dive slides
pdflatex -interaction=nonstopmode L01_deepdive.tex

# Clean auxiliary files
mkdir temp 2>nul & move *.aux *.log *.nav *.out *.snm *.toc temp/

# Build via CLI (from project root)
python infrastructure/course_cli.py build slides --topic L01
```

## PMSP Structure

The instructor guide breaks down the 3-hour session:

| Phase | Duration | Content |
|-------|----------|---------|
| **Problem** | 15 min | House price prediction motivation, why interpretability matters |
| **Method** | 45 min | OLS derivation, gradient descent, regularization theory |
| **Solution** | 45 min | NumPy implementation, scikit-learn comparison, live coding |
| **Practice** | 75 min | Jupyter notebook `L01_linear_regression.ipynb` with exercises |

## Key Concepts

- **OLS Assumptions**: Linearity, exogeneity, homoscedasticity, no multicollinearity
- **Gradient Descent**: Learning rate selection, convergence criteria, convergence rates (linear, superlinear, quadratic)
- **Regularization**: Ridge (L2) shrinks all coefficients, Lasso (L1) performs feature selection, Elastic Net combines both
- **Bias-Variance Tradeoff**: Underfitting (high bias) vs overfitting (high variance)
- **Statistical Inference**: Gauss-Markov theorem, OLS-MLE connection, F-test, confidence intervals
- **Diagnostics**: Breusch-Pagan (heteroscedasticity), Durbin-Watson (autocorrelation), Shapiro-Wilk (normality), Jarque-Bera, Cook's distance, hat matrix

## Common Pitfalls

1. **Overfull LaTeX warnings**: Keep bullet points to 3-4 per slide
2. **Chart font sizes**: Must be readable at Beamer 70% scale
3. **Residual plots**: Always check for heteroscedasticity before claiming OLS valid
4. **Regularization**: Standardize features before applying Ridge/Lasso

## Testing Checklist

- [ ] All 8 chart.py scripts generate chart.pdf
- [ ] L01_overview.tex compiles without errors
- [ ] L01_deepdive.tex compiles without errors
- [ ] ZERO "Overfull \hbox" warnings in LaTeX output
- [ ] All charts render correctly in PDFs
- [ ] Chart fonts are legible when included at 0.55\textwidth

## Related Assets

- **Notebook**: `notebooks/L01_linear_regression.ipynb`
- **Dataset**: `datasets/housing_synthetic.csv` (50 rows, features: size, location, age)
- **Quiz**: `quizzes/quiz1_topics_1_2.xml` (covers L01 + L02)
- **Template**: `templates/beamer_template.tex`, `templates/chart_template.py`

## Prerequisites

Students should know:
- Python basics (NumPy array operations)
- Statistics (mean, variance, correlation)
- Linear algebra (matrix multiplication, inversion)
- Calculus (partial derivatives for gradient descent)

## For AI Agents (Feb 2026 Hostile Review Remediation)

**Major additions completed in Feb 2026**:
- **Learning Objectives**: Rewritten to Bloom's Level 4-5 (Derive, Analyze, Evaluate, Compare)
- **Statistical Inference**: Added Gauss-Markov proof sketch, F-test for model significance, OLS-MLE connection under normality
- **Formal Diagnostics**: Breusch-Pagan test (heteroscedasticity), Durbin-Watson (autocorrelation), Shapiro-Wilk (normality), Jarque-Bera test, hat matrix, Cook's distance
- **Elastic Net**: Now uses standard Zou & Hastie (2005) form with alpha/lambda notation
- **Convergence Rates**: GD convergence rates added (linear for constant step size, superlinear/quadratic for Newton-Raphson)
- **Mathematical Rigor**: Overview has 7 equation environments + 14 inline math expressions. Deepdive: ~45 frames covering OLS derivation, inference theory, regularization paths, and diagnostic tests.

**Key files updated**: L01_overview.tex, L01_deepdive.tex, L01_instructor_guide.md, L01_overview.pdf, L01_deepdive.pdf

**Chart subdirectories**: 01_simple_regression/, 02_multiple_regression_3d/, 03_residual_plots/, 04_gradient_descent/, 05_learning_curves/, 06_regularization_comparison/, 07_bias_variance/, 08_decision_flowchart/, images/

## Next Lesson

→ [L02_Logistic_Regression/AGENTS.md](../L02_Logistic_Regression/AGENTS.md) - Binary classification with credit scoring
