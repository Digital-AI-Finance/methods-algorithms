# Work Plan: Cleanup Quiz and Template Compliance

**Plan ID:** cleanup-quiz-template
**Created:** 2026-01-29
**Status:** READY FOR EXECUTION
**Revision:** 2 (Addresses Critic feedback from Iteration 1)

---

## Context

### Original Request
Three tasks:
1. Remove the capstone section from course materials
2. Fix interactive quiz KaTeX bug (math not rendering)
3. Ensure all slides follow Beamer template layout

### Research Findings

**Task 1 - Capstone Removal:**
- `docs/index.html` lines 106-109: Sidebar nav with capstone details
- `docs/index.html` lines 299-307: Capstone section with 3 cards
- `manifest.json` lines 955-960: Capstone configuration block
- No actual capstone folder exists in repository (references are orphaned)
- Hero stats show "165 Quiz Questions" - appears correct (no capstone quiz count)

**Task 2 - Quiz KaTeX Bug:**
- Affected files: `quiz1_regression.html`, `quiz2_classification_ensemble.html`, `quiz3_advanced.html`
- All three load KaTeX CSS/JS (lines 7-9) but NEVER call `renderMathInElement()`
- Working reference: `L01_linear_regression.html` has proper initialization (lines 754-769)
- Per-lesson quizzes (L01-L06) already have correct KaTeX initialization
- **Pattern for fix:** Search for standalone `render();` at end of script (NOT inside functions)
  - quiz1: line 221
  - quiz2: line 195
  - quiz3: line 195

**Task 3 - Slide Template Compliance (ACCURATE PER-FILE AUDIT):**

Reference Template (`templates/beamer_template.tex`):
- `\documentclass[8pt,aspectratio=169]{beamer}`
- `\usetheme{Madrid}` + `\usecolortheme{default}`
- Packages: inputenc, fontenc, amsmath/amssymb, graphicx, booktabs, tikz, hyperref
- Colors: MLPurple, MLBlue, MLOrange, MLGreen, MLRed (RGB format, UPPERCASE)
- Custom footer: 3-part with "Methods and Algorithms | MSc Data Science | page/total"
- Custom commands: `\bottomnote` (italic), `\highlight`, `\mathbold`

### Per-File Differential Analysis

| File | inputenc | fontenc | tikz | hyperref | Colors | bottomnote | highlight | mathbold | Footer |
|------|----------|---------|------|----------|--------|------------|-----------|----------|--------|
| **L01_overview.tex** | YES | YES | NO | YES | UPPERCASE RGB | italic | YES | NO | YES |
| **L01_deepdive.tex** | YES | YES | NO | YES | UPPERCASE RGB | italic | YES | NO | YES |
| **L02_overview.tex** | NO | NO | YES | NO | lowercase HTML | gray text | NO | NO | NO |
| **L02_deepdive.tex** | NO | NO | YES | NO | lowercase HTML | gray text | NO | NO | NO |
| **L03_overview.tex** | NO | NO | YES | NO | lowercase HTML | gray text | NO | NO | NO |
| **L03_deepdive.tex** | NO | NO | YES | NO | lowercase HTML | gray text | NO | NO | NO |
| **L04_overview.tex** | NO | NO | YES | NO | lowercase HTML | gray text | NO | NO | NO |
| **L04_deepdive.tex** | NO | NO | YES | NO | lowercase HTML | gray text | NO | NO | NO |
| **L05_overview.tex** | NO | NO | YES | NO | lowercase HTML | gray text | NO | NO | NO |
| **L05_deepdive.tex** | NO | NO | YES | NO | lowercase HTML | gray text | NO | NO | NO |
| **L06_overview.tex** | NO | NO | YES | NO | lowercase HTML | gray text | NO | NO | NO |
| **L06_deepdive.tex** | NO | NO | YES | NO | lowercase HTML | gray text | NO | NO | NO |

### Critical Differences by Group

**Group A - L01 files (already close to template):**
- HAVE: inputenc, fontenc, hyperref, uppercase colors (MLPurple, etc.), custom footer, highlight command
- MISSING: tikz, mathbold
- Body content uses uppercase colors: `\textcolor{MLGreen}`, `\textcolor{MLRed}`, `\textcolor{MLOrange}`

**Group B - L02-L06 files (significantly different):**
- HAVE: tikz
- MISSING: inputenc, fontenc, hyperref, mathbold, highlight, custom footer
- Use lowercase HTML colors: `mlpurple`, `mlblue`, etc.
- `\bottomnote` uses `\textcolor{gray}{#1}` (gray text) vs template's `\textit{#1}` (italic)
- **NO body content uses color names directly** (only in bottomnote definition)

### Risk Analysis

