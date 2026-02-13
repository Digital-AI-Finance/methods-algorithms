# L05 Hostile Content Review Report: PCA & t-SNE

**Review Date:** 2026-02-06
**Reviewer Persona:** Hostile External Academic Examiner
**Target Audience:** MSc Data Science (various backgrounds, NO pre-knowledge)
**Execution Mode:** Ralph + Ultrawork (4 parallel agents)

---

## Executive Summary

**Final Score: 37/100 (FAIL - Grade F)**

The L05 lecture materials on PCA & t-SNE suffer from fundamental theoretical gaps and a critical absence of finance applications. While charts meet technical standards (12/12 pass), the content fails MSc-level requirements:

1. **NO yield curve PCA** - THE canonical finance application is completely absent
2. **NO numerical finance example** - Only bullet points, zero quantitative demonstration
3. **PCA optimality proof missing** - Students told eigenvectors maximize variance but never shown WHY
4. **t-SNE crowding problem not explained** - Key innovation (t-distribution) motivation absent
5. **Kaiser criterion stated incorrectly** - Missing "correlation matrix only" qualification
6. **"PCA assumes Gaussian" is FALSE** - Factually incorrect statement at line 241
7. **ZERO statistical inference** - No bootstrap CIs, permutation tests, or parallel analysis

**Comparison to Previous Reviews:**
- L01 (Linear Regression): ~66%
- L02 (Logistic Regression): ~55-65%
- L03 (KNN & K-Means): 29%
- L04 (Random Forests): 41%
- **L05 (PCA & t-SNE): 37%**

---

## Score Breakdown

| Section | Max | Score | Deductions |
|---------|-----|-------|------------|
| Formula Verification | 15 | 8 | -7 (Kaiser incorrect, centering implicit, symmetrization missing) |
| Misleading Statements | 10 | 4 | -6 (Gaussian claim FALSE, reversible unqualified, UMAP uncited) |
| Algorithm Correctness | 5 | 3 | -2 (SVD vs eigen disconnect, symmetrization step missing) |
| Learning Objectives | 20 | 6 | -14 (all partially/weakly met, no evaluation depth) |
| MSc Level | 20 | 0 | -20 (no proofs, no inference, no advanced methods) |
| Finance Use Cases | 15 | 2 | -13 (no yield curve, no numerical example, generic only) |
| Pedagogical Flow | 10 | 6 | -4 (7/7 chart redundancy, TBDs, time budget exceeded) |
| Completeness | 5 | 3 | -2 (missing finance charts, missing topics) |
| Chart Quality | +5 | +5 | BONUS: All 12/12 charts pass quality audit |
| **TOTAL** | **100** | **37** | **-63** |

---

## CRITICAL FINDINGS (Must Fix)

### C1: Yield Curve PCA Completely Absent
**Location:** Missing throughout both files
**Issue:** The decomposition of yield curve movements into level, slope, and curvature is THE most universally recognized finance application of PCA. Every fixed income professional knows this. An MSc Data Science course with "finance/banking applications" that omits this is incomplete.
**Evidence:** Zero occurrences of: "yield", "curve", "level", "slope", "curvature", "term structure"
**Impact:** Finance Use Cases section essentially fails
**Deduction:** -4 points

### C2: "PCA Assumes Gaussian" is Factually Incorrect
**Location:** deepdive.tex line 241
**Current:** "PCA assumes linear structure and Gaussian-like distributions"
**Issue:** This is FACTUALLY FALSE. PCA is a second-moment method based solely on covariance. It does NOT require any distributional assumption. PCA is:
- VALID for any distribution
- OPTIMAL (in likelihood sense) only for Gaussian data
**Correct Statement:** "PCA is optimal for Gaussian but does not require it"
**Impact:** Students would incorrectly state on exams that PCA "requires" Gaussian data
**Deduction:** -3 points

### C3: Kaiser Criterion Missing Critical Qualification
**Location:** deepdive.tex line 162
**Current:** "Kaiser criterion: keep components with λ > 1"
**Issue:** This rule is ONLY valid when using the correlation matrix (standardized variables). For the covariance matrix on unscaled data, the threshold λ > 1 is meaningless - a variable measured in millions would have huge eigenvalue regardless of importance.
**Fix:** Add "(for standardized data / correlation matrix only)"
**Deduction:** -5 points (formula-level error)

