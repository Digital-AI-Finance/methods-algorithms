# L03 Hostile Content Review - Execution Plan (v2)

**Plan Type:** Execution Checklist with Line-by-Line Audit
**Target:** L03 KNN & K-Means lecture materials
**Reviewer Persona:** Hostile external academic examiner (ML research background)
**Audience Assumption:** MSc Data Science students with NO pre-knowledge of ML
**Version:** 2 (Revised to address Critic feedback)
**Plan Created:** 2026-02-05

---

## CALIBRATION REFERENCE (L01/L02 Review Standards)

### L01 Review Standards Applied:
- **Severity Levels:** Critical (Must Fix) / High Priority (Should Fix) / Low Priority
- **PMSP Compliance:** Mandatory check (L01 scored 0/20 for ignoring PMSP)
- **Template Compliance:** 100% expected, chart width deviations are FAIL items
- **Frame-by-Frame Analysis:** Complete enumeration with line numbers

### L02 Review Standards Applied:
- **Predicted Score:** 55-65/100 (D-C range) - used explicit per-issue point costs
- **100-Point Rubric:** 6 sections with clear weights
- **Calibration Points:**
  - Missing statistical inference: CRITICAL (-10 points)
  - Generic finance: CRITICAL (-8 points)
  - TBD placeholder: MINOR (-2 points)

### L03 Expected Score Calibration:
Based on L01 (66.4%) and L02 (55-65%), L03 should be scored against same standards:
- Similar structural issues expected
- Cluster validity gap equivalent to missing inference in L02
- Finance use case depth comparable to L02

---

## EXECUTION OVERVIEW

This plan operationalizes the hostile review framework into concrete checklist items with VERIFIED line references, acceptance criteria, and a scoring rubric.

### Files Under Review

| File | Path | Lines | Frames | Role |
|------|------|-------|--------|------|
| Overview | `slides/L03_KNN_KMeans/L03_overview.tex` | 222 | ~12 | High-level introduction |
| Deepdive | `slides/L03_KNN_KMeans/L03_deepdive.tex` | 618 | ~32 | Mathematical depth |
| Instructor Guide | `slides/L03_KNN_KMeans/L03_instructor_guide.md` | 150 | N/A | Teaching notes |
| Charts | 7 chart.py files | ~80 each | N/A | Visualizations |

---

## TASK 1: FORMULA VERIFICATION (15 points max)

### 1.1 Minkowski Distance Formula
**Location:** deepdive.tex line 140 (VERIFIED)
**Current:** `$$d_p(\mathbf{x}, \mathbf{y}) = \left(\sum_{i=1}^{n}|x_i - y_i|^p\right)^{1/p}$$`

| Check | Status | Finding |
|-------|--------|---------|
| Formula mathematically correct | PENDING | Verify against ESL Ch.14 |
| Absolute value bars vs norm notation consistent | PENDING | Uses `|...|` - check consistency |
| Edge case p<1 mentioned | PENDING | Should note undefined for p<1 |
| Connection to Lp norm stated | PENDING | Check lines 143-146 |

**Severity:** MODERATE (notation correctness)
**Acceptance:** Formula correct AND edge cases noted AND Lp norm connection made

### 1.2 Weighted KNN Formula
**Location:** deepdive.tex line 195 (VERIFIED)
**Current:** `$$w_i = \frac{1}{d(\mathbf{x}, \mathbf{x}_i)^2}$$`

| Check | Status | Finding |
|-------|--------|---------|
| Formula mathematically correct | PENDING | YES - standard form |
| Division by zero handling | PENDING | **MISSING**: What if d=0? |
| Alternative weightings mentioned | PENDING | Check if 1/d, exp(-d) mentioned |

**Severity:** MAJOR (edge case causes runtime error in practice)
**Acceptance:** Formula includes d=0 handling OR explicitly warns about it

### 1.3 WCSS Objective Function
**Location:** deepdive.tex line 310 (VERIFIED)
**Current:** `$$\sum_{k=1}^{K}\sum_{\mathbf{x} \in C_k}\|\mathbf{x} - \mu_k\|^2$$`

| Check | Status | Finding |
|-------|--------|---------|
| Formula mathematically correct | PENDING | YES |
| Terminology: "inertia" or "distortion" mentioned | PENDING | Line 464 has "inertia_" attribute |
| Relationship to variance explained | PENDING | Check if total variance decomposition mentioned |

**Severity:** MINOR (terminology gap)
**Acceptance:** Formula correct AND inertia/distortion terminology included

