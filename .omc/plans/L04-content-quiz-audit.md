# L04 Content & Quiz Audit: Ultra-Deep Analysis and Remediation Plan

## Context

### Original Request
Two-part ultra-deep analysis: (1) Make L04 Decision Trees & Random Forests slides accessible without pre-knowledge, (2) audit ALL quizzes across the course for accuracy, pedagogy, and format consistency.

### Files in Scope

**Part 1 -- L04 Slides (4 .tex files only; chart.py files are OUT OF SCOPE -- content accuracy was verified in the prior hostile review):**
- `slides/L04_Random_Forests/L04_overview.tex` (25 slides)
- `slides/L04_Random_Forests/L04_deepdive.tex` (42 main + 10 appendix = 52 slides)
- `slides/L04_Random_Forests/L04_rf_mini.tex` (10 slides)
- `slides/L04_Random_Forests/L04_rf_full.tex` (31 slides)

**Part 2 -- ALL Quizzes (9 HTML + 3 XML + 3 legacy HTML):**
- `docs/quiz/L01_linear_regression.html` (20q)
- `docs/quiz/L02_logistic_regression.html` (20q)
- `docs/quiz/L03_knn.html` (20q)
- `docs/quiz/L03_kmeans.html` (20q)
- `docs/quiz/L03_knn_kmeans.html` (20q)
- `docs/quiz/L03_knn_kmeans_accessible.html` (20q)
- `docs/quiz/L04_random_forests.html` (20q)
- `docs/quiz/L05_pca_tsne.html` (20q)
- `docs/quiz/L06_embeddings_rl.html` (20q)
- `quizzes/quiz1_topics_1_2.xml` (16q: L01+L02, Moodle)
- `quizzes/quiz2_topics_3_4.xml` (16q: L03+L04, Moodle)
- `quizzes/quiz3_topics_5_6.xml` (16q: L05+L06, Moodle)
- `docs/quiz/quiz1_regression.html` (legacy)
- `docs/quiz/quiz2_classification_ensemble.html` (legacy)
- `docs/quiz/quiz3_advanced.html` (legacy)

---

## PART 1: L04 Slide Analysis -- Findings and Remediation

### 1.1 Cross-File Content Map

**NOTE FOR EXECUTORS:** Consult this map when implementing fixes. It shows where each topic appears across the 4 files, preventing duplicate or contradictory edits.

| Topic | Overview | Deepdive | Mini | Full |
|-------|----------|----------|------|------|
| Decision tree intro (what is a tree) | Slide 8 (chart only, no text) | Slides 5-10 (thorough) | Slide 1 (brief) | Frame 4-7 (thorough) |
| Gini impurity formula | Slide 13 (formula only) | Slides 6-7 (with properties) | Slide 3 (formula in footnote) | Frame 5 (with worked example) |
| Entropy / info gain | Slide 13 (formula only) | Slide 7 (separate slide) | -- | Frame 6 (separate slide) |
| Regression trees MSE | -- | Slide 8 | -- | -- |
| CART pseudocode | -- | Slide 9 | -- | -- |
| Pruning | -- | Slide 10 | -- | -- |
| Bootstrap / bagging | Slide 10-11 | Slides 12-14 | Slide 4 | Frame 8-9 |
| Variance formula | Slide 11 | Slides 13-14 (full proof) | Slide 5 | Frame 8, 12 |
| RF two sources of randomness | Slide 12 | Slide 15 | Slide 4-5 | Frame 11 |
| RF pseudocode | -- | Slide 16 | -- | Frame 15 |
| Hyperparameters | -- | Slides 17-19 | -- | Frame 24 |
| Feature importance (MDI) | Slide 16 | Slides 20-21 | -- | Frame 16-17 |
| Permutation importance | Slide 16 | Slide 22 | -- | Frame 17 |
| Statistical inference | -- | Slide 23 | -- | -- |
| SHAP | Slide 16 | Slide 24 | -- | Frame 18 |
| OOB error | Slide 14 | Slides 28-29 | Slide 4 | Frame 10 |
| Bias-variance decomposition | -- | Slide 25 | -- | -- |
| Variance chart (single vs forest) | -- | Slides 26-27 | -- | Frame 14 |
| Ensemble voting | Slide 15 | -- | Slide 7 (chart) | Frame 13 |
| Fraud detection / class imbalance | Slides 17-18 | Slides 35-36 | Slide 6 | Frame 25-26 |
| Boosting overview | Slides 19-20 | Slides 30-34 | Slide 3 (taxonomy) | Frame 19-22 |
| AdaBoost | -- | Slide 31 | -- | Frame 20 |
| Gradient boosting | -- | Slide 32 | -- | Frame 21 |
| XGBoost | -- | Slide 33 | -- | Frame 22 |
| Decision flowchart | Slide 21 | -- | Slide 9 | Frame 27 |
| Stakeholder analysis | -- | -- | Slide 8 | Frame 28 |
| Regulatory compliance | -- | Slide 24 (SHAP) | Slide 8 | Frame 29 |
| Closing comic | Slide 24 | Slide 42 | -- | Frame 31 |

### 1.2 Accessibility Findings (Slide-by-Slide)

#### L04_overview.tex -- 6 Issues Found

