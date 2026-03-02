# L01 Linear Regression: Ultra Deep Review Plan

## Executive Summary

This plan provides a comprehensive review of Lesson 1 (Linear Regression) slides and charts. The review covers:
- **Overview deck**: 20 frames (L01_overview.tex)
- **Deep dive deck**: 37 frames (L01_deepdive.tex)
- **Charts**: 8 chart.py files generating PDF visualizations

### Overall Assessment

| Category | Status | Issues Found |
|----------|--------|--------------|
| Template Compliance | GOOD | Minor variations from template |
| Chart Quality | GOOD | Font sizes correct; 1 chart deviates from standard |
| Academic Level | EXCELLENT | MSc appropriate, no prerequisites assumed |
| Slide Purpose | GOOD | Each slide has clear purpose |

### Critical Issues (Must Fix)
1. Decision flowchart (08) uses different font settings than other charts
2. Some chart widths vary inconsistently (0.42-0.55 textwidth)
3. XKCD images lack accessibility alt-text

### Improvements (Should Fix)
1. Standardize all chart widths to documented values (0.55 or 0.65)
2. Add missing GitHub URL watermarks to 7 of 8 charts
3. Add `axes.spines.top/right: False` to charts for cleaner look

---

## Part 1: Template Compliance Analysis

### L01_overview.tex Compliance

| Element | Template Requirement | Actual | Status |
|---------|---------------------|--------|--------|
| Document class | 8pt, aspectratio=169 | 8pt, aspectratio=169 | PASS |
| Theme | Madrid | Madrid | PASS |
| Color theme | default | default | PASS |
| MLPurple | RGB{51,51,178} | RGB{51,51,178} | PASS |
| MLBlue | RGB{0,102,204} | RGB{0,102,204} | PASS |
| MLOrange | RGB{255,127,14} | RGB{255,127,14} | PASS |
| MLGreen | RGB{44,160,44} | RGB{44,160,44} | PASS |
| MLRed | RGB{214,39,40} | RGB{214,39,40} | PASS |
| Footer | 3-part custom | 3-part custom | PASS |
| Navigation symbols | removed | removed | PASS |
| \bottomnote command | defined | defined | PASS |
| \highlight command | defined | defined | PASS |
| \mathbold command | defined | defined | PASS |

**Compliance Score: 100%**

### L01_deepdive.tex Compliance

Same structure as overview - **Compliance Score: 100%**

### Template Deviations

| File:Line | Issue | Severity |
|-----------|-------|----------|
| L01_overview.tex:57 | Date empty (template has "Spring 2026") | LOW |
| L01_deepdive.tex:56 | Date empty (template has "Spring 2026") | LOW |

---

## Part 2: Per-Slide Analysis - L01_overview.tex

### Frame 1: Title Page (Line 62-64)
| Aspect | Value |
|--------|-------|
| Purpose | Course introduction, topic identification |
| Template compliance | PASS - uses \titlepage |
| Chart | None |
| Academic level | N/A |
| Issues | None |

### Frame 2: Learning Objectives (Line 67-80)
| Aspect | Value |
|--------|-------|
| Purpose | Set expectations, outline learning outcomes |
| Template compliance | PASS - uses [t] alignment, \bottomnote |
| Chart | None |
| Academic level | GOOD - clear, actionable verbs (Understand, Apply, Interpret) |
| Issues | None |

### Frame 3: XKCD Linear Regression Humor (Line 83-90)
| Aspect | Value |
|--------|-------|
| Purpose | Lighten mood, introduce concept with humor |
| Template compliance | PASS |
| Chart | External image: images/1725_linear_regression.png |
| Image width | 0.55\textwidth - CORRECT |
| Academic level | GOOD - accessible entry point |
| Issues | XKCD images should have alt-text for accessibility |

### Frame 4: The Business Problem (Line 93-114)
| Aspect | Value |
|--------|-------|
| Purpose | Motivate linear regression with finance use case |
| Template compliance | PASS - uses \bottomnote |
| Chart | None |
| Academic level | EXCELLENT - real-world finance context |
| Issues | None |

### Frame 5: What is Linear Regression? (Line 117-133)
| Aspect | Value |
|--------|-------|
| Purpose | Define core concept and notation |
| Template compliance | PASS |
| Chart | None |
| Academic level | MSc APPROPRIATE - introduces equation with variable definitions |
| Issues | None |

### Frame 6: Simple Linear Regression (Line 136-143)
| Aspect | Value |
|--------|-------|
| Purpose | Visualize simple regression concept |
| Template compliance | PASS |
| Chart | 01_simple_regression/chart.pdf |
| Chart width | 0.50\textwidth - DEVIATION (should be 0.55) |
| Academic level | GOOD - visual supports equation from previous slide |
| Issues | Chart width 0.50 instead of documented 0.55 |

