# HOSTILE CONTENT REVIEW PLAN: L02 - Logistic Regression

**Plan Created:** 2026-02-04
**Reviewer:** Prometheus (Strategic Planning Consultant)
**Target Files:**
- `slides/L02_Logistic_Regression/L02_overview.tex` (243 lines, ~12 slides)
- `slides/L02_Logistic_Regression/L02_deepdive.tex` (682 lines, ~35 slides)
- `slides/L02_Logistic_Regression/L02_instructor_guide.md` (152 lines)

**Review Objective:** Ruthlessly evaluate L02 content for MSc-level rigor, finance applicability, and pedagogical completeness.

---

## EXECUTIVE SUMMARY OF INITIAL OBSERVATIONS

Based on initial file review, the following RED FLAGS are already apparent:

| Issue | Severity | Location |
|-------|----------|----------|
| **TBD placeholder in overview** | CRITICAL | Line 220: `[TBD]` for Colab link |
| **No statistical inference** | CRITICAL | Missing Wald test, LR test, standard errors |
| **Generic credit scoring** | HIGH | Mentions it but no Basel, scorecard development |
| **Missing deviance** | HIGH | No null deviance, residual deviance |
| **Overview duplicates deepdive** | MEDIUM | Sigmoid, decision boundary shown twice |

---

## SECTION 1: CONTENT ACCURACY AUDIT (30 points)

### 1.1 Mathematical Formulas Check (15 points)

**Items to Verify:**

| Formula | Location | Check For |
|---------|----------|-----------|
| Sigmoid function | Overview L155, Deepdive L121-122 | Correct: $\sigma(z) = \frac{1}{1+e^{-z}}$ |
| Log-likelihood | Deepdive L162 | Sign correct? Should be SUM of log probs |
| Cross-entropy loss | Deepdive L171 | Negative sign present? Average (1/n) included? |
| Gradient (matrix form) | Deepdive L182-183 | Correct: $\nabla = \frac{1}{n}X^T(p-y)$ |
| Odds ratio formula | Deepdive L140-148 | $e^{w_j}$ interpretation correct? |
| Softmax | Deepdive L262 | Normalization correct? |
| Brier score | Deepdive L360 | Correct: MSE between prob and outcome |
| L1/L2 penalty | Deepdive L393-400 | Correct formulations? |

**Scoring Rubric:**
- 15/15: All formulas mathematically correct
- 10/15: 1-2 minor errors (wrong sign, missing constant)
- 5/15: 3+ errors or 1 major conceptual error
- 0/15: Fundamental formula is wrong

### 1.2 Misleading Simplifications (10 points)

**Check for these COMMON ERRORS in logistic regression teaching:**

| Potential Issue | Where to Check | What's Wrong |
|-----------------|----------------|--------------|
| "Logistic regression assumes linearity" | Deepdive Decision Boundaries section | It assumes linearity in LOG-ODDS, not in raw probabilities |
| "Cross-entropy guarantees global optimum" | Deepdive L172, Overview L171 | TRUE, but only for unregularized case |
| "Coefficients show feature importance" | Deepdive L521-535 | MISLEADING without standardization caveat |
| "AUC = probability interpretation" | Deepdive L312 | Correct but often misunderstood |
| "Logistic regression is well-calibrated" | Deepdive L363-367 | Only ASYMPTOTICALLY; finite samples may not be |

**Scoring Rubric:**
- 10/10: No misleading statements, all caveats included
- 7/10: 1 oversimplification without caveat
- 4/10: 2-3 oversimplifications
- 0/10: Major conceptual misrepresentation

### 1.3 Consistency Between Files (5 points)

**Cross-Reference Check:**

| Topic | Overview Says | Deepdive Says | Consistent? |
|-------|---------------|---------------|-------------|
| Sigmoid definition | L155: $\sigma(z) = 1/(1+e^{-z})$ | L121: same | Check notation |
| Decision boundary | L163: $w'x + b = 0$ | L211: $w^Tx + b \geq 0$ | Notation match? |
| Cross-entropy | L176: "penalizes confident wrong predictions" | L172: mathematical form | Aligned? |
| Class imbalance | L196: "common in fraud detection" | L482-500: detailed solutions | Consistent advice? |

**Scoring Rubric:**
- 5/5: Perfect consistency
- 3/5: Minor notation differences
- 0/5: Contradictory statements

---

## SECTION 2: LEARNING OBJECTIVES ALIGNMENT (20 points)

### 2.1 Stated Objectives vs. Actual Content

**From L02_overview.tex lines 112-117:**

