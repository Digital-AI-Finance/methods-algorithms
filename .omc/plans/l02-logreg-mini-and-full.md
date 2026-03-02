# Plan: L02 Logistic Regression -- Mini-Lecture + Full-Length Lecture + GH Pages

## Context

### Original Request
Create two standalone Logistic Regression lectures for the Methods and Algorithms MSc course:
1. A 10-slide mini-lecture (`L02_logreg_mini.tex`) following the interleaved arc WHY-FEEL-WHAT-CASE-HOW-RISK-WHERE-IMPACT-SO WHAT-ACT
2. A full-length technical lecture (`L02_logreg_full.tex`) with ~30 slides, expanded arc, external Python charts, worked examples, MSc-level mathematical depth
3. GitHub Pages integration: add both PDFs as downloadable cards in `docs/index.html` under the L02 section

### Research Findings

**Existing Assets (verified)**:
- 7 chart PDFs in `slides/L02_Logistic_Regression/01_sigmoid_function/` through `07_decision_flowchart/`
- 1 XKCD image: `images/1132_frequentist_bayesian.png` (Frequentist vs. Bayesian)
- Existing `L02_deepdive.tex` (41 main slides + 8 appendix = 49 frames) -- rich content source
- Existing `L02_overview.tex` -- overview-level source
- Instructor guide at `L02_instructor_guide.md` with PMSP structure

**Template Reference (verified)**:
- Preamble: lines 1-99 of `slides/L03_KNN_KMeans/L03_knn_mini.tex` (exact copy, change title only)
- Structural model: `L03_kmeans_mini.tex` (full 10-slide arc with TikZ comics, comparison table, step diagram, stakeholder map, balance scale, activity frame)
- Structural model for full lecture: `L02_deepdive.tex` (section structure, chart usage, mathematical depth)

**GH Pages Layout (verified)**:
- L02 section at `docs/index.html` lines 163-184
- Current cards: Overview PDF, Deep Dive PDF, Colab Notebook, Dataset, 7 chart thumbnails
- Pattern: `<a class="ccard" href="..." download>` with icon + label

---

## Work Objectives

### Core Objective
Produce two self-contained, compilable Beamer `.tex` files and update the GitHub Pages site, all consistent with the existing L03 mini-lecture template and the course design system.

### Deliverables

| # | File | Description | Frame Count |
|---|------|-------------|-------------|
| 1 | `slides/L02_Logistic_Regression/L02_logreg_mini.tex` | 10-slide mini-lecture, self-contained, inline TikZ/pgfplots, one external chart on slide 7 | 10 |
| 2 | `slides/L02_Logistic_Regression/L02_logreg_full.tex` | Full-length technical lecture, self-contained preamble, external charts via `\includegraphics` | 31 |
| 3 | `docs/index.html` | Add two new PDF download cards under L02 section | N/A |

### Definition of Done
- [ ] Both `.tex` files compile with `pdflatex` with zero Overfull hbox/vbox warnings
- [ ] Mini-lecture produces exactly 10 frames (no title page)
- [ ] Full lecture produces 31 frames (with title page)
- [ ] All chart references resolve to existing files
- [ ] XKCD attribution present with CC BY-NC 2.5
- [ ] `docs/index.html` validates and displays both new cards
- [ ] All slide titles are questions (except mini slide 9 = numbered promise, and full lecture fixed frames: Title, Learning Objectives, Key Takeaways, Closing)

---

## Must Have / Must NOT Have

### Must Have
- Self-contained preamble in BOTH files (copied from L03_knn_mini.tex lines 1-99, title changed)
- Mini-lecture: inline TikZ comics on slides 1 and 6, inline pgfplots/tikz for all visuals EXCEPT slide 7
- Full lecture: external charts via `\includegraphics` for all 7 existing chart PDFs
- MSc-level content: Greek letters, MLE derivation, gradient formula, Newton-Raphson reference, odds ratios
- Finance domain: credit scoring PD estimation, Basel scorecards, Gini coefficient
- Fraud detection mentioned as imbalanced-data application example (Frame 21 of full lecture)
- `\bottomnote{}` on every frame
- `\compactlist` environment for bullet lists
- Two-column [T] layout on all content slides (0.55 + 0.42 split)
- Block types: `block{Insight}` for mini slides 1,3,4,5,6,7,8,9; `exampleblock` for mini slides 2,10
- `dfteal` and `dfred` colors for TikZ comics (defined in preamble)
- Core tension stated in both lectures

### Must NOT Have
- `\input{}` or `\include{}` for shared preambles -- each file is self-contained
- Title slide in the mini-lecture (10 content frames only; `\title` metadata is in preamble for footer)
- Subplots or multi-panel figures (one visual per slide)
- Any reference to chart files that do not exist in `slides/L02_Logistic_Regression/`
- Overview-level content in the full lecture (must be MSc depth: proofs, derivations, inference)
- Bullet overflow (max 3-4 bullets per compactlist, use `\scriptsize` or `\footnotesize` if needed)
- `\section{}` commands in the full lecture -- use comment-block markers (`%% === SECTION NAME ===`) instead
- Bare `\begin{itemize}` without `\compactlist` wrapper (except inside blocks)

---

## Deliverable 1: 10-Slide Mini-Lecture (`L02_logreg_mini.tex`)

### Core Tension
"Banks must decide who gets credit, **but** a yes/no answer hides the probability that separates a good loan from a disaster."

### Preamble
Copy lines 1-99 from `slides/L03_KNN_KMeans/L03_knn_mini.tex` verbatim, then change ONLY:
```latex
\title[Logistic Regression Mini-Lecture]{Logistic Regression}
\subtitle{A 10-Slide Mini-Lecture}
```
Keep `\author`, `\institute`, `\date{}` identical. Keep all color definitions, `compactlist`, `\highlight`, `\mathbold`, `\bottomnote`, footer template, TikZ libraries, pgfplots.

