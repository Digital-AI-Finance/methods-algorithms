# Hostile Content Review Plan: ALL Lectures (L01-L06)

## Review Scope
- **Persona**: Hostile external academic examiner
- **Standard**: MSc Data Science, various backgrounds, no pre-knowledge assumed
- **Focus**: Content accuracy, completeness, MSc rigor, finance applications
- **Files Reviewed**: 12 .tex files (overview + deepdive per lecture), 6 instructor guides

## Executive Summary

| Lecture | Score | Grade | Verdict | CRITICALs | MAJORs |
|---------|-------|-------|---------|-----------|--------|
| L01 Introduction & Linear Regression | 72/100 | C | CONDITIONAL PASS | 4 | 6 |
| L02 Logistic Regression | 68/100 | C+ | CONDITIONAL PASS | 4 | 6 |
| L03 KNN & K-Means | 64/100 | C | CONDITIONAL PASS | 3 | 6 |
| L04 Random Forests | 68/100 | C+ | CONDITIONAL PASS | 3 | 6 |
| L05 PCA & t-SNE | 62/100 | C | CONDITIONAL PASS | 3 | 5 |
| L06 Embeddings & RL | 72/100 | C+ | CONDITIONAL PASS | 2 | 8 |
| **COURSE AVERAGE** | **67.7/100** | **C+** | **CONDITIONAL PASS** | **19** | **37** |

**Overall Verdict: CONDITIONAL PASS - Significant remediation required across all lectures.**

> **Calibration Note (post-Critic review):** L03 and L04 were re-scored from equal 66 to 64/68 respectively. L04's post-fix state includes complete variance derivation, class imbalance coverage, corrected attribution, and proper pseudocode — measurably stronger than L03 which still lacks any proofs/derivations. L06 scores 72 (tied with L01) because its 8 MAJORs are individually less severe than L01's 4 CRITICALs; L06's CRITICALs (LOs, stale guide) are structural rather than content-gap issues. L01's overview is exempted from S1 (chart gallery) as it contains 7 equation environments and 14 inline math expressions.

## Scoring Rubric (100 points)

| Category | Weight | Description |
|----------|--------|-------------|
| Formula Verification | 15 | All formulas correct, complete, properly notated |
| Misleading Statements | 10 | No false claims, no oversimplifications |
| Algorithm Correctness | 5 | Pseudocode/steps accurate |
| Learning Objectives | 20 | MSc-appropriate Bloom's levels, all met by content |
| MSc Level | 20 | Proofs, derivations, formal rigor |
| Finance Use Cases | 15 | Substantive, quantitative, realistic |
| Pedagogical Flow | 10 | Logical progression, prerequisites clear |
| Completeness | 5 | No critical topic omissions |
| Chart Quality Bonus | +5 | Professional, data-driven, accurate |

---

## CROSS-CUTTING SYSTEMIC ISSUES

These issues appear in **3+ lectures** and should be addressed as course-wide fixes:

### S1. Overview Decks Are Chart Galleries (5/6 lectures)
**Severity: CRITICAL | Affects: L02, L03, L04, L05, L06**

Five of six overview decks rely almost entirely on charts with bullet-point commentary. L02 has only 2 inline math formulas in footnotes; L03-L06 overviews contain zero mathematical formulas. **Exception: L01's overview contains 7 equation environments and 14 inline math expressions** (regression model, OLS closed form, gradient descent, R-squared, RMSE) — it is the only overview that meets MSc expectations for mathematical content.

At MSc level, an overview should contain key equations and formal problem statements. Students who only attend the overview session leave without seeing formulas.

**Fix**: Add 3-5 key equations to each of L02-L06 overview decks (the defining formula, the loss function, the optimization objective at minimum). L01 is already adequate.

### S2. Learning Objectives Below MSc Bloom's Taxonomy (ALL 6 lectures)
**Severity: CRITICAL | Affects: L01-L06**

LOs consistently use Level 2-3 verbs ("Explain", "Describe", "Apply") instead of MSc-appropriate Level 4-5 ("Analyze", "Evaluate", "Derive", "Prove"). This is the single most consistent deficiency across the entire course.

