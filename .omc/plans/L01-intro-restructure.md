# Plan: L01 Linear Regression -- Intro Restructure

## Context

### Original Request
Restructure L01 (Introduction & Linear Regression) slides to:
1. Apply template_beamer_final.tex layout styles for visual variety
2. Add genuine INTRO section assuming zero pre-knowledge
3. Move advanced/proof content to Beamer `\appendix`
4. Scope: L01 only

### Current State
- `L01_overview.tex`: 487 lines, ~22 slides. PMSP structure. No intro section. Jumps straight to OLS derivation in learning objectives.
- `L01_deepdive.tex`: 969 lines, ~40+ slides. Heavy math: OLS derivation, Gauss-Markov proof, MLE, diagnostic tests, hat matrix, convergence theory -- all in main body.
- Template: 22 layouts available. Current slides use only 2-3 layout patterns (chart-only, two-column, bullet list).
- 8 charts available in subfolders (01-08). All generate chart.pdf.
- 3 XKCD images: 1725_linear_regression.png, 2048_curve_fitting.png, 605_extrapolating.png.

### Research Findings
- Preamble is identical in both files (lines 1-92). Must be preserved exactly (NOT copied from template).
- Template layouts are structural patterns, not importable macros. The executor must replicate the column/spacing patterns using standard Beamer commands.
- The `\appendix` command in Beamer resets slide numbering and excludes appendix slides from `\inserttotalframenumber`.
- Chart widths in current files range 0.42-0.55\textwidth. Plan standardizes to 0.50-0.55 (with text) and 0.65 (chart-only).

---

## Work Objectives

### Core Objective
Transform L01 from a single-pace "all core" deck into a two-tier structure: overview starts with genuine intro for beginners, deepdive separates details from advanced appendix content.

### Deliverables
1. **L01_overview.tex** -- Restructured: INTRO (8-10 slides) + CORE (12-14 slides) + PRACTICE/SUMMARY (4 slides)
2. **L01_deepdive.tex** -- Restructured: DETAILS (22 content slides + 3 title/outline/objectives = 25 main) + APPENDIX (9 slides after `\appendix`)

### Definition of Done
- Both files compile with `pdflatex -interaction=nonstopmode` without errors
- Zero Overfull hbox warnings (max 3-4 bullets per slide)
- All 8 chart references resolve correctly
- All 3 XKCD image references resolve correctly
- `\appendix` command present in deepdive, appendix slides excluded from total page count
- Template layouts used for visual variety (at least 6 distinct layout patterns across both files)
- Intro section is genuinely accessible (no formulas beyond y = a + bx in first 5 slides)

---

## Guardrails

### MUST Have
- Preamble copied exactly from current L01 files (lines 1-92), NOT from template_beamer_final.tex
- All 8 charts referenced somewhere across the two files
- All 3 XKCD images used where pedagogically appropriate
- `\bottomnote{}` on every content slide
- Chart widths: 0.50-0.55\textwidth with text, 0.65\textwidth chart-only
- Max 3-4 bullet items per slide
- `[t]` top alignment on all content frames
- `\appendix` Beamer command before appendix section in deepdive

### MUST NOT Have
- Formulas in the INTRO section beyond `y = a + bx` and basic residual concept
- Greek letters or matrix notation in INTRO
- Any content from template_beamer_final.tex preamble leaking in (no `\framebox`, no `[plain]` on content slides, no placeholder text)
- More than 4 bullet points on any slide
- Duplicate slides across overview and deepdive (each chart appears in ONE file only)

---

## Task Flow and Dependencies

```
Task 1 (L01_overview.tex) -----> Task 3 (Compile & Validate)
Task 2 (L01_deepdive.tex) ---/
```

Tasks 1 and 2 can run in parallel. Task 3 depends on both completing.

---

## Detailed TODOs

### Task 1: Rewrite L01_overview.tex