### Slide-by-Slide Specification

---

#### SLIDE 1: WHY -- TikZ Comic (Dilemma)

**Title**: "Why Would a Credit Officer Want a Probability Instead of a Rule?"

**Layout**: `\begin{columns}[T]` with `\begin{column}{0.55\textwidth}` + `\begin{column}{0.42\textwidth}`

**Left column**:
- Bold heading: "The Dilemma"
- compactlist (3 items):
  - A loan applicant scores 680 -- right at the boundary
  - The rulebook says "approve above 700, deny below 650" but says nothing about 680
  - A linear model predicts repayment of 1.3 -- but what does that even mean?
- Transition line: "What if instead of a number, you got the probability of default?"
- `\begin{block}{Insight}` Logistic regression replaces arbitrary cutoffs with calibrated probabilities: P(default) maps every applicant to a number between 0 and 1.

**Right column** -- TikZ comic (scale=0.75):
- Stick figure labeled "Officer" (dfteal) on left, standing at a desk
- Stick figure labeled "Applicant" (mlpurple) on right, with orange "?" above head
- Speech bubble from Officer: "Score is 680... now what?"
- Thought bubble from Officer: "...if only I had a probability"
- Below: a horizontal number line from 0 to 1 with a sigmoid-shaped curve sketched in dfteal, a dashed vertical line at 0.5 in dfred, and a dot at ~0.65 in mlorange labeled "PD"

**Bottomnote**: "Logistic regression outputs P(Y=1|X) -- a calibrated probability, not an unbounded score"

**Block type**: `block{Insight}`

---

#### SLIDE 2: FEEL -- Text-Only with Reflection Prompt

**Title**: "Predicting an Outcome -- Did You Think in Probabilities?"

**Layout**: Two columns [T], 0.55 + 0.42

**Left column**:
- Bold: "Think Before You Compute"
- `\footnotesize` narrative paragraph: "Imagine you are reviewing a stack of loan applications. Without any model, you instinctively sort them: this one looks safe, that one is risky, this one could go either way. You are not assigning 0 or 1. You are assigning a feeling of likelihood -- 'probably fine', 'probably not', 'fifty-fifty'. That is a probability."
- compactlist (3 items):
  - How confident were you in each assessment?
  - Did you use features like income, employment, or debt?
  - Were some features more important than others?
- `\begin{exampleblock}{Reflection Prompt}` "Write down one real decision you made this week where you mentally estimated a probability. What features did you use?"

**Right column**:
- `\fcolorbox{mlpurple}{mllavender4}` box:
  - Bold: "Pause and reflect:"
  - Text: "When you last decided whether to bring an umbrella, you estimated P(rain) from features: clouds, forecast, season. You did not predict rain = 1.3."
  - Bold: "That is logistic regression."

**Bottomnote**: "Human intuition naturally produces probabilities -- logistic regression formalizes this into a trainable model"

**Block type**: `exampleblock{Reflection Prompt}`

---

#### SLIDE 3: WHAT -- Comparison Table

**Title**: "What Makes Logistic Regression Different from Linear Regression and Decision Trees?"

**Layout**: Two columns [T], 0.55 + 0.42

**Left column**:
- Bold: "Taxonomy of Classifiers"
- `\footnotesize` tabular with `@{}l c c c@{}`:

| Property | **LogReg** (dfteal) | **LinReg** | **Dec. Tree** |
|----------|---------------------|------------|---------------|
| Output | Prob. | Real | Class/Prob. |
| Boundary | Linear | N/A | Axis-aligned |
| Loss | Cross-ent. | MSE | Gini/Entropy |
| Interpret. | High (OR) | High | Medium |
| Regularize | L1/L2/EN | L1/L2 | Pruning |
| Calibration | Native | Poor | Poor |

- With alternating `\rowcolor{mllavender4}` on rows 1, 3, 5
- `\scriptsize` bold summary: "Logistic regression is the only method here that directly outputs well-calibrated probabilities."
- `\begin{block}{Insight}` `\scriptsize` "LogReg occupies a unique niche: parametric, interpretable, probabilistic, and naturally calibrated -- which is why regulators love it."

**Right column**:
- Three colored boxes stacked vertically (matching L03 pattern):
  - `\colorbox{dfteal!15}` "LogReg: Probabilistic, parametric, linear boundary"
  - `\colorbox{mlorange!15}` "LinReg: Continuous output, no classification"
  - `\colorbox{mlpurple!15}` "Tree: Non-parametric, axis-aligned, uncalibrated"

**Bottomnote**: "Odds ratio interpretation: each coefficient tells you the multiplicative change in odds per unit feature change"

**Block type**: `block{Insight}`

---

#### SLIDE 4: CASE -- Step Diagram (TikZ Flow)

**Title**: "How Does One Loan Application Travel from Features to Probability?"

**Layout**: Two columns [T], 0.55 + 0.42

**Left column**:
- Bold: "One Prediction, Step by Step"
- compactlist (5 items):
  - Applicant arrives with features: income=50k, debt-ratio=0.35, employment=4yr
  - Compute linear combination: z = w_0 + w_1*income + w_2*debt + w_3*employment
  - Apply sigmoid: P(default) = 1/(1 + e^{-z})
  - Compare to threshold (e.g., 0.5): if P > 0.5, predict default
  - Bank uses the raw probability for capital reserves (Basel PD)
- `\begin{block}{Insight}` `\scriptsize` "The sigmoid is the bridge: it maps any real number z to a probability in (0,1). The threshold is a business decision, not a model decision."