**Color Name Compatibility:**
- L01: Uses uppercase colors in body (`\textcolor{MLGreen}`) - SAFE with template preamble
- L02-L06: Only use `gray` in bottomnote command, no direct ML color usage in body - SAFE to change preamble

**bottomnote Visual Change:**
- Template: `\vfill\footnotesize\textit{#1}` (italic text)
- L02-L06: `\vfill\footnotesize\textcolor{gray}{#1}` (gray text)
- **Decision:** Normalize to template style (italic). Gray-to-italic is minor visual change, acceptable.

**Footer Risk:**
- L02-L06 have no custom footer (use default Madrid footer)
- Adding custom footer is an improvement, no risk of breaking

---

## Work Objectives

### Core Objective
Clean up orphaned capstone references, fix quiz math rendering, and standardize slide preambles.

### Deliverables
1. `docs/index.html` with capstone section removed
2. `manifest.json` with capstone block removed
3. Three quiz files with working KaTeX initialization
4. 12 slide files with consistent preamble (template-compliant)

### Definition of Done
- [ ] No capstone references in docs/index.html
- [ ] No capstone block in manifest.json
- [ ] Math renders correctly in quiz1, quiz2, quiz3
- [ ] All 12 slides compile without errors
- [ ] All 12 slides have consistent preamble structure

---

## Guardrails

### MUST Have
- Preserve all existing functionality in quizzes
- Keep slide content unchanged (only preamble modifications)
- Maintain file structure
- Verify compilation after each slide change

### MUST NOT Have
- Changes to quiz question content
- Changes to slide body content (after preamble)
- Breaking the GitHub Pages deployment
- Breaking existing color usage in L01 body content

---

## Task Flow

```
[Task 1: Remove Capstone] -----> [Task 2: Fix Quizzes] -----> [Task 3: Standardize Slides]
         |                              |                              |
         v                              v                              v
   (2 files)                      (3 files)                      (12 files)
```

All tasks are independent and can be parallelized.

---

## Rollback Strategy

Before making changes:
1. Create backup of all files being modified (or rely on git)
2. After each .tex file change, run `pdflatex -interaction=nonstopmode` to verify
3. If compilation fails, revert and investigate

Rollback commands:
```bash
# Revert a specific file
git checkout -- path/to/file

# Revert all changes (nuclear option)
git checkout -- .
```

---

## Detailed TODOs

### Task 1: Remove Capstone Section

#### TODO 1.1: Remove capstone from docs/index.html sidebar
**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\docs\index.html`
**Action:** Delete lines 106-109 (capstone details element in sidebar)
**Before:**
```html
<details><summary style="border-left:3px solid #586069">Capstone</summary><ul>
<li><a href="#capstone">Specification</a></li>
<li><a href="#capstone">Rubric</a></li>
</ul></details>
```
**After:** (delete entirely)
**Acceptance:** Sidebar has no "Capstone" accordion

#### TODO 1.2: Remove capstone section from docs/index.html main content
**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\docs\index.html`
**Action:** Delete lines 299-307 (entire capstone section)
**Before:**
```html
<!-- Capstone Section -->
<section class="section" id="capstone">
<div class="section-head" style="border-color:#586069"><span style="background:#586069">C</span><h2>Capstone Project</h2></div>
<div class="lgrid" style="grid-template-columns:repeat(3,1fr)">
<a class="lcard" href="...">...</a>
<a class="lcard" href="...">...</a>
<a class="lcard" href="...">...</a>
</div>
</section>
```
**After:** (delete entirely)
**Acceptance:** No capstone section on page

