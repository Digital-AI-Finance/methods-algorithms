# Hostile Content Review Plan: L05 - PCA & t-SNE

**Plan Type:** Critical Academic Review
**Target:** L05 PCA & t-SNE lecture materials
**Review Mode:** HOSTILE - Seeking deficiencies at MSc level
**Reviewer Persona:** External academic examiner with dimensionality reduction / manifold learning research background

---

## Executive Summary

This plan defines a systematic hostile review of L05 content focusing on:
1. Mathematical rigor in eigendecomposition, KL divergence, and t-SNE formulation
2. Missing theoretical depth on PCA optimality proofs and t-SNE convergence
3. t-SNE caveats potentially incomplete (distances, sizes, global structure)
4. Finance application (portfolio risk decomposition) may be superficial
5. UMAP coverage adequate or too brief for modern practice?
6. 12 charts between overview and deepdive - check for redundancy vs complementarity

**Calibration Reference:**
- L01 (Linear Regression): ~66%
- L02 (Logistic Regression): ~55-65%
- L03 (KNN & K-Means): 29% (major cluster validity gaps)
- L04 (Random Forests): ~52-69% (class imbalance gaps)

**Expected Outcome:** Score 50-70/100 based on preliminary scan

---

## Files Under Review

| File | Lines | Est. Slides | Role |
|------|-------|-------------|------|
| `L05_overview.tex` | 225 | ~13 | High-level introduction |
| `L05_deepdive.tex` | 538 | ~30 | Mathematical depth |
| `L05_instructor_guide.md` | 152 | N/A | Teaching notes |
| 12 chart folders | varies | N/A | Visualizations |

**Chart Inventory:**
1. `01_scree_plot/` - Variance explained
2. `02_principal_components/` - PC visualization
3. `03_reconstruction/` - Reconstruction error
4. `04a_tsne_perplexity_5/` - Low perplexity
5. `04b_tsne_perplexity_30/` - Default perplexity
6. `04c_tsne_perplexity_100/` - High perplexity
7. `05a_pca_swiss_roll/` - PCA on non-linear manifold
8. `05b_tsne_swiss_roll/` - t-SNE on non-linear manifold
9. `06a_original_clusters/` - High-D clusters
10. `06b_pca_cluster_projection/` - PCA projection
11. `06c_tsne_cluster_projection/` - t-SNE projection
12. `07_decision_flowchart/` - Method selection

---

## SECTION 1: CONTENT ACCURACY (30 points)

### 1.1 Formula Verification (15 points)

**Target Formulas to Audit:**

| Formula | Location | Line | Check |
|---------|----------|------|-------|
| Covariance matrix | deepdive | 130-132 | Verify $\Sigma = \frac{1}{n-1} X^T X$ (centered data) |
| Eigendecomposition | deepdive | 135-138 | Verify $\Sigma v = \lambda v$ |
| Projection formula | deepdive | 141-143 | Verify $Z = X W_k$ where $W_k = [v_1, ..., v_k]$ |
| Explained variance ratio | deepdive | 149-151 | Verify $\frac{\lambda_i}{\sum_j \lambda_j}$ |
| Cumulative variance | deepdive | 154-156 | Verify $\sum_{i=1}^{k} \frac{\lambda_i}{\sum_j \lambda_j}$ |
| Reconstruction formula | deepdive | 187-189 | Verify $\hat{X} = Z W_k^T = X W_k W_k^T$ |
| Reconstruction error | deepdive | 192-194 | Verify $\|X - \hat{X}\|_F^2 = \sum_{i=k+1}^{p} \lambda_i$ |
| t-SNE high-D similarity | deepdive | 268-270 | Verify Gaussian kernel formulation |
| t-SNE low-D similarity | deepdive | 273-275 | Verify t-distribution kernel |
| KL divergence | deepdive | 278-280 | Verify $KL(P\|Q) = \sum_{i \neq j} p_{ij} \log \frac{p_{ij}}{q_{ij}}$ |

**Issues to Flag:**

