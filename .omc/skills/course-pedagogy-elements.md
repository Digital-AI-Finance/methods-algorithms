---
id: course-pedagogy-elements
name: "MSc Methods & Algorithms: Complete Pedagogical Elements"
description: "Comprehensive extraction of all pedagogical patterns, structures, and design decisions across L01-L06 of the Methods and Algorithms MSc course"
source: "Extracted from all 12 .tex files (6 overview + 6 deepdive) after hostile review, L01 restructure, and L05 PCA pedagogy fix"
triggers:
  - "slide pedagogy"
  - "lecture design"
  - "course structure"
  - "beamer teaching"
  - "MSc ML slides"
quality: verified
scope: project
---

# MSc Methods & Algorithms: Complete Pedagogical Elements

## 1. Course Architecture

### 1.1 Two-Deck System

Every lecture has exactly **two slide decks**:

| Deck | Purpose | Slide Count | Chart Density |
|------|---------|-------------|---------------|
| **Overview** | Intuition, motivation, key formulas, worked examples | 20-26 main | ~1:3-4 |
| **Deepdive** | Full derivations, proofs, algorithms, implementation, appendix | 35-45 main + 7-10 appendix | ~1:4-5 |

**Progressive disclosure**: Overview is self-contained (student can pass with overview alone). Deepdive adds rigor, proofs, and implementation details.

### 1.2 Six-Lecture Arc

| ID | Topic | Type | Finance Application |
|----|-------|------|---------------------|
| L01 | Linear Regression | Supervised (continuous) | Property valuation, CAPM |
| L02 | Logistic Regression | Supervised (binary) | Credit scoring, Basel PD |
| L03 | KNN & K-Means | Distance-based (sup + unsup) | Fraud detection, RFM segmentation |
| L04 | Random Forests | Ensemble (trees) | Fraud detection, feature importance |
| L05 | PCA & t-SNE | Dimensionality reduction | Yield curve factors, portfolio |
| L06 | Embeddings & RL | Neural + sequential | NLP in finance, trading strategies |

**Progression**: Parametric → non-parametric → ensemble → unsupervised → deep/sequential.

Cross-references link lectures: "see L05 for PCA before KNN" (L03), "basis for Logistic Regression (L02)" (L01 appendix).

## 2. Three-Zone Architecture (Overviews)

Every overview file is divided into three zones, marked by comments:

```
% === ZONE 1: INTRODUCTION (NO formulas, NO Greek letters) ===
% === ZONE 2: CORE CONTENT (PMSP framework -- formulas allowed) ===
% === ZONE 3: WRAP-UP ===
```

### Zone 1: Introduction (6-10 slides, ZERO Greek letters)

Purpose: Hook the student. Build motivation. Define vocabulary.

