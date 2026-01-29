# HOSTILE Ultra-Deep Presentation Review Plan (ITERATION 2)

**Generated:** 2026-01-28
**Status:** READY FOR EXECUTION
**Scope:** 12 presentations (6 overview + 6 deepdive), 49 chart.py scripts
**Severity Rating Scale:** CRITICAL | HIGH | MEDIUM | LOW
**TOLERANCE:** ZERO - No deviations, no exceptions, no mercy

---

## Executive Summary

This plan defines a HOSTILE ultra-deep review of all course presentations. Every deviation from template specifications, every missing element, every non-compliance issue will be documented with **ZERO TOLERANCE**.

### Severity Definitions (STRICT)

| Level | Definition | Action Required |
|-------|------------|-----------------|
| **CRITICAL** | Template specification violation, chart width deviation, missing required command | MUST FIX IMMEDIATELY |
| **HIGH** | Missing required content, missing sections, compilation warnings | MUST FIX BEFORE RELEASE |
| **MEDIUM** | Package inconsistency, formatting deviation | SHOULD FIX |
| **LOW** | Minor style preference | OPTIONAL FIX |

**REMOVED:** "BORDERLINE", "acceptable range", "minor deviation", "similar variants" - These terms are BANNED.

---

## Phase 1: Template Compliance Audit

### Objective
Line-by-line verification of each .tex header against the canonical template.

### Tasks

#### Task 1.1: Document Class Verification
**Acceptance Criteria:** EXACTLY `\documentclass[8pt,aspectratio=169]{beamer}`
**Tolerance:** ZERO - Any deviation = CRITICAL

| File | Expected | Action |
|------|----------|--------|
| L01_overview.tex | Verify exact match | Check line 1 |
| L01_deepdive.tex | Verify exact match | Check line 1 |
| L02_overview.tex | Verify exact match | Check line 1 |
| L02_deepdive.tex | Verify exact match | Check line 1 |
| L03_overview.tex | Verify exact match | Check line 1 |
| L03_deepdive.tex | Verify exact match | Check line 1 |
| L04_overview.tex | Verify exact match | Check line 1 |
| L04_deepdive.tex | Verify exact match | Check line 1 |
| L05_overview.tex | Verify exact match | Check line 1 |
| L05_deepdive.tex | Verify exact match | Check line 1 |
| L06_overview.tex | Verify exact match | Check line 1 |
| L06_deepdive.tex | Verify exact match | Check line 1 |

#### Task 1.2: Theme Verification
**Acceptance Criteria:** EXACTLY `\usetheme{Madrid}` AND `\usecolortheme{default}`
**Tolerance:** ZERO

#### Task 1.3: Color Definition Verification
**Acceptance Criteria:** EXACT RGB format using `\definecolor{name}{RGB}{r,g,b}`
**Tolerance:** ZERO - HTML format = CRITICAL

| Color | Required Definition | Hex Equivalent |
|-------|---------------------|----------------|
| MLPurple | `\definecolor{MLPurple}{RGB}{51,51,178}` | #3333B2 |
| MLBlue | `\definecolor{MLBlue}{RGB}{0,102,204}` | #0066CC |
| MLOrange | `\definecolor{MLOrange}{RGB}{255,127,14}` | #FF7F0E |
| MLGreen | `\definecolor{MLGreen}{RGB}{44,160,44}` | #2CA02C |
| MLRed | `\definecolor{MLRed}{RGB}{214,39,40}` | #D62728 |

**CRITICAL VIOLATIONS TO DOCUMENT:**
- HTML format (`\definecolor{mlpurple}{HTML}{3333B2}`) = CRITICAL
- Lowercase color names (`mlpurple` vs `MLPurple`) = CRITICAL
- Missing any of the 5 colors = CRITICAL

#### Task 1.4: Package Verification
**Required Packages (ALL MUST BE PRESENT):**
- `\usepackage[utf8]{inputenc}` - CRITICAL if missing
- `\usepackage[T1]{fontenc}` - CRITICAL if missing
- `\usepackage{amsmath,amssymb}` - CRITICAL if missing
- `\usepackage{graphicx}` - CRITICAL if missing
- `\usepackage{booktabs}` - CRITICAL if missing
- `\usepackage{tikz}` - HIGH if missing
- `\usepackage{hyperref}` - HIGH if missing