- [ ] Line 130-132: Covariance uses $\frac{1}{n-1}$ (Bessel correction) - but $X^T X$ without explicit centering. Is $X$ assumed centered? Must state explicitly.
- [ ] Line 135-138: Eigendecomposition shown for $\Sigma$ but should mention $\Sigma = V \Lambda V^T$ full form
- [ ] Line 143: Projection $Z = X W_k$ assumes $X$ is centered - if not stated, this is misleading
- [ ] Line 187-189: Reconstruction $\hat{X} = X W_k W_k^T$ - should note this is in centered space, need to add mean back
- [ ] Line 192-194: Reconstruction error = sum of discarded eigenvalues - need to state this is for Frobenius norm specifically
- [ ] Line 268-270: t-SNE uses $p_{j|i}$ (conditional) but formula should clarify symmetrization to $p_{ij} = \frac{p_{j|i} + p_{i|j}}{2n}$
- [ ] Line 273-275: Low-D similarity uses t-distribution with 1 degree of freedom (Cauchy) - should state this
- [ ] KL divergence: Should note asymmetry (penalizes small $q_{ij}$ for large $p_{ij}$ more than reverse)

**Scoring Rubric:**
| Finding | Deduction |
|---------|-----------|
| Formula error | -5 per formula |
| Missing assumption (centering) | -2 per instance |
| Notation inconsistency | -1 per instance |
| Missing symmetrization | -2 |

### 1.2 Misleading Statements (10 points)

**Review Targets:**

| Statement | Location | Line | Concern |
|-----------|----------|------|---------|
| "PCA: Linear projection preserving maximum variance" | overview | 133 | TRUE but should note "among linear projections" |
| "Components are uncorrelated" | deepdive | 122 | TRUE only for the projected data, not original features |
| "Reversible (can reconstruct original data)" | deepdive | 123 | MISLEADING - only lossless if k=p, otherwise lossy |
| "Eigenvalues tell us how much variance each component captures" | deepdive | 144 | Should note eigenvalues ARE the variances along PCs |
| "t-SNE: visualization method, NOT for preprocessing" | deepdive | 263 | TRUE - should explain WHY (no inverse transform, stochastic) |
| "t-distribution has heavier tails, allowing better separation" | deepdive | 281 | TRUE but should explain the crowding problem motivation |
| "Cluster sizes are not meaningful" | deepdive | 329 | TRUE but WHY? (optimization landscape, initialization) |
| "Distances between clusters are not meaningful" | deepdive | 330 | TRUE but should explain global structure loss |
| "PCA assumes linear structure and Gaussian-like distributions" | deepdive | 241 | PARTIALLY FALSE - PCA doesn't require Gaussianity, just linearity |
| "UMAP often preferred over t-SNE in modern practice" | deepdive | 490 | CLAIM needs citation or evidence |
| "Kaiser criterion: keep components with $\lambda > 1$" | deepdive | 162 | Only valid for correlation matrix (standardized data), not covariance |

**Scoring Rubric:**
| Finding | Deduction |
|---------|-----------|
| Misleading without qualification | -3 |
| Missing "typically" or "often" qualifier | -1 |
| Correct but oversimplified | -1 |
| Incorrect statement | -3 |

### 1.3 Algorithm Correctness (5 points)

**Check PCA Algorithm (implicit in slides):**
```
1. Center data: X_c = X - mean(X)
2. Compute covariance: Sigma = (1/(n-1)) * X_c^T * X_c
3. Eigendecompose: Sigma = V * Lambda * V^T
4. Sort by eigenvalue (descending)
5. Select top k eigenvectors: W_k = V[:, 1:k]
6. Project: Z = X_c * W_k
```

**Issues:**
- [ ] Step 1: Centering not explicitly shown in deepdive
- [ ] Step 2: Could use SVD instead (numerically more stable) - not mentioned
- [ ] Step 4: Sorting assumed but not stated
- [ ] Alternative: sklearn uses SVD internally, not eigendecomposition - inconsistency with "Implementation" section

**Check t-SNE Algorithm (implicit):**
```
1. Compute pairwise distances in high-D
2. Convert to conditional probabilities using Gaussian
3. Symmetrize: p_ij = (p_j|i + p_i|j) / 2n
4. Initialize low-D embedding (random or PCA)
5. For each iteration:
   - Compute low-D similarities (t-distribution)
   - Compute gradient of KL divergence
   - Update embedding using gradient descent
6. Return final embedding
```