| Objective | Claim | Evidence Required | Present? |
|-----------|-------|-------------------|----------|
| "Explain how logistic regression models binary outcomes" | Understand level | Sigmoid + probability interpretation | TBD |
| "Derive the maximum likelihood estimation" | Apply level | Step-by-step MLE derivation | TBD |
| "Interpret classification metrics" | Analyze level | Precision, recall, AUC explained with examples | TBD |
| "Apply logistic regression for credit scoring" | Apply level | Credit-specific example with coefficients | TBD |

### 2.2 Bloom's Level Verification

**For each objective, verify:**

| Objective | Claimed Bloom Level | Actual Content Depth | Match? |
|-----------|--------------------|--------------------|--------|
| Explain logistic regression | Understand | ? | TBD |
| Derive MLE | Apply (means DO IT, not just show) | ? | TBD |
| Interpret metrics | Analyze | ? | TBD |
| Apply to credit scoring | Apply | ? | TBD |

**CRITICAL CHECK:** Does the content enable students to ACTUALLY derive MLE, or does it just SHOW the derivation?

**Scoring Rubric:**
- 20/20: All 4 objectives fully addressed at correct Bloom level
- 15/20: 3/4 objectives met
- 10/20: 2/4 objectives met
- 5/20: 1/4 objectives met
- 0/20: None achieved

---

## SECTION 3: MSc LEVEL APPROPRIATENESS (20 points)

### 3.1 Statistical Inference for Logistic Regression (10 points)

**MSc students MUST understand:**

| Topic | Expected Coverage | Found In? |
|-------|-------------------|-----------|
| Standard errors of coefficients | Formula: $SE(\hat{\beta})$ from Fisher Information | NOT FOUND |
| Wald test for coefficients | $z = \hat{\beta}/SE(\hat{\beta})$ | NOT FOUND |
| Likelihood ratio test | $\Lambda = -2(\ell_{\text{null}} - \ell_{\text{full}})$ | NOT FOUND |
| Deviance | Residual deviance, null deviance | Deepdive L671 mentions "statsmodels for statistical inference" but NO CONTENT |
| Confidence intervals for odds ratios | $\exp(\hat{\beta} \pm z_{\alpha/2} \cdot SE)$ | NOT FOUND |
| p-values for predictors | Individual predictor significance | NOT FOUND |

**VERDICT ON INITIAL SCAN:** The slides mention "derive MLE" but provide NO statistical inference infrastructure. This is UNDERGRADUATE level, not MSc.

**Comparison to L01 pattern:** L01 was criticized for missing "Gauss-Markov conditions" equivalent. For L02, the equivalent is missing inference (Wald test, LR test, deviance).

**Scoring Rubric:**
- 10/10: All 6 topics covered
- 7/10: 4-5 topics covered
- 4/10: 2-3 topics covered
- 0/10: 0-1 topics covered

### 3.2 Advanced Model Diagnostics (5 points)

**Beyond basic metrics, MSc should cover:**

| Topic | Expected | Present? |
|-------|----------|----------|
| Hosmer-Lemeshow test | Goodness-of-fit | NOT FOUND |
| VIF for multicollinearity | Before fitting | NOT FOUND (only mentioned for L1) |
| Residual plots for logistic | Deviance residuals, Pearson residuals | NOT FOUND |
| Cook's distance for logistic | Influential observations | NOT FOUND |
| Link function alternatives | Probit, complementary log-log | NOT FOUND |

**Scoring Rubric:**
- 5/5: 4+ topics covered
- 3/5: 2-3 topics covered
- 0/5: 0-1 topics covered

### 3.3 Theoretical Depth (5 points)

**Expected for MSc level:**

| Topic | Check |
|-------|-------|
| Why logistic vs probit? | NOT FOUND |
| Newton-Raphson / IRLS | Mentioned at L459 ("L-BFGS") but not explained |
| Fisher scoring | NOT FOUND |
| Separation problems (perfect prediction) | NOT FOUND |
| Firth's penalized likelihood | NOT FOUND |

**Scoring Rubric:**
- 5/5: 3+ topics covered with depth
- 3/5: 1-2 topics covered
- 0/5: Only surface-level content

---

## SECTION 4: FINANCE USE CASE DEPTH (15 points)

### 4.1 Credit Scoring Reality Check (8 points)

**What the slides claim:** "Finance Application: Credit default prediction" (L119)

**What MSc-level finance coverage REQUIRES:**