**ISSUE O-1: Decision tree chart with no textual explanation (Slide 8)**
- Slide 8 is chart-only with a bottomnote. A student with no tree knowledge sees a chart.pdf and a footnote but NO explanation of what internal nodes, leaves, or paths mean.
- **Fix:** Add 3-4 bullet points above or beside the chart: "Internal node = test one feature threshold", "Branch = outcome of test", "Leaf = final prediction", "Path from root to leaf = one rule."
- **Cross-ref:** Related to HARMONY-2 (DT introduction quality). See issue IDs: O-1, O-4 (overview), M-2 (mini).

**ISSUE O-2: Gini/Entropy formulas presented without worked example (Slide 13)**
- Three formulas (Gini, Entropy, IG) are presented on one slide with no worked example. The bottomnote says "both measure impurity" but a student new to these concepts needs a concrete calculation.
- **Fix:** Add a minimal worked example: "For a node with 70 fraud, 30 legit: G = 1 - (0.7^2 + 0.3^2) = 0.42." Or split into two slides with one example each.

**ISSUE O-3: Variance formula presented cold (Slide 11)**
- The formula Var(f_bar) = rho*sigma^2 + (1-rho)/B * sigma^2 appears with variable definitions but the plain-language bridge is incomplete. Line 265 has a partial bridge: "Key insight: once B is large enough, reducing rho is the only way to improve further." This addresses the B term but does NOT explain the two-part structure of the formula or what rho represents intuitively.
- **Fix:** ADD (do not replace the existing line 265 insight) a 2-sentence plain-language interpretation before the bullet list: "In plain language: the ensemble variance has two parts -- a floor set by how similar the trees are (rho), and a shrinking part that goes to zero as we add more trees (B)." Keep the existing "Key insight" sentence as it complements this.

**ISSUE O-4: No definition of "decision tree" before first use**
- Slide 5 ("From One Tree to a Forest") references "a single decision tree" but never defines what a decision tree IS. The course has no separate DT lecture. L04 overview jumps straight to "one tree vs. many trees" without establishing the base concept.
- **Fix:** Add 1-2 sentences to Slide 5 or insert a new slide between 4 and 5: "A decision tree is a flowchart-like model that makes predictions by asking a sequence of yes/no questions about features. Each question splits the data; the final answer is at the leaf."
- **Cross-ref:** Related to HARMONY-2. See also M-2 (mini has same gap).

**ISSUE O-5: Closing comic is text-only, no actual image (Slide 24)**
- Slide 24 uses a text quote adapted from XKCD #1838 but does not include the actual image. The course standard (per CLAUDE.md) is to include the comic image.
- **Fix:** Either include the actual XKCD #1838 image or create a TikZ comic. The mini-lecture already shows how to do TikZ comics effectively.

**ISSUE O-6: Boosting section assumes prior knowledge (Slides 19-20)**
- The boosting slides compare RF vs boosting but never explain what a "weak learner" is or why sequential correction of errors works. A student encountering boosting for the first time needs: "A weak learner is a model barely better than random guessing (e.g., a tree stump with just one split)."
- **Fix:** Add one sentence defining "weak learner" at the start of Slide 20.

#### L04_deepdive.tex -- 4 Issues Found

**ISSUE D-1: No worked example for Gini (Slides 6-7)**
- The deepdive presents Gini properties thoroughly but has no worked example with actual numbers until the appendix (Slide A2). The full lecture (L04_rf_full.tex Frame 5) has an excellent worked example with 800 legit / 200 fraud. The deepdive should mirror this.
- **Fix:** Add a 3-line worked example to Slide 6: "Node: 800 legit, 200 fraud. p_fraud = 0.2. G = 1 - (0.8^2 + 0.2^2) = 1 - 0.68 = 0.32."

**ISSUE D-2: Proof slides lack "why this matters" framing (Slides 13-14)**
- The bagging variance proof is mathematically rigorous but lands without a practical anchor. After Step 4 (the limit), add: "Practical meaning: even with 10,000 trees, if your trees all split on the same dominant feature (rho near 1), the forest gains almost nothing. This is why feature randomization is the breakthrough."
- **Fix:** Add a 2-sentence "so what" after the proof conclusion.

**ISSUE D-3: XGBoost Taylor expansion not scaffolded (Slide 33)**
- The XGBoost slide drops a second-order Taylor expansion with g_i and h_i without explaining WHY we use a Taylor expansion here. Students who haven't seen Taylor expansions in an ML context need: "Instead of minimizing the exact loss (expensive), XGBoost approximates it with a quadratic function using the first derivative (gradient) and second derivative (curvature). This makes finding optimal leaf values a closed-form problem."
- **Fix:** Add 2 sentences of motivation before the formula.

**ISSUE D-4: Appendix slides are excellent but disconnected from main flow**
- The appendix has 10 slides with full proofs (Gini derivation, bagging proof, 63.2% rule, XGBoost derivation, SHAP axioms, etc.). These are high quality. However, the main slides reference concepts without pointing to the appendix.
- **Fix:** Add cross-references in bottomnotes with these explicit mappings:
  - Slide 6 (Gini properties) --> Appendix A2 (Gini derivation)
  - Slide 13 (Bagging variance) --> Appendix A3 (63.2% rule proof)
  - Slide 24 (SHAP) --> Appendix A8 (SHAP axioms)
  - Slide 33 (XGBoost) --> Appendix A6 (XGBoost derivation)