**Right column** -- TikZ step diagram (scale=0.75):
- stepnode style: `draw, rounded corners=3pt, font=\tiny, text width=2.2cm, align=center, minimum height=0.55cm`
- 5 nodes vertically:
  1. (mllavender4 fill) "1. Features x"
  2. (mllavender4 fill) "2. Linear combo z = w^T x"
  3. (dfteal!20 fill) "3. Sigmoid: sigma(z)"
  4. (mlorange!20 fill) "4. Threshold check"
  5. (mlgreen!20 fill, thick) "5. Decision + PD"
- Arrows between each with tiny labels: "encode", "dot product", "squash to (0,1)", "business rule"
- No decision diamond (simpler than KNN flow since it is a forward pass)

**Bottomnote**: "The model outputs P(default); the threshold is chosen by the business based on cost trade-offs"

**Block type**: `block{Insight}`

---

#### SLIDE 5: HOW -- Side-by-Side Architecture

**Title**: "Who Should Fit the Model -- Gradient Descent, Newton, or a Library?"

**Layout**: Two columns [T], 0.55 + 0.42

**Left column**:
- Bold: "Three Optimization Approaches"
- compactlist (3 items):
  - **Gradient Descent**: update w = w - eta * X^T(p - y)/n, simple but slow
  - **Newton-Raphson (IRLS)**: uses Hessian, converges quadratically, standard in statsmodels/R
  - **L-BFGS**: quasi-Newton, memory-efficient, default in scikit-learn
- `\scriptsize` "All three minimize the same convex cross-entropy loss -- global optimum guaranteed."
- `\begin{block}{Insight}` `\scriptsize` "Cross-entropy is convex in the weights, so every optimizer converges to the same solution. The choice is about speed, not correctness."

**Right column** -- TikZ diagram (scale=0.75):
- Top box: "Gradient Descent" (dfred label), show 3 zigzag arrows in a contour-like ellipse, slow convergence
- Bottom box: "Newton-Raphson" (dfteal label), show 2 direct arrows to center of contour, fast convergence
- Arrow between them with label "fixes this"
- Similar visual structure to L03_kmeans_mini.tex slide 5 (Random Init vs K-Means++ comparison)

**Bottomnote**: "Newton-Raphson converges in 5-10 iterations vs. hundreds for gradient descent -- but requires Hessian inversion"

**Block type**: `block{Insight}`

---

#### SLIDE 6: RISK -- TikZ Comic (Failure Scene)

**Title**: "What Could Go Wrong If You Trust the Default Threshold?"

**Layout**: Two columns [T], 0.55 + 0.42

**Left column**:
- Bold: "Three Ways Logistic Regression Fails Silently"
- compactlist (3 items):
  - **Class imbalance**: 99% non-default means predicting "no default" always gets 99% accuracy
  - **Separation**: if one feature perfectly predicts the outcome, coefficients explode to infinity
  - **Non-linear boundaries**: logistic regression draws a straight line -- curved patterns get misclassified
- `\begin{block}{Insight}` `\scriptsize` "The default 0.5 threshold is almost never optimal in finance. Fraud detection might use 0.1; credit scoring might use 0.3."

**Right column** -- TikZ comic (scale=0.75), DIFFERENT emotional register from slide 1 (frustration/failure):
- Stick figure labeled "Model" (dfred) in center, arms raised in distress
- Above: two groups of dots -- large cluster of mlgreen dots (non-default, ~15 dots) on left, tiny cluster of dfred dots (default, ~3 dots) on right
- A dashed horizontal line at threshold 0.5 in mlpurple, with ALL dots above or below the line incorrectly
- Speech bubble from Model: "I predicted no one defaults... 99% accuracy!"
- Large red X in corner
- Below: tiny label "Imbalanced data failure"

**Bottomnote**: "Always evaluate with AUC, precision-recall, and Gini -- never with accuracy alone on imbalanced data"

**Block type**: `block{Insight}`

---

#### SLIDE 7: WHERE -- External Chart (PDF)

**Title**: "Why Does Every Credit Risk Team Start with Logistic Regression?"

**Layout**: Two columns [T], 0.55 + 0.42

**Left column**:
- Bold: "Logistic Regression as the Regulatory Baseline"
- compactlist (4 items):
  - Interpretable: every coefficient has a direct odds-ratio interpretation
  - Auditable: regulators can inspect and validate each feature's contribution
  - Calibrated: output probabilities match observed default rates
  - Stable: small data changes produce small coefficient changes
- `\scriptsize` "The ROC curve shows how well the model discriminates defaulters from non-defaulters at every threshold."
- `\begin{block}{Insight}` `\scriptsize` "Logistic regression is not popular in credit scoring because it is the best predictor -- it is popular because it is the most interpretable predictor."

**Right column**:
- `\includegraphics[width=\textwidth]{04_roc_curve/chart.pdf}`
- This is the ONE external chart in the mini-lecture

**Chart selection**: `04_roc_curve/chart.pdf` -- chosen because the ROC curve is the single most important evaluation metric in credit scoring and directly connects to the Gini coefficient (Gini = 2*AUC - 1) that banks report.

**Bottomnote**: "Gini = 2*AUC - 1: industry standard. Gini > 0.40 acceptable; Gini > 0.60 good for credit scoring"

**Block type**: `block{Insight}`

---

#### SLIDE 8: IMPACT -- Stakeholder Map (TikZ)

**Title**: "Who Wins and Who Loses When a Bank Switches to Logistic Regression?"

**Layout**: Two columns [T], 0.55 + 0.42