### Frame 7: Multiple Linear Regression (Line 146-153)
| Aspect | Value |
|--------|-------|
| Purpose | Extend to multiple features, show hyperplane |
| Template compliance | PASS |
| Chart | 02_multiple_regression_3d/chart.pdf |
| Chart width | 0.42\textwidth - DEVIATION (3D needs smaller width, acceptable) |
| Academic level | GOOD - natural extension from simple case |
| Issues | Width deviation justified for 3D visualization |

### Frame 8: The Optimization Problem (Line 156-171)
| Aspect | Value |
|--------|-------|
| Purpose | Formalize objective function |
| Template compliance | PASS |
| Chart | None |
| Academic level | MSc APPROPRIATE - matrix notation, formal optimization |
| Issues | None |

### Frame 9: Two Solution Approaches (Line 174-215)
| Aspect | Value |
|--------|-------|
| Purpose | Compare closed-form vs iterative solutions |
| Template compliance | PASS - uses columns, MLGreen/MLRed colors |
| Chart | None |
| Academic level | EXCELLENT - pros/cons comparison, computational considerations |
| Issues | None |

### Frame 10: Gradient Descent in Action (Line 218-225)
| Aspect | Value |
|--------|-------|
| Purpose | Visualize optimization process |
| Template compliance | PASS |
| Chart | 04_gradient_descent/chart.pdf |
| Chart width | 0.45\textwidth - DEVIATION (acceptable for contour plot) |
| Academic level | GOOD - visual supports algorithm understanding |
| Issues | None |

### Frame 11: Interpreting Coefficients (Line 228-245)
| Aspect | Value |
|--------|-------|
| Purpose | Business interpretation of model parameters |
| Template compliance | PASS |
| Chart | None |
| Academic level | EXCELLENT - connects math to business meaning |
| Issues | None |

### Frame 12: Model Evaluation (Line 248-267)
| Aspect | Value |
|--------|-------|
| Purpose | Introduce evaluation metrics |
| Template compliance | PASS |
| Chart | None |
| Academic level | MSc APPROPRIATE - R2 and RMSE formulas |
| Issues | None |

### Frame 13: Residual Diagnostics (Line 270-277)
| Aspect | Value |
|--------|-------|
| Purpose | Model validation through residuals |
| Template compliance | PASS |
| Chart | 03_residual_plots/chart.pdf |
| Chart width | 0.50\textwidth |
| Academic level | GOOD - teaches diagnostic thinking |
| Issues | None |

### Frame 14: Learning Curves (Line 280-287)
| Aspect | Value |
|--------|-------|
| Purpose | Diagnose under/overfitting |
| Template compliance | PASS |
| Chart | 05_learning_curves/chart.pdf |
| Chart width | 0.50\textwidth |
| Academic level | GOOD - model selection concept |
| Issues | None |

### Frame 15: When to Use Linear Regression (Line 290-326)
| Aspect | Value |
|--------|-------|
| Purpose | Decision framework for method selection |
| Template compliance | PASS - uses columns, table with booktabs |
| Chart | None |
| Academic level | EXCELLENT - practical decision guidance |
| Issues | None |

### Frame 16: XKCD Overfitting Warning (Line 329-336)
| Aspect | Value |
|--------|-------|
| Purpose | Caution about overfitting |
| Template compliance | PASS |
| Chart | External image |
| Image width | 0.32\textwidth (small, appropriate for humor slide) |
| Academic level | GOOD - memorable visual |
| Issues | None |

### Frame 17: Regularization Comparison (Line 339-346)
| Aspect | Value |
|--------|-------|
| Purpose | Introduce Ridge vs Lasso |
| Template compliance | PASS |
| Chart | 06_regularization_comparison/chart.pdf |
| Chart width | 0.50\textwidth |
| Academic level | MSc APPROPRIATE - regularization concepts |
| Issues | None |

### Frame 18: Bias-Variance Tradeoff (Line 349-356)
| Aspect | Value |
|--------|-------|
| Purpose | Core ML concept |
| Template compliance | PASS |
| Chart | 07_bias_variance/chart.pdf |
| Chart width | 0.50\textwidth |
| Academic level | EXCELLENT - fundamental concept clearly illustrated |
| Issues | None |

### Frame 19: XKCD Extrapolation Warning (Line 359-366)
| Aspect | Value |
|--------|-------|
| Purpose | Caution about extrapolation |
| Template compliance | PASS |
| Chart | External image |
| Image width | 0.50\textwidth |
| Academic level | GOOD - important practical warning |
| Issues | None |