#### TODO 1.3: Remove capstone from manifest.json
**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\manifest.json`
**Action:** Delete the capstone block (around lines 955-965)
**Target:** Remove the entire `"capstone": { ... }` object
**Acceptance:** `grep -i capstone manifest.json` returns nothing

---

### Task 2: Fix Quiz KaTeX Bug

**Implementation Pattern (apply to all 3 files):**
Find the standalone `render();` call at end of script (outside any function) and wrap it with DOMContentLoaded + renderMath:

```javascript
function renderMath() {
    if (typeof renderMathInElement !== 'undefined') {
        renderMathInElement(document.body, {
            delimiters: [
                {left: '$$', right: '$$', display: true},
                {left: '$', right: '$', display: false}
            ],
            throwOnError: false
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    render();
    setTimeout(renderMath, 100);
});
```

Replace the standalone `render();` with the above block.

#### TODO 2.1: Add renderMath function to quiz1_regression.html
**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\docs\quiz\quiz1_regression.html`
**Action:** Find standalone `render();` (at end of script, outside functions) and replace with DOMContentLoaded block
**Acceptance:** Math formulas render correctly in quiz1

#### TODO 2.2: Add renderMath function to quiz2_classification_ensemble.html
**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\docs\quiz\quiz2_classification_ensemble.html`
**Action:** Find standalone `render();` (at end of script, outside functions) and replace with DOMContentLoaded block
**Acceptance:** Math formulas render correctly in quiz2

#### TODO 2.3: Add renderMath function to quiz3_advanced.html
**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\docs\quiz\quiz3_advanced.html`
**Action:** Find standalone `render();` (at end of script, outside functions) and replace with DOMContentLoaded block
**Acceptance:** Math formulas render correctly in quiz3

---

### Task 3: Standardize Slide Preambles

**Approach:** MINIMAL CHANGES - Only add what's missing per file, preserving working content.

**Standard Preamble Target:**
```latex
\documentclass[8pt,aspectratio=169]{beamer}

% Theme
\usetheme{Madrid}
\usecolortheme{default}

% Packages
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{tikz}
\usepackage{hyperref}

% Custom colors (ML palette)
\definecolor{MLPurple}{RGB}{51,51,178}
\definecolor{MLBlue}{RGB}{0,102,204}
\definecolor{MLOrange}{RGB}{255,127,14}
\definecolor{MLGreen}{RGB}{44,160,44}
\definecolor{MLRed}{RGB}{214,39,40}

% Apply colors
\setbeamercolor{structure}{fg=MLPurple}
\setbeamercolor{title}{fg=MLPurple}
\setbeamercolor{frametitle}{fg=MLPurple}

% Footer customization
\setbeamertemplate{footline}{
  \leavevmode%
  \hbox{%
    \begin{beamercolorbox}[wd=.333333\paperwidth,ht=2.25ex,dp=1ex,center]{author in head/foot}%
      \usebeamerfont{author in head/foot}Methods and Algorithms
    \end{beamercolorbox}%
    \begin{beamercolorbox}[wd=.333333\paperwidth,ht=2.25ex,dp=1ex,center]{title in head/foot}%
      \usebeamerfont{title in head/foot}MSc Data Science
    \end{beamercolorbox}%
    \begin{beamercolorbox}[wd=.333333\paperwidth,ht=2.25ex,dp=1ex,right]{date in head/foot}%
      \usebeamerfont{date in head/foot}\insertframenumber{} / \inserttotalframenumber\hspace*{2ex}
    \end{beamercolorbox}}%
  \vskip0pt%
}

% Remove navigation symbols
\setbeamertemplate{navigation symbols}{}

% Custom commands
\newcommand{\bottomnote}[1]{\vfill\footnotesize\textit{#1}}
\newcommand{\highlight}[1]{\textcolor{MLOrange}{\textbf{#1}}}
\newcommand{\mathbold}[1]{\boldsymbol{#1}}
```

#### TODO 3.1: Update L01_overview.tex preamble
**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\L01_overview.tex`
**Current state:** Has inputenc, fontenc, hyperref, uppercase colors, footer, highlight. Missing tikz, mathbold.
**Action:** Add `\usepackage{tikz}` and `\newcommand{\mathbold}[1]{\boldsymbol{#1}}`
**Acceptance:** pdflatex compiles without errors

#### TODO 3.2: Update L01_deepdive.tex preamble
**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\L01_deepdive.tex`
**Current state:** Has inputenc, fontenc, hyperref, uppercase colors, footer, highlight. Missing tikz, mathbold.
**Action:** Add `\usepackage{tikz}` and `\newcommand{\mathbold}[1]{\boldsymbol{#1}}`
**Acceptance:** pdflatex compiles without errors

#### TODO 3.3: Update L02_overview.tex preamble
**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L02_Logistic_Regression\L02_overview.tex`
**Current state:** Has tikz. Missing inputenc, fontenc, hyperref, footer, highlight, mathbold. Uses lowercase HTML colors.
**Action:** Replace entire preamble (before `\title`) with standard preamble
**Note:** bottomnote changes from gray text to italic (acceptable visual change)
**Acceptance:** pdflatex compiles without errors

#### TODO 3.4: Update L02_deepdive.tex preamble
**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L02_Logistic_Regression\L02_deepdive.tex`
**Current state:** Same as L02_overview + has algorithm/algorithmic packages
**Action:** Replace preamble, KEEP algorithm/algorithmic packages
**Acceptance:** pdflatex compiles without errors

#### TODO 3.5: Update L03_overview.tex preamble
**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L03_KNN_KMeans\L03_overview.tex`
**Current state:** Has tikz. Missing inputenc, fontenc, hyperref, footer, highlight, mathbold. Uses lowercase HTML colors.
**Action:** Replace entire preamble with standard preamble
**Acceptance:** pdflatex compiles without errors

#### TODO 3.6: Update L03_deepdive.tex preamble
**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L03_KNN_KMeans\L03_deepdive.tex`
**Current state:** Same as L03_overview + has algorithm/algorithmic packages
**Action:** Replace preamble, KEEP algorithm/algorithmic packages
**Acceptance:** pdflatex compiles without errors

#### TODO 3.7: Update L04_overview.tex preamble
**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L04_Random_Forests\L04_overview.tex`
**Current state:** Has tikz. Missing inputenc, fontenc, hyperref, footer, highlight, mathbold. Uses lowercase HTML colors.
**Action:** Replace entire preamble with standard preamble
**Acceptance:** pdflatex compiles without errors

#### TODO 3.8: Update L04_deepdive.tex preamble
**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L04_Random_Forests\L04_deepdive.tex`
**Current state:** Same as L04_overview + has algorithm/algorithmic packages
**Action:** Replace preamble, KEEP algorithm/algorithmic packages
**Acceptance:** pdflatex compiles without errors

#### TODO 3.9: Update L05_overview.tex preamble
**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L05_PCA_tSNE\L05_overview.tex`
**Current state:** Has tikz. Missing inputenc, fontenc, hyperref, footer, highlight, mathbold. Uses lowercase HTML colors.
**Action:** Replace entire preamble with standard preamble
**Acceptance:** pdflatex compiles without errors

#### TODO 3.10: Update L05_deepdive.tex preamble
**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L05_PCA_tSNE\L05_deepdive.tex`
**Current state:** Has tikz. Missing inputenc, fontenc, hyperref, footer, highlight, mathbold. Uses lowercase HTML colors.
**Action:** Replace entire preamble with standard preamble
**Acceptance:** pdflatex compiles without errors

#### TODO 3.11: Update L06_overview.tex preamble
**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L06_Embeddings_RL\L06_overview.tex`
**Current state:** Has tikz. Missing inputenc, fontenc, hyperref, footer, highlight, mathbold. Uses lowercase HTML colors.
**Action:** Replace entire preamble with standard preamble
**Acceptance:** pdflatex compiles without errors

#### TODO 3.12: Update L06_deepdive.tex preamble
**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L06_Embeddings_RL\L06_deepdive.tex`
**Current state:** Has tikz. Missing inputenc, fontenc, hyperref, footer, highlight, mathbold. Uses lowercase HTML colors.
**Action:** Replace entire preamble with standard preamble
**Acceptance:** pdflatex compiles without errors

---

## Verification Steps

### After Task 1 (Capstone Removal)
```bash
# Verify no capstone references
grep -i capstone docs/index.html     # Should return nothing
grep -i capstone manifest.json       # Should return nothing

# Visual check: Open docs/index.html in browser
# - Sidebar should not have Capstone accordion
# - Main content should end after quizzes section
```

### After Task 2 (Quiz Fix)
```bash
# Open each quiz in browser and verify:
# 1. docs/quiz/quiz1_regression.html - math formulas render
# 2. docs/quiz/quiz2_classification_ensemble.html - math formulas render
# 3. docs/quiz/quiz3_advanced.html - math formulas render

# Check for syntax errors in JS console (F12)
```

### After Task 3 (Slide Preambles)
```bash
# Compile each slide to verify no LaTeX errors
cd slides/L01_Introduction_Linear_Regression && pdflatex -interaction=nonstopmode L01_overview.tex
cd slides/L01_Introduction_Linear_Regression && pdflatex -interaction=nonstopmode L01_deepdive.tex
# ... repeat for L02-L06

# Or use course CLI:
python infrastructure/course_cli.py validate latex --strict
```

---

## Commit Strategy

### Suggested Commits
1. **Remove capstone section from course materials**
   - Files: `docs/index.html`, `manifest.json`

2. **Fix KaTeX math rendering in aggregated quizzes**
   - Files: `docs/quiz/quiz1_regression.html`, `docs/quiz/quiz2_classification_ensemble.html`, `docs/quiz/quiz3_advanced.html`

3. **Standardize Beamer preambles across all slides**
   - Files: All 12 `.tex` files in `slides/L0X_*/`

---

## Success Criteria

| Criterion | Metric |
|-----------|--------|
| Capstone removed | 0 references in docs/index.html and manifest.json |
| Quiz math works | All 3 quiz files render $...$ formulas correctly |
| Slides compile | All 12 .tex files compile with 0 errors |
| Template compliance | All slides have required packages and commands |

---

## Execution Notes

- Tasks 1, 2, 3 are independent - can be parallelized
- Task 3 L01 files: MINIMAL changes (add tikz + mathbold only)
- Task 3 L02-L06 files: Full preamble replacement
- Deepdive files with algorithm/algorithmic packages: preserve those packages
- No Python/infrastructure changes needed
- Changes are all in static files (HTML, JSON, LaTeX)
- bottomnote visual change: L02-L06 notes will change from gray to italic (minor, acceptable)