### 1.4 Silhouette Score Formula
**Location:** deepdive.tex line 383 (VERIFIED)
**Current:** `$$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$$`

| Check | Status | Finding |
|-------|--------|---------|
| Formula mathematically correct | PENDING | YES |
| Edge case: singleton cluster | PENDING | **MISSING**: s(i)=0 when cluster size=1 |
| Range interpretation complete | PENDING | Lines 385-389 cover [-1,1] |

**Severity:** MODERATE (edge case)
**Acceptance:** Singleton cluster edge case mentioned

### 1.5 Standardization Formula
**Location:** deepdive.tex line 221 (VERIFIED)
**Current:** `$z = \frac{x - \mu}{\sigma}$`

| Check | Status | Finding |
|-------|--------|---------|
| Formula correct | PENDING | YES |
| Edge case: sigma=0 | PENDING | **MISSING** |
| When to use vs Min-Max | PENDING | Line 226 gives brief guidance |

**Severity:** MINOR
**Acceptance:** Division by zero case mentioned

### 1.6 Min-Max Normalization Formula
**Location:** deepdive.tex line 222 (VERIFIED)
**Current:** `$x' = \frac{x - x_{min}}{x_{max} - x_{min}}$`

| Check | Status | Finding |
|-------|--------|---------|
| Formula correct | PENDING | YES |
| Edge case: x_max = x_min | PENDING | **MISSING** |
| Bounded [0,1] output stated | PENDING | YES |

**Severity:** MINOR
**Acceptance:** Edge case mentioned

---

## TASK 2: MISLEADING STATEMENTS AUDIT (10 points max)

### 2.1 K-Means Convergence Claim
**Location:** deepdive.tex line 336 (VERIFIED)
**Current:** "Guaranteed to converge (WCSS decreases each iteration)"

| Check | Status | Finding |
|-------|--------|---------|
| Claim technically true | PENDING | TRUE for local convergence |
| Global optimum clarification | PENDING | Line 337 says "may converge to local optimum" |
| Finite iterations bound | PENDING | **MISSING**: No mention of worst-case iterations |
| EM relationship | PENDING | **MISSING**: K-Means is hard EM special case |

**Severity:** CRITICAL (MSc should understand EM connection)
**Acceptance:** EM relationship explained OR convergence proof sketch provided

### 2.2 K-Means++ "Provably Better" Claim
**Location:** deepdive.tex line 365 (VERIFIED)
**Current:** "K-Means++ gives provably better initialization with theoretical guarantees"

| Check | Status | Finding |
|-------|--------|---------|
| Claim substantiated | PENDING | NO - vague "theoretical guarantees" |
| O(log k) competitive ratio cited | PENDING | **MISSING** |
| Arthur & Vassilvitskii reference | PENDING | Line 606 has reference but no detail |

**Severity:** MAJOR (unsubstantiated claim in academic material)
**Acceptance:** Competitive ratio stated OR approximation guarantee quantified

### 2.3 Curse of Dimensionality Claim
**Location:** deepdive.tex line 234 (VERIFIED)
**Current:** "All points become approximately equidistant"

| Check | Status | Finding |
|-------|--------|---------|
| Claim technically correct | PENDING | Qualitatively true |
| Probability bound or citation | PENDING | **MISSING** |
| Dimensionality threshold guidance | PENDING | Line 245: "<20" but no justification |

**Severity:** MODERATE (claims without citation)
**Acceptance:** Citation provided OR probability bound given

### 2.4 KD-Tree Complexity Claim
**Location:** deepdive.tex line 257 (VERIFIED)
**Current:** "$O(d \log n)$ average for low $d$"

| Check | Status | Finding |
|-------|--------|---------|
| Claim correct with qualification | PENDING | YES - "for low d" is stated |
| Degradation in high-d mentioned | PENDING | **MISSING** explicit statement |
| Definition of "low d" | PENDING | **MISSING** |

**Severity:** MINOR (qualification present but incomplete)
**Acceptance:** Threshold for "low d" stated (typically d < 20)

---

## TASK 3: ALGORITHM CORRECTNESS (5 points max)

### 3.1 K-Means Pseudocode
**Location:** deepdive.tex lines 324-332 (VERIFIED: algorithmic environment at lines 324-332)

| Check | Status | Finding |
|-------|--------|---------|
| Algorithm terminates correctly | PENDING | Line 330 has "or max iterations" |
| Empty cluster handling | PENDING | **MISSING**: What if cluster becomes empty? |
| Convergence criterion precise | PENDING | "centroids don't change" vs "assignments don't change" |
| Tolerance parameter for floats | PENDING | **MISSING** |