### Frame 20: Decision Framework (Line 369-376)
| Aspect | Value |
|--------|-------|
| Purpose | Algorithmic decision guide |
| Template compliance | PASS |
| Chart | 08_decision_flowchart/chart.pdf |
| Chart width | 0.45\textwidth |
| Academic level | GOOD - actionable decision tool |
| Issues | None |

### Frame 21: Key Takeaways (Line 379-398)
| Aspect | Value |
|--------|-------|
| Purpose | Summarize, point to next steps |
| Template compliance | PASS |
| Chart | None |
| Academic level | GOOD - consolidated learning |
| Issues | None |

---

## Part 3: Per-Slide Analysis - L01_deepdive.tex

### Summary Table

| Frame | Title | Purpose | Chart | Issues |
|-------|-------|---------|-------|--------|
| 1 | Title | Intro | None | - |
| 2 | Outline | Navigation | None | - |
| 3 | Matrix Notation | Formalize model | None | - |
| 4 | Design Matrix Structure | Explain X | None | - |
| 5 | OLS Assumptions | Foundation | None | - |
| 6 | The Loss Function | Define objective | None | - |
| 7 | Deriving Normal Equation | Math derivation | None | - |
| 8 | Simple Regression Visualization | Visual | 01_simple_regression | Width 0.55 CORRECT |
| 9 | Multiple Regression Surface | Visual | 02_multiple_regression_3d | Width 0.42 (3D) |
| 10 | Why Gradient Descent? | Motivation | None | - |
| 11 | The Gradient | Math | None | - |
| 12 | Gradient Descent Algorithm | Steps | None | - |
| 13 | Gradient Descent Visualization | Visual | 04_gradient_descent | Width 0.55 CORRECT |
| 14 | Learning Rate Selection | Hyperparameter | None | - |
| 15 | SGD | Extension | None | - |
| 16 | R-Squared | Metric | None | - |
| 17 | Adjusted R-Squared | Metric | None | - |
| 18 | RMSE and MAE | Metrics | None | - |
| 19 | Residual Analysis | Visual | 03_residual_plots | Width 0.55 CORRECT |
| 20 | Train-Test Split | Evaluation | None | - |
| 21 | Learning Curves | Visual | 05_learning_curves | Width 0.55 CORRECT |
| 22 | The Overfitting Problem | Motivation | None | - |
| 23 | Ridge Regression | Method | None | - |
| 24 | Lasso Regression | Method | None | - |
| 25 | Ridge vs Lasso Comparison | Visual | 06_regularization | Width 0.55 CORRECT |
| 26 | Elastic Net | Extension | None | - |
| 27 | Choosing Lambda | Hyperparameter | None | - |
| 28 | Decomposing Prediction Error | Theory | None | - |
| 29 | The Tradeoff Illustrated | Visual | 07_bias_variance | Width 0.55 CORRECT |
| 30 | Regularization and Bias-Variance | Theory | None | - |
| 31 | Algorithm Selection Guide | Visual | 08_decision_flowchart | Width 0.50 |
| 32 | Linear Regression: When and Why | Decision | None | - |
| 33 | Key Equations Summary | Reference | None | - |
| 34 | Key Takeaways | Summary | None | - |
| 35 | References | Resources | None | - |

---

## Part 4: Chart Analysis

### Chart Font Size Verification

| Chart | font.size | axes.labelsize | axes.titlesize | tick.labelsize | legend.fontsize | Status |
|-------|-----------|----------------|----------------|----------------|-----------------|--------|
| Template | 14 | 14 | 16 | 13 | 13 | STANDARD |
| 01_simple_regression | 14 | 14 | 16 | 13 | 13 | PASS |
| 02_multiple_regression_3d | 14 | 14 | 16 | 13 | 13 | PASS |
| 03_residual_plots | 14 | 14 | 16 | 13 | 13 | PASS |
| 04_gradient_descent | 14 | 14 | 16 | 13 | 13 | PASS |
| 05_learning_curves | 14 | 14 | 16 | 13 | 13 | PASS |
| 06_regularization | 14 | 14 | 16 | 13 | 13 | PASS |
| 07_bias_variance | 14 | 14 | 16 | 13 | 13 | PASS |
| 08_decision_flowchart | **11** | - | - | - | - | **FAIL** |

### Chart Configuration Details