#### Task 1.5: Footer Structure Verification
**Required:** Three beamercolorboxes with exact structure from template
**Tolerance:** ZERO - Missing footer = CRITICAL

**Must verify presence of:**
```latex
\setbeamertemplate{footline}{
  \leavevmode%
  \hbox{%
    \begin{beamercolorbox}[wd=.333333\paperwidth...]{author in head/foot}%
    ...
    \begin{beamercolorbox}[wd=.333333\paperwidth...]{title in head/foot}%
    ...
    \begin{beamercolorbox}[wd=.333333\paperwidth...]{date in head/foot}%
```

#### Task 1.6: Custom Command Verification
**Required Commands (EXACT DEFINITIONS):**

| Command | Required Definition | Severity if Missing |
|---------|---------------------|---------------------|
| `\bottomnote` | `\newcommand{\bottomnote}[1]{\vfill\footnotesize\textit{#1}}` | CRITICAL |
| `\highlight` | `\newcommand{\highlight}[1]{\textcolor{MLOrange}{\textbf{#1}}}` | CRITICAL |
| `\mathbold` | `\newcommand{\mathbold}[1]{\boldsymbol{#1}}` | CRITICAL |

**CRITICAL VIOLATIONS:**
- `\bottomnote` using `\textcolor{gray}{#1}` instead of `\textit{#1}` = CRITICAL
- `\highlight` command MISSING = CRITICAL
- `\mathbold` command MISSING = CRITICAL

#### Task 1.7: Navigation Symbols Verification
**Required:** `\setbeamertemplate{navigation symbols}{}`
**Tolerance:** ZERO - Missing = HIGH (navigation symbols will show)

#### Task 1.8: \setbeamercolor Verification (NEW)
**Required Commands (ALL THREE MUST EXIST):**

```latex
\setbeamercolor{structure}{fg=MLPurple}
\setbeamercolor{title}{fg=MLPurple}
\setbeamercolor{frametitle}{fg=MLPurple}
```

| Command | Severity if Missing |
|---------|---------------------|
| `\setbeamercolor{structure}{fg=MLPurple}` | CRITICAL |
| `\setbeamercolor{title}{fg=MLPurple}` | CRITICAL |
| `\setbeamercolor{frametitle}{fg=MLPurple}` | CRITICAL |

#### Task 1.9: Title/Author/Institute Verification
**Required Format:**
- `\title[SHORT]{FULL TITLE}` - Must have short title in brackets
- `\subtitle{...}` - Must exist
- `\author{Methods and Algorithms}` - EXACT match
- `\institute{MSc Data Science}` - EXACT match
- `\date{Spring 2026}` - EXACT match

**CRITICAL VIOLATIONS:**
- `\author{Methods and Algorithms -- MSc Data Science}` (combined) = CRITICAL
- `\date{}` (empty) = CRITICAL

---

## Phase 1.5: LaTeX Compilation Verification (NEW)

### Objective
Compile all presentations and FAIL on ANY overflow warning.

### Tasks

#### Task 1.5.1: Run Strict LaTeX Validation
**Command:**
```bash
python infrastructure/course_cli.py validate latex --strict
```

**Acceptance Criteria:** ZERO Overfull/Underfull hbox warnings
**Tolerance:** ZERO - Any warning = CRITICAL

#### Task 1.5.2: Individual Presentation Compilation
**For each .tex file:**
```bash
pdflatex -interaction=nonstopmode <file>.tex 2>&1 | grep -E "(Overfull|Underfull)"
```

| Result | Severity |
|--------|----------|
| Any "Overfull" warning | CRITICAL |
| Any "Underfull" warning | HIGH |
| Clean compilation | PASS |

**Documentation:** Capture exact line numbers and box dimensions for each warning.

---

## Phase 2: Content Deep Scan