**Severity:** MAJOR (empty clusters cause runtime errors)
**Acceptance:** Empty cluster reinit strategy mentioned OR convergence tolerance specified

---

## TASK 4: LEARNING OBJECTIVES ALIGNMENT (20 points max)

### 4.1 Bloom's Taxonomy Verification (L01/L02 Standard Applied)

**From overview.tex lines 113-116:**

| Objective | Bloom Level | Verb | Evidence Required | Present? |
|-----------|-------------|------|-------------------|----------|
| "Apply KNN for classification with appropriate K selection" | Apply | Apply | K selection demonstration with CV | PENDING |
| "Implement K-Means clustering and evaluate cluster quality" | Apply+Evaluate | Implement, Evaluate | Pseudocode + quality metrics | PENDING |
| "Compare distance metrics and their effects on results" | Analyze | Compare | Comparative analysis | PENDING |
| "Distinguish between supervised (KNN) and unsupervised (K-Means)" | Understand | Distinguish | Clear comparison table | PENDING |

### 4.2 Objective 1: "Apply KNN for classification with appropriate K selection"
**Stated:** overview.tex line 113, deepdive.tex implicit

| Coverage Item | Location | Depth | Finding |
|---------------|----------|-------|---------|
| KNN algorithm explained | deepdive 111-126 | GOOD | Clear explanation |
| K selection methods | deepdive 169-185 | PARTIAL | sqrt(n) rule, CV mentioned |
| Cross-validation code/example | N/A | **MISSING** | Only mentioned, not shown |
| Bias-variance empirical demo | N/A | **MISSING** | Only conceptual |

**Severity:** MAJOR (objective partially met without practical demonstration)
**Acceptance:** CV code snippet OR bias-variance plot included

### 4.3 Objective 2: "Implement K-Means and evaluate cluster quality"
**Stated:** overview.tex line 114

| Coverage Item | Location | Depth | Finding |
|---------------|----------|-------|---------|
| K-Means algorithm | deepdive 305-340 | GOOD | Clear pseudocode |
| Elbow method | deepdive 368-373 | BASIC | Subjective, no automation |
| Silhouette score | deepdive 375-398 | GOOD | Formula and interpretation |
| Gap statistic | N/A | **MISSING** | CRITICAL for MSc |
| Davies-Bouldin index | N/A | **MISSING** | |
| Calinski-Harabasz index | N/A | **MISSING** | |
| Hopkins statistic | N/A | **MISSING** | Should cluster at all? |

**Severity:** CRITICAL (cluster validity limited to 2 methods, no statistical tests)
**Acceptance:** At least Gap statistic OR Hopkins statistic added

### 4.4 Objective 3: "Compare distance metrics and their effects"
**Stated:** overview.tex line 115

| Coverage Item | Location | Depth | Finding |
|---------------|----------|-------|---------|
| Minkowski family (L1, L2, Linf) | deepdive 138-155 | GOOD | Clear explanation |
| Cosine similarity | N/A | **MISSING** | Critical for text/embeddings |
| Mahalanobis distance | N/A | **MISSING** | Accounts for correlation |
| Jaccard/Hamming | N/A | **MISSING** | For categorical data |
| Distance metric selection guide | deepdive 148-153 | WEAK | Only p-value guidance |

**Severity:** MAJOR (objective weakly met - limited to one family)
**Acceptance:** At least cosine similarity OR Mahalanobis distance added

### 4.5 Objective 4: "Distinguish supervised (KNN) vs unsupervised (K-Means)"
**Stated:** overview.tex line 116

| Coverage Item | Location | Depth | Finding |
|---------------|----------|-------|---------|
| Comparison table | deepdive 470-486 | GOOD | Clear 6-row comparison |
| Conceptual distinction | overview 123-138 | GOOD | Business problem framing |
| K meaning difference | deepdive 485 | GOOD | Explicitly stated |

**Severity:** NONE (objective well met)
**Acceptance:** PASS

---

## TASK 5: MSc LEVEL APPROPRIATENESS (20 points max)

### 5.1 Theoretical Depth Assessment

| Topic | MSc Expected | Present | Location | Gap |
|-------|--------------|---------|----------|-----|
| K-Means as EM special case | YES | **NO** | N/A | CRITICAL |
| Voronoi tessellation definition | YES | PARTIAL | deepdive 400-404 | Mentioned, not defined |
| Convergence proof sketch | YES | **NO** | N/A | Only states "guaranteed" |
| Lloyd's algorithm vs K-Means | YES | **NO** | N/A | Not distinguished |
| VC dimension of KNN | YES | **NO** | N/A | CRITICAL for theory |
| Consistency of KNN | YES | PARTIAL | deepdive 607 | Reference only |
| Computational complexity | PARTIAL | YES | deepdive 249-268 | Adequate |