**Left column**:
- Bold: "Stakeholder Analysis"
- compactlist (2 bullet groups):
  - **Winners**: Risk managers (calibrated PD), regulators (interpretable model), applicants (consistent decisions), capital planning (accurate reserves)
  - **Losers**: Data scientists wanting complex models (neural nets rejected), branch managers (discretion reduced), anyone with non-linear intuition
- `\scriptsize` "LogReg shifts power from subjective judgment to auditable probability."
- `\begin{block}{Insight}` `\scriptsize` "In regulated finance, interpretability is not optional -- it is a legal requirement under Basel II/III and GDPR Article 22."

**Right column** -- TikZ stakeholder map (scale=0.75):
- Center node: "LogReg" (mlpurple fill, white text, rounded, 1.4cm wide)
- Top: "Risk Manager" (mlgreen!20, draw=mlgreen) -- arrow from LogReg with label "calibrated PD"
- Right: "Regulator" (dfteal!20, draw=dfteal) -- arrow from LogReg with label "auditable coefficients"
- Bottom: "Data Scientist" (dfred!20, draw=dfred) -- arrow from LogReg with label "no deep learning"
- Left: "Applicant" (mlorange!20, draw=mlorange) -- arrow from LogReg with label "consistent decision"
- Same actor/arr styles as L03_kmeans_mini.tex slide 8

**Bottomnote**: "Basel IRB requires banks to demonstrate PD model validity annually -- logistic regression passes this test"

**Block type**: `block{Insight}`

---

#### SLIDE 9: SO WHAT -- Balance Scale (Numbered Promise)

**Title**: "3 Questions That Reveal Whether Logistic Regression Is the Right Model"

NOTE: This is the ONLY slide with a numbered title (not a question). Follows the mini-lecture-generator convention.

**Layout**: Two columns [T], 0.55 + 0.42

**Left column**:
- Bold: "The Decision Framework"
- `\begin{enumerate}` with `\setlength{\itemsep}{2pt}`:
  1. **Is the outcome binary (or ordinal)?** -- If continuous, use linear regression; if multi-class, consider softmax
  2. **Is interpretability required?** -- If regulators or stakeholders demand coefficient explanations, LogReg wins
  3. **Is the decision boundary approximately linear?** -- If strongly non-linear, consider tree ensembles or feature engineering
- `\scriptsize` "If all three answers are yes, logistic regression is the right first model."
- `\begin{block}{Insight}` `\scriptsize` "Logistic regression should be your first model for any binary classification problem in a regulated environment."

**Right column** -- TikZ balance scale (scale=0.75):
- Fulcrum triangle (mlgray) at bottom center
- Beam tilted: left side lower (Use LogReg wins)
- Left pan (dfteal fill, dfteal!20): three mlgreen rounded boxes labeled "Binary", "Interp.", "Linear OK"
- Label below: "Use LogReg" (dfteal)
- Right pan (dfred fill, dfred!20): three mlred rounded boxes labeled "Non-lin.", "No audit", "Multi-cls"
- Label below: "Avoid LogReg" (dfred)
- Large "?" in mlpurple at top center
- Identical structural pattern to L03_kmeans_mini.tex slide 9

**Bottomnote**: "Even when you suspect non-linearity, start with LogReg as a baseline -- you need something to beat"

**Block type**: `block{Insight}`

---

#### SLIDE 10: ACT -- Activity Frame

**Title**: "Can You Evaluate This Real Credit Scoring Problem?"

**Layout**: Two columns [T], 0.55 + 0.42

**Left column**:
- Bold: "The Scenario"
- `\footnotesize` paragraph: "A consumer bank wants to predict credit card default. Features: monthly income, credit utilization ratio, number of late payments (past 12 months), years with current employer, total debt. Dataset has 10,000 accounts with 3% default rate."
- compactlist (4 items):
  - Apply the 3-question framework from the previous slide
  - Decide: Is logistic regression appropriate here?
  - If yes: what threshold would you choose (hint: 3% default rate)?
  - What single metric would you report to the regulator?
- `\begin{exampleblock}{Deliverable}` `\scriptsize` "Fill in the table. Be prepared to defend your verdict to a skeptical Basel auditor."

**Right column**:
- `\footnotesize` table with fill-in blanks:

| Question | Your Answer |
|----------|-------------|
| Binary outcome? | ________ |
| Interpretable needed? | ________ |
| Linear boundary OK? | ________ |
| **Verdict** | ________ |
| Recommended threshold | ________ |
| Key metric for regulator | ________ |

- Using `\rule{2.5cm}{0.4pt}` for blanks, matching L03 pattern

**Bottomnote**: "Hint: with 3% default rate, accuracy is meaningless. Think about Gini, AUC, or precision-recall."

**Block type**: `exampleblock{Deliverable}`

---

### Mini-Lecture Checklist

- [ ] Preamble: lines 1-99 from L03_knn_mini.tex, title changed to `\title[Logistic Regression Mini-Lecture]{Logistic Regression}`
- [ ] NO `\begin{frame} \titlepage \end{frame}` -- starts directly with Slide 1
- [ ] All 10 frame titles are questions EXCEPT slide 9 (numbered promise)
- [ ] Slides 1, 6: TikZ comics with different emotional registers (dilemma vs. failure)
- [ ] Slide 2: text-only with reflection prompt, exampleblock
- [ ] Slide 3: comparison table with alternating row colors
- [ ] Slide 4: TikZ step diagram (forward pass flow)
- [ ] Slide 5: TikZ side-by-side architecture (GD vs Newton)
- [ ] Slide 7: ONE external chart (`04_roc_curve/chart.pdf`)
- [ ] Slide 8: TikZ stakeholder map (4 actors around center)
- [ ] Slide 9: TikZ balance scale (use/avoid framework)
- [ ] Slide 10: activity with fill-in table, exampleblock
- [ ] Every frame has `\bottomnote{}`
- [ ] Block types: block{Insight} for 1,3,4,5,6,7,8,9; exampleblock for 2,10
- [ ] Two-column [T] layout on ALL 10 frames (0.55 + 0.42)
- [ ] `compactlist` for all bullet lists
- [ ] `\scriptsize` or `\footnotesize` for body text to prevent overflow
- [ ] ZERO Overfull hbox/vbox warnings
- [ ] Core tension stated in slide 1 framing
- [ ] Credit scoring / Basel / PD references throughout