| Topic | Expected Coverage | Found? |
|-------|-------------------|--------|
| Basel II/III IRB requirements | Regulatory context for PD models | NOT FOUND |
| Scorecard development | WoE, IV, binning | NOT FOUND (only binning mentioned at L515) |
| Point allocation | How odds convert to points | NOT FOUND |
| Validation requirements | OoT, OoS, stability tests | NOT FOUND |
| Model governance | Documentation, monitoring | NOT FOUND (only "interpretability" mentioned) |
| Economic capital | PD, LGD, EAD relationship | NOT FOUND |

**INSTRUCTOR GUIDE CHECK (L02_instructor_guide.md):**
- Line 35: "Basel regulations on model interpretability" - MENTIONED in discussion points
- But NO slide content delivers this

**Scoring Rubric:**
- 8/8: 5+ finance topics with worked examples
- 5/8: 3-4 finance topics mentioned
- 2/8: 1-2 finance topics mentioned
- 0/8: Generic "credit scoring" without substance

### 4.2 Real Data Examples (4 points)

**Check for:**

| Item | Expected | Found? |
|------|----------|--------|
| Actual credit dataset characteristics | n, p, class distribution | NOT FOUND |
| Coefficient interpretation in credit context | "Age coefficient = 0.3 means..." | Deepdive L529-533 has generic example |
| Cost matrix for credit | FP cost vs FN cost with dollar values | NOT FOUND (only qualitative at L231-232) |
| Cutoff selection for credit | How banks actually choose thresholds | Qualitative only |

**Scoring Rubric:**
- 4/4: All with realistic numbers
- 2/4: Some examples but generic
- 0/4: No real data examples

### 4.3 Finance Vocabulary (3 points)

**MSc Data Science for Finance should use:**

| Term | Expected | Used? |
|------|----------|-------|
| PD (Probability of Default) | Primary metric | NOT FOUND (uses "P(y=1)") |
| Gini coefficient (not AUC*2-1) | Industry standard | NOT FOUND |
| KS statistic | Model discrimination | NOT FOUND |
| AR (Accuracy Ratio) | Same as Gini | NOT FOUND |
| Vintage analysis | Portfolio performance | NOT FOUND |

**Scoring Rubric:**
- 3/3: 3+ finance-specific terms used
- 1/3: 1-2 finance terms
- 0/3: Generic ML vocabulary only

---

## SECTION 5: PEDAGOGICAL FLOW (10 points)

### 5.1 Overview vs Deepdive Redundancy (5 points)

**Check for unnecessary duplication:**

| Topic | In Overview | In Deepdive | Redundant? |
|-------|-------------|-------------|------------|
| Sigmoid function | Slide 4 (L146-156) | Slide 2 (L125-135) | YES - same chart, same points |
| Decision boundary | Slide 5 (L159-164) | Slide 9 (L207-213) | YES - same chart |
| Cross-entropy | Slide 6 (L167-177) | Slide 5 (L166-173) | YES - overlapping |
| ROC curve | Slide 7 (L182-189) | Slides 15-16 (L297-324) | PARTIAL - deepdive adds more |
| Precision-Recall | Slide 8 (L192-197) | Slide 17-18 (L326-348) | PARTIAL |
| Confusion matrix | Slide 9 (L200-205) | Slides 13-14 (L273-295) | YES - overlapping |

**VERDICT:** Overview should INTRODUCE concepts; Deepdive should DEVELOP them. Current state: Overview and Deepdive first 10 slides are nearly identical.

**Scoring Rubric:**
- 5/5: Clear differentiation, overview introduces, deepdive extends
- 3/5: Some redundancy but value in both
- 0/5: Deepdive repeats overview without adding depth

### 5.2 Logical Progression (3 points)

**Expected flow for logistic regression:**

```
1. Motivation (why not linear?)
2. Model formulation (sigmoid, log-odds)
3. Estimation (MLE, gradient)
4. Inference (standard errors, tests) <- MISSING
5. Evaluation (metrics)
6. Regularization
7. Implementation
8. Practice
```

**Actual flow (Deepdive):**
1. From Linear to Logistic (OK)
2. Sigmoid (OK)
3. Odds and Log-Odds (OK)
4. MLE (OK)
5. Cross-Entropy (OK)
6. Gradient (OK)
7. Decision Boundaries (OK)
8. Evaluation Metrics (OK - but no inference)
9. Regularization (OK)
10. Implementation (OK)
11. Practice (OK)

**Gap:** Inference step completely missing between Estimation and Evaluation.

**Scoring Rubric:**
- 3/3: Logical flow with all key steps
- 2/3: Minor gaps or reordering
- 0/3: Major gaps (like missing inference)

### 5.3 Practice Integration (2 points)

**Check notebook alignment:**