**Issues:**
- [ ] Symmetrization step not mentioned in slides
- [ ] Perplexity sets the variance sigma_i via binary search - not explained
- [ ] Early exaggeration phase not mentioned
- [ ] Learning rate, momentum not discussed (important for convergence)
- [ ] Barnes-Hut approximation for O(n log n) not mentioned (only O(n^2) stated)

---

## SECTION 2: LEARNING OBJECTIVES ALIGNMENT (20 points)

### 2.1 Stated Objectives (Lines 109-115 overview)

| # | Objective | Bloom's Level | Coverage | Evidence |
|---|-----------|---------------|----------|----------|
| 1 | "Apply PCA for dimensionality reduction and feature extraction" | Apply (L3) | GOOD | deepdive 452-470, multiple charts |
| 2 | "Interpret variance explained and choose number of components" | Analyze (L4) | GOOD | deepdive 147-165, scree plot |
| 3 | "Use t-SNE for visualization of high-dimensional data" | Apply (L3) | GOOD | Multiple perplexity charts, comparison slides |
| 4 | "Compare linear (PCA) vs non-linear (t-SNE) methods" | Evaluate (L5) | GOOD | Comparison table line 362-380, Swiss roll example |

### 2.2 Objective Gaps Analysis

**Objective 1: Apply PCA for dimensionality reduction**
- Coverage adequate with formulas and implementation hints
- **Gap:** No actual Python code walkthrough (only parameter descriptions)
- **Gap:** No discussion of when to use correlation vs covariance matrix

**Objective 2: Interpret variance explained**
- Good coverage with scree plot and elbow method
- Kaiser criterion mentioned (line 162)
- **Gap:** Kaiser criterion only valid for correlation matrix - not stated
- **Gap:** No discussion of broken stick method or parallel analysis (advanced)

**Objective 3: Use t-SNE for visualization**
- Good coverage with perplexity variations (04a, 04b, 04c)
- Multiple t-SNE charts demonstrate different scenarios
- **Gap:** No discussion of learning rate sensitivity
- **Gap:** No discussion of early exaggeration importance
- **Gap:** How to interpret t-SNE results not deeply covered (beyond caveats)

**Objective 4: Compare PCA vs t-SNE**
- Comparison table present (lines 362-380)
- Swiss roll example excellent (shows PCA limitation)
- **Gap:** No quantitative comparison metric (trustworthiness, continuity)
- **Gap:** No discussion of when t-SNE gives misleading results

**Scoring Rubric:**
| Finding | Deduction |
|---------|-----------|
| Objective partially met | -3 |
| Objective weakly met | -5 |
| Objective unmet | -7 |
| Missing MSc-level depth | -2 per gap |

---

## SECTION 3: MSc LEVEL APPROPRIATENESS (20 points)

### 3.1 Theoretical Depth Gaps (10 points)

**Critical Missing Theory:**

| Topic | Expected at MSc | Present? | Lines |
|-------|-----------------|----------|-------|
| PCA optimality proof (max variance = eigenvalue) | YES | NO | Formula stated, not derived |
| SVD relationship to PCA | YES | NO | Not mentioned |
| t-SNE convergence properties | YES | NO | Not discussed |
| Perplexity as effective number of neighbors | YES | PARTIAL | Only "controls balance" |
| Crowding problem motivation for t-distribution | YES | NO | Not explained |
| KL divergence asymmetry implications | YES | NO | Not discussed |
| t-SNE gradient derivation | YES | NO | Not shown |
| Relationship to kernel PCA | YES | NO | Kernel PCA not mentioned |
| Probabilistic PCA | YES | NO | Not mentioned |
| Factor Analysis relationship | YES | NO | Not mentioned |
| Information theory view of PCA | YES | NO | Not mentioned |
| Manifold learning framework | YES | PARTIAL | Swiss roll shows, not formalized |

**Deep Dive Expectations - Missing Derivations:**

