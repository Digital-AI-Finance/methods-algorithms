# L04 Hostile Review Report

## Executive Summary

- **Overall score: 90/100 (A-)**
- **Verdict: PASS (pending 1 CRITICAL single-line fix)**
- Critical issues: 1
- Major issues: 13
- Minor issues: 17

The L04 Decision Trees & Random Forests content is strong overall. The dt_full and dt_mini files are exemplary (96/100 each) with excellent beginner accessibility, correct math, and engaging pedagogy. The main weaknesses are: (1) the deepdive's text-only closing comic (CRITICAL), (2) rf_full having zero exercises across 31 slides, and (3) missing worked examples for advanced formulas (AdaBoost, XGBoost, MSE regression) in several files. All 6 files compile clean with zero Overfull warnings. All math verified correct.

## Per-File Scores

| File | A1 | A2 | A3 | A4 | A5 | A6 | A7 | B1 | B2 | B3 | B4 | B5 | B6 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| overview | 10 | 7 | 6 | 7 | 4 | 5 | 4 | 15 | 10 | 5 | 10 | 3 | 5 | **91** |
| deepdive | 8 | 7 | 6 | 5 | 4 | 4 | 3 | 15 | 10 | 5 | 10 | 2 | 5 | **84** |
| dt_full | 11 | 8 | 8 | 7 | 4 | 5 | 4 | 14 | 10 | 5 | 10 | 5 | 5 | **96** |
| dt_mini | 12 | 8 | 7 | 8 | 3 | 5 | 4 | 15 | 10 | 5 | 10 | 4 | 5 | **96** |
| rf_full | 9 | 7 | 5 | 4 | 3 | 4 | 3 | 14 | 10 | 5 | 10 | 3 | 5 | **82** |
| rf_mini | 11 | 8 | 4 | 7 | 3 | 5 | 4 | 15 | 10 | 5 | 10 | 4 | 5 | **91** |
| **Average** | **10.2** | **7.5** | **6.0** | **6.3** | **3.5** | **4.7** | **3.7** | **14.7** | **10** | **5** | **10** | **3.5** | **5** | **90** |

**Score interpretation:**
- PASS: >= 75 AND zero CRITICAL issues remaining
- Currently: 90/100 with 1 CRITICAL (single-line fix) -> PASS after remediation

## Critical Issues (Must-Fix)

1. **[CRITICAL]** `L04_deepdive.tex:956-968` -- Closing "comic" is a TEXT-ONLY quote ("Stir the pile of decision trees..."), NOT an actual image or TikZ comic. The XKCD #1838 image file already exists at `images/1838_machine_learning.png`.
   - **Fix**: Replace text-only frame with `\includegraphics[width=0.30\textwidth]{images/1838_machine_learning.png}` (same pattern as `L04_overview.tex:503`).

## Major Issues (13 total)

### Missing Worked Examples (7 issues)

2. **[MAJOR]** `L04_overview.tex:264-266` -- Variance reduction formula ($\rho\sigma^2 + \frac{1-\rho}{B}\sigma^2$) presented without worked numerical example. Add: "With B=500 trees and $\rho=0.05$: Var = $0.05\sigma^2 + 0.95/500 \cdot \sigma^2 = 0.052\sigma^2$."

3. **[MAJOR]** `L04_deepdive.tex:197-216` -- Regression Trees MSE section has no worked numerical example. Add: "Parent: [100,150,200], mean=150, MSE=1666.7. Split: left [100,150] MSE=625, right [200] MSE=0. Weighted MSE=416.7. Reduction=1250."

4. **[MAJOR]** `L04_deepdive.tex:696-712` -- AdaBoost weight formula ($\alpha_t = \frac{1}{2}\ln\frac{1-\epsilon_t}{\epsilon_t}$) with no worked example. Add: "If $\epsilon=0.3$: $\alpha = 0.5 \cdot \ln(2.33) = 0.424$."

5. **[MAJOR]** `L04_deepdive.tex:738-761` -- XGBoost gain formula presented without worked example. Arguably the hardest formula in the file.

6. **[MAJOR]** `L04_rf_full.tex:860-909` -- AdaBoost algorithm pseudocode with no worked example. Same issue as deepdive.

7. **[MAJOR]** `L04_rf_full.tex:912-963` -- Gradient boosting pseudo-residual computation with no worked example.

8. **[MAJOR]** `L04_rf_full.tex:966-1011` -- XGBoost Taylor expansion and split gain with no worked example.

### Missing Active Learning Elements (3 issues)