**Required slides in order:**
1. Title page
2. Outline (`\tableofcontents`)
3. Opening comic (XKCD) with SCQ hook (Situation-Complication-Question)
4. Motivation/context slides (plain English, real-world examples)
5. Key vocabulary/terms slide
6. Learning Objectives (Bloom's 4-5: Analyze, Evaluate, Derive, Compare)
7. Road map ("now that you know basics, we go deeper")

**Hard rules for Zone 1:**
- ZERO formulas, ZERO Greek letters, ZERO subscripts
- All concepts in plain English with everyday analogies
- Finance context established immediately (banking, credit, fraud)
- At least one chart/visual before any formula appears

### Zone 2: Core Content (10-14 slides, PMSP framework)

**PMSP sections** (marked with `\section{}`):
1. **Problem**: Business context, why this method exists, what gap it fills
2. **Method**: Mathematical formulation, key equations, algorithm steps
3. **Solution**: Interpretation, evaluation metrics, diagnostics
4. **Practice** (or Decision Framework): When to use, comparison with alternatives

**Pedagogical rules for Zone 2:**
- Every formula paired with a worked numerical example
- Charts placed BEFORE or alongside formulas (visual-first)
- Max 3-4 bullet points per slide
- `\bottomnote{}` on every slide with key takeaway
- Comparison tables for method tradeoffs (Ridge vs Lasso, KNN vs K-Means)

### Zone 3: Wrap-Up (3-5 slides)

**Required slides:**
1. Hands-on exercise (with Colab link, 3 progressive exercises)
2. Key Takeaways (two-column summary: concepts + practical guidance)
3. Closing comic/XKCD callback
4. References (optional, can be in appendix)

## 3. Frame Title Pedagogy

### 3.1 Question-Based Titles (Dominant Pattern)

~80% of frame titles are questions. This activates curiosity before content:

| Pattern | Examples |
|---------|----------|
| "Can/Could..." | "Can a Computer Learn to Predict Prices?" |
| "How Do We..." | "How Do We Find the Best Coefficients?" |
| "What Does..." | "What Does the Model Look Like?" |
| "Why Does/Must..." | "Why Must We Scale Features?" |
| "When Should..." | "When Should You Use Linear Regression?" |
| "Which..." | "Which Penalty Should We Choose?" |
| "Is..." | "Is Our Model Learning or Memorizing?" |

### 3.2 Statement Titles (Minority, for reference slides)

Used only for definition/reference slides:
- "Key Equations Summary"
- "Key Takeaways"
- "The Gauss-Markov Theorem"

**Rule**: If the slide introduces a concept, use a question. If it summarizes or references, use a statement.

## 4. Bottomnote System

**Every single frame** has a `\bottomnote{}`. No exceptions across all 12 files.

Bottomnote types:
| Type | Example |
|------|---------|
| Key takeaway | "Always evaluate on data the model has never seen" |
| Practical guidance | "Use adjusted $R^2$ when comparing models with different features" |
| Connection | "Foundation for all supervised learning methods" |
| Attribution | "XKCD #1725 by Randall Munroe (CC BY-NC 2.5)" |
| Warning | "Unscaled features let high-magnitude variables dominate" |
| Context | "Basel II IRB approach: banks must estimate PD for all exposures" |

## 5. Visual-First Teaching

### 5.1 Chart Placement Rules

- **Visual BEFORE formula**: The chart or diagram appears on the slide before or alongside the mathematical formulation
- **Chart density**: Approximately 1 chart per 3-4 slides
- **Chart sizing**: `0.55\textwidth` (with text) or `0.65\textwidth` (chart-only slide)
- **Each chart in exactly ONE file** (no dual-assignment between overview and deepdive)

### 5.2 Chart Types Used

| Chart Type | Purpose | Examples |
|-----------|---------|----------|
| Algorithm visualization | Show how it works step-by-step | Gradient descent path, K-Means iteration |
| Comparison plot | Compare methods/metrics | Ridge vs Lasso paths, ROC curves |
| Diagnostic plot | Teach interpretation | Residual plots, learning curves |
| Decision flowchart | Guide method selection | "Which regression to use?" |
| Concept illustration | Build intuition before formulas | PCA before/after, decision boundaries |
| Worked example companion | Visual for mini-example | PCA by hand, scatter with best-fit line |

### 5.3 XKCD Comic Bookends

**HARD RULE**: Every lecture has an XKCD comic at opening AND a callback/closing comic at end.

| Lecture | Opening XKCD | Closing |
|---------|-------------|---------|
| L01 | #1725 Linear Regression | #605 Extrapolating + quote callback |
| L02 | #1132 Frequentist/Bayesian | #1132 callback with "probability not certainty" |
| L03 | #1838 Machine Learning | #2731 K-Means Clustering |
| L04 | #1885 Ensemble Model | Callback quote |
| L05 | Relevant PCA/dimensionality | Closing callback |
| L06 | Relevant embeddings/RL | Closing callback |

Attribution format: `\bottomnote{XKCD \#NNNN by Randall Munroe (CC BY-NC 2.5)}`

## 6. Formula Introduction Protocol

### 6.1 Motivate-Visualize-Formalize (MVF) Sequence

Every major formula follows this 3-step sequence:

1. **Motivate**: Plain-English statement of what we need and why
   - "We need a way to measure how wrong our predictions are"
2. **Visualize**: Chart or diagram showing the concept
   - Residual plot showing errors between points and line
3. **Formalize**: The formula with term-by-term explanation
   - $\text{RMSE} = \sqrt{\frac{1}{n}\sum(y_i - \hat{y}_i)^2}$

### 6.2 Term Definition Requirements

When a formula introduces new notation:
- Every Greek letter gets a plain-English label in italics
- Every subscript is explained
- A worked numerical example follows immediately

Example (L01 overview):
```latex
\begin{equation}
  y = \beta_0 + \beta_1 x_1 + \cdots + \beta_p x_p + \varepsilon
\end{equation}
\begin{itemize}
  \item $y$: target variable (house price)
  \item $x_1, \ldots, x_p$: features (size, bedrooms, age)
  \item $\beta_0, \ldots, \beta_p$: coefficients to learn
  \item $\varepsilon$: random error term
\end{itemize}
```

### 6.3 Key Terms Block (for dense topics)

When 5+ new terms are introduced simultaneously (like PCA), use a dedicated "Key Terms" slide:

```latex
\begin{frame}[t]{Key Terms for [Topic]}
  \begin{description}
    \item[Term 1] Plain-English definition + formula
    \item[Term 2] Plain-English definition + formula
    ...
  \end{description}
\end{frame}
```

This was added to L05 deepdive for: variance, covariance matrix, eigenvector, eigenvalue, orthogonal, mean-centering.

## 7. Worked Example Patterns

### 7.1 Running Finance Example

Each lecture has a **consistent running example** from finance:

| Lecture | Running Example |
|---------|----------------|
| L01 | House price prediction (property valuation for banks) |
| L02 | Credit scoring / loan default prediction |
| L03 | Fraud detection (KNN) + customer segmentation (K-Means) |
| L04 | Fraud detection ensemble + credit risk features |
| L05 | Yield curve PCA + portfolio dimensionality |
| L06 | Financial text embeddings + trading RL agent |

### 7.2 Numerical Mini-Examples

Every major concept gets a concrete numerical example:

- L01: "A 100 sqm apartment: $50,000 + 200 \times 100 = 70,000$"
- L02: "$\sigma(0) = 0.5$ (50-50 chance). If $z = 2$, then $\sigma(2) = 0.88$ (88%)"
- L03: "Points (1,2) and (4,6): distance = $\sqrt{9+16} = 5$"
- L04: "Node with 800 legit, 200 fraud: $G = 1 - (0.8^2 + 0.2^2) = 0.32$"
- L05: "PCA by Hand: 5 data points, covariance = [[2.5,2.5],[2.5,2.5]], eigenvalues 5 and 0"

### 7.3 "By Hand" Worked Examples

For complex algorithms, a full step-by-step worked example on real numbers:
- L05: "PCA by Hand: A 2D Mini-Example" (5 points → mean → covariance → eigendecomposition → project)
- These use small enough numbers that students can verify with a calculator

## 8. Deepdive Architecture

### 8.1 Structure

```
Title → Outline → Opening Comic + context bridge →
Learning Objectives →
[Core sections: full math, proofs, algorithms] →
Implementation (scikit-learn) → Hands-on Exercise →
Key Takeaways → Closing Comic →
\appendix → Advanced Topics (proofs, theory, references)
```

### 8.2 Context Bridge (Slide 3)

The deepdive always has a "bridge slide" that:
- References what was covered in the overview
- States what the deepdive adds ("Now we go deeper")
- Lists 3 questions the deepdive will answer
- Uses the same XKCD comic as the overview (visual continuity)

### 8.3 Appendix Content

After `\appendix`, use `\section*{Advanced Topics}` (starred to hide from TOC):
- Full proofs of theorems stated in main body
- Mathematical derivations
- Convergence theory
- Finance application deep dives (CAPM, Basel framework)
- References and resources

Typical: 7-10 appendix slides.

## 9. Learning Objectives Design

### 9.1 Bloom's Taxonomy Levels 4-5

All learning objectives use action verbs at Bloom's levels 4-5:

| Level | Verbs Used |
|-------|-----------|
| 4 (Analyze) | Analyze, Compare, Contrast, Examine |
| 5 (Evaluate) | Evaluate, Critique, Prove, Derive |

**Never used**: Remember (1), Understand (2), Apply (3 -- except in finance context)

### 9.2 Four Objectives Per Lecture

Every lecture has exactly 4 learning objectives:
1. Mathematical/derivation objective (Derive, Prove)
2. Analysis objective (Analyze bias-variance, convergence)
3. Evaluation objective (Evaluate metrics, model quality)
4. Application/comparison objective (Compare methods, Apply to finance)

### 9.3 Format

```latex
\begin{enumerate}
  \item \textbf{Derive} the OLS estimator and prove its optimality...
  \item \textbf{Analyze} gradient descent convergence...
  \item \textbf{Evaluate} regression diagnostics...
  \item \textbf{Compare} regularization strategies...
\end{enumerate}
\vspace{0.5em}
\textbf{Finance Applications:} [specific applications]
\bottomnote{Bloom's Levels 4--5: Analyze, Evaluate, Derive}
```

## 10. Comparison and Decision Slides

### 10.1 Comparison Tables

Used extensively for method tradeoffs:
- Ridge vs Lasso vs Elastic Net (L01 deepdive)
- Normal Equation vs Gradient Descent (L01)
- KNN vs K-Means (L03)
- Elbow vs Silhouette vs Gap Statistic (L03 deepdive)
- ROC vs Precision-Recall (L02 deepdive)

Format: `\begin{tabular}{lll} \toprule ... \bottomrule \end{tabular}`

### 10.2 Decision Flowchart Charts

Every lecture ends with a decision flowchart (`chart.py` generating `chart.pdf`) showing when to use each method. These are in the last chart folder (e.g., `07_decision_flowchart/`, `08_decision_flowchart/`).

### 10.3 "When to Use" Slides

Two-column format:
```latex
\textbf{Best When}
\begin{itemize}
  \item [condition 1]
  \item [condition 2]
\end{itemize}
\textbf{Consider Alternatives When}
\begin{itemize}
  \item [condition 1]
  \item [condition 2]
\end{itemize}
```

## 11. Hands-On Exercise Design

### 11.1 Three Progressive Exercises

Every lecture has exactly 3 exercises:
1. **From scratch**: Implement the algorithm manually (e.g., "Implement OLS from scratch")
2. **With library**: Use scikit-learn on a finance dataset
3. **Critical evaluation**: Compare, tune, or evaluate (e.g., "Compare distance metrics")

### 11.2 Format

```latex
\begin{frame}[t]{Hands-on Exercise}
\textbf{Open the Colab Notebook}
\begin{enumerate}
  \item \textbf{Exercise 1:} [from scratch task]
  \item \textbf{Exercise 2:} [scikit-learn task with finance data]
  \item \textbf{Exercise 3:} [evaluation/comparison task]
\end{enumerate}
\bottomnote{[time estimate or progression hint]}
\end{frame}
```

## 12. Slide Layout Patterns

### 12.1 Common Layouts

| Layout | When Used | Example |
|--------|-----------|---------|
| Two columns text | Comparison, pros/cons | Ridge vs Lasso |
| Two columns math | Definition + example | Model formula + worked example |
| Three-way split | Three alternatives | Ridge, Lasso, Elastic Net |
| Chart + text | Concept visualization | Gradient descent + explanation |
| Full-size chart | Key visualization | Decision flowchart |
| Step-by-step | Algorithm, process | "How the computer learns" |
| Definition-example | New concept introduction | Matrix notation + design matrix |
| Comparison table | Method differences | KNN vs K-Means |
| Pros/cons | Decision support | When to use linear regression |

### 12.2 Column Widths

- Two-column: `\column{0.48\textwidth}` each
- Chart + text: chart `0.55\textwidth`, text `0.42\textwidth`
- Three-way: `\column{0.30\textwidth}` each

## 13. Algorithmic Pseudocode

### 13.1 When to Use

Every major algorithm gets a pseudocode slide in the deepdive:
- Gradient descent (L01, L02)
- KNN classification (L03)
- Lloyd's K-Means algorithm (L03)
- PCA algorithm (L05)

### 13.2 Format

```latex
\begin{algorithmic}[1]
\STATE \textbf{Input}: ...
\STATE Initialize ...
\FOR{$t = 1$ to $T$}
  \STATE ... computation ...
  \IF{convergence criterion}
    \STATE \textbf{break}
  \ENDIF
\ENDFOR
\STATE \textbf{return} result
\end{algorithmic}
\bottomnote{In practice, use [library] for ... [practical note]}
```

## 14. Finance Integration Patterns

### 14.1 Finance Application Slides

Each lecture has 2-3 dedicated finance application slides:
- L01: Property valuation, CAPM
- L02: Credit scoring, Basel PD, scorecards
- L03: RFM segmentation, fraud detection with imbalance
- L04: Feature importance for audit, regulatory compliance
- L05: Yield curve factors, portfolio risk
- L06: Financial text analysis, trading agents

### 14.2 Regulatory Context

Banking regulations referenced where applicable:
- Basel II/III for PD estimation (L02)
- ECOA/GDPR for interpretability (L04)
- Capital requirements (L02 credit scoring)

### 14.3 Cost Asymmetry

Finance examples consistently emphasize cost asymmetry:
- FP vs FN costs in fraud detection
- Type I vs Type II errors in credit decisions
- This motivates threshold tuning, cost-sensitive metrics

## 15. Technical Standards

### 15.1 Beamer Configuration

```latex
\documentclass[8pt,aspectratio=169]{beamer}
\usetheme{Madrid}
% Custom ML colors: mlpurple, mlblue, mlorange, mlgreen, mlred, mlgray
% Custom footer: Methods and Algorithms | MSc Data Science | page/total
% \bottomnote{} command on every slide
% \highlight{} for orange bold emphasis
% compactlist environment for dense slides
```

### 15.2 Slide Count Budget

| Component | Slides |
|-----------|--------|
| Overview: Zone 1 (intro) | 6-10 |
| Overview: Zone 2 (core) | 10-14 |
| Overview: Zone 3 (wrap-up) | 3-5 |
| **Overview total** | **20-26** |
| Deepdive: main body | 35-45 |
| Deepdive: appendix | 7-10 |
| **Deepdive total** | **42-55** |

### 15.3 Overflow Prevention

- Max 3-4 bullets per slide
- `compactlist` environment for 5+ items
- Charts at `0.55\textwidth` (not wider) when text accompanies
- `\small` or `\footnotesize` only for references and tables
- Compile with `pdflatex -interaction=nonstopmode` and check for "Overfull"

## 16. Cross-Lecture Consistency

### 16.1 Structural Elements Present in ALL Lectures

- [ ] Title page → Outline → Opening comic with SCQ
- [ ] Learning Objectives (4 items, Bloom's 4-5)
- [ ] PMSP section structure (overview)
- [ ] Finance application slides (2-3)
- [ ] Comparison table for methods
- [ ] Decision flowchart chart
- [ ] Hands-on exercise (3 progressive tasks)
- [ ] Key Takeaways (two-column)
- [ ] Closing comic callback
- [ ] References (in appendix or final slide)
- [ ] `\bottomnote{}` on every single frame

### 16.2 Naming Conventions

- Files: `L0X_overview.tex`, `L0X_deepdive.tex`
- Charts: `NN_descriptive_name/chart.py` → `chart.pdf`
- Images: `images/NNNN_xkcd_name.png`
- Slide comments: `% SLIDE N: Description` or `% SLIDE N: Title (Layout NN)`

### 16.3 Section Names

Overviews consistently use: Introduction → Problem → Method → Solution → Practice → Summary

Deepdives use topic-specific sections but always include:
- Mathematical Foundations (early)
- Implementation (late, with scikit-learn code)
- Practice + Summary (final)
- Appendix: Advanced Topics (after `\appendix`)