- Line 130-144: PCA formulas stated but:
  - [ ] No proof that eigenvectors of covariance maximize variance
  - [ ] No mention of Rayleigh quotient
  - [ ] No connection to SVD (which sklearn actually uses)

- Line 266-280: t-SNE formulas stated but:
  - [ ] No explanation of why t-distribution (crowding problem)
  - [ ] No gradient formula shown
  - [ ] No convergence discussion
  - [ ] No connection to other SNE variants (SNE, symmetric SNE)

- Line 474-490: UMAP introduced but:
  - [ ] No mathematical foundation (topological data analysis)
  - [ ] No comparison of mathematical assumptions
  - [ ] "Can embed new points" stated but mechanism not explained

### 3.2 Statistical Inference for Dimensionality Reduction (5 points)

**CRITICAL GAP: No hypothesis testing or confidence intervals**

MSc-level should include:
- [ ] Bootstrap confidence intervals for PCA loadings
- [ ] Significance testing for principal components
- [ ] Cross-validation for choosing k
- [ ] Stability analysis for t-SNE (multiple runs)
- [ ] Trustworthiness and continuity metrics

**Current Coverage:**
- Line 338: "Run multiple times with different seeds" - acknowledges non-determinism
- **BUT:** No formal method to compare or aggregate runs

### 3.3 Advanced Topics (5 points)

**Missing Advanced Material:**

| Topic | Importance | Present? |
|-------|------------|----------|
| Kernel PCA | High | NO |
| Probabilistic PCA | Medium | NO |
| Sparse PCA | Medium | NO |
| Robust PCA | Medium | Mentioned line 237 but not explained |
| Incremental PCA | Medium | NO |
| t-SNE Barnes-Hut approximation | High | NO (only O(n^2) mentioned) |
| Parametric t-SNE | Low | NO |
| UMAP mathematical foundation | Medium | NO |
| Isomap, LLE comparison | Medium | NO |
| Autoencoders as non-linear alternative | Medium | NO |

**Scoring Rubric:**
| Finding | Deduction |
|---------|-----------|
| Missing major theory | -3 per topic |
| Missing statistical inference | -5 |
| Missing advanced methods | -2 per topic |
| Oversimplified for MSc | -2 per instance |

---

## SECTION 4: FINANCE USE CASES (15 points)

### 4.1 Portfolio Risk Decomposition Depth (10 points)

**Current Coverage:**
- Lines 117-118 (overview): "Finance Application: Portfolio risk decomposition, asset clustering"
- Lines 206-222 (deepdive): "Part 2: PCA in Finance" section

**Content in Finance Section (deepdive 206-222):**
```
Portfolio Risk Decomposition:
- PC1 often represents "market factor"
- PC2-3 may capture sector/size factors
- Higher PCs: idiosyncratic risk

Applications:
- Risk factor modeling
- Dimensionality reduction for trading signals
- Noise reduction in time series
- Feature extraction for ML models
```

**MSc Finance Expectations - MISSING:**

| Topic | Expected | Present? | Severity |
|-------|----------|----------|----------|
| Quantitative example with real returns | CRITICAL | NO | CRITICAL |
| Connection to Fama-French factors | HIGH | Implied but not explicit | HIGH |
| Variance-covariance matrix estimation issues | HIGH | NO | HIGH |
| Eigenvalue clustering in finance | MEDIUM | NO | MEDIUM |
| Random Matrix Theory (Marchenko-Pastur) | MEDIUM | NO | MEDIUM |
| Signal-to-noise in financial PCA | MEDIUM | NO | MEDIUM |
| PCA for yield curve modeling | HIGH | NO | HIGH |
| PCA for term structure (Nelson-Siegel) | HIGH | NO | HIGH |
| t-SNE for market regime visualization | MEDIUM | NO | MEDIUM |
| Clustering assets by similarity (with t-SNE) | MEDIUM | Implied but not demonstrated | MEDIUM |
| Risk factor rotation/interpretation | HIGH | NO | HIGH |

**Critical Issue - Finance Section Too Generic:**
- Line 208-212: Lists that PC1 = market, PC2-3 = sector/size
- **No numerical example** showing actual loadings from S&P 500 or similar
- **No discussion** of how many PCs explain typical equity portfolio variance
- **No mention** of the "first few PCs explain most variance" empirical fact in finance