**Severity:** CRITICAL (2+ major theory gaps)
**Acceptance:** At least EM connection OR VC dimension discussion added

### 5.2 Statistical Inference for Clustering

| Test/Method | MSc Expected | Present | Gap |
|-------------|--------------|---------|-----|
| Gap statistic (Tibshirani 2001) | YES | **NO** | CRITICAL |
| Bootstrap stability | YES | **NO** | |
| Cluster significance testing | YES | **NO** | |
| Null distribution for silhouette | YES | **NO** | |
| Hartigan's dip test | YES | **NO** | |
| Hopkins statistic | YES | **NO** | Should cluster at all? |

**Current Coverage:** ZERO statistical tests for cluster validity

**Severity:** CRITICAL (no hypothesis testing for clustering)
**Acceptance:** At least Gap statistic AND Hopkins statistic mentioned

### 5.3 Validation Methodologies

| Method | Present | Location |
|--------|---------|----------|
| Elbow method | YES | deepdive 368-373 |
| Silhouette score | YES | deepdive 375-398 |
| Internal vs external validation | **NO** | |
| Stability via perturbation | **NO** | |
| NbClust framework | **NO** | |

**Severity:** MAJOR (limited to 2 basic methods)
**Acceptance:** Internal/external validation distinction made

---

## TASK 6: FINANCE USE CASE DEPTH (15 points max)

### 6.1 Customer Segmentation (deepdive lines 488-506)

| MSc Finance Topic | Expected | Present | Line |
|-------------------|----------|---------|------|
| RFM Analysis | YES | **NO** | Generic features only |
| Customer Lifetime Value | YES | **NO** | |
| Segment migration analysis | YES | **NO** | |
| Basel III risk segmentation | YES | **NO** | |
| Marketing lift measurement | YES | **NO** | |
| A/B testing on segments | YES | **NO** | |
| GDPR profiling implications | YES | **NO** | |

**Current:** Generic features (frequency, amount, balance, products) with generic segments

**Severity:** MAJOR (undergraduate-level example)
**Acceptance:** RFM analysis added OR CLV connection made

### 6.2 Fraud Detection (deepdive lines 508-525)

| MSc Finance Topic | Expected | Present | Line |
|-------------------|----------|---------|------|
| Class imbalance (100:1) | YES | **NO** | |
| SMOTE/undersampling | YES | **NO** | |
| Fraud pattern types | YES | **NO** | |
| Real-time scoring constraints | YES | **NO** | |
| Velocity features | YES | **NO** | |
| Precision-recall tradeoff | YES | **NO** | |
| Cost-sensitive learning | YES | **NO** | |
| PSD2 regulatory context | YES | **NO** | |

**Current:** Line 512-515 suggests simple KNN majority vote - naive at MSc level

**Critical Issue:** No discussion that majority vote fails when fraud is <1%

**Severity:** CRITICAL (recommendation would fail in practice)
**Acceptance:** Class imbalance discussed AND weighted voting or cost-sensitive approach mentioned

---

## TASK 7: PEDAGOGICAL FLOW (10 points max)

### 7.1 Chart Redundancy Audit

| Chart | Overview Line | Deepdive Line | Redundancy |
|-------|---------------|---------------|------------|
| 01_knn_boundaries | 144 | 159 | SAME |
| 02_distance_metrics | 151 | 131 | SAME |
| 03_kmeans_iteration | 158 | 344 | SAME |
| 04_elbow_method | 165 | 370 | SAME |
| 05_silhouette | 174 | 395 | SAME |
| 06_voronoi | 181 | 402 | SAME |
| 07_decision_flowchart | 203 | 548 | SAME |

**Finding:** 100% chart redundancy (7/7 charts duplicated)
**Impact:** Deepdive adds text but no new visualizations
**Severity:** MAJOR (wasted opportunity for MSc-level charts)

**Acceptance:** At least 3 unique deepdive charts added OR charts enhanced with MSc-level content

### 7.2 TBD Placeholder Audit

| File | Line | Content |
|------|------|---------|
| overview.tex | 196 | `[TBD]` for Colab link |
| deepdive.tex | 299 | `[TBD]` for Colab link |