#### L04_rf_mini.tex -- 2 Issues Found

**ISSUE M-1: Gini formula appears only in slide 3 footnote (scriptsize)**
- The taxonomy table slide has the Gini formula at scriptsize at the very bottom. This is easy to miss. For a mini-lecture intended as an accessible entry point, the formula should be more prominent or omitted entirely (the mini uses the "feel" approach, so formulas might not be needed).
- **Fix:** Either remove the formula (the mini is formula-light by design) or move it into an Insight block with a brief example.

**ISSUE M-2: No explicit definition of "decision tree" before use (Slide 1)**
- Slide 1 references "A single decision tree overfits" but never defines what a decision tree is. The TikZ comic shows a single tree figure vs. crowd but doesn't explain the tree concept itself.
- **Fix:** Add one sentence in the first compactlist: "A decision tree makes predictions by asking yes/no questions about features (e.g., Is transaction amount > $500? Is location foreign?)."
- **Cross-ref:** Related to HARMONY-2. Same gap as O-4 (overview).

#### L04_rf_full.tex -- 3 Issues Found

**ISSUE F-1: Excellent worked examples -- best of the 4 files**
- Frame 5 has a thorough worked Gini example (800 legit, 200 fraud). Frame 12 has a numerical variance table. Frame 25 has a worked feature importance case study. This file is the accessibility GOLD STANDARD among the four.
- **Action:** Use L04_rf_full.tex as the reference for what "accessible" looks like. Port its worked examples to overview and deepdive where missing.

**ISSUE F-2: AdaBoost weight update uses different notation than deepdive (Frame 20)**
- Full lecture uses: w_i <- w_i * exp(alpha_t * 1[misclassified_i])
- Deepdive uses: w_i <- w_i * exp(-alpha_t * y_i * h_t(x_i))
- Both are correct (different but equivalent formulations) but students seeing both will be confused.
- **Fix:** Harmonize notation. The deepdive formulation is more standard (matches Freund & Schapire). Update the full lecture to match, or add a note explaining the equivalence.

**ISSUE F-3: No MSE/regression criterion slide (unlike deepdive)**
- The full lecture covers classification trees thoroughly but has no slide on regression trees (MSE criterion). The deepdive has this (Slide 8). Since RF is used for both classification and regression, at least mentioning MSE in a bullet point would help.
- **Fix:** Add a brief mention to Frame 6 or Frame 15: "For regression: the splitting criterion is MSE reduction (variance reduction)."

### 1.3 Cross-File Harmonization Issues

**HARMONY-1: Four files cover the same topic at four different depths with some inconsistencies**
- Overview: 25 slides, formula-light except Gini/Entropy/Variance, chart-heavy
- Deepdive: 52 slides, proof-heavy with appendix, most comprehensive
- Mini: 10 slides, TikZ-comic-driven, discovery-first, highly accessible
- Full: 31 slides, question-driven frames, best worked examples

**HARMONY-2: Decision tree introduction quality varies dramatically**
- Overview: 1 chart-only slide (inadequate) -- addressed by O-1 and O-4
- Deepdive: 6 slides (thorough, good)
- Mini: 1 sentence in passing (inadequate) -- addressed by M-2
- Full: 4 slides (thorough, good with TikZ diagrams)

**HARMONY-3: Boosting coverage overlap**
- Overview: 2 slides (comparison table + brief overview)
- Deepdive: 5 slides (AdaBoost + gradient boosting + XGBoost + LightGBM/CatBoost + finance)
- Mini: 1 cell in taxonomy table
- Full: 4 slides (AdaBoost + gradient boosting + XGBoost)
- Issue: Notation inconsistency only -- addressed by F-2

### 1.4 Three-Zone Architecture Compliance

| File | Zone 1 (Intro, no Greek) | Zone 2 (Core) | Zone 3 (Wrap-up) | Appendix |
|------|--------------------------|---------------|-------------------|----------|
| Overview | Slides 3-7 (good, no formulas) | Slides 8-21 (formulas start at 11, fine) | Slides 23-25 (good) | None |
| Deepdive | Slides 3-4 (LO slide has Bloom terms, no formulas) | Slides 5-42 | -- | Slides A1-A10 (excellent) |
| Mini | Slide 1-2 (good, no formulas) | Slides 3-9 | Slide 10 | None |
| Full | Frames 1-3 (good) | Frames 4-29 | Frames 30-31 | None |

**Assessment:** Overview follows three-zone architecture well. Deepdive has a very short Zone 1 (2 slides after title) before jumping into formulas at Slide 5. Mini and Full have appropriate zones. The deepdive's Zone 1 could be extended with 1-2 more intuition slides before the formulas begin.

---

## PART 2: Quiz Analysis -- Findings and Remediation

### 2.1 Format Consistency Audit