---

## Deliverable 2: Full-Length Technical Lecture (`L02_logreg_full.tex`)

### Core Tension
"Classification demands a probability, **but** a linear model gives you a number that can be negative, greater than one, or anything in between -- the sigmoid bridges this gap, and everything else follows from maximum likelihood."

### Learning Objectives (Bloom's Levels 3-5)
1. **Derive** the MLE for logistic regression via the gradient of the log-likelihood (Analyze)
2. **Evaluate** classification performance using ROC, precision-recall, calibration, and Gini (Evaluate)
3. **Analyze** model fit via deviance, Wald test, LRT, AIC/BIC, and Hosmer-Lemeshow (Analyze)
4. **Apply** logistic regression to credit scoring with Basel-compliant PD estimation (Apply)
5. **Compare** regularization strategies (L1, L2, Elastic Net) and their effect on model selection (Evaluate)

### Preamble
SAME self-contained preamble as the mini-lecture (copied from L03_knn_mini.tex lines 1-99), with title changed to:
```latex
\title[L02: Logistic Regression Full Lecture]{L02: Logistic Regression}
\subtitle{Full Lecture: Mathematical Foundations, Inference, and Credit Scoring}
\author{Methods and Algorithms}
\institute{MSc Data Science}
\date{Spring 2026}
```

### Section Framework and Frame-by-Frame Specification

The full lecture expands the 10-slide arc into ~31 frames organized in 8 sections. Each WHY/FEEL/WHAT/CASE/HOW/RISK/WHERE/IMPACT/SO WHAT/ACT slot gets 2-5 frames for depth.

---

#### SECTION 0: Opening (Frames 1-4) -- WHY + FEEL

| Frame | Title | Arc Slot | Content | Visual |
|-------|-------|----------|---------|--------|
| 1 | Title Page | FIXED | `\titlepage` | N/A |
| 2 | "The Eternal Debate" | FEEL (Opening Comic) | XKCD #1132 (frequentist_bayesian.png) with caption | `\includegraphics[height=0.65\textheight]{images/1132_frequentist_bayesian.png}` + `\bottomnote{XKCD \#1132 by Randall Munroe (CC BY-NC 2.5)}` |
| 3 | Learning Objectives | FIXED | 5 objectives with Bloom's verbs, finance application statement | Numbered list, no visual |
| 4 | "Why Would a Bank Want a Probability Instead of a Score?" | WHY | Core tension: linear model output is unbounded, need P(Y=1) in [0,1]. Credit scoring motivation. Cost of FP vs FN. | TikZ: number line showing linear model output going beyond [0,1] vs. sigmoid squashing it. Two-column layout. |

---

#### SECTION 1: Mathematical Foundations (Frames 5-11) -- WHAT + CASE

| Frame | Title | Arc Slot | Content | Visual |
|-------|-------|----------|---------|--------|
| 5 | "What Happens When You Pass a Linear Combination Through a Sigmoid?" | WHAT | Sigmoid definition, properties: range (0,1), sigma(0)=0.5, symmetry. Derivative: sigma'(z) = sigma(z)(1-sigma(z)). | `\includegraphics[width=0.55\textwidth]{01_sigmoid_function/chart.pdf}` |
| 6 | "How Do Odds and Log-Odds Connect Features to Probabilities?" | WHAT | Odds = p/(1-p), logit link, coefficient interpretation via odds ratios. Worked example: w_income = 0.5 => OR = 1.65. | Inline TikZ: log-odds scale with annotations. Two-column. |
| 7 | "How Does Maximum Likelihood Find the Best Coefficients?" | CASE | Likelihood function: product of p_i^{y_i}(1-p_i)^{1-y_i}. Log-likelihood: sum form. Why MLE and not OLS. | Inline math display, no visual needed (math-heavy frame). |
| 8 | "Why Does Cross-Entropy Loss Guarantee a Global Optimum?" | CASE | Binary cross-entropy = negative log-likelihood. Convexity proof sketch. | `\includegraphics[width=0.55\textwidth]{03_log_loss/chart.pdf}` |
| 9 | "What Does the Gradient Look Like in Matrix Form?" | CASE | Chain rule derivation: dL/dw_j = (p_i - y_i)*x_ij. Full gradient: X^T(p-y)/n. Connection to linear regression gradient. | Inline math display. Key formula boxed. |
| 10 | "How Does Gradient Descent Update the Weights?" | HOW | Update rule: w^{t+1} = w^t - eta*X^T(sigma(Xw^t)-y)/n. Learning rate, convergence, standardization. | Inline TikZ: contour lines with gradient arrows. |
| 11 | "Why Do Statisticians Prefer Newton-Raphson Over Gradient Descent?" | HOW | Hessian: H = -X^T*diag(p(1-p))*X. Newton update. IRLS interpretation. Quadratic convergence. | Algorithm pseudocode box (algorithmic environment). |

---

#### SECTION 2: Decision Boundaries (Frames 12-14) -- HOW continued