**Severity:** MINOR
**Acceptance:** Placeholders replaced with actual links OR removed

### 7.3 Exercise Progression

| File | Exercise Content | Progression |
|------|------------------|-------------|
| overview.tex | Lines 188-197 | Exercise 1-3 |
| deepdive.tex | Lines 289-300 | SAME Exercise 1-3 |

**Finding:** Identical exercise text in both files
**Severity:** MODERATE (no progression from overview to deepdive)
**Acceptance:** Deepdive exercises are advanced versions OR clearly labeled as same

---

## TASK 8: COMPLETENESS CHECK (5 points max)

### 8.1 Essential Topics Checklist

| Topic | Required | Present | Location | Notes |
|-------|----------|---------|----------|-------|
| KNN algorithm | YES | YES | deepdive 111-126 | |
| Distance metrics | YES | YES | deepdive 128-155 | Limited to Minkowski |
| K selection for KNN | YES | PARTIAL | deepdive 169-185 | No CV code |
| Feature scaling | YES | YES | deepdive 209-227 | |
| Curse of dimensionality | YES | YES | deepdive 229-246 | |
| K-Means algorithm | YES | YES | deepdive 305-340 | |
| Initialization (K-Means++) | YES | YES | deepdive 349-366 | Claim unsubstantiated |
| Elbow method | YES | YES | deepdive 368-373 | |
| Silhouette score | YES | YES | deepdive 375-398 | |
| K-Means assumptions | YES | YES | deepdive 407-423 | |
| Variants (Mini-Batch, K-Medoids) | YES | YES | deepdive 425-446 | |
| KNN vs K-Means comparison | YES | YES | deepdive 470-486 | |
| Finance applications | YES | WEAK | deepdive 488-525 | Generic |
| Alternatives (DBSCAN, GMM) | YES | YES | deepdive 553-569 | |

### 8.2 Missing Charts (Opportunities)

| Chart Topic | Value at MSc | Present |
|-------------|--------------|---------|
| Curse of dimensionality visualization | HIGH | NO |
| K-Means++ initialization process | HIGH | NO |
| Cluster validity metrics comparison | HIGH | NO |
| Finance-specific example | MEDIUM | NO |
| Gap statistic plot | HIGH | NO |
| Class imbalance impact | HIGH | NO |

---

## TASK 9: TIME BUDGET VERIFICATION (NEW - Per Critic Feedback)

### 9.1 Session Duration Analysis

**Instructor Guide Specification:** 3 hours total (L03_instructor_guide.md line 5)

**Timing Guide from Instructor Guide (lines 109-118):**

| Phase | Duration | Content |
|-------|----------|---------|
| Problem | 15 min | Dual problem motivation |
| Method | 45 min | KNN vs K-Means distinction |
| Solution | 45 min | Live coding both algorithms |
| Break | 15 min | |
| Practice | 60 min | Customer segmentation focus |
| Q&A | 15 min | Preview random forests |
| **TOTAL** | **195 min** | 3 hours 15 min |

### 9.2 Slide Count Analysis

| File | Lines | Est. Frames | Est. Time @ 2 min/slide |
|------|-------|-------------|-------------------------|
| Overview | 222 | ~12 | 24 min |
| Deepdive | 618 | ~32 | 64 min |
| **TOTAL** | 840 | ~44 | **88 min** |

### 9.3 Content vs Time Budget

| Item | Instructor Guide Allocation | Actual Content Estimate |
|------|----------------------------|-------------------------|
| Presentation (Method+Solution) | 90 min | 88 min slides only |
| Live coding "both algorithms" | 45 min | NO CODE IN SLIDES |
| Practice notebook | 60 min | Notebook TBD |

**CRITICAL ISSUE:** Instructor Guide specifies "Live coding both algorithms" (line 73-76) but slides contain NO executable code examples, only scikit-learn API snippets.

**Severity:** HIGH (instructor guide promises content not in slides)
**Acceptance:** Either add code examples to slides OR update instructor guide expectations

### 9.4 Prerequisite Dependency Verification

**Instructor Guide (line 10):** "Prerequisites: L01-L02, basic statistics"

| Prerequisite | How L03 Uses It | Explicit Call-out? |
|--------------|-----------------|-------------------|
| L01 Linear Regression | Distance metrics relate to loss functions | NO |
| L02 Logistic Regression | Classification context for KNN | NO |
| Basic statistics | Mean, variance for standardization | NO |

**For "No Pre-Knowledge" Audience:** Material assumes students know:
- What classification means (from L02)
- What a loss function is (from L01)
- Mean and standard deviation (from "basic statistics")