**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\L01_overview.tex`

**Acceptance Criteria:**
- 24-28 slides total (intro 8-10, core 12-14, practice/summary 4)
- Uses at least 5 distinct template layout patterns
- INTRO section genuinely accessible, no advanced formulas
- All overview charts (03, 04, 05, 06, 07, 08) referenced; charts 01/02 in deepdive only

**Slide-by-Slide Plan:**

#### Preamble (lines 1-98: KEEP EXACTLY AS-IS)

No changes to documentclass, packages, colors, footer, commands, title/subtitle/author/date.

#### SLIDE 1: Title Page
- **Layout:** Standard title (Layout 2 pattern -- `\titlepage`)
- **Content:** Keep exactly as-is
- **LaTeX:** `\begin{frame} \titlepage \end{frame}`

#### SLIDE 2: Outline
- **Layout:** Table of contents
- **Content:** `\tableofcontents` -- sections will auto-update
- **LaTeX:** Keep exactly as-is

---

#### SECTION: Introduction to Machine Learning
`\section{Introduction}`

#### SLIDE 3: What is Machine Learning?
- **Layout:** Layout 8 pattern (Mixed Media -- text left, image right)
- **Content LEFT column:**
  - "Teaching computers to learn from data, without being explicitly programmed"
  - Everyday examples: email spam filter, Netflix recommendations, voice assistants
  - Key idea: the computer finds patterns in data, then uses those patterns to make predictions on new data
- **Content RIGHT column:**
  - XKCD #1725 (linear regression humor): `images/1725_linear_regression.png` at 0.45\textwidth
- **Bottomnote:** "Machine learning is already part of your daily life -- now we learn how it works"
- **Notes:** No formulas. Pure intuition. The XKCD comic is a perfect visual hook here.

#### SLIDE 4: Supervised vs Unsupervised Learning
- **Layout:** Layout 10 pattern (Comparison -- two columns)
- **Content LEFT column:**
  - Header: "Supervised Learning"
  - We have the answers (labels) for training data
  - Goal: predict the answer for new data
  - Examples: predicting house prices, classifying emails
- **Content RIGHT column:**
  - Header: "Unsupervised Learning"
  - No answers -- just data
  - Goal: find hidden structure or groups
  - Examples: customer segments, anomaly detection
- **Bottomnote:** "This course covers both: L01-L04 supervised, L05 unsupervised"

#### SLIDE 5: What is Regression?
- **Layout:** Layout 7 pattern (Full width text -- NO chart; chart 01 is reserved for deepdive S8)
- **Content (text):**
  - "Predicting a number (not a category)"
  - Example: Predicting house price from its size in square meters
  - "We draw the best line through the data points"
  - "The line captures the relationship between input and output"
- **Content:** Text-only slide. No chart. The simple regression chart appears in the deepdive.
- **Bottomnote:** "Regression = predicting a continuous value. Classification = predicting a category."

#### SLIDE 6: The Simplest Model
- **Layout:** Layout 4 pattern (Two columns with math -- but SIMPLE math only)
- **Content LEFT column:**
  - Header: "The Idea"
  - Price goes up as size increases
  - We write this as: `y = a + b * x`
  - `y` = price (what we predict)
  - `x` = size (what we know)
  - `a` = starting price, `b` = price per sqm
- **Content RIGHT column:**
  - Header: "Example"
  - `Price = 50,000 + 200 * Size`
  - A 100 sqm apartment: 50,000 + 200*100 = 70,000
  - A 150 sqm apartment: 50,000 + 200*150 = 80,000
  - "Each extra square meter adds 200 to the price"
- **Bottomnote:** "This is the entire idea of linear regression -- the rest is details"

#### SLIDE 7: What Makes a Good Prediction?
- **Layout:** Layout 22 pattern (Chart with bottom explanations)
- **Content (chart):**
  - Chart 03: `03_residual_plots/chart.pdf` at 0.55\textwidth
- **Content (explanations below chart):**
  - "The red lines show prediction errors (residuals)"
  - "A good model has small, random errors"
  - "Patterns in errors = something the model missed"
- **Bottomnote:** "We want errors to be small and random -- not systematic"

#### SLIDE 8: How Does the Computer Learn?
- **Layout:** Layout 11 pattern (Step-by-step process -- two columns)
- **Content LEFT column:**
  - Header: "The Learning Process"
  - Step 1: Start with a random line
  - Step 2: Measure how wrong it is (errors)
  - Step 3: Adjust the line to reduce errors
- **Content RIGHT column:**
  - Step 4: Repeat until errors are small
  - Step 5: Use the final line to predict
  - "This process is called optimization"
- **Bottomnote:** "The computer tries thousands of lines and keeps the best one"

#### SLIDE 9: Key Vocabulary
- **Layout:** Layout 6 pattern (Three-way split -- three columns)
- **Content COLUMN 1:** "Data"
  - Features (inputs): size, bedrooms, age
  - Target (output): price
  - Observation: one data point (one house)
- **Content COLUMN 2:** "Learning"
  - Training: fitting the model to data
  - Coefficients: the numbers the model learns
  - Loss: how wrong the model is
- **Content COLUMN 3:** "Evaluation"
  - Prediction: model output for new data
  - Error: difference between prediction and truth
  - Overfitting: memorizing instead of learning
- **Bottomnote:** "Master these terms -- they appear in every ML method we study"

#### SLIDE 10: Road Map for Today
- **Layout:** Layout 7 pattern (Full width text + image placeholder area)
- **Content:**
  - "Now that you know the basics, we go deeper:"
  - 1. A real business problem (house prices for banks)
  - 2. The math behind finding the best line
  - 3. How to tell if our model is good
  - 4. How to prevent our model from being too complex
- **Bottomnote:** "Everything ahead builds on the intuition from this intro"

---

#### SECTION: Problem
`\section{Problem}`

#### SLIDE 11: The Business Problem
- **Layout:** Layout 3 pattern (Two columns text) -- adapted
- **Content:** Keep current content from existing slide (finance use case: house prices)
- **Adapted:** Same as current "The Business Problem" slide but trimmed to max 3 bullets per group
  - LEFT: Finance Use Case (banks need valuations, insurers assess risk, investors evaluate portfolios)
  - RIGHT: Why Linear Regression? (interpretable, fast, strong baseline)
- **Bottomnote:** "Linear regression: the 'hello world' of machine learning"

---

#### SECTION: Method
`\section{Method}`

#### SLIDE 12: Linear Regression Formula
- **Layout:** Layout 9 pattern (Definition-Example)
- **Content LEFT (Definition):**
  - The model: `y = beta_0 + beta_1*x_1 + ... + beta_p*x_p + epsilon`
  - y: target, x: features, beta: coefficients, epsilon: error
- **Content RIGHT (Example):**
  - Price = 50,000 + 200*Size + 15,000*Bedrooms - 1,000*Age
  - Interpretation bullets (same as current)
- **Bottomnote:** "Goal: Find coefficients that minimize prediction error"

#### SLIDE 13: The Optimization Problem (Simplified)
- **Layout:** Standard single-column with math
- **Content:**
  - Objective: minimize sum of squared errors
  - Formula: `min sum (y_i - y_hat_i)^2`
  - Why squared errors? (3 bullets: penalizes large errors, differentiable, closed-form)
- **Bottomnote:** "This defines 'ordinary least squares' (OLS)"

#### SLIDE 14: Normal Equation vs Gradient Descent
- **Layout:** Layout 10 pattern (Comparison -- two columns)
- **Content:** Keep current "Two Solution Approaches" slide EXACTLY (already uses this layout)
- **Bottomnote:** "Both methods yield the same solution for OLS"

#### SLIDE 15: Gradient Descent in Action
- **Layout:** Layout 21 pattern (Full-size chart)
- **Chart:** `04_gradient_descent/chart.pdf` at 0.65\textwidth (chart-only slide)
- **Bottomnote:** "Iteratively update parameters in the direction of steepest descent"

---

#### SECTION: Solution
`\section{Solution}`

#### SLIDE 16: Interpreting Coefficients
- **Layout:** Standard (keep current content, already good)
- **Content:** Same as current slide with house price example equation + 4 bullet interpretation
- **Bottomnote:** "Coefficients show marginal effect, holding others constant"

#### SLIDE 17: Model Evaluation -- R-squared and RMSE
- **Layout:** Standard with math (keep current)
- **Content:** Keep R^2 and RMSE formulas with brief interpretation
- **Bottomnote:** "Always evaluate on held-out test data"

#### SLIDE 18: Learning Curves
- **Layout:** Layout 22 pattern (Chart with bottom explanations)
- **Chart:** `05_learning_curves/chart.pdf` at 0.55\textwidth
- **Explanations below:**
  - "Gap between train and test = overfitting"
  - "Curves converging = more data won't help"
- **Bottomnote:** "Learning curves diagnose underfitting vs overfitting"

---

#### SECTION: Decision Framework
`\section{Decision Framework}`

#### SLIDE 19: When to Use Linear Regression
- **Layout:** Layout 18 pattern (Pros and Cons / Advantages-Disadvantages)
- **Content LEFT (Advantages):**
  - [+] Interpretable coefficients
  - [+] Fast training and prediction
  - [+] Well-understood theory
  - [+] Works as strong baseline
- **Content RIGHT (Disadvantages):**
  - [-] Assumes linear relationships
  - [-] Sensitive to outliers
  - [-] Limited flexibility
  - [-] Needs feature engineering for non-linear patterns
- **Bottomnote:** "When in doubt, start with linear regression as your baseline"

#### SLIDE 20: The Danger of Overfitting (XKCD)
- **Layout:** Layout 21 pattern (Full-size chart -- but with XKCD image)
- **Image:** `images/2048_curve_fitting.png` at 0.32\textwidth (keep small, as current)
- **Bottomnote:** "XKCD #2048 -- Simpler models often generalize better (CC BY-NC 2.5)"

#### SLIDE 21: Regularization Overview -- Ridge vs Lasso
- **Layout:** Layout 10 pattern (Comparison)
- **Content LEFT (Ridge / L2):**
  - Adds penalty on squared coefficients
  - Shrinks all coefficients toward zero
  - Never removes features entirely
- **Content RIGHT (Lasso / L1):**
  - Adds penalty on absolute coefficients
  - Can set coefficients exactly to zero
  - Automatic feature selection
- **Chart:** `06_regularization_comparison/chart.pdf` at 0.50\textwidth, placed below the columns
- **Bottomnote:** "Regularization prevents overfitting by penalizing large coefficients"

#### SLIDE 22: Bias-Variance Tradeoff
- **Layout:** Layout 22 pattern (Chart with bottom explanations)
- **Chart:** `07_bias_variance/chart.pdf` at 0.55\textwidth
- **Explanations below:**
  - "Bias: error from wrong assumptions (too simple)"
  - "Variance: error from sensitivity to training data (too complex)"
  - "Sweet spot: minimize total error"
- **Bottomnote:** "Model complexity controls the tradeoff between bias and variance"

---

#### SECTION: Practice
`\section{Practice}`

#### SLIDE 23: Hands-on Exercise
- **Layout:** Standard (keep current)
- **Content:** Exercises 1-3 (OLS from scratch, sklearn, gradient descent comparison)
- **Bottomnote:** (none currently, add) "Start with Exercise 2 if short on time"

#### SLIDE 24: A Word of Caution (XKCD Extrapolation)
- **Layout:** Layout 21 pattern (Full-size chart with XKCD)
- **Image:** `images/605_extrapolating.png` at 0.50\textwidth
- **Bottomnote:** "XKCD #605 by Randall Munroe (CC BY-NC 2.5) -- Extrapolation is dangerous!"

#### SLIDE 25: Decision Framework
- **Layout:** Layout 21 pattern (Full-size chart)
- **Chart:** `08_decision_flowchart/chart.pdf` at 0.55\textwidth
- **Bottomnote:** "Use this flowchart to decide when linear regression is appropriate"

---

#### SECTION: Summary
`\section{Summary}`

#### SLIDE 26: Key Takeaways
- **Layout:** Layout 13 pattern (Summary -- two columns)
- **Content LEFT (Key Concepts):**
  - Linear regression predicts continuous outcomes
  - OLS minimizes sum of squared errors
  - Solve via normal equation or gradient descent
- **Content RIGHT (Practical Guidance):**
  - Coefficients are directly interpretable
  - Evaluate with R-squared and RMSE on test data
  - Use regularization to prevent overfitting
- **Below:** Next: Deep dive into mathematics and implementation
- **References:** ISLR Ch.3, ESL Ch.3
- **Bottomnote:** "Foundation for all supervised learning methods"

**Total Overview Slides: 26** (title+outline: 2, intro: 8, core: 12, practice: 3, summary: 1 = 26)

---

### Task 2: Rewrite L01_deepdive.tex

**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\L01_deepdive.tex`