**Missing Yield Curve Application:**
- PCA is THE standard tool for yield curve modeling
- 3 PCs (level, slope, curvature) explain 99%+ of yield curve variance
- This is a canonical finance example - its absence is notable

### 4.2 General Finance Applications (5 points)

**Missing Finance-Specific Topics:**

| Topic | Relevance | Present? |
|-------|-----------|----------|
| Yield curve PCA (level/slope/curvature) | CRITICAL | NO |
| Equity return factor extraction | HIGH | Generic mention only |
| Correlation matrix visualization | MEDIUM | NO |
| Risk model construction | HIGH | Generic mention only |
| Portfolio optimization with PCA | MEDIUM | NO |
| Asset clustering with t-SNE | MEDIUM | Learning objective but not demonstrated |
| Market regime detection | MEDIUM | NO |
| High-frequency data visualization | LOW | NO |

**Scoring Rubric:**
| Finding | Deduction |
|---------|-----------|
| Missing canonical example (yield curve) | -4 |
| Generic finance without numerical example | -3 |
| Missing industry-standard application | -2 per item |
| Superficial treatment | -2 |

---

## SECTION 5: PEDAGOGICAL FLOW (10 points)

### 5.1 PMSP Compliance Check (3 points)

**Overview Structure:**
- [x] Learning Objectives (lines 108-119)
- [x] Problem (lines 121-137)
- [x] Method (lines 139-163)
- [x] Solution (lines 165-187)
- [x] Practice (lines 189-200)
- [x] Decision Framework (lines 202-211)
- [x] Summary/References (lines 213-222)

**Deepdive Structure:**
- [x] Part 1: PCA Foundations (lines 108-165)
- [x] Method (charts) (lines 167-203)
- [x] Part 2: PCA in Finance (lines 205-242)
- [x] Solution/Part 3: t-SNE (lines 244-343)
- [x] Part 4: Comparison (lines 345-423)
- [x] Practice (lines 425-436)
- [x] Decision Framework (lines 438-447)
- [x] Implementation (lines 449-491)
- [x] Summary (lines 493-534)

**Issue:** Both overview and deepdive follow reasonable structure. Deepdive uses "Part" organization which works for the material.

### 5.2 Overview/Deepdive Redundancy (4 points)

**Chart Usage Analysis:**

| Chart | Overview? | Deepdive? | Redundancy? |
|-------|-----------|-----------|-------------|
| 01_scree_plot | Line 143 | Line 171 | YES - DUPLICATED |
| 02_principal_components | Line 151 | Line 179 | YES - DUPLICATED |
| 03_reconstruction | Line 159 | Line 200 | YES - DUPLICATED |
| 04a_tsne_perplexity_5 | NO | Line 286 | NO - Deepdive only |
| 04b_tsne_perplexity_30 | Line 168 | Line 293 | YES - DUPLICATED |
| 04c_tsne_perplexity_100 | NO | Line 301 | NO - Deepdive only |
| 05a_pca_swiss_roll | NO | Line 349 | NO - Deepdive only |
| 05b_tsne_swiss_roll | Line 175 | Line 357 | YES - DUPLICATED |
| 06a_original_clusters | NO | Line 384 | NO - Deepdive only |
| 06b_pca_cluster_projection | NO | Line 391 | NO - Deepdive only |
| 06c_tsne_cluster_projection | Line 184 | Line 399 | YES - DUPLICATED |
| 07_decision_flowchart | Line 207 | Line 443 | YES - DUPLICATED |

**Redundancy Summary:**
- 7 out of 12 charts appear in overview (58%)
- 6 of those 7 are duplicated in deepdive (86% duplication rate for overview charts)
- Deepdive has 5 unique charts (04a, 04c, 05a, 06a, 06b)
- **Better than L04** which had 100% redundancy
- Still significant duplication but deepdive does add perplexity variations and cluster comparison

### 5.3 TBD Placeholders (2 points)