**Finding:** Prerequisites ARE used but NOT explicitly called out in slides

**Severity:** MODERATE (could confuse students without L01/L02)
**Acceptance:** Add 1 slide connecting to L01/L02 OR note in instructor guide

---

## TASK 10: PMSP COMPLIANCE CHECK (NEW - Per L01 Standard)

### 10.1 PMSP Section Mapping

**Template PMSP Framework:**
1. `\section{Problem}`
2. `\section{Method}`
3. `\section{Solution}`
4. `\section{Practice}`
5. `\section{Decision Framework}` (optional)
6. `\section{Summary}`

### 10.2 Overview.tex PMSP Analysis

| Section in File | Line | PMSP Match | Notes |
|-----------------|------|------------|-------|
| `\section{Problem}` | 108 | **YES** | |
| `\section{Method}` | 140 | **YES** | |
| `\section{Solution}` | 170 | **YES** | |
| `\section{Practice}` | 186 | **YES** | |
| `\section{Decision Framework}` | 199 | **YES** | |
| `\section{Summary}` | 208 | **YES** | |

**Overview PMSP Compliance:** **PASS** (6/6 sections match)

### 10.3 Deepdive.tex PMSP Analysis

| Section in File | Line | PMSP Match | Notes |
|-----------------|------|------------|-------|
| `\section{K-Nearest Neighbors}` | 109 | **NO** | Should be Problem/Method |
| `\section{Practice}` | 289 | **YES** | |
| `\section{K-Means Clustering}` | 303 | **NO** | Should be Solution |
| `\section{Comparison and Applications}` | 468 | **NO** | Not in PMSP |
| `\section{Summary}` | 572 | **YES** | |

**Deepdive PMSP Compliance:** **FAIL** (2/5 sections match)

**Comparison to L01:** L01 deepdive scored 0/20 for PMSP violation. L03 deepdive has SAME issue - uses topic names instead of PMSP sections.

**Severity:** MAJOR (violates course structure per L01 precedent)
**Acceptance:** Restructure deepdive to follow PMSP OR document intentional deviation

---

## TASK 11: CHART QUALITY CRITERIA (NEW - Per Critic Feedback)

### 11.1 Chart Technical Standards

Based on `templates/chart_template.py` and `CLAUDE.md`:

| Criterion | Standard | To Verify |
|-----------|----------|-----------|
| Figure size | (10, 6) | All 7 charts |
| Font size (base) | 14 | All 7 charts |
| Axes label size | 14 | All 7 charts |
| Title size | 16 | All 7 charts |
| Tick label size | 13 | All 7 charts |
| Legend font size | 13 | All 7 charts |
| DPI | 150 | All 7 charts |
| Output format | PDF | All 7 charts |

### 11.2 Color Palette Compliance

**Required Colors (per CLAUDE.md):**
- MLPurple: #3333B2
- MLBlue: #0066CC
- MLOrange: #FF7F0E
- MLGreen: #2CA02C
- MLRed: #D62728
- MLLavender: #ADADE0

**Chart Color Audit (from code inspection):**

| Chart | Colors Used | Compliant? |
|-------|-------------|------------|
| 01_knn_boundaries | MLRED, MLGREEN, MLBLUE | YES |
| 02_distance_metrics | MLBLUE, MLRED, MLGREEN, MLORANGE | YES |
| 05_silhouette | MLRED, MLGREEN, MLBLUE | YES |

**Preliminary Finding:** Charts use correct color palette

### 11.3 Accessibility Considerations

| Criterion | Standard | Status |
|-----------|----------|--------|
| Colorblind-safe palette | Red-green distinction problematic | **NEEDS REVIEW** |
| Sufficient contrast | Text on backgrounds | PENDING |
| Alternative to color (shape/pattern) | For class distinction | **MISSING** in some charts |
| Alt-text metadata | Chart description | Present in CHART_METADATA |

**Severity:** MODERATE (accessibility not fully addressed)
**Acceptance:** Add marker shapes to distinguish classes OR note colorblind caveat

---

## SCORING RUBRIC

### Section Weights and Deductions

| Section | Max Points | Deduction Rules |
|---------|------------|-----------------|
| **Formula Verification** | 15 | -5 per error, -2 per missing edge case, -1 per notation issue |
| **Misleading Statements** | 10 | -3 per unqualified claim, -2 per missing citation |
| **Algorithm Correctness** | 5 | -2 per bug, -1 per imprecision |
| **Learning Objectives** | 20 | -7 unmet, -5 weak, -3 partial |
| **MSc Level** | 20 | -5 missing inference, -3 per theory gap |
| **Finance Use Cases** | 15 | -4 generic example, -3 missing industry method |
| **Pedagogical Flow** | 10 | -3 chart redundancy, -1 per TBD, -2 duplicate exercises |
| **Completeness** | 5 | -1 per missing essential topic |

