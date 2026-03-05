# Ultra Hostile Review Plan: L04 Decision Trees & Random Forests

## Task
Conduct an ultra hostile review of all L04 slide content through the lens of a true beginner (zero ML background). Evaluate both pedagogical effectiveness and content accuracy equally, with a full visual audit of all 13 chart.py scripts and cartoon placements.

## Scope
6 files under review:
1. `L04_overview.tex` (25 slides) - Main overview with PMSP framework
2. `L04_deepdive.tex` (42 main + 10 appendix = 52 slides) - Deep dive with proofs
3. `L04_dt_full.tex` (25 slides) - Full decision trees prerequisite lecture
4. `L04_dt_mini.tex` (10 slides) - Mini decision trees prerequisite
5. `L04_rf_full.tex` (31 slides) - Full random forests prerequisite lecture
6. `L04_rf_mini.tex` (10 slides) - Mini random forests prerequisite

Total: ~153 slides, 13 chart folders, 2 XKCD images

## Scoring Methodology

**Consistent scoring:** Each file is scored out of 100 points with the following fixed weight distribution. The per-file scores are then averaged (equal weight per file) to produce the overall L04 score.

| Criterion | Points | Category |
|---|---|---|
| A1: True Beginner Accessibility | 12 | Pedagogy |
| A2: Narrative Arc & Motivation | 8 | Pedagogy |
| A3: Worked Examples | 8 | Pedagogy |
| A4: Active Learning & Engagement | 8 | Pedagogy |
| A5: LOs & Assessment Alignment | 4 | Pedagogy |
| A6: File Differentiation & Standalone | 5 | Pedagogy |
| A7: Content Overlap (intentional vs accidental) | 5 | Pedagogy |
| B1: Mathematical Correctness | 15 | Accuracy |
| B2: Conceptual Accuracy | 10 | Accuracy |
| B3: Reference Accuracy | 5 | Accuracy |
| B4: Chart Accuracy (per chart-type) | 10 | Accuracy |
| B5: Visual Density & Cartoon Compliance | 5 | Accuracy |
| B6: LaTeX Compilation (zero Overfull) | 5 | Accuracy |
| **Total** | **100** | |

**PASS/FAIL thresholds:**
- PASS: Overall score >= 75 AND zero CRITICAL issues remaining
- CONDITIONAL PASS: Overall score >= 65 AND zero CRITICAL math errors
- FAIL: Overall score < 65 OR any CRITICAL mathematical error

**Severity definitions:**
- CRITICAL: Mathematical error, factual falsehood, or missing closing comic (HARD RULE violation). ONE critical issue = automatic review of that file.
- MAJOR: Significant pedagogical gap (e.g., formula with no worked example, jargon undefined for beginners). >5 major issues in one file = score cap at 70.
- MINOR: Style, formatting, or mild clarity issues. Informational only.

## Review Criteria (Detailed)

### A. Pedagogical Effectiveness (50 points)

#### A1. True Beginner Accessibility (12 pts)
For each file, evaluate:
- Can a student with ZERO ML background follow from slide 1?
- Are concepts introduced before they're used? (no forward references)
- Is every piece of jargon defined on first use?
- Are there enough "plain English" explanations before formulas?
- Does the intro zone truly contain ZERO Greek letters/formulas?
- Is every file STANDALONE for its intended audience? (mini = zero-prerequisite; full = assumes prior lectures L01-L03; overview/deepdive = assumes DT understanding)

#### A2. Narrative Arc & Motivation (8 pts)
- Is there a compelling "why should I care?" before any technical content?
- Does each lecture tell a story (problem -> method -> solution -> practice)?
- Are bridges between topics explicit? (DT -> RF -> Boosting)
- Does complexity ramp gradually or jump abruptly?

#### A3. Worked Examples & Concrete Illustrations (8 pts)
- Does every formula have a worked numerical example within 1-2 slides?
- Are examples relatable (loan approval, fraud detection, not abstract)?
- Are the numerical values in worked examples arithmetically correct?
- Are there enough "intuition before formula" moments?
- Are worked example numbers CONSISTENT across files that cover the same concept? (e.g., same Gini example should use same numbers, OR different numbers should be clearly intentional pedagogical variety)

#### A4. Active Learning & Engagement (8 pts)
- Are there reflection prompts, exercises, or "pause and think" moments?
- Do the mini-lectures use the WHY-FEEL-WHAT-CASE-HOW-RISK-WHERE-IMPACT-SOWHAT-ACT framework?
- Are exercises scaffolded (easy -> medium -> hard)?
- Is there a hand-calculable exercise (not just "run this code")?

#### A5. Learning Objectives & Assessment Alignment (4 pts)
- Are LOs at Bloom's 4-5 (Analyze, Evaluate, Create)?
- Do the exercises actually test the stated LOs?
- Is every LO addressed somewhere in the slides?