### Objective
Frame-by-frame content analysis for PMSP compliance, bullet limits, chart widths.

### Tasks

#### Task 2.1: Frame Count Verification

| Presentation | Type | Target | Acceptable | Action |
|--------------|------|--------|------------|--------|
| L01_overview | Overview | 17 | 15-22 | Count frames |
| L01_deepdive | Deepdive | 30 | 25-40 | Count frames |
| L02_overview | Overview | 17 | 15-22 | Count frames |
| L02_deepdive | Deepdive | 30 | 25-40 | Count frames |
| L03_overview | Overview | 17 | 15-22 | Count frames |
| L03_deepdive | Deepdive | 30 | 25-40 | Count frames |
| L04_overview | Overview | 17 | 15-22 | Count frames |
| L04_deepdive | Deepdive | 30 | 25-40 | Count frames |
| L05_overview | Overview | 17 | 15-22 | Count frames |
| L05_deepdive | Deepdive | 30 | 25-40 | Count frames |
| L06_overview | Overview | 17 | 15-22 | Count frames |
| L06_deepdive | Deepdive | 30 | 25-40 | Count frames |

**Severity Ratings:**
- Below minimum = HIGH
- Above maximum = HIGH
- Within range = PASS

#### Task 2.2: PMSP Framework Verification
**Required Sections:** Problem, Method, Solution, Practice

| Presentation | Problem | Method | Solution | Practice | Decision Framework | Summary | References |
|--------------|---------|--------|----------|----------|-------------------|---------|------------|
| L01_overview | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY |
| L01_deepdive | N/A* | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY |
| L02-L06_* | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY |

**Severity for Missing Sections:**
- Missing PMSP section = CRITICAL
- Missing Decision Framework = HIGH
- Missing Summary = HIGH
- Missing References = HIGH

#### Task 2.3: Bullet Count Verification (Max 4 per slide)
**Tolerance:** ZERO - 5+ bullets = HIGH violation

**Action:** Scan each frame for itemize/enumerate environments, count items
**Document:** Frame title, line number, actual count

#### Task 2.4: Chart Width Verification (ZERO TOLERANCE)
**ONLY ACCEPTABLE widths:**
- `0.55\textwidth` (with text)
- `0.65\textwidth` (chart-only slide)

**ALL OTHER WIDTHS = CRITICAL VIOLATION**

**Banned widths (document ALL occurrences):**
- 0.50\textwidth = CRITICAL
- 0.48\textwidth = CRITICAL
- 0.47\textwidth = CRITICAL
- 0.45\textwidth = CRITICAL
- 0.42\textwidth = CRITICAL
- 0.40\textwidth = CRITICAL
- 0.35\textwidth = CRITICAL
- 0.32\textwidth = CRITICAL
- 0.6\textwidth = CRITICAL
- ANY other width = CRITICAL

**Action:** Grep all `\includegraphics` commands, extract width values, flag ALL non-compliant

#### Task 2.5: \includegraphics Path Verification
**Action:** Extract all image paths, verify files exist

**Severity:**
- Path points to non-existent file = CRITICAL
- Path uses wrong extension = HIGH

---

## Phase 3: Chart Compilation Test

### Objective
Execute ALL 49 chart.py scripts, verify PDFs generated with non-zero size, verify template compliance.

### Tasks

#### Task 3.1: Chart Inventory
(Same as before - all 49 charts listed)

#### Task 3.2: Chart Script Execution
**Command per chart:**
```bash
cd <chart_folder> && python chart.py 2>&1
```

**Capture:**
- Exit code (non-zero = CRITICAL)
- stdout/stderr
- Any matplotlib warnings
- File size of generated chart.pdf (0 bytes = CRITICAL)

#### Task 3.3: Chart Template Compliance (EXPANDED)

**Per chart.py, verify ALL of the following:**