| Quiz | Format | Questions | CSS Theme | JS Engine | KaTeX | Nav Links |
|------|--------|-----------|-----------|-----------|-------|-----------|
| L01_linear_regression.html | 3-column grid | 20 | Consistent | initQuiz + waitForKaTeX | Yes | Dashboard + GitHub |
| L02_logistic_regression.html | 3-column grid | 20 | Consistent | initQuiz + waitForKaTeX | Yes | Dashboard + GitHub |
| L03_knn.html | 3-column grid | 20 | Consistent | initQuiz + waitForKaTeX | Yes | Dashboard + GitHub |
| L03_kmeans.html | 3-column grid | 20 | Consistent | initQuiz + waitForKaTeX | Yes | Dashboard + GitHub |
| L03_knn_kmeans.html | 3-column grid | 20 | Consistent | initQuiz + waitForKaTeX | Yes | Dashboard + GitHub |
| L03_knn_kmeans_accessible.html | 3-column grid | 20 | Consistent | initQuiz + waitForKaTeX | Yes | Dashboard + GitHub |
| L04_random_forests.html | 3-column grid | 20 | Consistent | initQuiz + waitForKaTeX | Yes | Dashboard + GitHub |
| L05_pca_tsne.html | 3-column grid | 20 | Consistent | initQuiz + waitForKaTeX | Yes | Dashboard + GitHub |
| L06_embeddings_rl.html | 3-column grid | 20 | Consistent | initQuiz + waitForKaTeX | Yes | Dashboard + GitHub |

**Finding FORMAT-1:** All 9 topic quizzes use identical HTML/CSS/JS structure. KaTeX loaded via CDN (0.16.9). Math rendering uses `renderMathInElement` with `$...$` and `$$...$$` delimiters. Format is CONSISTENT across all quizzes.

**Finding FORMAT-2:** XML quizzes (Moodle format) use `<question type="multichoice">` with `shuffleanswers=true` and `penalty=0.3333333`. Consistent across all 3 XML files.

**Finding FORMAT-3:** Legacy quizzes (quiz1_regression.html, quiz2_classification_ensemble.html, quiz3_advanced.html) likely use an older format. These should be checked for format consistency but are lower priority since the L0X_ quizzes are the current standard.

### 2.2 L04 Quiz Deep Analysis (L04_random_forests.html)

#### Content Accuracy -- All 20 Answers Verified Correct

| Q# | Topic | Answer | Verified |
|----|-------|--------|----------|
| 1 | Gini impurity calculation | A (0.48) | CORRECT: 1-(0.6^2+0.4^2) = 0.48 |
| 2 | Entropy at 50/50 | B (1.0) | CORRECT: -2(0.5*log2(0.5)) = 1.0 |
| 3 | Information gain | B (0.5) | CORRECT: 0.9 - 0.4 = 0.5 |
| 4 | Recursive partitioning | B | CORRECT |
| 5 | NOT a stopping criterion | C (max features) | CORRECT |
| 6 | Bootstrap with replacement | B | CORRECT |
| 7 | OOB percentage | B (37%) | CORRECT: 1/e ~ 0.368 |
| 8 | Bagging purpose | B (reduce variance) | CORRECT |
| 9 | Two sources of randomness | B | CORRECT |
| 10 | Features per split sqrt(100) | D (10) | CORRECT |
| 11 | Majority vote | C | CORRECT |
| 12 | MDI definition | B | CORRECT |
| 13 | Permutation importance | B | CORRECT |
| 14 | OOB as free CV | D (all above) | CORRECT |
| 15 | Bias-variance tradeoff | B | CORRECT |
| 16 | n_estimators range | B (100-500) | CORRECT |
| 17 | Decreasing max_features | B | CORRECT |
| 18 | RF advantage | C | CORRECT |
| 19 | RF limitation | B | CORRECT |
| 20 | RF vs logistic in fraud | B | CORRECT |

#### Bloom's Taxonomy Analysis -- CRITICAL ISSUE

| Q# | Bloom's Level | Classification |
|----|---------------|----------------|
| 1 | 2 (Understand) -- apply a formula | Calculate |
| 2 | 2 (Understand) -- apply a formula | Calculate |
| 3 | 2 (Understand) -- apply a formula | Calculate |
| 4 | 1 (Remember) -- definition recall | Recall |
| 5 | 1 (Remember) -- identify exception | Recall |
| 6 | 1 (Remember) -- definition recall | Recall |
| 7 | 1 (Remember) -- numeric fact recall | Recall |
| 8 | 1 (Remember) -- definition recall | Recall |
| 9 | 1 (Remember) -- definition recall | Recall |
| 10 | 2 (Understand) -- apply a rule | Calculate |
| 11 | 1 (Remember) -- definition recall | Recall |
| 12 | 1 (Remember) -- definition recall | Recall |
| 13 | 1 (Remember) -- definition recall | Recall |
| 14 | 1 (Remember) -- definition recall | Recall |
| 15 | 2 (Understand) -- describe mechanism | Understand |
| 16 | 1 (Remember) -- numeric range recall | Recall |
| 17 | 2 (Understand) -- describe effect | Understand |
| 18 | 2 (Understand) -- identify advantage | Understand |
| 19 | 2 (Understand) -- identify limitation | Understand |
| 20 | 2 (Understand) -- compare approaches | Understand |

**Distribution: 9 questions at Level 1 (Remember), 11 at Level 2 (Understand). ZERO at Level 3-5.**

**CRITICAL MISMATCH:** The L04 LOs are at Bloom 4-5 (Analyze, Evaluate, Compare, Critique). The quiz tests NONE of these. Students can score 100% by memorizing definitions without any analytical thinking.