### Severity Classification (L01/L02 Aligned)

| Severity | Definition | Impact on Score |
|----------|------------|-----------------|
| **CRITICAL** | Would cause an external examiner to reject | -5 to -7 points |
| **MAJOR** | Significant gap for MSc-level material | -3 to -4 points |
| **MODERATE** | Notable omission but not disqualifying | -2 points |
| **MINOR** | Polish issue or minor gap | -1 point |

---

## EXPECTED SCORE CALCULATION (Calibrated to L01/L02)

### Detailed Deduction Justification

| Issue | Severity | Points | L02 Comparison |
|-------|----------|--------|----------------|
| Missing EM connection | CRITICAL | -5 | L02: Missing Wald test (-10) |
| Missing Gap statistic | CRITICAL | -5 | L02: Missing deviance (-5) |
| K-Means++ unsubstantiated | MAJOR | -3 | L02: Generic finance (-4) |
| Class imbalance in fraud | CRITICAL | -5 | New for L03 |
| Generic customer segmentation | MAJOR | -4 | L02: Same issue (-4) |
| Chart redundancy | MAJOR | -3 | L01: N/A |
| TBD placeholders (2) | MINOR | -2 | L02: -2 |
| Missing cosine/Mahalanobis | MAJOR | -3 | New for L03 |
| Deepdive PMSP violation | MAJOR | -4 | L01: -20 (more severe) |
| Missing edge cases (4) | MODERATE | -8 | 4 x -2 |
| Empty cluster handling | MAJOR | -2 | New for L03 |
| Duplicate exercises | MODERATE | -2 | New for L03 |

### Score Calculation

| Section | Max | Expected Deductions | Expected Score |
|---------|-----|---------------------|----------------|
| Formula Verification | 15 | -8 (edge cases) | 7 |
| Misleading Statements | 10 | -6 (EM, K-Means++, curse) | 4 |
| Algorithm Correctness | 5 | -2 (empty cluster) | 3 |
| Learning Objectives | 20 | -12 (objectives 1-3) | 8 |
| MSc Level | 20 | -13 (theory, inference) | 7 |
| Finance Use Cases | 15 | -9 (generic, imbalance) | 6 |
| Pedagogical Flow | 10 | -7 (redundancy, TBDs, exercises) | 3 |
| Completeness | 5 | -2 (distance metrics, CV code) | 3 |
| **TOTAL** | **100** | **-59** | **41** |

**Expected Final Score: 41-50/100 (F-D range)**