| Requirement | Expected Value | Severity if Wrong |
|-------------|----------------|-------------------|
| `figure.figsize` | `(10, 6)` | CRITICAL |
| `figure.dpi` | `150` (in rcParams) | HIGH |
| `font.size` | `14` | HIGH |
| `axes.labelsize` | `14` | HIGH |
| `axes.titlesize` | `16` | HIGH |
| `xtick.labelsize` | `13` | HIGH |
| `ytick.labelsize` | `13` | HIGH |
| `legend.fontsize` | `13` | HIGH |
| `axes.spines.top` | `False` | CRITICAL |
| `axes.spines.right` | `False` | CRITICAL |

**savefig() Parameters:**
| Parameter | Expected Value | Severity if Wrong |
|-----------|----------------|-------------------|
| `dpi` | `300` | CRITICAL |
| `bbox_inches` | `'tight'` | CRITICAL |
| `facecolor` | `'white'` | CRITICAL |

**Color Palette Verification:**
| Color Name | Required Hex | Severity if Wrong |
|------------|--------------|-------------------|
| primary/MLPurple | `#3333B2` | CRITICAL |
| secondary/MLBlue | `#0066CC` | CRITICAL |
| accent/MLOrange | `#FF7F0E` | CRITICAL |
| success/MLGreen | `#2CA02C` | CRITICAL |
| danger/MLRed | `#D62728` | CRITICAL |
| lavender | `#ADADE0` | HIGH |

**Additional Checks:**
- Output file = `chart.pdf` in same directory = CRITICAL if wrong
- No subplots (ONE figure per script) = CRITICAL if violated
- No hardcoded absolute paths = HIGH if found

#### Task 3.4: Hardcoded Path Detection
**Grep for patterns:**
- `/home/` = HIGH
- `/Users/` = HIGH
- `C:\\` or `C:/` = HIGH
- `D:\\` or `D:/` = HIGH

---

## Phase 4: Placeholder/TODO Detection (NEW)

### Objective
Find ALL incomplete content markers.

### Tasks

#### Task 4.1: Grep All Files for Placeholders
**Patterns to find (case-insensitive):**
- `TODO`
- `FIXME`
- `XXX`
- `HACK`
- `PLACEHOLDER`
- `TBD`
- `Lorem ipsum`
- `...` (ellipsis in content, not code)
- `INSERT_`
- `CHANGE_`
- `UPDATE_`

**Severity:** HIGH for each occurrence

#### Task 4.2: Template Placeholder Detection
**Check .tex files for unfilled template markers:**
- `TOPIC_SHORT`
- `TOPIC_TITLE`
- `SUBTITLE`
- `FINANCE_CASE`
- `NEXT_TOPIC`

**Severity:** CRITICAL if found (indicates template not customized)

---

## Phase 5: Supporting File Verification (NEW)

### Objective
Verify all required supporting files exist and have content.

### Tasks

#### Task 5.1: Instructor Guide Verification
**Required:** Each topic must have `LXX_instructor_guide.md`

| Topic | File | Exists | Has Content (>100 bytes) |
|-------|------|--------|--------------------------|
| L01 | L01_instructor_guide.md | VERIFY | VERIFY |
| L02 | L02_instructor_guide.md | VERIFY | VERIFY |
| L03 | L03_instructor_guide.md | VERIFY | VERIFY |
| L04 | L04_instructor_guide.md | VERIFY | VERIFY |
| L05 | L05_instructor_guide.md | VERIFY | VERIFY |
| L06 | L06_instructor_guide.md | VERIFY | VERIFY |

**Severity:** HIGH if missing or empty

#### Task 5.2: Notebook Verification
**Required:** Each topic should have notebook in `notebooks/` folder

**Severity:** HIGH if missing

#### Task 5.3: manifest.json Consistency
**Verify:** All files listed in manifest.json actually exist

**Severity:** CRITICAL if manifest lists non-existent file

#### Task 5.4: URL Verification
**Check validity of:**
- Colab links (format: `https://colab.research.google.com/...`)
- GitHub URLs (format: `https://github.com/...`)

**Severity:** HIGH if URL format invalid

---

## Phase 6: Deficiency Report

### Objective
Comprehensive findings with severity ratings.

### Severity Definitions (FINAL)