#### Topic Coverage Analysis

| Slide Topic | Questions Covering It | Gap? |
|-------------|----------------------|------|
| Decision tree structure | Q4, Q5 | No |
| Gini impurity | Q1 | Low coverage (1 calc question) |
| Entropy / information gain | Q2, Q3 | Adequate for calculation |
| Bootstrap / bagging | Q6, Q7, Q8 | Adequate |
| Feature randomization | Q9, Q10 | Adequate |
| Ensemble voting | Q11 | Low coverage |
| Feature importance (MDI) | Q12 | Low coverage |
| Permutation importance | Q13 | Low coverage |
| SHAP values | -- | **GAP: NO coverage** |
| OOB error | Q7, Q14 | Adequate |
| Bias-variance | Q15 | Low coverage |
| Hyperparameters | Q16, Q17 | Adequate |
| Boosting (AdaBoost, GB, XGBoost) | -- | **GAP: NO coverage** |
| Class imbalance / fraud detection | Q20 | Low coverage |
| Regulatory compliance / ECOA/GDPR | -- | **GAP: NO coverage** |
| SMOTE / resampling | -- | **GAP: NO coverage** |
| Cost-sensitive learning | -- | **GAP: NO coverage** |
| RF advantages/limitations | Q18, Q19 | Adequate |

**Major gaps:** SHAP values, boosting algorithms, regulatory compliance, SMOTE/resampling, cost-sensitive learning are all covered extensively in slides but have ZERO quiz questions.

#### Distractor Quality Assessment

| Q# | Distractor Quality | Issue |
|----|-------------------|-------|
| 1-3 | Good | Numeric distractors are plausible |
| 4 | Adequate | Options cover different concepts |
| 5 | Good | Tricky -- max_features is an RF param, not a stopping criterion |
| 6 | Adequate | Standard multiple-choice |
| 7-8 | Adequate | Common misconception distractors |
| 9-14 | Adequate | Definition-based, distractors are other concepts |
| 15-17 | Good | Require understanding of mechanism |
| 18-20 | Adequate | Compare/contrast distractors |

Overall distractor quality: ADEQUATE but not challenging. No "gotcha" distractors that test deep understanding.

### 2.3 Cross-Quiz Consistency Analysis (All L0X Quizzes)

**Bloom's Level Distribution Across All Quizzes:**

| Quiz | Level 1 (Remember) | Level 2 (Understand) | Level 3+ (Apply/Analyze) | Finance Application |
|------|--------------------|--------------------|------------------------|---------------------|
| L01 | ~8 | ~10 | ~2 | Yes (beta interpretation) |
| L02 | ~6 | ~10 | ~4 | Moderate (odds ratio) |
| L03 KNN | ~8 | ~10 | ~2 | Minimal |
| L03 K-Means | ~8 | ~10 | ~2 | Minimal |
| L04 | 9 | 11 | **0** | 1 question (Q20) |
| L05 | ~7 | ~10 | ~3 | Minimal |
| L06 | ~7 | ~10 | ~3 | Minimal |

**Finding BLOOM-1:** L04 has the WORST Bloom's alignment of any quiz -- zero questions above Level 2 while having the highest-level LOs (Bloom 4-5).

**Finding BLOOM-2:** All quizzes skew heavily toward Level 1-2. None have substantial Level 3+ coverage. This is a SYSTEMIC issue, not just L04-specific.

**Finding FINANCE-1:** Finance application coverage is thin across all quizzes. L01 and L02 have some financial interpretation questions. L03-L06 rarely test finance domain knowledge.

### 2.4 Moodle XML Quiz Analysis (quiz2_topics_3_4.xml -- L04-relevant questions)

**L04 questions in quiz2_topics_3_4.xml (Q9-Q15):**
- Q9: Bagging definition -- Level 1 (recall)
- Q10: Feature randomization purpose -- Level 2 (understand)
- Q11: OOB error definition -- Level 1 (recall)
- Q12: Feature importance method -- Level 1 (recall)
- Q13: Gini = 0 meaning -- Level 1 (recall)
- Q14: RF vs single tree -- Level 2 (understand)
- Q15: max_features hyperparameter -- Level 1 (recall)

**Finding XML-1:** Moodle XML questions are also all Level 1-2. Consistent with HTML quiz but equally deficient in higher-order thinking.

**Finding XML-2:** XML quiz has 7 L04 questions (out of 16 total). This is reasonable coverage for a combined L03+L04 quiz.

**Finding XML-3:** Content accuracy is correct in all XML questions examined. Explanations in feedback tags are clear.

### 2.5 Legacy Quiz Assessment

Legacy quizzes (quiz1_regression.html, quiz2_classification_ensemble.html, quiz3_advanced.html) should be deprecated in favor of the L0X_ topic quizzes. They likely use an older format and may have overlapping content. Lower priority for remediation.

---

## Work Objectives

### Core Objective
Fix L04 accessibility gaps, elevate the L04 quiz to match the Bloom's level of its LOs, and produce a comprehensive Bloom audit report for ALL 9 HTML quizzes.

### Deliverables