**Found:**
- Line 199 (overview): `[TBD]` for Colab notebook link
- Line 435 (deepdive): `[TBD]` for Colab notebook link

**2 TBD placeholders - same as L04**

### 5.4 Time Budget Verification (1 point)

**Instructor Guide Timing (Lines 115-122):**
| Phase | Duration | Notes |
|-------|----------|-------|
| Problem | 15 min | Curse of dimensionality |
| Method | 45 min | PCA math, t-SNE intuition |
| Solution | 45 min | Live coding both methods |
| Break | 15 min | |
| Practice | 60 min | Portfolio analysis |
| Q&A | 15 min | Preview embeddings/RL |
| **Total** | **195 min** | 3h 15min - EXCEEDS 3h budget by 15min |

**Same timing issue as L04**

**Scoring Rubric:**
| Finding | Deduction |
|---------|-----------|
| ~50% chart redundancy | -2 |
| TBD placeholder | -1 per instance |
| Time budget exceeded | -1 |
| PMSP compliance issue | -2 |

---

## SECTION 6: COMPLETENESS (5 points)

### 6.1 Essential Topics Checklist

| Topic | Required | Present? | Lines |
|-------|----------|----------|-------|
| PCA motivation (curse of dimensionality) | YES | YES | overview 123-137 |
| Covariance matrix | YES | YES | deepdive 129-132 |
| Eigendecomposition | YES | YES | deepdive 134-138 |
| Principal components as orthogonal directions | YES | YES | deepdive 114 |
| Variance explained | YES | YES | deepdive 147-165 |
| Scree plot / elbow method | YES | YES | deepdive 169-174 |
| Kaiser criterion | YES | YES | deepdive 162 |
| Reconstruction | YES | YES | deepdive 185-202 |
| PCA limitations | YES | YES | deepdive 225-241 |
| t-SNE introduction | YES | YES | deepdive 247-263 |
| t-SNE mathematical formulation | YES | YES | deepdive 266-281 |
| Perplexity parameter | YES | YES | deepdive 284-322 |
| t-SNE caveats | YES | YES | deepdive 325-342 |
| PCA vs t-SNE comparison | YES | YES | deepdive 362-380 |
| When to use which | YES | YES | deepdive 405-422 |
| UMAP alternative | YES | YES | deepdive 474-490 |
| Finance application (portfolio) | YES | WEAK | deepdive 206-222 |
| Yield curve PCA example | YES | **NO** | **MAJOR GAP** |
| Statistical inference for PCA | YES | **NO** | **MAJOR GAP** |
| t-SNE convergence/stability | YES | PARTIAL | Line 338 mentions "run multiple times" |

### 6.2 Charts Completeness

All 12 charts present and serve distinct purposes:
- [x] 01_scree_plot - Variance explained
- [x] 02_principal_components - PC visualization
- [x] 03_reconstruction - Error vs components
- [x] 04a_tsne_perplexity_5 - Low perplexity effect
- [x] 04b_tsne_perplexity_30 - Default perplexity
- [x] 04c_tsne_perplexity_100 - High perplexity effect
- [x] 05a_pca_swiss_roll - PCA limitation
- [x] 05b_tsne_swiss_roll - t-SNE strength
- [x] 06a_original_clusters - Baseline comparison
- [x] 06b_pca_cluster_projection - PCA on clusters
- [x] 06c_tsne_cluster_projection - t-SNE on clusters
- [x] 07_decision_flowchart - Method selection

**Chart Gaps - Missing Visualizations:**
- [ ] Finance example chart (portfolio loadings, yield curve PCs)
- [ ] Multiple t-SNE runs comparison (stability visualization)
- [ ] Learning rate / iteration convergence
- [ ] UMAP comparison chart
- [ ] Trustworthiness/continuity metric comparison

### 6.3 Chart Quality Audit (to be verified in execution)