#### A6. File Differentiation & Standalone Completeness (5 pts)
- Mini-lectures (10 slides) must be genuinely simpler than full lectures (25+ slides)
- Each mini-lecture must be STANDALONE: a student watching ONLY the mini should get a complete, self-contained understanding of the topic
- Full lectures must add genuine depth vs. just being longer
- Overview/deepdive must have clear scope separation (overview = breadth, deepdive = depth)
- No file should assume knowledge only presented in a different L04 file without explicit cross-reference

#### A7. Content Overlap Audit (5 pts)
- Quantify: how many concepts appear in >1 file? Is duplication intentional (pedagogical reinforcement) or accidental (copy-paste)?
- The variance formula, Gini formula, and OOB rule appear in 4+ files each. For each duplicated concept, is the presentation ADAPTED to the file's audience level, or is it identical text?
- Different worked example numbers for the same formula across files: document and assess whether this is good variety or confusing inconsistency

### B. Content Accuracy (50 points)

#### B1. Mathematical Correctness (15 pts)
- Are ALL formulas correct? (Gini, Entropy, IG, Variance reduction, MSE, SHAP, AdaBoost, XGBoost)
- Are worked example calculations arithmetically correct?
- Are edge cases handled? (e.g., 0*log(0) = 0 convention)
- Are the variance reduction derivation steps correct?
- Verify: AdaBoost weight update formula signs and normalization
- Verify: XGBoost Taylor expansion and optimal leaf weight formula

#### B2. Conceptual Accuracy (10 pts)
- Is the bias-variance tradeoff correctly described?
- Is the relationship between bagging, RF, and boosting correct?
- Are the differences between Gini and Entropy correctly stated?
- Is the OOB 63.2% rule correctly derived?
- Are SHAP axioms correctly stated?

#### B3. Reference Accuracy (5 pts)
- Are paper citations correct? (Breiman 2001, Friedman 2001, Chen & Guestrin 2016, etc.)
- Are the default hyperparameter values correct for scikit-learn (current version)?
- Are regulatory references accurate? (ECOA, GDPR, EU AI Act)
- Are XKCD comic numbers and titles correct?

#### B4. Chart Accuracy (10 pts)

**Chart-Type Taxonomy** (apply different criteria per type):

| Type | Charts | Audit Focus |
|---|---|---|
| **Trained-model charts** (must use real sklearn) | 06a, 06b, 09, 10 | Verify sklearn call, check model params, verify the chart shows what the slide claims |
| **Diagram/illustration charts** (no sklearn needed) | 01, 03, 05, 07, 08 | Verify labels, colors, readability, pedagogical accuracy of the diagram |
| **Mathematical visualization charts** (computed quantities) | 02, 04, 11, 12 | Verify mathematical correctness, check axis labels, verify data source is appropriate |

For ALL chart types:
- figsize=(10,6), dpi=150, font.size=14?
- ML color palette (MLPurple, MLBlue, MLOrange, etc.)?
- Output to chart.pdf in same directory?
- Does the chart actually demonstrate what the slide text claims?
- Are axis labels correct, readable at Beamer scale?

For synthetic-data charts (like 12_nonlinear_classes):
- If axis labels imply real-world data (e.g., "Income"), but data is `rng.randn`, flag as misleading labeling
- Acceptable if clearly labeled as illustrative/synthetic

#### B5. Visual Density & Cartoon Compliance (5 pts)

**Closing comic definition (HARD RULE):** A closing comic must be either:
- An actual XKCD/comic IMAGE (includegraphics), OR
- A TikZ-drawn comic with visual characters and humor

A text-only quote referencing a comic does NOT satisfy this rule.

Per-file checks:
- Opening comic/cartoon present? (HARD RULE)
- Closing comic/cartoon present? (HARD RULE - image or TikZ, not text-only quote)
- Visual density: ~1 chart or visual per 4 slides?
- XKCD images attributed correctly (CC BY-NC 2.5)?
- TikZ comics well-designed and relevant?
- Chart-only slides: 0.65\textwidth; chart+text slides: 0.55\textwidth?

**Known issues to verify:**
- L04_deepdive.tex closing: uses text-only quote, no actual image -> CRITICAL if confirmed
- L04_rf_mini.tex: does it have a closing comic? -> CRITICAL if missing

#### B6. LaTeX Compilation (5 pts)
- Compile ALL 6 .tex files with `pdflatex -interaction=nonstopmode`
- Grep output for "Overfull" warnings
- ZERO Overfull warnings required (CLAUDE.md HARD RULE)
- Score: 5/5 if zero Overfull, 3/5 if 1-3, 0/5 if >3

## Chart-Slide Mapping (Verify via \includegraphics in .tex files)