#### 01_simple_regression/chart.py
- **Line 14-18**: Correct rcParams
- **Colors**: MLPURPLE, MLORANGE, MLBLUE defined correctly
- **figsize**: (10, 6) CORRECT
- **Missing**: GitHub URL watermark (template has it, chart does not)
- **Missing**: axes.spines.top/right removal

#### 02_multiple_regression_3d/chart.py
- **Line 15-19**: Correct rcParams
- **Note**: 3D plots naturally need smaller display width
- **Missing**: GitHub URL watermark
- **Missing**: axes.spines settings (less relevant for 3D)

#### 03_residual_plots/chart.py
- **Line 14-18**: Correct rcParams
- **Missing**: GitHub URL watermark
- **Line 60-62**: Annotation fontsize=11 (acceptable for annotation)

#### 04_gradient_descent/chart.py
- **Line 14-18**: Correct rcParams
- **Missing**: GitHub URL watermark

#### 05_learning_curves/chart.py
- **Line 14-18**: Correct rcParams
- **Line 46-47**: Annotation fontsize=11 (acceptable)
- **Missing**: GitHub URL watermark

#### 06_regularization_comparison/chart.py
- **Line 19-23**: Correct rcParams
- **Line 73**: Legend fontsize=11 (deviation from 13)
- **Line 77-79**: Annotation fontsize=11 (acceptable)
- **Missing**: GitHub URL watermark

#### 07_bias_variance/chart.py
- **Line 14-18**: Correct rcParams
- **Line 66-71**: Annotation fontsize=11 (acceptable)
- **Missing**: GitHub URL watermark

#### 08_decision_flowchart/chart.py (ISSUES)
- **Line 14-16**: Uses font.size=11 (SHOULD BE 14)
- **Line 32**: Box text fontsize=10 (acceptable for flowchart)
- **Line 42**: Diamond text fontsize=9 (acceptable for flowchart)
- **Line 76**: Title fontsize=14 (correct)
- **Missing**: GitHub URL watermark
- **Note**: Flowcharts need smaller fonts for readability in boxes

---

## Part 5: Academic Level Assessment

### Prerequisites Check

The slides assume NO prerequisites beyond basic math literacy:
- Matrix notation is introduced from scratch (L01_deepdive Frame 3-4)
- All variables are defined when first used
- Business context provides intuition before math

### Concept Progression

| Slide Range | Conceptual Level | Notes |
|-------------|-----------------|-------|
| 1-5 | Introductory | Problem motivation, basic definition |
| 6-10 | Intermediate | Optimization, gradient descent |
| 11-15 | Intermediate | Interpretation, evaluation |
| 16-21 | Advanced | Regularization, bias-variance |

### MSc Appropriateness

| Criterion | Assessment |
|-----------|------------|
| Mathematical rigor | YES - matrix calculus, formal derivations |
| Practical relevance | YES - finance use cases throughout |
| Depth of treatment | YES - covers assumptions, limitations, alternatives |
| Research connection | YES - references to seminal texts (ISLR, ESL) |

---

## Part 6: Issues Summary

### Critical (Must Fix)

| ID | File | Line | Issue | Fix |
|----|------|------|-------|-----|
| C1 | 08_decision_flowchart/chart.py | 14-16 | font.size=11 instead of 14 | Update rcParams to match template |

### High Priority (Should Fix)

| ID | File | Line | Issue | Fix |
|----|------|------|-------|-----|
| H1 | L01_overview.tex | 139 | Chart width 0.50 vs 0.55 standard | Change to 0.55\textwidth |
| H2 | All chart.py | - | Missing GitHub URL watermark | Add watermark per template |
| H3 | 06_regularization_comparison/chart.py | 73 | legend.fontsize=11 vs 13 | Keep at 13 for consistency |

### Low Priority (Nice to Have)

| ID | File | Line | Issue | Fix |
|----|------|------|-------|-----|
| L1 | L01_overview.tex | 57 | Empty date field | Add "Spring 2026" |
| L2 | L01_deepdive.tex | 56 | Empty date field | Add "Spring 2026" |
| L3 | All chart.py | - | Missing axes.spines.top/right=False | Add for cleaner visuals |
| L4 | L01_overview.tex | 86,332,363 | XKCD images lack alt-text | Consider adding \pdftooltip for accessibility |

---

## Part 7: Verification Steps

### Pre-Implementation Checklist

- [ ] Review this plan with instructor/stakeholder
- [ ] Backup current files before changes
- [ ] Note current chart PDF timestamps

### Post-Implementation Verification

1. **Template Compliance**
   ```bash
   # Check document class
   grep -n "documentclass" slides/L01_*/L01_*.tex
   # Should show: 8pt,aspectratio=169
   ```