### C4: PCA Centering Requirement Not Explicit
**Location:** deepdive.tex lines 131, 141-142, 187-188
**Issue:** The covariance formula shows "(centered data)" parenthetically once, but:
- Projection formula Z = X W_k does not state X must be centered
- Reconstruction formula does not show adding mean back
**Impact:** Students implementing PCA would get wrong results
**Deduction:** -6 points (3 instances × -2)

### C5: t-SNE Crowding Problem Not Explained
**Location:** deepdive.tex line 281
**Current:** "t-distribution has heavier tails, allowing better separation"
**Issue:** The WHY is never explained. The crowding problem (moderate distances in high-D become small in low-D, causing points to collapse) is the key insight motivating the t-distribution. Without this, students don't understand the paper's core innovation.
**Deduction:** -3 points

### C6: PCA Optimality Proof Missing
**Location:** Missing throughout
**Expected at MSc level:**
- Constrained optimization: max w^T Σ w subject to ||w||=1
- Lagrangian: L = w^T Σ w - λ(w^T w - 1)
- First-order condition yields Σw = λw
**Current:** Students told eigenvectors give maximum variance but never shown WHY
**Impact:** Cannot generalize to related problems
**Deduction:** -3 points

### C7: Zero Statistical Inference for Dimensionality Reduction
**Location:** Missing throughout
**Expected at MSc level:**
- Bootstrap confidence intervals for PCA loadings
- Parallel analysis for choosing k
- Permutation tests for component significance
- Multiple t-SNE runs stability analysis
- Trustworthiness/continuity metrics
**Current Coverage:** ZERO
**Deduction:** -5 points

---

## MAJOR FINDINGS (Should Fix)

### M1: No Numerical Finance Example
**Location:** deepdive.tex lines 206-222
**Issue:** Portfolio risk decomposition section is entirely qualitative:
- "PC1 often represents market factor"
- "PC2-3 may capture sector/size factors"
- "Higher PCs: idiosyncratic risk"
**Missing:** Actual loadings, eigenvalues, asset names, interpretable numbers
**Fix:** Add concrete example with 5-10 stocks and their factor loadings
**Deduction:** -3 points

### M2: t-SNE Symmetrization Step Missing
**Location:** deepdive.tex lines 268-279
**Issue:** Slides show conditional probabilities p_{j|i} but KL formula uses joint p_{ij}. The conversion step p_{ij} = (p_{j|i} + p_{i|j})/2n is NEVER shown.
**Impact:** Mathematical chain is incomplete
**Deduction:** -2 points

### M3: SVD Relationship to PCA Absent
**Location:** Missing throughout
**Issue:** Deepdive teaches eigendecomposition (Σv = λv), but sklearn's PCA uses truncated SVD on centered X directly for numerical stability. Students will not understand what their code actually does.
**Deduction:** -3 points

### M4: "Reversible" Statement Misleading
**Location:** deepdive.tex lines 122-123, 373
**Current:** "Reversible (can reconstruct original data)"
**Issue:** Only fully reversible when k=p (all components). For k<p, reconstruction is LOSSY.
**Fix:** "Partially reversible (lossy for k<p)"
**Deduction:** -3 points (2 occurrences)

### M5: Perplexity = Effective Neighbors Not Explained
**Location:** deepdive.tex ~line 315
**Current:** "controls balance between local and global structure"
**Issue:** Perplexity has a precise meaning: perplexity = 2^H where H is entropy. This is the effective number of neighbors. Without this, students can't understand why typical values are 5-50.
**Deduction:** -2 points

### M6: KL Divergence Asymmetry Not Discussed
**Location:** deepdive.tex line 279
**Issue:** KL(P||Q) penalizes q_{ij} being small when p_{ij} is large, not the reverse. This is WHY t-SNE preserves local structure (nearby points stay nearby). The asymmetry is never mentioned.
**Deduction:** -2 points

---

## MODERATE FINDINGS