**Fix**: Rewrite all LOs to target Bloom's Level 4-5. Examples:
- "Explain OLS" → "Derive OLS estimator and prove its optimality under Gauss-Markov"
- "Describe K-Means" → "Analyze K-Means convergence properties and evaluate initialization strategies"

### S3. Finance Examples Are Qualitative, Not Quantitative (5/6 lectures)
**Severity: MAJOR | Affects: L01-L06 (varying degree)**

Finance applications are mentioned in bullet points ("used in credit scoring", "applied to portfolio management") but rarely include worked numerical examples with real-world parameters. An MSc Finance student expects to see actual calculations.

**Fix**: Add at least one fully worked numerical finance example per lecture (e.g., compute VaR using the model, classify a loan application step-by-step, compute portfolio weights).

### S4. Missing Proofs and Derivations (3/6 lectures)
**Severity: MAJOR | Affects: L03, L05, L06**

L03 contains zero proofs (Cover & Hart theorem and K-Means convergence are STATED but not proved). L05 is missing the SVD-PCA equivalence proof. L06 has partial derivations. **Note: L04 now has a complete variance derivation (post-fix) but still lacks CART splitting criterion derivation.** At MSc level, at least the central result of each lecture should have a formal proof or derivation.

**Fix**: Add proof/derivation of the core result in each lecture:
- L03: KNN consistency theorem proof sketch, K-Means convergence proof
- L04: CART splitting criterion derivation (variance derivation already present)
- L05: SVD-PCA equivalence proof (currently missing)
- L06: Skip-gram objective derivation (present but could be tighter)

### S5. Instructor Guide Timing Inconsistencies (4/6 lectures)
**Severity: MINOR | Affects: L02, L03, L04, L05**

Timing allocations in instructor guides sum to more than 180 minutes in several lectures. Some guides reference slides that don't exist or are stale relative to current slide content.

**Fix**: Audit all instructor guides against actual slide content and recalculate timings.

### S6. Algorithm/Algorithmic Packages Loaded But Unused (2/6 lectures)
**Severity: MINOR | Affects: L04, L05**

`\usepackage{algorithm}` and `\usepackage{algorithmic}` are loaded but no formal algorithm environments appear. **Note: L03 now uses `\begin{algorithmic}` for K-Means pseudocode (line 388) — correctly removed from this finding.** L04 and L05 still load but don't use these packages. Either add proper pseudocode or remove the packages.

---

## PER-LECTURE DETAILED FINDINGS

### L01: Introduction & Linear Regression (72/100)

**CRITICAL Issues:**
| ID | Issue | Description |
|----|-------|-------------|
| C1 | Gauss-Markov no proof | Theorem stated but not proved; MSc requires at least sketch |
| C2 | No F-test | Joint hypothesis testing completely absent |
| C3 | No OLS-MLE connection | MLE under normality not shown; fundamental MSc topic |
| C4 | No formal diagnostic tests | Breusch-Pagan, Durbin-Watson, Jarque-Bera absent |

**MAJOR Issues:**
| ID | Issue |
|----|-------|
| M1 | Elastic Net regularization path non-standard |
| M2 | CAPM application superficial (no numerical example) |
| M3 | LOs below MSc Bloom's levels |
| M4 | GD convergence analysis insufficient |
| M5 | LO mismatch (LOs promise more than delivered) |
| M6 | No hat matrix / leverage / Cook's distance |

**Strengths**: OLS derivation clean and correct, inference section solid, chart quality professional, VIF treatment correct.

---

### L02: Logistic Regression (68/100)

**CRITICAL Issues:**
| ID | Issue | Description |
|----|-------|-------------|
| C1 | No LRT formal presentation | Likelihood ratio test not derived |
| C2 | No Newton-Raphson/IRLS | Optimization algorithm not shown |
| C3 | LO2 "Derive MLE" not met | Content doesn't deliver what LO promises |
| C4 | Overview too thin | Only 12 content slides; needs more substance |