| Frame | Title | Arc Slot | Content | Visual |
|-------|-------|----------|---------|--------|
| 12 | "Where Does the Decision Boundary Live in Feature Space?" | HOW | w^Tx + b = 0 defines a hyperplane. Threshold selection: 0.5 = default, cost-based alternatives. | `\includegraphics[width=0.55\textwidth]{02_decision_boundary/chart.pdf}` |
| 13 | "How Can a Linear Model Capture Non-Linear Patterns?" | HOW | Polynomial features, interaction terms, feature engineering. Trade-off: flexibility vs. overfitting. | Inline TikZ: showing linear boundary vs. polynomial boundary. |
| 14 | "What Changes When There Are More Than Two Classes?" | HOW | Softmax: P(y=k|x) = exp(w_k^Tx)/sum. One-vs-Rest. Categorical cross-entropy. | Inline math display with softmax equation. |

---

#### SECTION 3: Statistical Inference (Frames 15-18) -- WHAT (depth)

| Frame | Title | Arc Slot | Content | Visual |
|-------|-------|----------|---------|--------|
| 15 | "How Certain Are We About Each Coefficient?" | WHAT | Standard errors from Hessian inverse. SE(beta_j) = sqrt([H^{-1}]_jj). Intuition: more data => smaller SE. | Inline math. |
| 16 | "Is This Feature Significant? (Wald Test)" | WHAT | H0: beta_j = 0. Wald z-statistic. Decision rule: |z| > 1.96. | Inline math with worked example. |
| 17 | "Does Adding These Features Actually Improve the Model?" | WHAT | LRT: Lambda = -2[l(reduced) - l(full)] ~ chi^2. More powerful than Wald for multiple coefficients. Example: adding 3 credit bureau features. | Inline math. |
| 18 | "How Do You Choose Between Two Non-Nested Models?" | WHAT | Deviance, McFadden pseudo-R^2. AIC = -2l + 2k, BIC = -2l + k*ln(n). BIC preferred for regulatory models. | Inline comparison table. |

---

#### SECTION 4: Evaluation Metrics (Frames 19-23) -- RISK + WHERE

| Frame | Title | Arc Slot | Content | Visual |
|-------|-------|----------|---------|--------|
| 19 | "How Do You Measure Discrimination Across All Thresholds?" | WHERE | ROC curve: TPR vs FPR. Diagonal = random. AUC interpretation. | `\includegraphics[width=0.55\textwidth]{04_roc_curve/chart.pdf}` |
| 20 | "What Does AUC Really Mean, and What Is the Gini Coefficient?" | WHERE | AUC = P(random positive ranks higher). Gini = 2*AUC - 1. Industry benchmarks. KS statistic. | Inline math + table of AUC-to-Gini conversions. |
| 21 | "When Does ROC Lie, and Why Should You Use Precision-Recall?" | RISK | Imbalanced data makes ROC overly optimistic. PR curve focus on positive class. **Fraud detection example:** with 0.1\% fraud rate, 99.9\% accuracy means predicting "no fraud" always. | `\includegraphics[width=0.55\textwidth]{05_precision_recall/chart.pdf}` |
| 22 | "How Do You Know If Your Probabilities Are Truthful?" | RISK | Calibration: predicted P should match observed frequency. Brier score. Reliability diagram. Hosmer-Lemeshow test. | `\includegraphics[width=0.55\textwidth]{06_confusion_matrix/chart.pdf}` |
| 23 | "What Could Go Wrong When Data Perfectly Separates the Classes?" | RISK | Complete/quasi-complete separation. Coefficients -> infinity. Solutions: Firth's penalized likelihood, L2 regularization. | Inline TikZ: scatter plot with perfect separating line, arrows showing coefficients diverging. |

---

#### SECTION 5: Regularization (Frames 24-26) -- HOW (depth)

| Frame | Title | Arc Slot | Content | Visual |
|-------|-------|----------|---------|--------|
| 24 | "Why Would You Penalize Coefficients That Fit the Data Well?" | HOW | Overfitting: many features, limited data. Regularized loss: L + lambda*R(w). Bias-variance trade-off. | Inline math. |
| 25 | "Should You Shrink All Coefficients or Zero Some Out?" | HOW | L2 (Ridge): shrinks all. L1 (Lasso): zeros some. Elastic Net: both. Equations for each. | Inline comparison with three equations side by side. |
| 26 | "How Do You Choose the Regularization Strength?" | HOW | Cross-validation for lambda. LogisticRegressionCV. C = 1/lambda convention. | Inline description of CV procedure. |

---

#### SECTION 6: Finance Application (Frames 27-29) -- IMPACT

| Frame | Title | Arc Slot | Content | Visual |
|-------|-------|----------|---------|--------|
| 27 | "How Do Banks Turn Logistic Regression Into Credit Scores?" | IMPACT | PD estimation under Basel II/III. Why interpretability matters legally. Scorecard conversion: log-odds to points. PDO (points to double the odds). | `\includegraphics[width=0.55\textwidth]{07_decision_flowchart/chart.pdf}` |
| 28 | "What Features Do Credit Scorecards Actually Use?" | IMPACT | WoE encoding, binning, feature engineering. Credit-specific features: debt-to-income, employment stability, bureau delinquency. Worked numerical example: applicant with specific features -> PD = 0.045. | Inline worked example with numbers. |
| 29 | "Who Wins and Who Loses When Models Replace Loan Officers?" | IMPACT | Stakeholder analysis: risk managers, regulators, applicants, data scientists, branch managers. Fairness considerations: protected attributes, disparate impact. | Inline TikZ stakeholder map (similar to mini slide 8 but expanded with fairness node). |

---

#### SECTION 7: Summary and Practice (Frames 30-31) -- SO WHAT + ACT