2. **Chart Font Sizes**
   ```bash
   # Check rcParams in all charts
   grep -n "font.size" slides/L01_*/*/chart.py
   # All should show: 14
   ```

3. **Chart Widths**
   ```bash
   # Check includegraphics widths
   grep -n "textwidth" slides/L01_*/L01_*.tex
   # Document any deviations from 0.55/0.65
   ```

4. **Recompile All Charts**
   ```bash
   python infrastructure/course_cli.py build charts --topic L01
   ```

5. **Recompile Slides**
   ```bash
   cd slides/L01_Introduction_Linear_Regression
   pdflatex -interaction=nonstopmode L01_overview.tex
   pdflatex -interaction=nonstopmode L01_deepdive.tex
   ```

6. **Visual Inspection**
   - Open both PDFs
   - Check chart readability at presentation size
   - Verify no text overflow warnings

---

## Part 8: Task Breakdown

### Task 1: Fix Decision Flowchart Font Size
- **File**: D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\08_decision_flowchart\chart.py
- **Line**: 14-16
- **Change**: Update `'font.size': 11` to `'font.size': 14`
- **Acceptance**: `grep "font.size" chart.py` returns 14

### Task 2: Standardize Chart Widths in Overview
- **File**: D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\L01_overview.tex
- **Lines**: 139, 149, 221, 273, 283, 342, 353, 372
- **Change**: Ensure all charts use 0.55\textwidth (except 3D at 0.42)
- **Acceptance**: `grep "includegraphics" L01_overview.tex` shows consistent widths

### Task 3: Add GitHub URL Watermarks to Charts
- **Files**: All 8 chart.py files in L01
- **Change**: Add URL watermark per template (lines 84-90 of chart_template.py)
- **Acceptance**: Visual inspection of regenerated PDFs shows watermark

### Task 4: Add Missing Date to Title Slides
- **Files**: L01_overview.tex (line 57), L01_deepdive.tex (line 56)
- **Change**: Update `\date{}` to `\date{Spring 2026}`
- **Acceptance**: `grep "date" L01_*.tex` returns "Spring 2026"

### Task 5: Regenerate All Charts
- **Command**: `python infrastructure/course_cli.py build charts --topic L01`
- **Acceptance**: All 8 chart.pdf files have new timestamps

### Task 6: Recompile LaTeX Slides
- **Command**: pdflatex on both .tex files
- **Acceptance**: No overflow warnings, PDFs updated

---

## Commit Strategy

### Commit 1: Chart Font Standardization
```
fix(L01): standardize font sizes in decision flowchart chart

- Update 08_decision_flowchart/chart.py to use font.size=14
- Ensures consistency with other L01 charts
```

### Commit 2: Chart Width Standardization
```
fix(L01): standardize chart widths in overview slides

- Update L01_overview.tex to use consistent 0.55\textwidth
- Exception: 3D chart remains at 0.42 for aspect ratio
```

### Commit 3: Add GitHub Watermarks
```
feat(L01): add GitHub URL watermarks to all charts

- Add watermark to all 8 chart.py files
- Follows chart_template.py specification
```

### Commit 4: Minor Template Fixes
```
fix(L01): add missing dates and accessibility improvements

- Add Spring 2026 dates to both slide decks
- Minor formatting consistency improvements
```

---

## Success Criteria

| Criterion | Metric | Target |
|-----------|--------|--------|
| Template Compliance | % matching template | 100% |
| Chart Font Consistency | Charts with correct font.size | 8/8 |
| Chart Readability | Readable at 0.55\textwidth | All pass visual test |
| LaTeX Compilation | Overflow warnings | 0 |
| Academic Level | Appropriate for MSc | Yes |
| Purpose Clarity | Each slide has clear purpose | Yes |

---

## Appendix: File Inventory

### Source Files
- D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\L01_overview.tex (400 lines)
- D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\L01_deepdive.tex (635 lines)
- D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\L01_instructor_guide.md

### Chart Files
1. D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\01_simple_regression\chart.py
2. D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\02_multiple_regression_3d\chart.py
3. D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\03_residual_plots\chart.py
4. D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\04_gradient_descent\chart.py
5. D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\05_learning_curves\chart.py
6. D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\06_regularization_comparison\chart.py
7. D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\07_bias_variance\chart.py
8. D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\08_decision_flowchart\chart.py

### Template Files
- D:\Joerg\Research\slides\Methods_and_Algorithms\templates\beamer_template.tex
- D:\Joerg\Research\slides\Methods_and_Algorithms\templates\chart_template.py

---

*Plan generated: 2026-02-02*
*Reviewer: Prometheus (Strategic Planning Consultant)*