1. **L04 slide fixes** -- concrete edits to all 4 .tex files addressing 15 identified issues
2. **L04 quiz upgrade** -- replace 8 low-value questions with Bloom Level 3-5 questions covering missing topics (SHAP, boosting, regulatory, SMOTE, class imbalance, bias-variance)
3. **All-quiz Bloom audit report** -- per-question Bloom classification for all 9 HTML quizzes (180 questions), aggregate distribution tables, topic gap identification, and brief recommendations (audit only, NO remediation of non-L04 quizzes)

### Definition of Done
- All 15 L04 slide issues resolved
- L04 quiz has at least 6 questions at Bloom Level 3+ (Apply/Analyze/Evaluate)
- L04 quiz covers SHAP, boosting, regulatory compliance, SMOTE, class imbalance, and bias-variance analysis
- All quiz answers verified correct and answerable from L04 slide content
- JSON format preserved (no structural changes to HTML/CSS/JS)
- LaTeX compiles with 0 errors, 0 Overfull warnings
- Bloom audit report covers all 9 HTML quizzes with per-question classification

---

## Must Have / Must NOT Have

### Must Have
- Worked examples with concrete numbers for Gini, Entropy, and variance formula (overview + deepdive)
- Decision tree definition BEFORE first use in overview and mini
- At least 6 Bloom Level 3+ questions in L04 quiz
- SHAP, boosting, regulatory, SMOTE, class imbalance, and bias-variance quiz coverage
- ALL quiz questions answerable from L04 slide content (no external knowledge required)
- Notation consistency across all 4 .tex files
- Cross-references from main slides to appendix (deepdive) with explicit A2/A3/A6/A8 mappings
- Q4 (recursive partitioning) RETAINED -- it is the only DT fundamentals question
- Per-question Bloom classification for all 180 questions across 9 HTML quizzes
- All existing correct answers preserved (keep JSON)