| Frame | Title | Arc Slot | Content | Visual |
|-------|-------|----------|---------|--------|
| 30 | Key Takeaways | FIXED (SO WHAT) | 3 blocks: Mathematical Foundation (sigmoid, MLE, convexity), Evaluation & Inference (Wald, LRT, ROC, Gini, calibration), Practical (regularization, interpretability = regulatory standard). | Structured bullet list. |
| 31 | "Until Next Time..." | FIXED (Closing) | Callback to XKCD #1132. "With logistic regression, you can quantify the answer." Next session: L03 KNN & K-Means. | Text-only closing with reference to opening comic. |

---

### Chart Allocation Table (Full Lecture)

| Chart | File Path | Frame # | Usage |
|-------|-----------|---------|-------|
| Sigmoid Function | `01_sigmoid_function/chart.pdf` | 5 | `\includegraphics[width=0.55\textwidth]` |
| Decision Boundary | `02_decision_boundary/chart.pdf` | 12 | `\includegraphics[width=0.55\textwidth]` |
| Log Loss | `03_log_loss/chart.pdf` | 8 | `\includegraphics[width=0.55\textwidth]` |
| ROC Curve | `04_roc_curve/chart.pdf` | 19 | `\includegraphics[width=0.55\textwidth]` |
| Precision-Recall | `05_precision_recall/chart.pdf` | 21 | `\includegraphics[width=0.55\textwidth]` |
| Confusion Matrix | `06_confusion_matrix/chart.pdf` | 22 | `\includegraphics[width=0.55\textwidth]` |
| Decision Flowchart | `07_decision_flowchart/chart.pdf` | 27 | `\includegraphics[width=0.55\textwidth]` |

All 7 charts used. Frames without external charts use inline TikZ or math-only layouts.

### Chart Frame Left-Column Template (Full Lecture)

Every chart-containing frame in the full lecture MUST include 3 interpretation bullets in the left column:
- **What you see:** [1 sentence describing the visual -- axes, colors, series]
- **Key pattern:** [1 sentence about the important observation]
- **Takeaway:** [1 sentence connecting to theory or practice]

This applies to frames 5, 8, 12, 19, 21, 22, and 27. Each chart frame uses `block{Insight}` at the bottom.

### Full Lecture Block and Bottomnote Rules

- All content frames (4-29) use `\begin{block}{Insight}...\end{block}` at the bottom
- Fixed frames (1-3, 30-31) do NOT need insight blocks
- Every frame (including fixed frames except Title) has a `\bottomnote{}`
- All bullet lists use `\compactlist` environment (except inside blocks)

### XKCD Image Usage (Full Lecture Only)

| Image | Frame | Attribution |
|-------|-------|-------------|
| `images/1132_frequentist_bayesian.png` | 2 (Opening Comic) | `\bottomnote{XKCD \#1132 by Randall Munroe (CC BY-NC 2.5) -- "Is the sun going to explode?"}` |

Closing frame (31) references the comic textually but does not re-display the image.

### Inline TikZ Frames (Full Lecture)

| Frame | Visual Type | Description |
|-------|-------------|-------------|
| 4 | Number line + sigmoid | Linear output beyond [0,1] vs. sigmoid squashing |
| 6 | Log-odds scale | Annotated scale showing odds, log-odds, probability mapping |
| 10 | Contour + gradient | Contour lines of loss surface with gradient arrows |
| 13 | Boundary comparison | Linear vs. polynomial decision boundary |
| 23 | Separation diagram | Perfect separating line with diverging coefficient arrows |
| 29 | Stakeholder map | Extended 5-node map with fairness node |

### Full Lecture Checklist

- [ ] Self-contained preamble (same as mini-lecture, different title/subtitle)
- [ ] Frame 1: `\titlepage` (the only non-question title)
- [ ] Frame 2: XKCD opening comic with CC BY-NC 2.5 attribution
- [ ] Frame 3: 5 learning objectives with Bloom's verbs
- [ ] All 7 external chart PDFs referenced and paths verified
- [ ] MLE derivation: likelihood -> log-likelihood -> gradient -> matrix form (frames 7-9)
- [ ] Newton-Raphson / IRLS with Hessian (frame 11)
- [ ] Statistical inference: SE, Wald, LRT, AIC/BIC, Hosmer-Lemeshow (frames 15-18)
- [ ] Regularization: L1, L2, Elastic Net, cross-validation for lambda (frames 24-26)
- [ ] Credit scoring worked example with numerical PD (frame 28)
- [ ] Basel/scorecard content (frame 27)
- [ ] Fairness/disparate impact mentioned (frame 29)
- [ ] Closing callback to opening comic (frame 31)
- [ ] `\bottomnote{}` on every frame
- [ ] All content frames use question titles (except fixed frames 1, 3, 30, 31)
- [ ] Two-column [T] layout on all content frames with visuals
- [ ] Math-heavy frames may use full-width layout (frames 7, 9, 14, 15, 16, 17, 18, 24, 25, 26)
- [ ] ZERO Overfull hbox/vbox warnings
- [ ] 31 total frames

---

## Deliverable 3: GitHub Pages Integration

### Current State
The L02 section in `docs/index.html` (lines 163-184) currently has:
- Overview PDF, Deep Dive PDF, Colab Notebook, Dataset (4 cards)
- 7 chart thumbnail cards

### Changes Required
Add two new PDF download cards after the existing Deep Dive PDF card (line 170), before the Colab Notebook card (line 171).

### New Cards HTML

Insert after line 170 (`Deep Dive PDF` card):

```html
<a class="ccard" href="slides/pdf/L02_logreg_mini.pdf" download><div class="ccard-icon">PDF</div>Mini-Lecture PDF<div class="ccard-label">10-slide mini</div></a>
<a class="ccard" href="slides/pdf/L02_logreg_full.pdf" download><div class="ccard-icon">PDF</div>Full Lecture PDF<div class="ccard-label">31-slide technical</div></a>
```