### Mo1: All Charts Use Synthetic Data
**Location:** All 12 chart files
**Issue:** Every visualization uses generic blobs, Swiss rolls, or random clusters. Not a single chart shows actual financial time series.
**Impact:** Undermines finance positioning of course
**Deduction:** -1 point

### Mo2: t-SNE O(n²) Claim Outdated
**Location:** deepdive.tex line 331
**Current:** "Slow for large datasets O(n²)"
**Issue:** Barnes-Hut approximation gives O(n log n) and is default in sklearn since 2018. Should mention.
**Deduction:** 0 points (minor)

### Mo3: UMAP Claim Uncited
**Location:** deepdive.tex line 490
**Current:** "UMAP often preferred over t-SNE in modern practice"
**Issue:** Subjective statement without citation. Should cite survey or soften language.
**Deduction:** -1 point

### Mo4: Kernel PCA Dangling Reference
**Location:** deepdive.tex line 237
**Issue:** Kernel PCA mentioned as "solution" to non-linearity but never explained. Students have no way to understand how it works.
**Deduction:** -2 points

---

## MINOR FINDINGS

### Mi1: TBD Placeholders (2 found)
- overview.tex line 199: `[TBD]` for Colab link
- deepdive.tex line 435: `[TBD]` for Colab link
**Deduction:** -2 points

### Mi2: Time Budget Exceeds 3 Hours
**Location:** instructor_guide.md lines 115-122
**Issue:** 195 minutes total (15 over budget)
**Deduction:** -1 point

### Mi3: 100% Chart Redundancy (Overview to Deepdive)
**Finding:** All 7 overview charts appear in deepdive
- 01_scree_plot: overview 143 → deepdive 171
- 02_principal_components: overview 151 → deepdive 179
- 03_reconstruction: overview 159 → deepdive 200
- 04b_tsne_perplexity_30: overview 168 → deepdive 293
- 05b_tsne_swiss_roll: overview 175 → deepdive 357
- 06c_tsne_cluster_projection: overview 183 → deepdive 399
- 07_decision_flowchart: overview 207 → deepdive 443
**Note:** Deepdive does add 5 unique charts (04a, 04c, 05a, 06a, 06b)
**Deduction:** -2 points (same as L04)

---

## POSITIVE FINDINGS

### Chart Quality: EXCELLENT (12/12)
All 12 charts meet technical standards:
- Correct figsize (10, 6) ✓
- Correct dpi (150 in rcParams) ✓
- Correct font sizes (14pt body, 16pt title) ✓
- Correct color palette (MLPurple, MLBlue, MLOrange, MLGreen, MLRed) ✓
- CHART_METADATA present in all ✓
- Single figure per chart ✓
- PDF output ✓

**Bonus:** +5 points for perfect chart quality

### PMSP Compliance: PASS
- Overview follows Problem-Method-Solution-Practice structure
- Deepdive uses logical Part-based organization

### Comparison Table Present
- Lines 362-380 provide good PCA vs t-SNE comparison
- Swiss roll example effectively shows PCA limitation

### Perplexity Variations Well Visualized
- Charts 04a, 04b, 04c show perplexity 5, 30, 100 effects clearly

---

## Recommended Additions (Prioritized by Impact)

### HIGH PRIORITY (Would raise score to 60+)

| Addition | Effort | Impact |
|----------|--------|--------|
| 1. Yield curve PCA example (level/slope/curvature) | 3 hours | +7 points |
| 2. Correct line 241: PCA does NOT require Gaussian | 5 min | +3 points |
| 3. Add Kaiser criterion "(correlation matrix only)" | 5 min | +5 points |
| 4. Explicit centering in all PCA formulas | 30 min | +4 points |
| 5. Explain crowding problem for t-distribution | 1 hour | +3 points |
| 6. Add numerical portfolio example with loadings | 2 hours | +3 points |

### MEDIUM PRIORITY (Would raise score to 75+)

| Addition | Effort | Impact |
|----------|--------|--------|
| 7. PCA optimality proof (Lagrangian sketch) | 1 hour | +3 points |
| 8. t-SNE symmetrization formula | 15 min | +2 points |
| 9. Qualify "reversible" as lossy | 10 min | +2 points |
| 10. Perplexity = 2^H explanation | 30 min | +2 points |
| 11. Statistical inference section (bootstrap, parallel analysis) | 3 hours | +5 points |
| 12. SVD relationship to PCA | 1 hour | +3 points |