9. **[MAJOR]** `L04_rf_full.tex` (entire file) -- ZERO exercises across 31 slides. No exercise slide, no reflection prompt, no "pause and think" moment. Add at least one mid-lecture reflection and one closing exercise.

10. **[MAJOR]** `L04_rf_mini.tex` (entire file) -- No worked numerical example in 10 slides. Add at least one (e.g., variance formula with B=500, rho=0.1).

11. **[MAJOR]** `L04_overview.tex:467-479` -- Exercises lack scaffolding. All three exercises are medium-to-hard. Missing easy warm-up and hand-calculable exercise.

### Accessibility Issues (2 issues)

12. **[MAJOR]** `L04_deepdive.tex:119-128` -- LO slide (slide 4) uses undefined terminology: "variance reduction formula", "tree correlation", "gradient boosting", "statistical inference". True beginner at slide 4 has not been taught what a DT is yet.

13. **[MAJOR]** `L04_rf_full.tex:170-178` -- Frame 4 uses "Bias-variance decomposition: MSE = Bias^2 + Variance + Noise" without defining bias or variance. File is labeled a "prerequisite" but assumes prior knowledge.

### Chart Code Issue (1 issue)

14. **[MAJOR]** `06b_random_forest_variance/chart.py` -- Labeled "Random Forest (50 trees)" but uses `scipy.interpolate.interp1d(kind='nearest')` instead of `sklearn.ensemble.RandomForestRegressor`. Fakes RF behavior with nearest-neighbor interpolation. Fix: Replace with actual `RandomForestRegressor(n_estimators=50).fit().predict()` to match 06a which correctly uses `DecisionTreeRegressor`.

## Minor Issues (17 total)

1. [MINOR] `L04_overview.tex:143` -- Galton bottomnote says "crowd's median estimate" but Galton's 1907 paper reports the mean.
2. [MINOR] `L04_overview.tex:309-311` -- Entropy formula given but no worked example alongside the Gini example.
3. [MINOR] `L04_overview.tex:150` -- Dollar sign in "Is income > $50k?" might confuse LaTeX; compiles fine but fragile.
4. [MINOR] `L04_deepdive.tex:413` -- "B = 100-500" as default. scikit-learn default is n_estimators=100 since v0.22.
5. [MINOR] `L04_deepdive.tex:108` -- Outline slide has no bottomnote, unlike overview. Inconsistent.
6. [MINOR] `L04_dt_full.tex:253-256` -- Intro zone contains `$\to$` arrows in ML landscape listing. Borderline formula usage.
7. [MINOR] `L04_dt_full.tex:499` -- Time complexity $O(n \cdot p \cdot d)$ omits the $\log n$ sorting factor.
8. [MINOR] `L04_dt_full.tex:881-884` -- Bridge slide with variance formula appears after "Closing Zone" header.
9. [MINOR] `L04_dt_mini.tex:267` -- Parent Gini "G = 0.48" stated without showing arithmetic.
10. [MINOR] `L04_dt_mini.tex:236-239` -- CASE slide switches from loan-approval to fraud-detection framing without transition.
11. [MINOR] `L04_dt_mini.tex` -- No explicit LO slide.
12. [MINOR] `L04_rf_full.tex:1372-1406` -- Closing comic reuses XKCD #1885 (same as opening). Use #1838 instead.
13. [MINOR] `L04_rf_full.tex:659` -- States "Default: 500" but scikit-learn default is 100.
14. [MINOR] `L04_rf_full.tex:318` -- "$H \approx 2G$ near $p=0.5$" approximation is generous at p far from 0.5.
15. [MINOR] `L04_rf_mini.tex:304` -- Uses `\dfrac` while other files use `\frac`. Cosmetic inconsistency.
16. [MINOR] `L04_rf_mini.tex` -- No explicit LO slide.
17. [MINOR] `12_nonlinear_classes/chart.py` -- Axis labels say "Income" and "Credit Score" for synthetic `rng.randn` data. Acceptable but could note "illustrative."

## Chart Audit Results