### GH Pages Checklist
- [ ] Two new `<a class="ccard">` elements added
- [ ] href points to `slides/pdf/L02_logreg_mini.pdf` and `slides/pdf/L02_logreg_full.pdf`
- [ ] `download` attribute present on both
- [ ] Labels descriptive: "10-slide mini" and "31-slide technical"
- [ ] Card order: Overview, Deep Dive, Mini-Lecture, Full Lecture, Colab, Dataset
- [ ] HTML validates (no unclosed tags)

---

## Task Flow and Dependencies

```
Task 1 ──────────────────────────────────────────────────┐
  Write L02_logreg_mini.tex                              │
  (self-contained, no dependencies)                      │
                                                         │
Task 2 ──────────────────────────────────────────────────┤
  Write L02_logreg_full.tex                              ├─── Task 4: Compile both
  (self-contained, no dependencies)                      │    with pdflatex, verify
                                                         │    zero warnings
Task 3 ──────────────────────────────────────────────────┤
  Edit docs/index.html                                   │
  (independent of Tasks 1-2)                             │
                                                         │
                                                    Task 4 ──── Task 5: Copy PDFs
                                                                 to docs/slides/pdf/
```

### Task Details

**Task 1: Write `L02_logreg_mini.tex`**
- File: `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L02_Logistic_Regression\L02_logreg_mini.tex`
- Copy preamble from `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L03_KNN_KMeans\L03_knn_mini.tex` lines 1-99
- Change title to Logistic Regression
- Implement all 10 slides per the specification above
- Validate: 10 frames, no title page, question titles (except slide 9)
- Acceptance criteria: pdflatex compiles with zero Overfull warnings

**Task 2: Write `L02_logreg_full.tex`**
- File: `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L02_Logistic_Regression\L02_logreg_full.tex`
- Same preamble as Task 1, different title/subtitle
- Implement all 31 frames per the specification above
- All 7 chart references must resolve
- XKCD attribution present
- Acceptance criteria: pdflatex compiles with zero Overfull warnings

**Task 3: Edit `docs/index.html`**
- File: `D:\Joerg\Research\slides\Methods_and_Algorithms\docs\index.html`
- Insert two new card elements after line 170
- Acceptance criteria: HTML validates, cards display correctly

**Task 4: Compile and Verify**
- Run `pdflatex -interaction=nonstopmode L02_logreg_mini.tex` (twice for page numbers)
- Run `pdflatex -interaction=nonstopmode L02_logreg_full.tex` (twice for page numbers)
- Check for zero Overfull warnings
- Verify frame counts: 10 and 31

**Task 5: Copy PDFs to docs**
- Copy compiled PDFs to `docs/slides/pdf/` for GH Pages
- Verify links work

### Parallelization
- Tasks 1, 2, and 3 are fully independent and can run in parallel
- Task 4 depends on Tasks 1 and 2
- Task 5 depends on Task 4

---

## Commit Strategy

| Commit | Content | Message |
|--------|---------|---------|
| 1 | `L02_logreg_mini.tex` | "Add L02 logistic regression 10-slide mini-lecture" |
| 2 | `L02_logreg_full.tex` | "Add L02 logistic regression full technical lecture (31 slides)" |
| 3 | `docs/index.html` changes | "Add mini-lecture and full lecture PDF cards to L02 GH Pages section" |
| 4 | Compiled PDFs (if tracked) | "Add compiled PDFs for L02 mini and full lectures" |

---

## Success Criteria

### Compilation
- [ ] `L02_logreg_mini.tex` compiles with pdflatex -- ZERO Overfull hbox/vbox warnings
- [ ] `L02_logreg_full.tex` compiles with pdflatex -- ZERO Overfull hbox/vbox warnings
- [ ] Mini-lecture PDF has exactly 10 pages
- [ ] Full lecture PDF has exactly 31 pages

### Content Accuracy
- [ ] Sigmoid function formula correct: sigma(z) = 1/(1 + e^{-z})
- [ ] MLE derivation correct: likelihood, log-likelihood, gradient
- [ ] Gradient formula correct: nabla L = (1/n) X^T (p - y)
- [ ] Newton-Raphson Hessian correct: H = -X^T diag(p(1-p)) X
- [ ] Odds ratio interpretation correct: e^{w_j}
- [ ] Gini = 2*AUC - 1 stated correctly
- [ ] Basel/regulatory references accurate

### Structural Compliance
- [ ] Mini-lecture follows exact 10-slide arc: WHY-FEEL-WHAT-CASE-HOW-RISK-WHERE-IMPACT-SO WHAT-ACT
- [ ] Mini-lecture has NO title page
- [ ] Full lecture HAS title page
- [ ] Both files self-contained (no \input or \include)
- [ ] Preamble matches L03_knn_mini.tex template exactly (except title)
- [ ] All `\bottomnote{}` present
- [ ] All block types correct per specification
- [ ] Two-column [T] layouts present where specified

### Visual Compliance
- [ ] Mini-lecture TikZ comics on slides 1 and 6 with different emotional registers
- [ ] Mini-lecture comparison table on slide 3 with alternating row colors
- [ ] Mini-lecture step diagram on slide 4
- [ ] Mini-lecture balance scale on slide 9
- [ ] Mini-lecture stakeholder map on slide 8
- [ ] Mini-lecture activity table on slide 10
- [ ] Full lecture: all 7 external charts referenced and paths correct
- [ ] Full lecture: XKCD image referenced with CC BY-NC 2.5 attribution

### GH Pages
- [ ] Two new cards appear under L02 section
- [ ] Download links use correct file names
- [ ] Card order logical: Overview, Deep Dive, Mini, Full, Colab, Dataset