### LOW PRIORITY (Polish)

| Addition | Effort | Impact |
|----------|--------|--------|
| 13. Remove TBD placeholders | 5 min | +2 points |
| 14. Fix time budget | 15 min | +1 point |
| 15. Add finance-specific chart | 2 hours | +1 point |
| 16. Cite UMAP claim | 5 min | +1 point |

**Total potential improvement:** +47 points → 84/100 (Grade B+)

---

## Acceptance Criteria for Passing (≥70)

**All CRITICAL issues must be resolved:**
- [ ] Yield curve PCA example added
- [ ] Line 241 "Gaussian" claim corrected
- [ ] Kaiser criterion qualified for correlation matrix
- [ ] PCA centering explicit in all formulas
- [ ] Crowding problem explained
- [ ] PCA optimality proof sketch added
- [ ] At least one statistical inference method added

**At least 4/6 MAJOR issues resolved:**
- [ ] Numerical finance example added
- [ ] t-SNE symmetrization shown
- [ ] SVD relationship mentioned
- [ ] "Reversible" qualified
- [ ] Perplexity as effective neighbors explained
- [ ] KL asymmetry mentioned

---

## Verdict

**FAIL** - The L05 materials are not suitable for MSc-level delivery in their current state.

**Primary Deficiencies:**
1. **Finance application critical gap:** Missing yield curve PCA (THE canonical example)
2. **Factually incorrect claim:** "PCA assumes Gaussian" is false
3. **Incomplete theory:** No proofs, no derivations, formulas without context
4. **No statistical inference:** Cannot assess uncertainty in any result
5. **Kaiser criterion wrong:** Would lead students to incorrect component selection

**Comparison to L04:** Similar issues pattern (class imbalance ↔ yield curve, wrong metric emphasis ↔ wrong Gaussian claim). L05 scores slightly lower due to more severe theoretical gaps.

**Recommendation:** Major revision required. Estimate 15-20 hours to reach passing threshold.

---

## Issues Summary for Fix Phase

| ID | Severity | Issue | Location | Fix |
|----|----------|-------|----------|-----|
| C1 | CRITICAL | Missing yield curve PCA | N/A | Add 2-3 slides |
| C2 | CRITICAL | "PCA assumes Gaussian" FALSE | line 241 | Correct to "optimal for" |
| C3 | CRITICAL | Kaiser criterion unqualified | line 162 | Add "(correlation matrix only)" |
| C4 | CRITICAL | PCA centering implicit | 131, 141, 187 | Make explicit |
| C5 | CRITICAL | Crowding problem missing | line 281 | Add explanation |
| C6 | CRITICAL | PCA proof missing | N/A | Add Lagrangian sketch |
| C7 | CRITICAL | No statistical inference | N/A | Add section |
| M1 | MAJOR | No numerical finance example | 206-222 | Add portfolio loadings |
| M2 | MAJOR | Symmetrization missing | 268-279 | Add formula |
| M3 | MAJOR | SVD relationship absent | N/A | Add note |
| M4 | MAJOR | "Reversible" misleading | 122, 373 | Qualify as lossy |
| M5 | MAJOR | Perplexity unexplained | ~315 | Add 2^H definition |
| M6 | MAJOR | KL asymmetry missing | 279 | Add explanation |
| Mo1 | MODERATE | All synthetic data | charts | Add finance chart |
| Mo3 | MODERATE | UMAP claim uncited | 490 | Add citation |
| Mo4 | MODERATE | Kernel PCA dangling | 237 | Expand or remove |
| Mi1 | MINOR | TBD placeholders | 199, 435 | Complete |
| Mi2 | MINOR | Time budget exceeded | guide | Trim 15 min |

---

**Report Generated:** 2026-02-06
**Execution Time:** ~20 minutes (parallel agent execution)
**Calibration Reference:** L01: 66%, L02: 55-65%, L03: 29%, L04: 41%