| Slide Content | Notebook Exercise | Aligned? |
|---------------|-------------------|----------|
| MLE derivation | "Implement from scratch" | TBD |
| Regularization | "L2 regularization" | TBD |
| Class imbalance | "class weights" | TBD |
| Interpretation | "interpret coefficients" | TBD |

**Overview issue:** Line 220 has `[TBD]` placeholder for Colab link - UNPROFESSIONAL.

**Scoring Rubric:**
- 2/2: All exercises align with slides, no TBD markers
- 1/2: Alignment but TBD markers present
- 0/2: Misalignment or missing exercises

---

## SECTION 6: COMPLETENESS CHECK (5 points)

### 6.1 Essential Topics Checklist

**For logistic regression at MSc level:**

| Topic | Essential? | Present? | Quality |
|-------|------------|----------|---------|
| Sigmoid function | Yes | Yes | Good |
| Log-odds interpretation | Yes | Yes | Good |
| MLE derivation | Yes | Yes | Shown but not derived by student |
| Gradient descent | Yes | Yes | Good |
| Decision boundary | Yes | Yes | Good |
| Confusion matrix | Yes | Yes | Good |
| Precision/Recall | Yes | Yes | Good |
| ROC/AUC | Yes | Yes | Good |
| **Standard errors** | Yes | **NO** | **MISSING** |
| **Hypothesis testing** | Yes | **NO** | **MISSING** |
| Regularization | Yes | Yes | Good |
| Multiclass (softmax) | Yes | Yes | Brief |
| Class imbalance | Yes | Yes | Good |
| Calibration | Yes | Yes | Brief |
| **Deviance** | Yes | **NO** | **MISSING** |
| Feature engineering | Helpful | Yes | Brief |
| Solver selection | Helpful | Yes | Good |
| Convergence issues | Helpful | Yes | Good |

**Missing Essential Topics:**
1. Standard errors of coefficients
2. Hypothesis testing (Wald, LR)
3. Deviance (null, residual)

### 6.2 Chart Inventory

**7 charts expected, check all present:**

| Chart | Path | Purpose | Present? |
|-------|------|---------|----------|
| 01_sigmoid_function | chart.pdf | Sigmoid curve | YES |
| 02_decision_boundary | chart.pdf | Linear boundary | YES |
| 03_log_loss | chart.pdf | Cross-entropy visualization | YES |
| 04_roc_curve | chart.pdf | ROC curve | YES |
| 05_precision_recall | chart.pdf | PR curve | YES |
| 06_confusion_matrix | chart.pdf | Confusion matrix viz | YES |
| 07_decision_flowchart | chart.pdf | When to use | YES |

**All charts present. No missing visuals.**

### 6.3 TBD/Placeholder Check

**Search results:**

| Location | Text | Issue |
|----------|------|-------|
| Overview L220 | `[TBD]` | Incomplete Colab link |
| Deepdive L628 | GitHub link placeholder | Check if real |

**Scoring Rubric:**
- 5/5: All essential topics, no placeholders
- 3/5: 1-2 missing topics OR 1 placeholder
- 0/5: 3+ missing essential topics OR multiple placeholders

---

## SECTION 7: SCORING RUBRIC SUMMARY

| Category | Max Points | Criteria |
|----------|------------|----------|
| **Content Accuracy** | 30 | Math correct, no misleading statements, consistent |
| **Learning Objectives** | 20 | All 4 objectives achieved at correct Bloom level |
| **MSc Level** | 20 | Statistical inference, diagnostics, theory depth |
| **Finance Use Case** | 15 | Real credit scoring, Basel, scorecard development |
| **Pedagogical Flow** | 10 | No redundancy, logical progression, practice aligned |
| **Completeness** | 5 | All essential topics, no placeholders |
| **TOTAL** | 100 | |

### Grading Scale

| Score | Grade | Interpretation |
|-------|-------|----------------|
| 90-100 | A | Ready for MSc delivery |
| 80-89 | B | Minor revisions needed |
| 70-79 | C | Significant gaps, usable with instructor supplements |
| 60-69 | D | Major revision required |
| < 60 | F | Rewrite needed |

---

## SECTION 8: PREDICTED ISSUES (Based on L01 Patterns)

From L01 hostile review, these patterns are likely to recur:

| L01 Issue | L02 Equivalent | Initial Evidence |
|-----------|----------------|------------------|
| Missing Gauss-Markov | Missing statistical inference (Wald, LR, deviance) | Confirmed: not found |
| PMSP structure violation | Same structure issues | Deepdive uses custom sections |
| Generic finance examples | Credit scoring mentioned but not taught | Confirmed: generic |
| Feature scaling hidden | Mentioned at L197 but not main slide | Same pattern |
| TBD placeholders | Overview L220 | Confirmed |
| Chart width deviations | Need to check | TBD |
| Negative vspace hacks | Need to check | TBD |