| Level | Definition | Examples |
|-------|------------|----------|
| **CRITICAL** | Template specification violation | Wrong color format, missing footer, wrong chart width, compilation overflow |
| **HIGH** | Missing required content | No PMSP sections, no references, placeholders, compilation underfull |
| **MEDIUM** | Package deviation | Missing optional package |
| **LOW** | Minor inconsistency | Style preference |

### Deficiency Categories

1. **Template Non-Compliance (CRITICAL)**
   - Color format (RGB vs HTML)
   - Footer structure
   - Custom commands (\highlight, \mathbold)
   - \setbeamercolor commands
   - Navigation symbols

2. **Compilation Failures (CRITICAL/HIGH)**
   - Overfull hbox warnings
   - Underfull hbox warnings
   - Missing files

3. **Content Missing (HIGH)**
   - PMSP sections
   - Summary slides
   - References slides
   - Instructor guides

4. **Chart Width Violations (CRITICAL)**
   - ANY width other than 0.55 or 0.65

5. **Chart Template Violations (CRITICAL)**
   - Wrong savefig parameters
   - Wrong rcParams
   - Wrong color hex values

6. **Placeholder/TODO (HIGH)**
   - Incomplete content markers

---

## Phase 7: Per-Presentation JSON Inventories

### Objective
Create detailed inventory for each presentation with compliance status.

### Output Location
`.omc/inventories/`

### Inventory Schema (UPDATED)
```json
{
  "presentation": "L01_overview",
  "path": "slides/L01_Introduction_Linear_Regression/L01_overview.tex",
  "type": "overview",
  "audit_timestamp": "2026-01-28T12:00:00Z",
  "tolerance_mode": "ZERO",
  "compliance": {
    "overall": "PASS|PARTIAL|FAIL",
    "document_class": "PASS|FAIL",
    "theme": "PASS|FAIL",
    "colors": {
      "status": "PASS|FAIL",
      "format": "RGB|HTML",
      "case": "PascalCase|lowercase",
      "missing_colors": []
    },
    "packages": {
      "status": "PASS|FAIL",
      "missing": [],
      "extra": []
    },
    "footer": "PASS|FAIL",
    "custom_commands": {
      "bottomnote": "PASS|FAIL|WRONG_DEFINITION",
      "highlight": "PASS|FAIL|MISSING",
      "mathbold": "PASS|FAIL|MISSING"
    },
    "setbeamercolor": {
      "structure": "PASS|FAIL",
      "title": "PASS|FAIL",
      "frametitle": "PASS|FAIL"
    },
    "navigation_symbols": "PASS|FAIL",
    "title_info": {
      "title_short": "PASS|FAIL",
      "subtitle": "PASS|FAIL",
      "author": "PASS|FAIL",
      "institute": "PASS|FAIL",
      "date": "PASS|FAIL"
    }
  },
  "compilation": {
    "status": "PASS|FAIL",
    "overfull_warnings": [],
    "underfull_warnings": [],
    "errors": []
  },
  "content": {
    "frame_count": 20,
    "frame_count_status": "PASS|FAIL",
    "pmsp_sections": {
      "problem": true,
      "method": true,
      "solution": true,
      "practice": true
    },
    "decision_framework": true,
    "summary": true,
    "references": true,
    "bullet_violations": [
      {
        "frame": "Frame Title",
        "line": 115,
        "count": 5,
        "severity": "HIGH"
      }
    ],
    "chart_width_violations": [
      {
        "line": 45,
        "width": "0.50\\textwidth",
        "expected": "0.55\\textwidth or 0.65\\textwidth",
        "severity": "CRITICAL"
      }
    ]
  },
  "placeholders": [
    {
      "type": "TODO",
      "line": 23,
      "text": "TODO: Add example",
      "severity": "HIGH"
    }
  ],
  "charts": [
    {
      "folder": "01_simple_regression",
      "script_exists": true,
      "pdf_exists": true,
      "pdf_size_bytes": 12345,
      "last_compiled": "2026-01-28T10:00:00Z",
      "template_compliance": {
        "figsize": "PASS|FAIL",
        "dpi_rcparams": "PASS|FAIL",
        "dpi_savefig": "PASS|FAIL",
        "bbox_inches": "PASS|FAIL",
        "facecolor": "PASS|FAIL",
        "spines_top": "PASS|FAIL",
        "spines_right": "PASS|FAIL",
        "colors": "PASS|FAIL",
        "hardcoded_paths": "PASS|FAIL"
      }
    }
  ],
  "supporting_files": {
    "instructor_guide": "PASS|FAIL|MISSING",
    "notebook": "PASS|FAIL|MISSING"
  },
  "issues": [
    {
      "severity": "CRITICAL",
      "category": "template",
      "description": "Color format is HTML instead of RGB",
      "location": "line 17-21",
      "expected": "\\definecolor{MLPurple}{RGB}{51,51,178}",
      "actual": "\\definecolor{mlpurple}{HTML}{3333B2}"
    }
  ],
  "issue_summary": {
    "critical": 0,
    "high": 0,
    "medium": 0,
    "low": 0
  }
}
```