**Acceptance Criteria:**
- MAIN body: 25 slides (3 title/outline/objectives + 22 content slides)
- APPENDIX section: 9 slides (advanced proofs and specialized topics)
- `\appendix` Beamer command separating the two sections
- Charts 01, 02 referenced (these are the deepdive's charts; overview uses 03-08)
- Uses at least 4 distinct template layout patterns

**Slide-by-Slide Plan:**

#### Preamble (lines 1-98: KEEP EXACTLY AS-IS)

No changes.

#### SLIDE 1: Title Page
- **Layout:** Standard title (`\titlepage`)
- **Content:** Keep as-is

#### SLIDE 2: Outline
- **Layout:** Table of contents
- **Content:** `\tableofcontents`

#### SLIDE 3: Learning Objectives
- **Layout:** Standard
- **Content:** Keep current 4 learning objectives (derive OLS, analyze GD, evaluate diagnostics, compare regularization)
- **Bottomnote:** "Foundation for all supervised learning methods"

---

#### SECTION: Mathematical Foundations
`\section{Mathematical Foundations}`

#### SLIDE 4: Matrix Notation
- **Layout:** Layout 9 pattern (Definition-Example)
- **Content LEFT (Definition):**
  - y = X*beta + epsilon
  - y in R^n, X in R^{n x (p+1)}, beta in R^{p+1}, epsilon in R^n
- **Content RIGHT (Design Matrix):**
  - Show design matrix structure (ones column + features)
  - n observations, p features, p+1 parameters
- **Bottomnote:** "Matrix notation enables elegant derivations and efficient computation"
- **Note:** Merges current slides "Matrix Notation" + "Design Matrix Structure" into one

#### SLIDE 5: OLS Assumptions
- **Layout:** Standard enumerated list
- **Content:** Keep current 5 assumptions (linearity, exogeneity, homoscedasticity, full rank, normality)
- **Trim:** Max 1 line per assumption. Remove "Violations?" paragraph (save for later).
- **Bottomnote:** "Assumptions 1-4 for unbiased estimates; 5 for t-tests and CIs"

#### SLIDE 6: The Loss Function
- **Layout:** Standard with math
- **Content:** SSR formula in matrix form + expanded form. Keep as-is from current.
- **Bottomnote:** "Quadratic in beta -- has unique minimum if X is full rank"

#### SLIDE 7: Deriving the Normal Equation
- **Layout:** Standard with math
- **Content:** Derivative, set to zero, solve. Keep as-is from current.
- **Bottomnote:** "This is the closed-form OLS solution"

#### SLIDE 8: Simple Regression Visualization
- **Layout:** Layout 21 pattern (Full-size chart)
- **Chart:** `01_simple_regression/chart.pdf` at 0.65\textwidth
- **Bottomnote:** "The fitted line minimizes vertical distances squared"

#### SLIDE 9: Multiple Regression Surface
- **Layout:** Layout 21 pattern (Full-size chart)
- **Chart:** `02_multiple_regression_3d/chart.pdf` at 0.65\textwidth
- **Bottomnote:** "With 2 features, we fit a plane; with p features, a hyperplane"

---

#### SECTION: Optimization
`\section{Optimization}`

#### SLIDE 10: Why Gradient Descent?
- **Layout:** Layout 10 pattern (Comparison)
- **Content LEFT (Normal Equation):**
  - O(p^3) computation
  - Stores p x p matrix
  - Exact but slow for large p
- **Content RIGHT (Gradient Descent):**
  - Memory efficient (one sample at a time)
  - Scales to big data (SGD)
  - Generalizes to non-linear models
- **Bottomnote:** "For p > 10,000, gradient descent usually faster"

#### SLIDE 11: The Gradient + Update Rule
- **Layout:** Layout 4 pattern (Two columns with math)
- **Content LEFT:**
  - Gradient formula: nabla L = -2X^T(y - X*beta)
  - Intuition: gradient points uphill, we go downhill
- **Content RIGHT:**
  - Update rule: beta_{t+1} = beta_t - alpha * nabla L
  - Algorithm steps (init, compute, update, repeat)
- **Bottomnote:** "Convergence: ||beta_{t+1} - beta_t|| < epsilon or max iterations"

#### SLIDE 12: Learning Rate and SGD
- **Layout:** Layout 3 pattern (Two columns text)
- **Content LEFT (Learning Rate):**
  - Too small: slow convergence
  - Too large: divergence
  - Practical: start with 0.01, use adaptive methods
- **Content RIGHT (Mini-Batch SGD):**
  - m=1: stochastic (noisy, fast)
  - m=n: batch (stable, slow)
  - m in [32,256]: mini-batch (good tradeoff)
- **Bottomnote:** "SGD is how we train all modern ML models, not just linear regression"

#### SLIDE 13: Feature Scaling
- **Layout:** Standard with math
- **Content:** Standardization formula, 3 reasons (coefficient comparison, GD convergence, regularization fairness)
- **Bottomnote:** "Always standardize for regularization; optional for OLS if only predicting"

---

#### SECTION: Evaluation and Inference
`\section{Evaluation and Inference}`

#### SLIDE 14: R-squared and Adjusted R-squared
- **Layout:** Layout 4 pattern (Two columns with math)
- **Content LEFT (R^2):**
  - Formula, interpretation (proportion of variance explained)
  - Problem: always increases with more features
- **Content RIGHT (Adjusted R^2):**
  - Formula with n-1, n-p-1 correction
  - Can decrease with irrelevant features
  - Better for model comparison
- **Bottomnote:** "Use adjusted R-squared when comparing models with different numbers of features"
- **Note:** Merges current R^2 + Adjusted R^2 slides into one

#### SLIDE 15: RMSE and MAE
- **Layout:** Standard with math
- **Content:** Both formulas + comparison (RMSE penalizes large errors, MAE more robust, both in original units)
- **Bottomnote:** "Report both for comprehensive evaluation"

#### SLIDE 16: Hypothesis Testing and Confidence Intervals
- **Layout:** Layout 4 pattern (Two columns with math)
- **Content LEFT (t-test):**
  - SE formula, t-statistic, decision rule (p < 0.05)
- **Content RIGHT (Confidence Intervals):**
  - 95% CI formula
  - Interpretation: repeated sampling
  - Prediction vs confidence interval distinction
- **Bottomnote:** "Always check significance before interpreting coefficients"
- **Note:** Merges current "Standard Errors" + "Hypothesis Testing" + "Confidence Intervals" into one dense slide

#### SLIDE 17: F-Test for Overall Significance
- **Layout:** Standard with math
- **Content:** F-statistic formula, null hypothesis, complements individual t-tests. Keep current but trim to 3 bullets.
- **Bottomnote:** "Check the F-statistic before interpreting individual coefficients"

---

#### SECTION: Regularization and Model Selection
`\section{Regularization and Model Selection}`

#### SLIDE 18: The Overfitting Problem
- **Layout:** Standard
- **Content:** High-dimensional data, large coefficients, solution: add penalty. Keep current.
- **Bottomnote:** "Lambda controls strength of regularization"

#### SLIDE 19: Ridge, Lasso, and Elastic Net
- **Layout:** Layout 6 pattern (Three-way split)
- **Content COLUMN 1 (Ridge/L2):**
  - Formula, closed-form, shrinks all toward zero
- **Content COLUMN 2 (Lasso/L1):**
  - Formula, no closed form, sparse solutions
- **Content COLUMN 3 (Elastic Net):**
  - Formula, mixing parameter alpha, best of both worlds
- **Bottomnote:** "Ridge for many small effects, Lasso for feature selection, Elastic Net for correlated features"
- **Note:** Merges current Ridge + Lasso + Elastic Net into one comparison slide

#### SLIDE 20: Choosing Lambda
- **Layout:** Layout 11 pattern (Step-by-step process)
- **Content:** 4-step CV process (define grid, K-fold CV, select best lambda, refit)
- **sklearn references:** RidgeCV, LassoCV
- **Bottomnote:** "Larger lambda = more regularization = simpler model"

#### SLIDE 21: Bias-Variance Decomposition
- **Layout:** Standard with math
- **Content:** E[(y - f_hat)^2] = Bias^2 + Var + sigma^2, three bullet definitions
- **Bottomnote:** "We cannot reduce irreducible error -- focus on bias and variance"

#### SLIDE 22: VIF and Multicollinearity
- **Layout:** Layout 9 pattern (Definition-Example)
- **Content LEFT (VIF Definition):**
  - Formula, interpretation thresholds (1, >5, >10)
- **Content RIGHT (Remedies):**
  - Remove correlated features
  - Use Ridge regression
  - Apply PCA before regression
- **Bottomnote:** "Always check VIF before trusting coefficient estimates"

---

#### SECTION: Generalization
`\section{Generalization}`

#### SLIDE 23: Train-Test Split and Cross-Validation
- **Layout:** Layout 10 pattern (Comparison)
- **Content LEFT (Simple Split):**
  - 70-80% train, 20-30% test
  - Report test metrics
  - Fast but high variance
- **Content RIGHT (K-Fold CV):**
  - K folds (typically 5 or 10)
  - Train on K-1, validate on 1
  - More reliable with limited data
- **Bottomnote:** "Always evaluate on data the model has never seen"

---

#### SECTION: Summary
`\section{Summary}`

#### SLIDE 24: Key Equations Summary
- **Layout:** Layout 12 pattern (Formula Reference -- three columns)
- **Content:** Current equations summary reformatted into three columns:
  - Column 1 (Model): y=Xbeta+epsilon, OLS solution
  - Column 2 (Optimization): gradient, GD update
  - Column 3 (Regularization): Ridge solution, R^2
- **Bottomnote:** "Keep this slide as a reference sheet"

#### SLIDE 25: Key Takeaways
- **Layout:** Standard
- **Content:** 5 takeaways (keep current), next session pointer, references
- **Bottomnote:** "Foundation for all supervised learning -- next: Logistic Regression"

---

#### `\appendix`

**Insert Beamer `\appendix` command here. All slides below will NOT count in total page numbering.**

#### SECTION: Advanced Topics (Appendix)
`\section*{Advanced Topics}` -- Use starred form so it does NOT appear in `\tableofcontents` on Slide 2

#### APPENDIX SLIDE 1: Appendix Title
- **Layout:** Section divider (centered beamercolorbox, like template section dividers)
- **Content:** "Appendix: Advanced Topics and Proofs"
- **Subtitle:** "These slides are supplementary material for self-study"

#### APPENDIX SLIDE 2: The CAPM -- Linear Regression in Finance
- **Layout:** Standard with math
- **Content:** CAPM equation, variable definitions, beta interpretation. Keep current deepdive slide.
- **Bottomnote:** "CAPM: The original factor model -- basis for portfolio management"

#### APPENDIX SLIDE 3: The Gauss-Markov Theorem
- **Layout:** Standard
- **Content:** Theorem statement (BLUE), what BLUE means (3 bullets). Keep current but trim.
- **Bottomnote:** "Gauss-Markov justifies why OLS is the default for linear regression"

#### APPENDIX SLIDE 4: Gauss-Markov Proof Sketch
- **Layout:** Standard with math
- **Content:** Proof sketch with C = (X'X)^{-1}X' + D, unbiasedness forces DX=0, variance comparison. Keep current.
- **Bottomnote:** "Any deviation from OLS adds noise without reducing bias"

#### APPENDIX SLIDE 5: OLS and Maximum Likelihood
- **Layout:** Standard with math
- **Content:** Likelihood function, log-likelihood, OLS = MLE connection, sigma^2_MLE bias. Keep current.
- **Bottomnote:** "OLS = MLE under normality -- bridges to Logistic Regression (L02)"

#### APPENDIX SLIDE 6: Formal Diagnostic Tests
- **Layout:** Standard with table
- **Content:** Breusch-Pagan, White, Durbin-Watson, Shapiro-Wilk, Jarque-Bera, Ramsey RESET table. Keep current.
- **Content below table:** 3 remedies (robust SE, Newey-West, bootstrap). Keep current.
- **Bottomnote:** "Regulators require formal test results -- 'residuals looked fine' is insufficient"

#### APPENDIX SLIDE 7: Hat Matrix and Cook's Distance
- **Layout:** Standard with math
- **Content:** Hat matrix definition, leverage, Cook's distance formula, interpretation. Keep current.
- **Bottomnote:** "Investigate points with D_i > 4/n or leverage h_ii > 2(p+1)/n"

#### APPENDIX SLIDE 8: Convergence Theory
- **Layout:** Standard with math
- **Content:** Convergence rates (convex O(1/t), strongly convex O(rho^t)), learning rate condition, optimal eta formula
- **Source:** Extracted from current "Learning Rate Selection" slide's advanced content
- **Bottomnote:** "For OLS, optimal eta = 1/lambda_max(X^T X)"

#### APPENDIX SLIDE 9: References
- **Layout:** Layout 20 pattern (References -- two columns)
- **Content:** Keep current references (ISLR, ESL, Bishop) + online resources (sklearn, CS229)
- **Bottomnote:** (none, or "Curated resources for further study")

**Total Deepdive Slides: 25 main + 9 appendix = 34** (main section page count: 25)

---

### Task 3: Compile and Validate

**Depends on:** Tasks 1 and 2

**Steps:**
1. Compile both files:
   ```
   cd D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression
   pdflatex -interaction=nonstopmode L01_overview.tex
   pdflatex -interaction=nonstopmode L01_deepdive.tex
   ```
2. Check for errors in log output
3. Check for Overfull hbox warnings:
   ```
   grep -i "overfull" L01_overview.log
   grep -i "overfull" L01_deepdive.log
   ```
4. Verify all chart/image references resolved (no missing file warnings)
5. Run course validator:
   ```
   cd D:\Joerg\Research\slides\Methods_and_Algorithms
   python infrastructure/course_cli.py validate latex --strict
   ```

**Acceptance Criteria:**
- Both files compile without errors
- Zero Overfull hbox warnings
- All image/chart references resolved
- Validator passes with `--strict`

---

## Chart Allocation Across Files

| Chart | File | Slide | Layout |
|-------|------|-------|--------|
| 01_simple_regression | deepdive | Slide 8 | Layout 21 (full-size) |
| 02_multiple_regression_3d | deepdive | Slide 9 | Layout 21 (full-size) |
| 03_residual_plots | overview | Slide 7 (INTRO) | Layout 22 (chart + explanations) |
| 04_gradient_descent | overview | Slide 15 | Layout 21 (full-size) |
| 05_learning_curves | overview | Slide 18 | Layout 22 (chart + explanations) |
| 06_regularization_comparison | overview | Slide 21 | Layout 10 + chart below |
| 07_bias_variance | overview | Slide 22 | Layout 22 (chart + explanations) |
| 08_decision_flowchart | overview | Slide 25 | Layout 21 (full-size) |

All 8 charts are referenced exactly once. No duplicates.

## XKCD Image Allocation

| Image | File | Slide | Purpose |
|-------|------|-------|---------|
| 1725_linear_regression.png | overview | Slide 3 (INTRO) | Visual hook for "What is ML?" |
| 2048_curve_fitting.png | overview | Slide 20 | Overfitting warning |
| 605_extrapolating.png | overview | Slide 24 | Extrapolation caution |

All 3 XKCD images in overview. Deepdive is pure math (no humor slides).

## Template Layout Usage Summary

| Layout Pattern | Times Used | Where |
|----------------|-----------|-------|
| Layout 3 (Two columns text) | 2 | overview S11, deepdive S12 |
| Layout 4 (Two columns math) | 3 | overview S6, deepdive S11/S14/S16 |
| Layout 6 (Three-way split) | 2 | overview S9, deepdive S19 |
| Layout 7 (Full width text) | 2 | overview S5 (text-only), S10 |
| Layout 8 (Mixed media) | 1 | overview S3 |
| Layout 9 (Definition-example) | 3 | overview S12, deepdive S4/S22 |
| Layout 10 (Comparison) | 5 | overview S4/S14/S21, deepdive S10/S23 |
| Layout 11 (Step-by-step) | 2 | overview S8, deepdive S20 |
| Layout 12 (Formula reference) | 1 | deepdive S24 |
| Layout 13 (Summary) | 1 | overview S26 |
| Layout 18 (Pros/Cons) | 1 | overview S19 |
| Layout 20 (References) | 1 | deepdive appendix S9 |
| Layout 21 (Full-size chart) | 6 | overview S15/S20/S24/S25, deepdive S8/S9 |
| Layout 22 (Chart + explanations) | 3 | overview S7/S18/S22 |

14 distinct layout patterns used across both files. Significant visual variety vs current (which uses ~3 patterns).

## Deliberately Dropped Content

The following current slides are intentionally removed (content is subsumed or redundant):

| Dropped Slide | From | Reason |
|---|---|---|
| "Regularization and Bias-Variance" (deepdive lines 819-836) | deepdive | Subsumed by deepdive S21 (Bias-Variance Decomposition) + overview S22 (chart) |
| "Linear Regression: When and Why" (deepdive lines 867-892) | deepdive | Redundant with overview S19 (When to Use LR, pros/cons) |
| "Business Challenge" (deepdive ~line 130) | deepdive | Redundant with overview S11 (The Business Problem) |
| "Hands-on Exercise" (deepdive) | deepdive | Identical to overview S23 -- no need for duplicate |

## Implementation Notes

- **Feature Scaling** moved from before gradient descent (current) to after (deepdive S13). Rationale: GD motivation and update rule should come first; scaling is a practical consideration applied after understanding the algorithm.
- **Deepdive S16** merges 3 current slides (Standard Errors, Hypothesis Testing, CIs) into 1 two-column slide. This is the highest overflow risk. Executor should use compact formatting and may need to split into 2 slides if overflow occurs.
- **Overview S21** (Ridge vs Lasso + chart below columns) is also a moderate overflow risk. Two columns of 3 bullets each + chart at 0.50\textwidth + bottomnote on a single frame. Executor should test and may reduce to 2 bullets per column or shrink chart.
- **Deepdive has only 2 charts** (01, 02) in the main body. This is intentional -- the deepdive is math-focused. All visualization is in the overview.

---

## Commit Strategy

Single commit after both files pass validation:
```
Restructure L01 slides: add intro section, use template layouts, move advanced content to appendix
```

---

## Success Criteria

1. [ ] L01_overview.tex has INTRO section (8+ slides, no advanced math)
2. [ ] L01_overview.tex has CORE section (10+ slides with formulas)
3. [ ] L01_deepdive.tex has DETAILS section (15+ slides)
4. [ ] L01_deepdive.tex has APPENDIX after `\appendix` command (8+ slides)
5. [ ] All 8 charts referenced exactly once across both files
6. [ ] All 3 XKCD images used
7. [ ] 10+ distinct template layout patterns used
8. [ ] Both files compile without errors
9. [ ] Zero Overfull hbox warnings
10. [ ] Intro slides use no formulas beyond y = a + bx