**Calibration Note:** This is LOWER than L02's predicted 55-65 because:
1. L03 has MORE critical gaps (EM, Gap statistic, class imbalance - 3 vs 2)
2. Chart redundancy is a new issue not present in L02
3. Deepdive PMSP violation (though less severe than L01's complete abandonment)

---

## REVIEW PASS CRITERIA vs CONTENT QUALITY CRITERIA (Separated per Critic)

### Review Pass Criteria (Procedural)

The review is COMPLETE when all these boxes are checked:

- [ ] All formulas verified against authoritative sources
- [ ] All line numbers confirmed accurate in current files
- [ ] All TBD markers documented
- [ ] All charts confirmed to exist and compile
- [ ] Frame count verified for both files
- [ ] Time budget analysis completed
- [ ] PMSP compliance assessed for both files
- [ ] Cross-reference with instructor guide completed
- [ ] Score calculated with justifications
- [ ] Report generated with severity-prioritized findings

### Content Quality Criteria (For MSc-Level Approval)

The materials would pass hostile review (score >= 70) if:

**CRITICAL items resolved (ALL mandatory):**
- [ ] EM relationship to K-Means explained
- [ ] Gap statistic or equivalent cluster validity test included
- [ ] Class imbalance in fraud detection addressed
- [ ] K-Means++ guarantee quantified (O(log k) competitive ratio)

**MAJOR items mostly resolved (at least 5 of 8):**
- [ ] Weighted KNN edge case handled (d=0)
- [ ] Cross-validation code example provided
- [ ] At least one non-Minkowski distance added (cosine OR Mahalanobis)
- [ ] RFM or CLV in customer segmentation
- [ ] Empty cluster handling in pseudocode
- [ ] At least 3 unique deepdive charts
- [ ] Internal/external validation distinction
- [ ] Deepdive PMSP structure corrected OR justified

---

## REVIEW EXECUTION PROTOCOL

### Phase 1: Automated Checks (30 min)
1. [ ] Verify all formula LaTeX compiles correctly
2. [ ] Check all chart.py files execute without error
3. [ ] Validate all \includegraphics paths exist
4. [ ] Count frames in overview (expected ~12) and deepdive (expected ~32)
5. [ ] Find all TBD/TODO markers
6. [ ] Verify line numbers against current file versions

### Phase 2: Formula Audit (20 min)
1. [ ] Verify each formula against ISLR Chapter 12 (clustering) and Chapter 2 (KNN)
2. [ ] Cross-check against ESL Chapter 13-14
3. [ ] Check notation consistency throughout
4. [ ] Document missing edge cases
5. [ ] Note terminology gaps

### Phase 3: Claims Verification (20 min)
1. [ ] Flag all "always", "never", "guaranteed", "provably" statements
2. [ ] Check each claim against cited sources
3. [ ] Identify unsubstantiated assertions
4. [ ] Rate each by misleading potential

### Phase 4: Learning Objectives Mapping (15 min)
1. [ ] For each objective, list all supporting content with line numbers
2. [ ] Rate depth of coverage (GOOD/PARTIAL/WEAK/MISSING)
3. [ ] Verify Bloom's taxonomy level achieved
4. [ ] Identify gaps between stated and delivered

### Phase 5: MSc Appropriateness (20 min)
1. [ ] Compare against standard MSc ML syllabus (ESL, ISLR, Murphy)
2. [ ] Check for statistical inference coverage
3. [ ] Verify theoretical depth meets postgraduate level
4. [ ] Note undergraduate-level content that needs elevation

### Phase 6: Finance Domain Review (15 min)
1. [ ] Evaluate realism of finance examples
2. [ ] Check for industry-standard methods (RFM, CLV, etc.)
3. [ ] Identify missing practical considerations (class imbalance, cost-sensitive)
4. [ ] Note regulatory/compliance gaps

### Phase 7: PMSP and Structure Review (15 min)
1. [ ] Verify PMSP compliance for both files
2. [ ] Count redundancies between files
3. [ ] Assess exercise progression
4. [ ] Check instructor guide alignment

### Phase 8: Time Budget Verification (10 min)
1. [ ] Calculate total presentation time from frame count
2. [ ] Compare against instructor guide allocations
3. [ ] Identify content gaps between guide and slides
4. [ ] Verify prerequisite dependencies

### Phase 9: Chart Quality Audit (10 min)
1. [ ] Verify rcParams in each chart.py
2. [ ] Check color palette compliance
3. [ ] Assess accessibility (colorblind-safe, contrast)
4. [ ] Verify metadata completeness

### Phase 10: Report Generation (20 min)
1. [ ] Compile findings by severity
2. [ ] Calculate final score with justification
3. [ ] Compare to L01/L02 scores for calibration
4. [ ] Prioritize recommendations by impact
5. [ ] Generate hostile review report

**Total Estimated Time: 175 minutes (2.9 hours)**

---

## DELIVERABLES

Upon execution, generate:

1. **`.omc/reports/L03-hostile-review-report.md`**
   - Executive summary with score and L01/L02 comparison
   - Findings by severity (CRITICAL, MAJOR, MODERATE, MINOR)
   - Evidence with exact line references
   - Score breakdown by section

2. **`.omc/reports/L03-recommended-additions.md`**
   - Prioritized list of improvements
   - Effort estimates (LOW/MEDIUM/HIGH)
   - Impact on score per improvement

3. **`.omc/notepads/L03-hostile-review/issues.md`**
   - Detailed issue log for tracking

---

**Plan Status:** READY FOR EXECUTION (v2)
**Estimated Execution Time:** 175 minutes (2.9 hours)
**Plan Created:** 2026-02-05
**Revision Notes:** Addressed all Critic feedback from v1:
- Re-verified ALL line numbers against source files
- Added TASK 9: Time Budget Verification
- Added TASK 10: PMSP Compliance Check (per L01 standard)
- Added TASK 11: Chart Quality Criteria
- Added prerequisite dependency verification
- Separated Review Pass Criteria from Content Quality Criteria
- Added calibration section referencing L01/L02 scores
- Revised expected score to 41-50 with detailed justification

---

PLAN_READY: .omc/plans/L03-hostile-review-execution.md