---

## Task Dependencies

```
Phase 1 (Template Audit)
    |
    v
Phase 1.5 (LaTeX Compilation) --+
    |                           |
    v                           |
Phase 2 (Content Scan) --------+
    |                           |
    v                           |
Phase 3 (Charts) --------------+
    |                           |
    v                           |
Phase 4 (Placeholders) --------+
    |                           |
    v                           |
Phase 5 (Supporting Files) ----+
    |                           |
    +---------------------------+
             |
             v
      Phase 6 (Report)
             |
             v
      Phase 7 (Inventories)
```

---

## Commit Strategy

1. **Commit 1:** Deficiency report (`.omc/reports/hostile_audit.md`)
2. **Commit 2:** JSON inventories (`.omc/inventories/*.json`)
3. **Commit 3:** Fixes (if authorized) - SEPARATE PR

---

## Success Criteria

1. All 12 presentations audited with ZERO tolerance
2. All 49 chart scripts tested for template compliance
3. LaTeX compilation verified with --strict flag
4. Every issue documented with:
   - Severity rating (CRITICAL/HIGH/MEDIUM/LOW only)
   - Location (file:line)
   - Expected vs actual
5. JSON inventory per presentation (updated schema)
6. Summary report with issue counts by severity
7. Placeholder/TODO detection complete
8. Supporting file verification complete

---

## Pre-Identified Critical Issues Summary (UPDATED)

### CRITICAL (Zero Tolerance Violations)
1. **Color Format Mismatch** (10 files): L02-L06 use HTML format instead of RGB
2. **Footer Missing** (10 files): L02-L06 lack custom footer structure
3. **\highlight Command Missing** (10 files): L02-L06
4. **\mathbold Command Missing** (10 files): L02-L06 (to verify)
5. **\setbeamercolor Commands Missing** (10 files): L02-L06 (to verify)
6. **Chart Width Violations** (multiple): Widths other than 0.55/0.65 = CRITICAL
7. **Compilation Overflow** (to verify): Any Overfull hbox = CRITICAL

### HIGH (Must Fix Before Release)
1. **Navigation Symbols Not Disabled** (10 files): L02-L06
2. **Summary Slides Missing** (5 files): L02-L06 overview presentations
3. **References Slides Missing** (5 files): L02-L06 overview presentations
4. **Package Inconsistencies**: inputenc, fontenc, hyperref missing
5. **Compilation Underfull** (to verify): Any Underfull hbox
6. **Placeholders/TODOs** (to verify): Any incomplete markers

### MEDIUM (Should Fix)
1. **\bottomnote Format Mismatch**: gray text vs italic text

### LOW (Minor)
1. **Date Field Empty**: L02-L06 have `\date{}`
2. **Author Format**: Combined author/institute string

---

## Execution Notes

- Run all phases in sequence
- Capture all output
- **ZERO TOLERANCE MODE ACTIVE**
- No issue is too minor to document
- All findings must be evidence-based
- "BORDERLINE" is not a valid severity
- "minor deviation" is not valid language
- "acceptable range" for chart widths is BANNED

---

PLAN_READY: .omc/plans/hostile-presentation-review.md