**MAJOR Issues:**
| ID | Issue |
|----|-------|
| M1 | No complete/quasi-complete separation coverage |
| M2 | Hessian matrix undefined |
| M3 | No AIC/BIC model selection |
| M4 | No Hosmer-Lemeshow test |
| M5 | Deviance residuals lack context |
| M6 | Gradient descent drops bias term |

**Strengths**: All formulas correct, inference additions strong, finance integration (Basel/scorecards) substantive, calibration coverage good.

---

### L03: KNN & K-Means (64/100)

**CRITICAL Issues:**
| ID | Issue | Description |
|----|-------|-------------|
| C1 | Overview is chart gallery | Zero formulas in 13 slides |
| C2 | Zero proofs/derivations | Not a single proof in entire lecture |
| C3 | LOs below MSc standard | All Level 2-3 Bloom's |

**MAJOR Issues:**
| ID | Issue |
|----|-------|
| M1 | Finance examples qualitative only |
| M2 | Gap statistic formula incomplete |
| M3 | NP-hardness of K-Means not mentioned |
| M4 | Weighted KNN formula non-standard |
| M5 | No bias-variance decomposition for KNN |
| M6 | DBSCAN/hierarchical clustering only name-dropped |

**Strengths**: All formulas correct, K-Means++ correctly cited with Arthur & Vassilvitskii, Hopkins statistic included, singleton silhouette convention correct.

---

### L04: Random Forests (68/100)

**CRITICAL Issues:**
| ID | Issue | Description |
|----|-------|-------------|
| C1 | Zero boosting coverage | AdaBoost, XGBoost, gradient boosting completely absent |
| C2 | No formal CART pseudocode | Decision tree splitting not formalized |
| C3 | ~~Bias-variance derivation incomplete~~ | **PARTIALLY FIXED**: Full variance derivation now present (lines 302-322). CART splitting derivation still absent. |

**MAJOR Issues:**
| ID | Issue |
|----|-------|
| M1 | LO2 "Implement" not achievable from slides alone |
| M2 | OOB ≈ LOOCV claim misleading (OOB ≈ 0.632 bootstrap) |
| M3 | Overview too thin for MSc |
| M4 | No SHAP values |
| M5 | MDI formula absent |
| M6 | Feature importance lacks formal statistical test description |

**Strengths**: All formulas correct, correlated variance derivation is strong, class imbalance treatment thorough, statistical inference for feature importance present.

---

### L05: PCA & t-SNE (62/100) — LOWEST SCORE

**CRITICAL Issues:**
| ID | Issue | Description |
|----|-------|-------------|
| C1 | 5 t-SNE charts FABRICATED | Charts use synthetic Gaussian blobs, not actual t-SNE on real data |
| C2 | Swiss roll & cluster charts also fabricated | Don't run actual algorithms |
| C3 | SVD-PCA equivalence not derived | Fundamental MSc-level proof missing |

**MAJOR Issues:**
| ID | Issue |
|----|-------|
| M1 | Instructor guide covariance formula omits centering (shows X^T X, should be X_c^T X_c) |
| M2 | No pseudocode for PCA or t-SNE |
| M3 | Yield curve PCA qualitative (no numerical example) |
| M4 | Parallel analysis incomplete |
| M5 | Overview has zero formulas |

**Strengths**: PCA optimality proof correct, Kaiser criterion correctly qualified as controversial, t-SNE KL divergence formulation admirably complete, PCA-Gaussian clarification correct.

---

### L06: Embeddings & RL (72/100) — POST-FIX

**CRITICAL Issues:**
| ID | Issue | Description |
|----|-------|-------------|
| C1 | LOs below MSc standard | Level 2-3 Bloom's verbs throughout |
| C2 | Instructor guide stale | References slides that no longer exist post-fix |

**MAJOR Issues:**
| ID | Issue |
|----|-------|
| M1 | Sharpe ratio as RL reward problematic (no transaction costs) |
| M2 | FinBERT 92% accuracy uncited |
| M3 | Reward/training curves synthetic |
| M4 | Q-table grid hardcoded |
| M5 | No pseudocode for Word2Vec or Q-learning |
| M6 | Statistical inference section is checklist format |
| M7 | Overview has zero formulas |
| M8 | Backtesting section honest but thin |