| Chart | Check Template | Check Pedagogical Value | Check Finance Relevance |
|-------|----------------|------------------------|------------------------|
| 01_scree_plot | figsize, fonts, colors | Does it show elbow clearly? | Could use financial data |
| 02_principal_components | figsize, fonts, colors | PC directions clear? | Generic data |
| 03_reconstruction | figsize, fonts, colors | Error curve clear? | Generic |
| 04a/b/c_perplexity | figsize, fonts, colors | Perplexity effect clear? | Generic |
| 05a/b_swiss_roll | figsize, fonts, colors | Non-linearity shown? | Generic |
| 06a/b/c_clusters | figsize, fonts, colors | Cluster preservation? | Could be financial |
| 07_decision_flowchart | figsize, fonts, colors | Decision logic clear? | Finance branch? |

---

## SCORING MATRIX

| Section | Max | Expected Issues | Est. Score |
|---------|-----|-----------------|------------|
| Content Accuracy | 30 | Centering assumptions, Kaiser limitation, crowding problem missing | 19-24 |
| Learning Objectives | 20 | All covered but depth gaps | 14-17 |
| MSc Level | 20 | Missing derivations, no inference, sparse advanced topics | 8-12 |
| Finance Use Cases | 15 | Generic portfolio, no yield curve, no numerical example | 4-8 |
| Pedagogical Flow | 10 | ~50% redundancy (better than L04), TBDs, time budget | 5-7 |
| Completeness | 5 | Missing finance chart, no inference section | 3-4 |
| **TOTAL** | **100** | | **53-72** |

---

## REVIEW EXECUTION CHECKLIST

### Phase 1: Formula & Claims Verification (Parallel Task 1)
Agent: `architect` or `analyst`
- [ ] Verify all 10 mathematical formulas for correctness
- [ ] Check centering assumptions are stated
- [ ] Verify KL divergence formula and symmetrization
- [ ] Check Kaiser criterion limitation (correlation vs covariance)
- [ ] Verify t-distribution DOF = 1 (Cauchy) statement
- [ ] Flag all claims requiring qualification

**Key Lines to Examine:**
- deepdive 128-144 (PCA formulas)
- deepdive 147-165 (variance explained)
- deepdive 185-195 (reconstruction)
- deepdive 266-281 (t-SNE formulas)
- overview 133, deepdive 122-123, 241 (potentially misleading statements)

### Phase 2: Learning Objectives & MSc-Level Analysis (Parallel Task 2)
Agent: `architect` or `analyst`
- [ ] Map each of 4 objectives to specific content
- [ ] Verify Bloom's level achieved for each
- [ ] Check for missing derivations (PCA optimality, t-SNE gradient)
- [ ] Identify MSc-level gaps (probabilistic PCA, kernel PCA, etc.)
- [ ] Check for statistical inference methods
- [ ] Compare to ISLR Ch12 / ESL Ch14 coverage

**Key Sections:**
- overview 108-115 (stated objectives)
- deepdive Part 1 (PCA theory)
- deepdive Part 3 (t-SNE theory)
- deepdive 474-490 (UMAP)

### Phase 3: Finance Applications & Structure Review (Parallel Task 3)
Agent: `analyst`
- [ ] Evaluate portfolio risk decomposition depth
- [ ] Check for yield curve PCA example (canonical, should be present)
- [ ] Verify numerical/quantitative examples exist
- [ ] Check PMSP compliance
- [ ] Count chart redundancies
- [ ] Find all TBD placeholders
- [ ] Verify time budget

**Key Sections:**
- deepdive 206-222 (finance section)
- overview/deepdive structure comparison
- instructor guide timing

### Phase 4: Chart Quality Audit (Parallel Task 4)
Agent: `explore` + `vision`
- [ ] Read all 12 chart.py files
- [ ] Verify figsize=(10, 6), dpi settings
- [ ] Check font sizes (14pt body, 16pt title per CLAUDE.md)
- [ ] Verify color palette (MLPurple, MLBlue, etc.)
- [ ] Check single figure per chart (no subplots)
- [ ] Assess pedagogical value of each
- [ ] Identify missing visualizations

**Chart Files:**
```
01_scree_plot/chart.py
02_principal_components/chart.py
03_reconstruction/chart.py
04a_tsne_perplexity_5/chart.py
04b_tsne_perplexity_30/chart.py
04c_tsne_perplexity_100/chart.py
05a_pca_swiss_roll/chart.py
05b_tsne_swiss_roll/chart.py
06a_original_clusters/chart.py
06b_pca_cluster_projection/chart.py
06c_tsne_cluster_projection/chart.py
07_decision_flowchart/chart.py
```