| Chart | Type (Plan) | Type (Actual) | Standards | Correct? | Issues |
|---|---|---|---|---|---|
| 01_decision_tree | Diagram | Diagram | Pass | Yes | None |
| 02_feature_importance | Math viz | **Trained-model** | Pass | Yes | Plan misclassified; uses sklearn RF |
| 03_bootstrap | Diagram | Diagram | Pass | Yes | None |
| 04_oob_error | Math viz | **Trained-model** | Pass | Yes | Plan misclassified; uses sklearn RF |
| 05_ensemble_voting | Diagram | Diagram | Pass | Yes | None |
| 06a_single_tree_variance | Trained-model | Trained-model | Pass | Yes | Uses sklearn DecisionTreeRegressor |
| 06b_random_forest_variance | Trained-model | **scipy interp** | Pass | **No** | **MAJOR: fakes RF with interpolation** |
| 07_decision_flowchart | Diagram | Diagram | Pass | Yes | None |
| 08_gini_split | Diagram | Diagram | Pass | Yes | Math verified: 0.48->0.276, reduction=0.204 |
| 09_dt_overfitting | Trained-model | Trained-model | Pass | Yes | Uses sklearn DecisionTreeClassifier |
| 10_dt_decision_boundary | Trained-model | Trained-model | Pass | Yes | Uses sklearn DT + DecisionBoundaryDisplay |
| 11_gini_vs_entropy | Math viz | Math viz | Pass | Yes | Gini=2p(1-p), Entropy scaled 0.5H(p) correct |
| 12_nonlinear_classes | Math viz | Diagram/synthetic | Pass | Yes | MINOR: synthetic labeled as Income/Credit |

**All 13 charts pass:** figsize=(10,6), dpi=150, font.size=14, ML color palette, output to chart.pdf.

**Math verified on chart 08:**
- Parent: 60/100 repay, Gini = 1-(0.36+0.16) = 0.48
- Left: 40 apps (70/30), Gini = 1-(0.49+0.09) = 0.42
- Right: 60 apps (90/10), Gini = 1-(0.81+0.01) = 0.18
- Weighted: (40/100)*0.42 + (60/100)*0.18 = 0.276
- Impurity reduction: 0.48 - 0.276 = 0.204

## Content Overlap Analysis

| Concept | Files Present | Count | Assessment |
|---|---|---|---|
| Gini formula | overview, deepdive, dt_full, dt_mini, rf_full | 5/6 | Intentional reinforcement; adapted per depth |
| Entropy formula | overview, deepdive, dt_full, rf_full | 4/6 | Appropriate |
| Variance formula | overview, deepdive, dt_full, rf_full, rf_mini | 5/6 | Heavy repetition; dt_full is just a bridge preview |
| OOB 63.2% rule | overview, deepdive, rf_full, rf_mini | 4/6 | Appropriate foundational fact |
| SHAP | deepdive, rf_full | 2/6 | Good depth separation |
| AdaBoost | deepdive, rf_full | 2/6 | Near-identical; borderline redundant |
| XGBoost | deepdive, rf_full | 2/6 | Similar coverage |
| XKCD #1885 | overview, deepdive, rf_full (2x) | 3/6 | **Overused** -- rf_full uses it for both open AND close |
| Gini worked example (60/40) | dt_full, dt_mini | 2/6 | Consistent numbers |
| Gini worked example (800/200) | deepdive, rf_full | 2/6 | Consistent numbers |

**Cross-file consistency:** Terminology consistent across all files. Worked example numbers consistent within related pairs. Prerequisites chain correctly: dt_mini -> dt_full -> rf_mini -> rf_full -> overview -> deepdive.

## Remediation Plan (Prioritized)

### Priority 1: CRITICAL Fix (1 item)
1. Replace deepdive text-only closing with actual XKCD #1838 image (single-line fix)

### Priority 2: Missing Worked Examples (7 items)
2. Add variance formula worked example to overview
3. Add MSE regression worked example to deepdive
4. Add AdaBoost alpha worked example to deepdive
5. Add XGBoost gain worked example to deepdive
6. Add AdaBoost worked example to rf_full
7. Add gradient boosting residual worked example to rf_full
8. Add XGBoost worked example to rf_full

### Priority 3: Active Learning Gaps (3 items)
9. Add exercise slide + reflection prompt to rf_full
10. Add worked numerical example to rf_mini
11. Add easy warm-up exercise to overview

### Priority 4: Accessibility Fixes (2 items)
12. Add plain-English intro before LOs in deepdive
13. Define bias/variance before formula in rf_full frame 4

### Priority 5: Chart Code Fix (1 item)
14. Fix chart 06b to use actual sklearn RandomForestRegressor

### Priority 6: Minor Polish (optional, 17 items)
See Minor Issues list above. Most impactful: change rf_full closing comic from #1885 to #1838.

---

*Review conducted: 2026-03-04*
*Methodology: Per-file hostile review (100-point rubric, 13 criteria) + 13 chart.py code audit*
*Compilation: All 6 files, zero Overfull warnings*