**Strengths**: Policy visualization now runs genuine Q-learning, negative sampling fully addressed, TD learning present, worked Q-learning example correct, static vs contextual embeddings clearly explained, DQN loss present.

---

## PRIORITIZED REMEDIATION PLAN

### Priority 1: CRITICAL Fixes (Must-Fix for MSc Accreditation)

| # | Action | Lectures | Effort | Est. Hours |
|---|--------|----------|--------|------------|
| 1 | Fix 5+ fabricated charts in L05 (run actual t-SNE/PCA) | L05 | HIGH | 8-10 |
| 2 | Add boosting section to L04 (AdaBoost + gradient boosting) — largest content gap in course | L04 | HIGH | 6-8 |
| 3 | Rewrite ALL learning objectives to Bloom's Level 4-5 | L01-L06 | MEDIUM | 4-6 |
| 4 | Add key formulas to L02-L06 overview decks (3-5 per deck; L01 already adequate) | L02-L06 | MEDIUM | 5-8 |
| 5 | Add LRT derivation and Newton-Raphson/IRLS (L02) | L02 | HIGH | 4-6 |
| 6 | Add Gauss-Markov proof sketch (L01) | L01 | MEDIUM | 2-3 |
| 7 | Add F-test and formal diagnostics (L01) | L01 | MEDIUM | 3-4 |
| 8 | Add at least one proof to L03 (Cover & Hart sketch, K-Means convergence) | L03 | MEDIUM | 3-4 |
| 9 | Derive SVD-PCA equivalence (L05) | L05 | MEDIUM | 2-3 |
| 10 | Add OLS-MLE connection (L01) — easy win for a CRITICAL | L01 | LOW | 1-2 |

### Priority 2: MAJOR Fixes (Required for Grade B)

| # | Action | Lectures | Effort |
|---|--------|----------|--------|
| 11 | Add worked numerical finance example per lecture | L01-L06 | MEDIUM |
| 12 | Add formal CART pseudocode (L04) | L04 | LOW |
| 13 | Add SHAP values section (L04) | L04 | MEDIUM |
| 14 | Fix OOB ≈ LOOCV claim (L04) | L04 | LOW |
| 15 | Add AIC/BIC model selection (L02) | L02 | LOW |
| 16 | Add Hosmer-Lemeshow test (L02) | L02 | LOW |
| 17 | Add bias-variance decomposition for KNN (L03) | L03 | MEDIUM |
| 18 | Add hat matrix / leverage / Cook's distance (L01) | L01 | MEDIUM |
| 19 | Add pseudocode throughout (L04, L05, L06); L03 already has K-Means pseudocode | L04, L05, L06 | LOW |
| 20 | Fix instructor guide covariance formula centering (X→X_c) (L05) | L05 | LOW |

### Priority 3: MODERATE/MINOR Fixes (Polish)

| # | Action | Lectures | Effort |
|---|--------|----------|--------|
| 21 | Audit all instructor guides for timing/content sync | L01-L06 | LOW |
| 22 | Remove unused algorithm/algorithmic packages | L04, L05 | LOW |
| 23 | Add separation coverage for logistic regression (L02) | L02 | LOW |
| 24 | Expand DBSCAN/hierarchical beyond name-drops (L03) | L03 | LOW |
| 25 | Add Gap statistic complete formula (L03) | L03 | LOW |

## Expected Score Impact

If Priority 1 fixes completed (~38-54 hours):
| Lecture | Current | Projected | Est. Hours |
|---------|---------|-----------|------------|
| L01 | 72 | 82-85 | 6-9 |
| L02 | 68 | 80-83 | 6-8 |
| L03 | 64 | 76-80 | 5-7 |
| L04 | 68 | 82-85 | 8-10 |
| L05 | 62 | 78-82 | 10-13 |
| L06 | 72 | 80-82 | 3-5 |
| **Average** | **67.7** | **~80-83** | **38-52** |

If Priority 1 + 2 fixes completed (~55-75 hours): **Average ~85-90/100 (Grade A-/A)**

> **Note**: L06 requires fewer hours because it was recently remediated (35→72). L05 requires the most because fabricated charts need complete rewrites.