| Chart Folder | Expected .tex Files | Verify \includegraphics call exists |
|---|---|---|
| 01_decision_tree | overview:222, dt_full:309, dt_mini:247, rf_full:336 | Y |
| 02_feature_importance | deepdive:492, rf_full:693 | Y |
| 03_bootstrap | overview:254, deepdive:(none?), rf_full:415 | Y |
| 04_oob_error | deepdive:635, rf_full:447 | Y |
| 05_ensemble_voting | overview:353, rf_full:591, rf_mini:426 | Y |
| 06a_single_tree_variance | deepdive:618, rf_full:615 | Y |
| 06b_random_forest_variance | deepdive:626, rf_full:617 | Y |
| 07_decision_flowchart | overview:456, rf_full:1234 | Y |
| 08_gini_split | dt_full:374, dt_mini:276 | Y |
| 09_dt_overfitting | dt_full:670 | Y |
| 10_dt_decision_boundary | dt_full:469 | Y |
| 11_gini_vs_entropy | dt_full:404 | Y |
| 12_nonlinear_classes | dt_full:283 | Y |

**IMPORTANT:** During review, VERIFY these line numbers by actually checking the \includegraphics calls. The line numbers above are approximate.

## Review Process

### Step 0: LaTeX Compilation Check (MANDATORY)
- Compile all 6 .tex files
- Grep for "Overfull" warnings
- Record results per file
- Any file with Overfull = immediate deduction under B6

### Step 1: Per-File Hostile Review
For each of the 6 .tex files, produce:
- A slide-by-slide assessment with specific issues (file:line references)
- Score per criterion (A1-A7, B1-B6) with justification
- Specific remediation actions (not vague "improve this" suggestions)
- Priority: review overview and deepdive first (highest-value files), then full lectures, then mini lectures

**Execution note:** Review files in 2 passes to manage depth:
- Pass 1: L04_overview.tex + L04_deepdive.tex (the main lecture pair, ~77 slides)
- Pass 2: L04_dt_full.tex + L04_dt_mini.tex + L04_rf_full.tex + L04_rf_mini.tex (~76 slides)

### Step 2: Chart.py Audit
For each of the 13 chart.py files:
- Read the Python source code
- Apply the chart-type taxonomy (trained-model / diagram / mathematical)
- Verify dimensions, fonts, colors, output path
- Flag any chart-slide mismatch (chart doesn't show what the slide claims)

### Step 3: Cross-File Consistency & Overlap Audit
- Quantify content overlap per concept (which files, which lines)
- Assess whether overlap is pedagogically intentional or accidental
- Verify file differentiation (mini < full < overview/deepdive)
- Check standalone completeness of each mini-lecture

### Step 4: Scoring & Verdict
- Score each file on all criteria (A1-A7, B1-B6)
- Compute overall L04 score (average of 6 file scores)
- Categorize all issues by severity (CRITICAL/MAJOR/MINOR)
- Render final PASS/FAIL/CONDITIONAL PASS verdict
- Produce prioritized remediation plan (CRITICAL first, then MAJOR)

## Report Structure
Output to: `.omc/reports/l04-hostile-review.md`

```
# L04 Hostile Review Report

## Executive Summary
- Overall score: X/100
- Verdict: PASS/FAIL/CONDITIONAL PASS
- Critical issues: N
- Major issues: N
- Minor issues: N

## Per-File Scores
| File | A1 | A2 | A3 | A4 | A5 | A6 | A7 | B1 | B2 | B3 | B4 | B5 | B6 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| overview | | | | | | | | | | | | | | |
| deepdive | | | | | | | | | | | | | | |
| dt_full | | | | | | | | | | | | | | |
| dt_mini | | | | | | | | | | | | | | |
| rf_full | | | | | | | | | | | | | | |
| rf_mini | | | | | | | | | | | | | | |

## Critical Issues (Must-Fix)
1. [CRITICAL] file:line - description - fix

## Major Issues
1. [MAJOR] file:line - description - fix

## Minor Issues
1. [MINOR] file:line - description - fix

## Chart Audit Results
| Chart | Type | Correct? | Issues |
|---|---|---|---|

## Content Overlap Analysis
| Concept | Files | Assessment |
|---|---|---|

## Remediation Plan (Prioritized)
1. Fix all CRITICAL issues
2. Fix all MAJOR issues
3. Address MINOR issues (optional)
```

## Execution Plan
1. **Conductor** compiles all 6 .tex files and records Overfull warnings (Step 0)
2. **Architect agent** (opus) conducts hostile review of all 6 .tex files in 2 passes (Step 1)
3. **Conductor** audits all 13 chart.py files directly (Step 2) -- these are short Python scripts, no agent needed
4. **Conductor** compiles findings from Steps 0-3 into the report (Steps 3-4)
5. **Conductor** writes the final report to `.omc/reports/l04-hostile-review.md`

**Note:** The Conductor owns the final report compilation. The Architect agent provides raw findings; the Conductor scores, classifies, and formats.