### Phase 5: Gap Analysis & Scoring (Sequential, after 1-4)
Agent: `architect`
- [ ] Compile findings from all phases
- [ ] Calculate section-by-section scores
- [ ] Prioritize gaps by severity (CRITICAL > HIGH > MEDIUM > LOW)
- [ ] Generate improvement recommendations
- [ ] Produce final score with justification

---

## EXPECTED MAJOR FINDINGS

Based on content analysis, the review should identify:

1. **CRITICAL:** Finance section too generic - no numerical example
   - Location: deepdive 206-222
   - Impact: Finance application objective undermined
   - Fix: Add actual portfolio PCA example with loadings interpretation

2. **CRITICAL:** Missing yield curve PCA example
   - Location: Absent from entire lecture
   - Impact: Canonical finance application missing
   - Fix: Add 2-3 slides on yield curve PCA (level/slope/curvature)

3. **MAJOR:** PCA centering assumption not explicit
   - Location: deepdive 130-143
   - Impact: Mathematical imprecision
   - Fix: State "X is assumed centered (mean-subtracted)"

4. **MAJOR:** Kaiser criterion limitation not stated
   - Location: deepdive 162
   - Impact: Misleading guidance
   - Fix: Add "(for standardized data / correlation matrix)"

5. **MAJOR:** t-SNE crowding problem not explained
   - Location: deepdive 281 mentions "heavier tails" but not WHY
   - Impact: Student won't understand motivation for t-distribution
   - Fix: Add 1 slide on crowding problem

6. **MAJOR:** No statistical inference for dimensionality reduction
   - Location: Missing throughout
   - Impact: Not MSc-level without confidence intervals
   - Fix: Add section on bootstrap for PCA, stability for t-SNE

7. **MODERATE:** ~50% chart redundancy between overview and deepdive
   - Location: 6 of 7 overview charts duplicated
   - Impact: Missed opportunity but better than L04
   - Note: Deepdive does add 5 unique charts

8. **MODERATE:** Missing advanced methods (Kernel PCA, probabilistic PCA)
   - Location: Not covered
   - Impact: Limited MSc depth
   - Fix: Add "Advanced Variants" slide

9. **MINOR:** TBD placeholders in practice sections
   - Location: overview 199, deepdive 435
   - Impact: Incomplete materials
   - Fix: Add actual Colab links

10. **MINOR:** Time budget exceeds 3 hours by 15 minutes
    - Location: instructor guide 115-122
    - Impact: Session overrun risk
    - Fix: Trim Method or Solution by 15 min

---

## ACCEPTANCE CRITERIA

**Passing Score:** >= 70/100

**Current Estimated Score:** 53-72/100 (BORDERLINE)

**Primary Blockers to Passing:**
1. Finance section needs substantive example (+4-6 points)
2. Yield curve PCA example needed (+3-4 points)
3. Statistical inference section would help (+2-3 points)
4. Fix Kaiser criterion limitation (+1-2 points)
5. Explain crowding problem (+1-2 points)

**Quick Wins (1-2 hours each):**
- Add centering assumption statements
- Add Kaiser criterion limitation note
- Add 1 paragraph on crowding problem
- Fix TBD placeholders

**Major Additions (4+ hours each):**
- New section: Yield curve PCA example
- New chart: Portfolio loadings visualization
- New section: Statistical inference for DR
- New section: Advanced variants (Kernel PCA, PPCA)

---

## DELIVERABLES

Upon completion, generate:
1. **Hostile Review Report** (`.omc/reports/L05-hostile-review.md`)
2. **Issue List** with severity ratings and line references
3. **Recommended Additions** prioritized by impact
4. **Final Score** with per-section justification

---

**Plan Created:** 2026-02-06
**Plan Status:** READY FOR EXECUTION
**Estimated Review Time:** 90-120 minutes
**Parallel Execution:** Phases 1-4 can run concurrently

---

PLAN_READY: .omc/plans/L05-hostile-content-review.md