### Must NOT Have
- Changes to HTML/CSS/JS quiz engine code
- Changes to quiz question count (keep 20 questions per quiz)
- Removal of existing correct content from slides
- New chart.py files (use existing 8 charts; chart accuracy verified in prior hostile review)
- Changes to preamble/footer/color definitions
- Changes to other lectures' .tex files (Part 1 is L04-only)
- Changes to non-L04 quiz question content (Phase 3 is audit-report-only)
- Quiz questions requiring knowledge not taught in L04 slides (e.g., Bayes' theorem, confusion matrix math)

---

## Task Flow

**NOTE:** Consult the cross-file content map in Section 1.1 when implementing all fixes.

### Phase 1: L04 Slide Accessibility Fixes (4 .tex files)

**Task 1.1: L04_overview.tex fixes (6 issues)**

| Sub-task | Issue | Action | Acceptance Criteria |
|----------|-------|--------|---------------------|
| 1.1.1 | O-4: No DT definition | Add 2-sentence DT definition to Slide 5 or new slide between 4-5 | "Decision tree" defined in plain language before first use |
| 1.1.2 | O-1: Chart-only Slide 8 | Add 3-4 bullets explaining tree structure alongside chart | Text explains nodes, branches, leaves, paths |
| 1.1.3 | O-2: No worked example for Gini/Entropy | Add 1-line worked Gini example to Slide 13 | Concrete numbers (e.g., 70/30 split => G = 0.42) |
| 1.1.4 | O-3: Variance formula incomplete bridge | ADD a 2-sentence interpretation BEFORE the existing "Key insight" at line 265. Do NOT replace the existing text. Add: "In plain language: the ensemble variance has two parts -- a floor set by how correlated the trees are (rho), and a shrinking part that vanishes as B grows." | New bridge sentence present AND existing line 265 "Key insight" preserved |
| 1.1.5 | O-6: Weak learner undefined | Add 1 sentence defining "weak learner" to Slide 20 | Definition present before first use |
| 1.1.6 | O-5: No closing comic image | Add XKCD #1838 image or TikZ comic to Slide 24 | Visual comic present on closing slide |

**Task 1.2: L04_deepdive.tex fixes (4 issues)**

| Sub-task | Issue | Action | Acceptance Criteria |
|----------|-------|--------|---------------------|
| 1.2.1 | D-1: No worked Gini example | Add 3-line worked example to Slide 6 (matching full lecture Frame 5) | Numbers: 800 legit, 200 fraud, G = 0.32 |
| 1.2.2 | D-2: Proof lacks "so what" | Add 2-sentence practical meaning after Slide 14 conclusion | "Practical meaning: even with 10,000 trees..." |
| 1.2.3 | D-3: XGBoost not scaffolded | Add 2-sentence motivation before Taylor expansion on Slide 33 | "Instead of minimizing exact loss..." explanation |
| 1.2.4 | D-4: No appendix cross-refs | Add bottomnote cross-references with these EXPLICIT mappings: (1) Slide 6 --> "Full derivation in Appendix A2 (Gini derivation)"; (2) Slide 13 --> "Full proof in Appendix A3 (Bagging variance reduction)"; (3) Slide 24 --> "Formal axioms in Appendix A8 (SHAP axioms)"; (4) Slide 33 --> "Full derivation in Appendix A6 (XGBoost objective)" | All 4 cross-references added with correct appendix slide numbers |

**Task 1.3: L04_rf_mini.tex fixes (2 issues)**

| Sub-task | Issue | Action | Acceptance Criteria |
|----------|-------|--------|---------------------|
| 1.3.1 | M-2: No DT definition | Add 1 sentence to Slide 1 compactlist defining DT | Decision tree defined before "overfits" claim |
| 1.3.2 | M-1: Gini in scriptsize footnote | Either remove formula or move to Insight block | Formula is either prominent or absent (not hidden) |

**Task 1.4: L04_rf_full.tex fixes (2 issues)**

| Sub-task | Issue | Action | Acceptance Criteria |
|----------|-------|--------|---------------------|
| 1.4.1 | F-2: AdaBoost notation mismatch | Harmonize to match deepdive notation (standard Freund & Schapire) | Frame 20 uses same notation as deepdive Slide 31 |
| 1.4.2 | F-3: No regression tree mention | Add 1 sentence about MSE criterion for regression | Regression use case mentioned |

**Task 1.5: Compile and verify all 4 .tex files**

| Sub-task | Action | Acceptance Criteria |
|----------|--------|---------------------|
| 1.5.1 | pdflatex each file, check for errors and Overfull | 0 errors, 0 Overfull warnings for all 4 files |

### Phase 2: L04 Quiz Upgrade

**Task 2.1: Replace 8 low-value L04 quiz questions with higher-order questions**

Replace Q5, Q6, Q7, Q8, Q11, Q14, Q16, Q19 with new questions. **KEEP Q4 (recursive partitioning)** -- it is the only question covering DT fundamentals.

**Rationale for dropping Q8 instead of Q4:** Q8 ("Bagging purpose = reduce variance") is redundant with Q15 (bias-variance tradeoff) and Q17 (max_features effect on variance). Q4 is the sole DT fundamentals question and removing it would leave zero coverage of decision tree structure.

**CONSTRAINT: All new questions MUST be answerable solely from L04 slide content.** No external knowledge (e.g., Bayes' theorem, confusion matrix algebra) may be required.

| New Q# | Topic | Bloom Level | Question Type | Slide Source |
|--------|-------|-------------|---------------|--------------|
| Q5-new | Boosting vs RF | 4 (Analyze) | "A model has low training error but high test error. Is this more likely RF or boosting? Diagnose the issue." | Overview slides 19-20, deepdive slides 30-34, full frames 19-22 |
| Q6-new | Class imbalance strategy | 3 (Apply) | "Your fraud dataset has 0.1% positive rate. The model achieves 99.9% accuracy by predicting all-negative. Which strategy should you apply: class_weight='balanced', SMOTE, or threshold tuning? Justify." | Overview slides 17-18, deepdive slides 35-36, full frames 25-26 |
| Q7-new | Regulatory compliance | 5 (Evaluate) | "A bank uses RF for credit scoring. Which explanation method satisfies ECOA adverse action requirements and why?" | Deepdive slide 24, mini slide 8, full frame 29 |
| Q8-new | SHAP interpretation | 4 (Analyze) | "Given SHAP values for a denied loan application, which feature contributed most to denial? What does a negative SHAP value mean in this context?" | Overview slide 16, deepdive slide 24, full frame 18 |
| Q11-new | Feature importance comparison | 4 (Analyze) | "MDI ranks feature X highest but permutation importance ranks it low. What does this indicate about feature X?" | Overview slide 16, deepdive slides 20-22, full frames 16-17 |
| Q14-new | SMOTE application | 3 (Apply) | "When should you apply SMOTE -- before or after train-test split? Why?" | Overview slides 17-18, deepdive slides 35-36, full frames 25-26 |
| Q16-new | Variance formula analysis | 4 (Analyze) | "Given $\rho = 0.9$ and $B = 500$ trees, the ensemble variance is still high. Diagnose the problem and recommend a fix based on the variance formula." | Overview slide 11, deepdive slides 13-14, full frame 12 |
| Q19-new | Bias-variance tradeoff diagnosis | 5 (Evaluate) | "An RF model with max_depth=None and 50 trees shows low bias but high variance on test data. Which hyperparameter changes would most effectively address this? Evaluate the tradeoffs." | Deepdive slides 17-19, 25, full frame 24 |

**New Bloom distribution after replacement:**
- Level 1 (Remember): 4 questions (Q4, Q9, Q12, Q13)
- Level 2 (Understand): 8 questions (Q1, Q2, Q3, Q10, Q15, Q17, Q18, Q20)
- Level 3 (Apply): 2 questions (Q6-new, Q14-new)
- Level 4 (Analyze): 4 questions (Q5-new, Q8-new, Q11-new, Q16-new)
- Level 5 (Evaluate): 2 questions (Q7-new, Q19-new)
- **Total Level 3+: 8 questions (target was >= 6)**

**Task 2.2: Verify all 20 questions (12 existing + 8 new) have correct answers**
- Each new question's answer must be derivable from the slide source listed above.

**Task 2.3: Verify KaTeX rendering for all new questions with math**

### Phase 3: All-Quiz Bloom Audit Report (audit only, NO changes to non-L04 quizzes)

**Scope:** Per-question Bloom classification for all 9 HTML quizzes (180 questions total). NO remediation execution -- report only with recommendations for future work.

**Bloom Classification Criteria (use consistently across all quizzes):**

| Level | Label | Signal Words | Example |
|-------|-------|-------------|---------|
| 1 | Remember | "What is...", "Which of...", "Name...", "Define..." | Definition recall, fact identification |
| 2 | Understand | "Why does...", "How does...", "Explain...", "Describe..." | Describe mechanism, paraphrase concept |
| 3 | Apply | "Calculate...", "Given data, determine...", "Apply X to scenario Y" | Use formula in new context, apply rule to case |
| 4 | Analyze | "Compare...", "What does this indicate...", "Diagnose from evidence" | Distinguish causes, interpret conflicting signals |
| 5 | Evaluate | "Which approach is best for...", "Critique...", "Judge with justification" | Defend a choice, assess tradeoffs |

**Task 3.1: L01 Linear Regression quiz (20 questions)**
- Read `docs/quiz/L01_linear_regression.html`
- Classify each question by Bloom level using criteria above
- Record topic, Bloom level, finance application (Y/N)

**Task 3.2: L02 Logistic Regression quiz (20 questions)**
- Read `docs/quiz/L02_logistic_regression.html`
- Same classification protocol

**Task 3.3: L03 KNN quiz (20 questions)**
- Read `docs/quiz/L03_knn.html`
- Same classification protocol

**Task 3.4: L03 K-Means quiz (20 questions)**
- Read `docs/quiz/L03_kmeans.html`
- Same classification protocol

**Task 3.5: L03 KNN+K-Means combined quiz (20 questions)**
- Read `docs/quiz/L03_knn_kmeans.html`
- Same classification protocol

**Task 3.6: L03 KNN+K-Means accessible quiz (20 questions)**
- Read `docs/quiz/L03_knn_kmeans_accessible.html`
- Same classification protocol

**Task 3.7: L05 PCA & t-SNE quiz (20 questions)**
- Read `docs/quiz/L05_pca_tsne.html`
- Same classification protocol

**Task 3.8: L06 Embeddings & RL quiz (20 questions)**
- Read `docs/quiz/L06_embeddings_rl.html`
- Same classification protocol

**Task 3.9: Compile aggregate report**
- Aggregate distribution table (all 9 quizzes x 5 Bloom levels)
- Topic gap identification per quiz
- Finance application coverage per quiz
- Brief recommendations list for future upgrades (no execution)
- Save to `.omc/reports/quiz-bloom-audit.md`

**NOTE:** L04 quiz is already classified in Section 2.2 of this plan. Task 3.9 should incorporate that existing analysis.

### Phase 4: Verification

**Task 4.1: LaTeX compilation verification**
- Compile all 4 L04 .tex files
- Verify 0 errors, 0 Overfull

**Task 4.2: Quiz verification**
- Open L04 quiz HTML in browser (or validate JSON structure)
- Verify all 20 questions render correctly
- Verify KaTeX math renders

---

## Commit Strategy

| Commit | Contents |
|--------|----------|
| 1 | L04 overview + deepdive + mini + full slide accessibility fixes |
| 2 | L04 quiz upgrade (8 new higher-order questions) |
| 3 | All-quiz Bloom audit report (.omc/reports/quiz-bloom-audit.md) |

---

## Success Criteria

1. **Accessibility:** A student with zero decision tree background can follow L04_overview.tex from slide 1 to 25 without encountering undefined concepts
2. **Worked examples:** Every formula slide in overview and deepdive has at least one concrete worked example
3. **Bloom alignment:** L04 quiz has at least 6 questions at Bloom Level 3+ matching the Bloom 4-5 LOs (target: 8)
4. **Topic coverage:** L04 quiz covers SHAP, boosting, regulatory, SMOTE, class imbalance, bias-variance (6 major gaps filled)
5. **Slide content constraint:** Every quiz question is answerable from L04 slide content alone
6. **DT fundamentals preserved:** Q4 (recursive partitioning) retained for decision tree coverage
7. **Format preserved:** Quiz HTML/CSS/JS unchanged; only JSON question data modified
8. **Compilation clean:** All 4 .tex files compile with 0 errors, 0 Overfull
9. **Notation consistent:** AdaBoost formula uses same notation across all 4 files
10. **Appendix cross-refs:** 4 explicit mappings (Slide 6->A2, 13->A3, 24->A8, 33->A6) present in deepdive
11. **Bloom audit complete:** All 180 questions across 9 HTML quizzes classified with aggregate report

---

## Risk Identification

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Slide edits cause Overfull warnings | Medium | Medium | Check after every edit; keep bullets to 3-4 per slide |
| New quiz questions have incorrect answers | Low | High | Double-check all math; verify answers against specific slide sources listed in Task 2.1 |
| New quiz questions require knowledge not in slides | Medium | High | Each question in Task 2.1 has an explicit "Slide Source" column; verify against it |
| KaTeX fails to render complex formulas | Low | Medium | Test LaTeX syntax in KaTeX playground first |
| Adding text to chart-only slides causes overflow | Medium | Medium | Use 0.55\textwidth for chart when adding text column |
| Replacing 8 questions changes quiz difficulty balance | Medium | Low | New mix: 2 Apply + 4 Analyze + 2 Evaluate provides graduated difficulty |
| Phase 3 audit takes excessive time | Low | Medium | Scoped to classification + tables only, no remediation execution |