---

## SECTION 9: SPECIFIC ITEMS TO VERIFY

### 9.1 Line-by-Line Checks (Overview)

| Line | Item | Check |
|------|------|-------|
| 155 | Sigmoid formula | Verify correct |
| 163 | Decision boundary notation | w'x vs w^Tx consistency |
| 171 | Cross-entropy convexity claim | Is it always true? |
| 188 | AUC interpretation | Correct probability statement |
| 220 | TBD marker | FAIL - must be complete |

### 9.2 Line-by-Line Checks (Deepdive)

| Line | Item | Check |
|------|------|-------|
| 121-122 | Sigmoid formula | Correct |
| 162 | Log-likelihood formula | Check sign |
| 171 | Cross-entropy formula | Check negative, average |
| 182-183 | Gradient formula | Check matrix dimensions |
| 262 | Softmax formula | Check normalization |
| 360 | Brier score | Check formula |
| 393-400 | L1/L2 penalties | Check formulas |
| 671 | statsmodels reference | But no CONTENT about what to use it for |

### 9.3 Cross-Reference with Instructor Guide

| Guide Says | Slides Must Have | Present? |
|------------|------------------|----------|
| "Basel regulations on model interpretability" (L35) | Basel content slide | NO |
| "Cost of false positives vs false negatives" (L34) | Cost matrix with numbers | NO |
| "Coefficient interpretation in credit context" (L86) | Credit-specific coefficient example | PARTIAL |
| "scikit-learn: LogisticRegression" (L72) | Implementation code | YES |

---

## SECTION 10: REVIEW EXECUTION CHECKLIST

### Phase 1: Mathematical Accuracy (30 min)

- [ ] Verify all formulas in Section 1.1
- [ ] Check for misleading statements in Section 1.2
- [ ] Cross-reference overview/deepdive consistency

### Phase 2: Learning Objectives (20 min)

- [ ] Map each objective to specific slides
- [ ] Verify Bloom's level depth
- [ ] Check if students can ACTUALLY derive MLE

### Phase 3: MSc Level (30 min)

- [ ] Search for statistical inference content
- [ ] Check for advanced diagnostics
- [ ] Evaluate theoretical depth

### Phase 4: Finance (20 min)

- [ ] Count finance-specific examples
- [ ] Check for Basel/scorecard content
- [ ] Verify vocabulary alignment

### Phase 5: Pedagogy (15 min)

- [ ] Analyze overview/deepdive overlap
- [ ] Verify logical flow
- [ ] Check practice alignment

### Phase 6: Completeness (10 min)

- [ ] Essential topics checklist
- [ ] TBD marker search
- [ ] Chart verification

### Phase 7: Scoring (15 min)

- [ ] Assign scores per category
- [ ] Calculate total
- [ ] Determine grade

---

## SECTION 11: OUTPUT REQUIREMENTS

The hostile review report should produce:

1. **Compliance Matrix** - What matches, what deviates
2. **Critical Issues List** - Prioritized by severity
3. **Score Breakdown** - Per category with justification
4. **Specific Fix List** - Line numbers, current, fix to
5. **Content Gap Analysis** - What's missing for MSc level
6. **Finance Gap Analysis** - What's missing for finance focus
7. **Verdict** - PASS/FAIL with conditions

---

## APPENDIX A: COMPARISON TO L01 REVIEW

| Criterion | L01 Score | L02 Expected |
|-----------|-----------|--------------|
| PMSP Structure | 0/20 FAIL | Similar issues expected |
| Business Context | 0/5 FAIL | Slightly better (credit mentioned) |
| Chart Widths | 8/10 | Need to verify |
| Content Accuracy | Not scored separately | New focus area |
| MSc Level | Not scored separately | CRITICAL gap expected |

---

## APPENDIX B: EXPECTED VERDICT

Based on initial scan, **PREDICTED SCORE: 55-65/100 (D-C range)**

**Primary failures expected:**
1. Missing statistical inference (Wald, LR, deviance) - will cost 10 points
2. Generic finance content (no Basel, scorecard) - will cost 8 points
3. TBD placeholder - will cost 2 points
4. Redundancy between overview/deepdive - will cost 3 points

**Primary strengths expected:**
1. Mathematical formulas appear correct
2. Good coverage of evaluation metrics
3. Regularization well covered
4. Class imbalance addressed

---

**PLAN_READY: .omc/plans/L02-hostile-content-review.md**
