---
id: beamer-slide-restructure
name: Universal Beamer Slide Restructure -- Structure, Content, Charts, Comics, Appendix + BSc Overlay
description: >
  Complete skill for restructuring university-level Beamer slides for any course
  and any subject. Covers three-zone architecture, audience-level adaptation
  (BSc/MSc/PhD), content depth scaling, chart creation (12 generalized types),
  domain application integration, comic/cartoon framing, notation consistency,
  flexible section frameworks (6 options), instructor guide integration, and
  topic-agnostic quality verification. Includes BSc Digital Finance course
  overlay with 7 accessibility rules and BSc-specific preamble.
source: Generalized from course-specific restructure + hostile reviews (Feb 2026)
triggers:
  - "restructure slides"
  - "create lecture"
  - "beamer slides"
  - "new lecture"
  - "add intro section"
  - "template layouts"
  - "move to appendix"
  - "visual variety"
  - "create chart"
  - "chart.py"
  - "slide content"
  - "university slides"
  - "academic lecture"
  - "course slides"
  - "assume no preknowledge"
  - "beginner friendly slides"
  - "BSc accessible"
  - "jargon definition"
  - "chart interpretation"
  - "formula worked example"
  - "student accessibility"
  - "no prior knowledge"
  - "accessible lecture"
  - "quiz questions"
  - "BSc preamble"
  - "BSc quiz alignment"
quality: v3 -- generalized + BSc overlay merged
---

# Universal Beamer Slide Restructure

## The Insight

Good academic slides need FOUR things working together: (1) **structure** -- zones that progress from engagement to rigor, (2) **content depth** -- matched to audience level with proofs, examples, and domain applications, (3) **visual density** -- charts in BOTH overview AND deepdive, governed by a minimum of 1 chart per 4 slides, and (4) **framing** -- comics/cartoons that open and close every lecture to engage and reinforce. Structure alone is necessary but not sufficient.

## Why This Matters

Hostile reviews of academic slides consistently score low for content gaps (insufficient depth, missing domain applications, no worked examples), NOT structural issues. A perfectly structured slide deck with shallow content still fails. And a rigorous deck without engagement hooks loses students in the first five minutes. The opening comic earns attention; the closing comic cements memory.

## Recognition Pattern

Apply when restructuring ANY university lecture, or when:
- Slides need a beginner-friendly intro followed by rigorous core
- Slides use only 2-3 layout patterns (needs visual variety)
- Advanced proofs clutter the main slide count (needs appendix)
- Deepdive is a wall of equations with no charts
- Domain applications are generic one-liners
- Lectures lack opening or closing engagement hooks (comics/cartoons)
- Content depth is mismatched to audience level

**IMPORTANT: Before restructuring any lecture, read the instructor guide (if one exists) for topic-specific build specifications, required derivations, mandatory charts, and domain application requirements.**

---

## PART 1: SLIDE STRUCTURE

### 1. Three-Zone Architecture

**Overview file (accessible, visual):**
```
INTRO (2-4 slides)            --> Problem motivation, where this fits, comic hook
CORE (variable by audience)   --> Formulas, examples, charts, evaluation
CLOSING (3-5 slides)          --> Exercises, decision guide, takeaways, closing comic
```

**Deepdive file (mathematical, detailed):**
```
MAIN BODY (variable)          --> Derivations, proofs, algorithms, diagnostics
\appendix
APPENDIX (variable)           --> Pure theory, historical context, advanced proofs
```

**Audience-scaling table:**
| Audience | Overview Slides | Deepdive Slides | Appendix Slides |
|----------|----------------|-----------------|-----------------|
| BSc      | 25-35          | 20-30           | 3-6             |
| MSc      | 22-28          | 30-40           | 6-10            |
| PhD      | 15-22          | 35-50           | 10-15           |

BSc lectures are longer because more explanation is needed; PhD lectures are shorter overviews with heavier deepdives. The comic requirement applies at ALL levels.

### 2. The Intro Section (2-4 Slides)

Every lecture MUST open with a relevant comic or cartoon. The intro should:
- **Slide 1:** Frame the specific problem this lecture solves (with comic/cartoon)
- **Slide 2:** Where this method/topic fits within the broader subject, and when it applies
- **Slide 3 (optional):** Key intuition using a concrete example with appropriate notation
- **Slide 4 (optional):** Road map for the lecture

**Audience-parameterized rules:**
| Audience | Intro Length | Notation Entry | Prerequisites |
|----------|-------------|----------------|---------------|
| BSc      | 3-4 slides  | Plain English first, then symbols gradually | Define ALL terms; assume no prior knowledge |
| MSc      | 2-3 slides  | Greek letters acceptable from slide 2 | Assume foundational knowledge of the field |
| PhD      | 2 slides    | Full notation from slide 1 | Assume deep background; jump to frontier quickly |

Rules for all levels:
- The lecture's key formula/concept should appear in simplified form by slide 3-4
- Do NOT spend slides on material covered in previous lectures (reference, don't re-teach)

### 3. Section Framework Options

Choose ONE framework for the overview. The deepdive MAY use topical sections but must cover equivalent content.

| Option | Framework | Best For | Core Sections |
|--------|-----------|----------|---------------|
| A | **PMSP** (Problem-Method-Solution-Practice) | Applied/methods courses | Intro, Problem, Method, Solution, Decision, Practice, Summary |
| B | **Conceptual** (Motivation-Theory-Evidence-Implications) | Theory courses | Intro, Motivation, Theory, Evidence, Implications, Summary |
| C | **Case-Based** (Context-Challenge-Analysis-Resolution) | Case study courses | Intro, Context, Challenge, Analysis, Resolution, Summary |
| D | **Custom** (user-defined sections) | Anything else | User defines sections to suit the material |
| E | **PBL** (Scenario-Investigation-Synthesis-Reflection) | Problem-based learning | Intro, Scenario, Investigation, Synthesis, Reflection, Summary |
| F | **Flipped** (PreWork Recap-Guided Practice-Application-Debrief) | Flipped classrooms | Intro, PreWork Recap, Guided Practice, Application, Debrief, Summary |

Every framework begins with an Introduction (2-4 slides with comic hook) and ends with a Summary (1 slide with closing comic + references).

**Section templates** (use these `\section{}` names in your `.tex` file):

Option A -- PMSP:
```latex
\section{Introduction}  \section{Problem}  \section{Method}  \section{Solution}
\section{Decision Framework}  \section{Practice}  \section{Summary}
```
Option B -- Conceptual:
```latex
\section{Introduction}  \section{Motivation}  \section{Theory}  \section{Evidence}
\section{Implications}  \section{Summary}
```
Option C -- Case-Based:
```latex
\section{Introduction}  \section{Context}  \section{Challenge}  \section{Analysis}
\section{Resolution}  \section{Summary}
```
Option E -- PBL:
```latex
\section{Introduction}  \section{Scenario}  \section{Investigation}
\section{Synthesis}  \section{Reflection}  \section{Summary}
```
Option F -- Flipped:
```latex
\section{Introduction}  \section{PreWork Recap}  \section{Guided Practice}
\section{Application}  \section{Debrief}  \section{Summary}
```

### 4. Layout Diversity (minimum 8 distinct patterns)

Map from your course's Beamer template:
| Layout | When to Use | Beamer Pattern |
|--------|-------------|----------------|
| Layout 3 (Two cols text) | Qualitative comparison | `\begin{columns}[T] \column{0.48\textwidth}` |
| Layout 4 (Two cols math) | Formula + explanation | Same columns with `$$...$$` |
| Layout 6 (Three-way split) | Taxonomy, 3 method variants | `\column{0.30\textwidth}` x3 |
| Layout 7 (Full width text) | Conceptual overview | No columns, just itemize |
| Layout 8 (Mixed media) | Text + image side by side | Column + `\includegraphics` |
| Layout 9 (Definition-Example) | Formula + worked example | Left=definition, Right=numbers |
| Layout 10 (Comparison) | Two approaches/methods | Left vs Right with headers |
| Layout 11 (Step-by-step) | Algorithm/process | Steps across two columns |
| Layout 12 (Formula reference) | Equation summary sheet | Three narrow columns |
| Layout 13 (Summary) | Key takeaways | Two columns: concepts + guidance |
| Layout 17 (Code example) | Implementation snippet | `\texttt{}` with code formatting |
| Layout 18 (Pros/Cons) | When to use a method | [+] advantages vs [-] disadvantages |
| Layout 20 (References) | Bibliography | Two columns of citations |
| Layout 21 (Full-size chart) | Chart-only slide | `\includegraphics[width=0.65\textwidth]` |
| Layout 22 (Chart + explanations) | Chart with interpretation | Chart 0.55\textwidth + itemize below |

### 5. The Appendix Mechanism

```latex
\appendix
\section*{Advanced Topics}  % STARRED: won't appear in \tableofcontents

\begin{frame}[t]
\vfill
\centering
\begin{beamercolorbox}[sep=8pt,center]{title}
\usebeamerfont{title}\Large Appendix: Advanced Topics and Proofs\par
\end{beamercolorbox}
\vfill
\end{frame}
```

### 6. Content Triage Decision

| Content Type | Goes To |
|---|---|
| Intuitive explanation, visual, worked example | Overview INTRO/CORE |
| Formula derivation, algorithm pseudocode | Deepdive MAIN |
| **Basic diagnostics** (residual plots, evaluation metrics, model checks) | **Deepdive MAIN** |
| **Model evaluation** (cross-validation, train-test split) | **Overview Solution + Deepdive MAIN** |
| **Inference** (hypothesis tests, confidence intervals, p-values) | **Deepdive MAIN** |
| Formal statistical tests (domain-specific) | Deepdive APPENDIX |
| Pure theory proofs (convergence, optimality, equivalences) | Deepdive APPENDIX |
| Historical context, theoretical connections | Deepdive APPENDIX |
| Redundant with other file | DROP (document in plan) |

**Key rule:** Diagnostics, evaluation, and inference are MAIN BODY content, not appendix.

---

## PART 2: CONTENT DEPTH

### 7. Audience-Level Adaptation

| Dimension | BSc | MSc | PhD |
|-----------|-----|-----|-----|
| Prerequisite check | Define ALL terms | Assume foundations | Assume deep background |
| Notation entry | Plain English first, then symbols gradually | Greek from slide 2 | Full notation from slide 1 |
| Proof depth | Show intuition, skip formal proofs | Show 2+ key derivations | Show all proofs, discuss limitations |
| Worked examples | 2+ per section, simple numbers | 1+ per section, realistic data | Optional, focus on edge cases |
| Domain applications | Real-world analogies | Industry worked examples | Research frontiers |
| Exercises | Guided, scaffolded | Open-ended, multi-step | Research-oriented |
| Intro length | 3-4 slides | 2-3 slides | 2 slides |
| Chart density | 1 per 4 slides; prefer intuitive viz | 1 per 4 slides; mix intuitive + diagnostic | 1 per 4 slides; favor diagnostic + frontier viz |
| Appendix depth | Light (3-6 slides): optional proofs, further reading only | Moderate (6-10 slides): proofs, convergence theory, historical context | Heavy (10-15 slides): full proofs, open problems, alternative formulations |
| Code/implementation | Full walkthrough with comments, copy-paste ready | Pseudocode + library snippets, not hand-held | Pseudocode only; assume students implement from spec |

### 8. Content Depth Checklist

Every lecture's content requirements scale by audience level:

**BSc:**

| Requirement | What It Means | Example |
|---|---|---|
| **0 formal derivations** | Show results, not proofs | State the formula, explain each term |
| **2+ intuitive explanations** | Build understanding without math | "Think of it as..." analogies |
| **2+ worked examples per section** | Numbers through every formula | 3 data points, compute step by step |
| **1+ real-world analogy** | Connect to everyday experience | "Like sorting mail into bins" |

**MSc:**

| Requirement | What It Means | Example |
|---|---|---|
| **2+ derivations/proofs** | Show the math, not just the result | Derive the update rule from the loss function |
| **1+ inference slide** | Hypothesis tests, CIs, p-values | Test significance of model parameters |
| **1+ worked numerical example** | Actual numbers through a formula | Matrix computation with realistic data |
| **1+ diagnostics section** | How to check model validity | Residual analysis, assumption verification |
| **1+ model evaluation slide** | Cross-validation, metric interpretation | Performance metrics on held-out test set |

**PhD:**

| Requirement | What It Means | Example |
|---|---|---|
| **3+ derivations/proofs** | Full mathematical treatment | Prove optimality, derive convergence rate |
| **Convergence analysis** | Formal rate discussion | Show O(1/t) convergence with proof sketch |
| **Open problems** | Current research frontiers | "It remains unknown whether..." |
| **Alternative formulations** | Multiple perspectives | Primal vs dual, Bayesian vs frequentist |

### 9. Notation Consistency Rules

Before writing either file, create a **notation table**:
```markdown
| Symbol | Meaning | Where Used |
|--------|---------|------------|
| \eta   | Learning rate | Update rule (deepdive) |
| \alpha | Significance level / mixing parameter | Inference / regularization |
| \lambda | Regularization strength | Penalty term |
| \beta  | Coefficients / parameters | Model definition |
```

Rules:
- Use `\eta` for learning rate (NOT `\alpha` -- avoids collision with significance level)
- If a symbol must be reused, add explicit disambiguation: "here $\alpha$ denotes the mixing parameter, not the significance level"
- Use consistent loss function naming: pick ONE convention and use it in both files
- Use `^\top` for transpose (not prime notation `'`)

### 10. Domain Application Requirements

Each lecture needs 2-3 slides of genuine domain application:

Rules:
- At least 1 application must include a **worked numerical example** with realistic data
- Generic one-liners ("[method] is used in [domain]") do NOT count
- The overview gets the intuitive application; the deepdive gets the mathematical detail
- Applications should demonstrate WHY the method matters for the course's target audience
- Non-quantitative courses may substitute timelines, concept maps, or formatted text for charts where a data visualization would be forced or artificial

Example domains (adapt to your course):
| Domain | Application Style |
|--------|-------------------|
| Finance | Risk models, portfolio optimization, credit scoring |
| Healthcare | Diagnostic models, survival analysis, drug discovery |
| Physics | Simulation, signal processing, particle classification |
| Humanities | Text analysis, network graphs, sentiment mining |
| Engineering | Control systems, quality assurance, predictive maintenance |

### 11. Bottomnote Quality

Bottomnotes should add VALUE not visible on the slide:
- **Good:** "Coefficients show marginal effect, holding others constant" (interpretation guidance)
- **Good:** "See [Textbook] Ch.3 for proof" (reference pointer)
- **Good:** "This bridges to [next topic] in the following lecture" (cross-lecture connection)
- **Bad:** Repeating text already on the slide
- **Bad:** Generic platitudes ("This is important")

---

## PART 3: COMICS AND VISUAL FRAMING

### 12. Comic/Cartoon Placement Rules

**HARD RULE: Every lecture MUST have a cartoon/comic in TWO positions:**

1. **OPENING:** Slide 1 or 2 of the Intro section (sets the tone, engages audience)
2. **CLOSING:** Final content slide before References (sends students off with a smile)

The opening comic FRAMES the lecture's problem.
The closing comic REFLECTS on the lecture's key insight or common pitfall.

This rule applies at ALL audience levels (BSc, MSc, PhD). Even a PhD seminar benefits from a well-chosen cartoon that makes a technical point memorable.

### 13. Comic Sources and Attribution

| Source | License | Attribution Format |
|--------|---------|-------------------|
| XKCD | CC BY-NC 2.5 | `\bottomnote{XKCD \#NNN by Randall Munroe (CC BY-NC 2.5)}` |
| PhD Comics | Permission required | `\bottomnote{PhD Comics by Jorge Cham, used with permission}` |
| The Oatmeal | Link-back required | `\bottomnote{The Oatmeal by Matthew Inman, theoatmeal.com}` |
| xkcd-style DIY | Original work | `\bottomnote{Original illustration}` |
| Instructor-made | Original work | No attribution needed |
| AI-generated | Varies by tool | `\bottomnote{Generated with [tool name]}` |

**PREFERRED:** XKCD (free, high quality, math/science/tech focus, CC licensed).
**FALLBACK for non-STEM:** PhD Comics (academia-universal), instructor-made cartoons.

**NOTE:** Syndicated comics (Calvin and Hobbes, etc.) require commercial licensing for educational slide use. Verify your institution's licensing agreements before including any syndicated content.

### 14. Opening Comic Guidelines

**Purpose:** Hook attention, frame the lecture's central question.
**Placement:** Slide 1 (after title) or Slide 2.
**Layout:** Layout 8 (mixed media) -- image 0.45\textwidth + 2-3 framing bullets in 0.55\textwidth column, OR full-width image.

Rules:
- The comic MUST relate to the lecture topic (not just "funny")
- Add 1-2 bullets below explaining the connection to today's topic
- Bottomnote includes attribution AND "This is the problem we solve today"

Selection criteria:
- Does this comic make the lecture's central question obvious?
- Would a student who sees ONLY this slide know what the lecture is about?
- Is it appropriate for the audience level and institutional context?

### 15. Closing Comic Guidelines

**Purpose:** Reinforce the key takeaway with humor, memorable exit.
**Placement:** Last content slide (before References) or second-to-last.
**Layout:** Same as opening -- Layout 8 or full-width.

Rules:
- The comic MUST relate to the lecture's conclusion or a common mistake
- Add 1-2 bullets: "Now you know why..." or "The takeaway: ..."
- Bottomnote: attribution + cross-reference to next lecture

Selection criteria:
- Does this comic reference something the students NOW understand?
- Does it reinforce the key insight or warn against a common pitfall?
- Would students share this comic after class? (engagement test)

Closing comic categories:
| Category | When to Use | Example Angle |
|----------|-------------|---------------|
| "Now you know" | After teaching a concept | Comic about the concept in the wild |
| "Common mistake" | After a nuanced method | Comic about doing it wrong |
| "Real-world irony" | After applied content | Comic about practice vs theory |
| "What's next" | When next lecture builds on this | Teaser for next topic |

---

## PART 4: CHARTS

### 16. Chart Architecture -- BOTH Files Need Charts

**GOVERNING RULE: Minimum 1 chart per 4 slides in each file.**

This is the ONLY chart count rule. Do not memorize fixed counts. Derive minimums from your slide count:
| File Length | Minimum Charts | Typical Lecture Type |
|-------------|----------------|----------------------|
| 15-20 slides | 4-5 charts | BSc overview, PhD overview |
| 22-28 slides | 6-7 charts | MSc overview |
| 30-40 slides | 8-10 charts | MSc deepdive, PhD deepdive |
| 40-50 slides | 10-13 charts | PhD deepdive with appendix visuals |

**Relaxation:** For derivation-heavy sections, 1 per 5 slides is acceptable if equations serve a single continuous proof. But 4+ consecutive formula slides with no chart MUST trigger adding a visualization.

**Chart roles across files:**
| Role | Overview Example | Deepdive Example |
|------|-----------------|------------------|
| Concept | Core relationship scatter | Multi-dimensional surface |
| Diagnostic | Residual/error patterns | Statistical test visualization |
| Algorithm | Process result | Convergence/iteration tracking |
| Evaluation | Performance curves | Cross-validation error curves |
| Comparison | Method A vs B (intuitive) | Parameter sensitivity analysis |
| Tradeoff | Bias-variance / precision-recall | Confidence/uncertainty bands |
| Decision | Flowchart | (not needed in deepdive) |

### 17. Chart Types Taxonomy (12 universal types)

| Type | Description | Use When | matplotlib Pattern |
|------|-------------|----------|-------------------|
| **Scatter + Fit** | Data points + model overlay | Showing model fit to data | `ax.scatter()` + `ax.plot()` |
| **Decision/Region Map** | Colored regions showing boundaries | Classification or segmentation | `ax.contourf()` + scatter |
| **Metric Curves** | Parameter vs performance metric | Tuning, evaluation | `ax.plot()` + `fill_between` |
| **Evaluation Curves** | ROC, PR, lift, calibration | Model assessment | `ax.plot()` with reference line |
| **Heatmap/Matrix** | 2D grid with color intensity | Confusion, correlation, distance | `ax.imshow()` + annotations |
| **Iterative Process** | Algorithm convergence over steps | Optimization, iterative methods | Arrows + contour background |
| **Cluster/Group Viz** | Points colored by group membership | Clustering, segmentation | `ax.scatter(c=labels)` |
| **Dimensionality Reduction** | 2D projection of high-dim data | Visualization of complex data | `ax.scatter()` with colormap |
| **Structure Diagram** | Trees, networks, architectures | Hierarchical/graph structures | `matplotlib.patches` + arrows |
| **Flowchart** | Decision guide (EVERY lecture) | Method selection, troubleshooting | `FancyBboxPatch` + arrows |
| **Bar/Distribution** | Frequency, comparison across groups | Categorical data, distributions | `ax.bar()` or `ax.hist()` |
| **Time Series** | Values over time with annotations | Temporal patterns, trends | `ax.plot()` + `ax.axvspan()` |

### 18. Chart.py Boilerplate

```python
"""[Title] - [One-line description]"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    "title": "Chart Title",
    "description": "What this chart shows",
    "url": "https://[COURSE_REPO]/slides/LXX_Topic/XX_name"
}

# MANDATORY rcParams
plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False
})

# MANDATORY color palette
MLPURPLE = '#3333B2'
MLBLUE   = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN  = '#2CA02C'
MLRED    = '#D62728'
MLLAVENDER = '#ADADE0'

np.random.seed(42)

# --- Data / model fitting ---
# --- Plotting ---
fig, ax = plt.subplots(figsize=(10, 6))
# ...
ax.grid(True, alpha=0.3)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
```

### 19. Chart Rules

| Rule | Value |
|------|-------|
| `figsize` | `(10, 6)` always |
| Save `dpi` | `300` |
| Spines | Top + right OFF |
| Output | `chart.pdf` only, one per folder |
| Subplots | NEVER (one figure, one ax) |
| Seed | `np.random.seed(42)` |
| Colors | ML palette only |
| URL | Bottom-right, 7pt gray |

### 20. Color Convention

| Color | Hex | Semantic Use |
|-------|-----|-------------|
| MLPURPLE | `#3333B2` | Primary model/result (fitted line, total error) |
| MLBLUE | `#0066CC` | Data points, secondary info (scatter, bias, Class A) |
| MLORANGE | `#FF7F0E` | Contrast/alternative (second model, variance, Class B) |
| MLGREEN | `#2CA02C` | Good/optimal (optimal point, correct predictions) |
| MLRED | `#D62728` | Bad/warning (errors, overfitting, misclassified) |
| MLLAVENDER | `#ADADE0` | Background/neutral (fill regions, flowchart questions) |

**NOTE:** The MLPURPLE/MLBLUE/etc. names are legacy from the original course where this skill was developed. They are semantic color names (primary, secondary, contrast, good, bad, neutral) that work for any subject. Renaming is optional -- the hex values and semantic roles are what matter.

### 21. Flowchart Pattern

```python
import matplotlib.patches as mpatches

def draw_box(ax, x, y, text, color, width=1.8, height=0.6):
    box = mpatches.FancyBboxPatch(
        (x - width/2, y - height/2), width, height,
        boxstyle="round,pad=0.05,rounding_size=0.1",
        facecolor=color, edgecolor='black', linewidth=1.5, alpha=0.8)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=10, fontweight='bold')

def draw_diamond(ax, x, y, text, color, size=0.8):
    diamond = mpatches.RegularPolygon(
        (x, y), numVertices=4, radius=size/1.4,
        facecolor=color, edgecolor='black', linewidth=1.5, alpha=0.8)
    ax.add_patch(diamond)
    ax.text(x, y, text, ha='center', va='center', fontsize=9, fontweight='bold')
```

- Diamonds (MLLAVENDER) = questions
- Green boxes = recommended, Orange = alternative, Red = wrong approach
- Always `ax.axis('off')` and `ax.set_aspect('equal')`
- Adjust `width`/`height` per topic complexity

### 22. Chart-Slide Integration

| Slide Layout | Chart Width | Additional Content |
|---|---|---|
| Layout 21 (chart-only) | `0.65\textwidth` | Title + bottomnote only |
| Layout 22 (chart + explanations) | `0.55\textwidth` | 2-3 bullet interpretation below |
| Layout 8 (mixed media) | `0.45\textwidth` | Text column beside it |
| Layout 10 + chart below | `0.50\textwidth` | Two comparison columns above |

If Overfull vbox: `\vspace{-2mm}` before `\begin{center}` or reduce to `0.60\textwidth`.

### 23. Chart Naming

```
XX_descriptive_name/
  chart.py
  chart.pdf
```

- `XX` = two-digit sequence (01-14+)
- Variants: `04a_variant_one`, `04b_variant_two`
- Every lecture ends with `XX_decision_flowchart`

---

## PART 5: BEAMER FORMATTING

### 24. Frame Rules

- ALL content frames: `\begin{frame}[t]{Title}`
- `\bottomnote{}` on every content slide
- Max 3-4 bullets per column (NEVER exceed 4)
- Comic/cartoon images: attribution in bottomnote (see Section 13)
- Two-column: `\begin{columns}[T] \column{0.48\textwidth}`
- Three-column: `\begin{columns}[T] \column{0.30\textwidth}`
- Column headers: `\textbf{\textcolor{MLBlue}{Header}}`
- Preamble: ALWAYS preserve from current file (NEVER copy from template files)

### 25. Pseudocode Guidelines

When the lecture includes algorithms or formal procedures, use the `algorithmic` environment for formal pseudocode:

```latex
\begin{algorithmic}[1]
\REQUIRE Input data, parameters
\ENSURE Output
\STATE Initialize...
\WHILE{not converged}
  \STATE Update step
  \IF{edge case}
    \STATE Handle it
  \ENDIF
\ENDWHILE
\RETURN result
\end{algorithmic}
```

Every pseudocode block MUST include:
- Initialization step
- Main loop with convergence criterion
- Edge case handling (edge cases specific to the algorithm: empty sets, ties, division by zero, boundary conditions)

Use Layout 11 (Step-by-step) for informal process descriptions; `algorithmic` for formal pseudocode.

---

## PART 6: PLAN CHECKLIST

Before executing, verify the plan has:

### 26. Structure
- [ ] Slide-by-slide spec with layout, content, chart ref, bottomnote
- [ ] Section framework chosen and applied (PMSP, Conceptual, Case-Based, PBL, Flipped, or Custom)
- [ ] Intro is 2-4 slides (audience-adjusted)
- [ ] Opening comic/cartoon specified for intro
- [ ] `\appendix` + `\section*` in deepdive (if deepdive exists)
- [ ] Slide count arithmetic verified against audience-scaling table

### 27. Content Depth
- [ ] Derivations/proofs appropriate for audience level (see Section 8 depth table)
- [ ] Worked numerical examples appropriate for audience level
- [ ] Diagnostics/evaluation in deepdive MAIN body (not appendix)
- [ ] Notation table with no symbol collisions

### 28. Charts
- [ ] Chart allocation table (each chart in exactly ONE file)
- [ ] Minimum 1 chart per 4 slides in each file (governing rule)
- [ ] No chart dual-assignment across files
- [ ] Chart types selected from the 12-type taxonomy

### 29. Domain Applications
- [ ] 2-3 domain application slides with worked example
- [ ] Applications are genuine (not generic one-liners)
- [ ] At least 1 application includes realistic numerical data

### 30. Comics
- [ ] Opening comic/cartoon in EVERY lecture (slide 1-2)
- [ ] Closing comic/cartoon in EVERY lecture (before References)
- [ ] Attribution in bottomnote for EVERY comic
- [ ] Comics relate to lecture content (not arbitrary humor)

### 31. Quality
- [ ] Layout usage summary (8+ distinct patterns)
- [ ] "Deliberately Dropped Content" table
- [ ] Bottomnotes add value (not just echoing slide text)
- [ ] Instructor guide consulted before restructuring (if available)

---

## PART 7: GOTCHAS

### 32. Common Pitfalls

1. **Chart dual-assignment trap.** A chart is assigned to both overview and deepdive. ALWAYS cross-check the allocation table vs `\includegraphics` references.

2. **Slide count arithmetic drift.** Totals are correct but breakdowns are wrong. Verify: title/outline + intro + core + closing = total.

3. **`\section*` after `\appendix`.** Use starred form to hide from `\tableofcontents`.

4. **Overfull vbox on chart-only slides.** Fix with `\vspace{-2mm}` or reduce to `0.60\textwidth`.

5. **Preamble preservation.** NEVER copy preamble from template files. Preserve existing preamble byte-for-byte.

6. **Merging 3+ slides into 1.** Flag as overflow risk. Give the executor permission to split back if needed.

7. **Intro length.** 2-4 slides (adjust by audience level: BSc may need 3-4, PhD may need only 2). Longer intros waste time for advanced audiences; shorter intros lose beginners.

8. **Deepdive wall of equations.** If a section has 4+ consecutive formula slides with no chart, add a visualization.

9. **Diagnostics in main body.** Basic diagnostics (method-appropriate) are CORE content. Only formal statistical tests go in appendix.

10. **Notation collisions.** Create notation table before writing. Never use the same symbol for two different quantities without explicit disambiguation.

11. **Missing closing comic.** Opening comics are natural; closing comics get forgotten. Build the closing comic into the plan from the start, not as an afterthought.

12. **Audience level drift.** A BSc lecture that slips into MSc notation mid-deck loses students. A PhD lecture that over-explains basics wastes time. Pick a level and hold it throughout.

13. **Generic domain applications.** "[Method] is used in [field]" is not an application. A worked example with realistic numbers IS an application. If you cannot produce specific numbers, you do not have a real application.

---

## APPENDIX A: Instructor Guide Template

Add a "Slide Build Specification" section to each lecture's instructor guide:
```markdown
## Slide Build Specification
### Required Content
- Intro key formula: [formula in simple notation]
- Must-have derivations: [list of proofs/derivations for deepdive]
- Must-have inference: [hypothesis tests, confidence intervals if applicable]
### Chart Requirements
- [Chart name]: [description, which file (overview/deepdive)]
### Pseudocode Requirements
- [Algorithm name]: [key edge cases to handle]
(omit section if lecture has no algorithmic content)
### Domain Applications
- [Application]: [description, worked example required?]
### Appendix Content
- [Topic]: [what goes in appendix vs main body]
```

This bridges the universal skill (HOW to structure) with topic-specific knowledge (WHAT to include).

---

## APPENDIX B: Course Overlay Convention

A course-specific skill can EXTEND this universal skill using the overlay pattern:
```yaml
---
id: [course-specific-id]
extends: beamer-slide-restructure
name: [Course-Specific] Overlay
description: >
  Course-specific overrides for [Course Name]. Extends the universal
  beamer-slide-restructure skill with [course-specific] rules.
triggers:
  - [course-specific triggers ONLY -- shared triggers belong to universal skill]
---
```

**The overlay file should contain ONLY:**
1. Course-specific preamble (if different from universal patterns)
2. Course-specific accessibility rules (e.g., BSc no-Greek-letters rule)
3. Course-specific quality checks (e.g., quiz alignment)
4. Course-specific audience assumptions

**The overlay should NOT duplicate:** Three-zone architecture, layout diversity, chart boilerplate, comic/cartoon rules, Beamer formatting, notation consistency, or plan checklist -- all of these live in the universal skill.

When both skills are active, the overlay SUPPLEMENTS universal defaults. Where they conflict, the overlay takes precedence for its specific course.

---

## APPENDIX C: BSc Digital Finance Course Overlay

> **NOTE:** This appendix contains BSc-specific rules for the Economics of Digital Finance course.
> These rules override or supplement the universal defaults in Parts 1-7 above.
> Use this as both a working overlay AND as an example of how to create course-specific overlays per Appendix B.

## BSc-Specific Preamble

This is the EXACT preamble for the Economics of Digital Finance course (BSc). Copy verbatim when creating new lectures.

### Full Preamble (copy exactly)

```latex
\documentclass[8pt,aspectratio=169]{beamer}
\usetheme{Madrid}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{adjustbox}
\usepackage{multicol}
\usepackage{amsmath}

% Color definitions
\definecolor{mlblue}{RGB}{0,102,204}
\definecolor{mlpurple}{RGB}{51,51,178}
\definecolor{mllavender}{RGB}{173,173,224}
\definecolor{mllavender2}{RGB}{193,193,232}
\definecolor{mllavender3}{RGB}{204,204,235}
\definecolor{mllavender4}{RGB}{214,214,239}
\definecolor{mlorange}{RGB}{255, 127, 14}
\definecolor{mlgreen}{RGB}{44, 160, 44}
\definecolor{mlred}{RGB}{214, 39, 40}
\definecolor{mlgray}{RGB}{127, 127, 127}

\definecolor{lightgray}{RGB}{240, 240, 240}
\definecolor{midgray}{RGB}{180, 180, 180}

% Apply custom colors to Madrid theme
\setbeamercolor{palette primary}{bg=mllavender3,fg=mlpurple}
\setbeamercolor{palette secondary}{bg=mllavender2,fg=mlpurple}
\setbeamercolor{palette tertiary}{bg=mllavender,fg=white}
\setbeamercolor{palette quaternary}{bg=mlpurple,fg=white}

\setbeamercolor{structure}{fg=mlpurple}
\setbeamercolor{section in toc}{fg=mlpurple}
\setbeamercolor{subsection in toc}{fg=mlblue}
\setbeamercolor{title}{fg=mlpurple}
\setbeamercolor{frametitle}{fg=mlpurple,bg=mllavender3}
\setbeamercolor{block title}{bg=mllavender2,fg=mlpurple}
\setbeamercolor{block body}{bg=mllavender4,fg=black}

\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{itemize items}[circle]
\setbeamertemplate{enumerate items}[default]
\setbeamersize{text margin left=5mm,text margin right=5mm}

\newcommand{\bottomnote}[1]{%
\vfill
\vspace{-2mm}
\textcolor{mllavender2}{\rule{\textwidth}{0.4pt}}
\vspace{1mm}
\footnotesize
\textbf{#1}
}
```

### Title Block Pattern (BSc Course)

```latex
\title{[Topic Name] in Digital Finance}
\subtitle{L0X: [Motivating hook question or statement]}
\author{Economics of Digital Finance}
\institute{BSc Course}
\date{}
```

The `\subtitle` MUST contain a motivating hook, not a dry description. Examples:
- L01: `Understanding the trillion-dollar shift from cash to code`
- L02: `Can Bitcoin replace the dollar? What monetary theory tells us.`
- L06: `When you swap ETH for USDC on Uniswap, who sets the price---and who profits?`

---

## BSc Intro Rules (Override Universal Defaults)

The intro section (8-10 slides) MUST be genuinely accessible:

1. **No Greek letters** (no beta, alpha, epsilon)
2. **No matrix notation** (no X, bold symbols)
3. Only formula allowed: simple notation (e.g., `y = a + bx` using a,b not beta)
4. Use **everyday examples** (spam filters, Netflix, house prices, remittance costs)
5. Start with "What is [topic]?" not "Learning Objectives"
6. Use visual hooks (XKCD comics, memorable images) on the first content slide
7. End with a "Road Map" slide transitioning to the core
8. **Length:** 8-10 slides for BSc (not 4-6 as in MSc courses)

---

## Content Accessibility (7 BSc-Specific Rules)

These rules emerged from remediating 191 issues across 8 BSc lectures. Distribution:
- 38% Jargon (terms without definitions)
- 15% Chart References (charts without interpretation)
- 14% Formula Clarity (formulas without worked examples)
- 13% Missing Context (no motivation or real-world anchors)
- 8% Density (too many concepts per slide)
- 6% Logical Gaps (prerequisites assumed, never stated)
- 6% Assumed Knowledge (domain expertise taken for granted)

### Rule 1: EVERY Jargon Term Gets a Parenthetical at First Use

**Pattern:** `term (plain English explanation)`

```latex
% BAD
\item Blockchain enables disintermediation and re-intermediation

% GOOD
\item Blockchain enables disintermediation (removing middlemen)
  or re-intermediation (replacing old middlemen with new digital
  ones like crypto exchanges)
```

**Decision heuristic:** If a term would not appear in a high school newspaper, it needs a parenthetical. When in doubt, define it.

Common traps:
- **Acronyms** (MoE, UoA, EMH, AMM, DEX, OLS, MLE) -- expand at first use
- **Ticker symbols** (BTC, ETH, USDT) -- add full name
- **Academic jargon disguised as plain English** ("welfare effects", "adverse selection", "outside option", "friction")
- **Cross-lecture forward references** (term used in L01 but defined in L02 -- add inline definition anyway)
- **Domain-specific verbs** ("hedge", "arbitrage", "short") -- define the action

### Rule 2: EVERY Formula Gets a Worked Numerical Example

**Pattern:** `\smallskip\textbf{Example:}` block with concrete numbers

```latex
% BAD
$$MV = PY$$

% GOOD
$$MV = PY$$
\smallskip\textbf{Example:} If money supply $M{=}\$100$,
velocity $V{=}2$, and output $Y{=}100$ units, then price
level $P = MV/Y = \$2$. If $M$ doubles to \$200, $P$
doubles to \$4 --- this is how ``printing money'' causes inflation.
```

**Decision heuristic:** A formula without numbers is a formula students will skip. Always:
1. Define every variable explicitly (even if "obvious")
2. Pick realistic parameter values -- sanity-check against real-world data
3. Show the substitution step, not just the answer
4. Connect the result to an intuition ("this means...")

**Parameter realism traps:**
- Financial volatility: sigma ~0.01-0.02, not 0.1
- Cost/price examples: use round numbers ($100, not $137.42)
- Model answers: always verify by plugging back into formula

### Rule 3: EVERY Chart-Only Slide Gets 2-3 Interpretive Bullets

**Pattern:** Bullets BELOW the `\includegraphics` line

```latex
% BAD
\begin{frame}{Network Effects}
\includegraphics[width=0.6\textwidth]{chart.pdf}
\end{frame}

% GOOD
\begin{frame}{Network Effects}
\includegraphics[width=0.55\textwidth]{chart.pdf}
\begin{itemize}
  \item The S-curve shows slow adoption initially, then explosive growth
        after reaching a ``tipping point'' (around 16\% market share)
  \item Notice how the curve flattens at the top --- this is market saturation
  \item \textbf{Key insight:} Early platforms must subsidize users to reach
        the tipping point; after that, growth becomes self-sustaining
\end{itemize}
\end{frame}
```

**The three bullets must answer:**
1. **What am I looking at?** (axes, units, what each line/color represents)
2. **What pattern should I notice?** (the shape, the trend, the surprise)
3. **So what?** (the economic/practical takeaway)

**Chart-text alignment:** Bottomnotes must describe what the chart ACTUALLY shows, not what you WISH it showed. Always read chart.py before writing interpretation.

### Rule 4: MAX 5-6 Concepts Per Slide (Split at 8+)

**Pattern:** `\end{frame}\begin{frame}{Same Title (cont.)}`

```latex
% BAD - 16 bullet points on one slide
\begin{frame}{Understanding Systemic Risk Channels}
  % ... 16 items crammed together
\end{frame}

% GOOD - split into two focused slides
\begin{frame}{Systemic Risk Channels (1/2): Traditional}
  % ... 8 items about traditional channels
\end{frame}
\begin{frame}{Systemic Risk Channels (2/2): Digital Amplifiers}
  % ... 8 items about digital-specific channels
\end{frame}
```

**Decision heuristic:** Count distinct concepts (not bullet points). If >8 concepts, split. Group by theme, not arbitrary midpoint.

Special cases for BSc:
- **Key Terms slides** with 20+ terms: split into 2-3 themed groups of ~10
- **Case study slides** with 3+ cases: split into 1-2 cases per slide
- **Formula-heavy slides**: one formula + example per slide maximum

### Rule 5: Charts Must Exist AND Be Referenced

**Orphaned charts** (files on disk never shown in slides) are invisible wasted effort.

**Audit pattern:**
1. List all `\includegraphics` in the .tex file
2. List all chart.pdf files in subdirectories
3. Any chart.pdf not in an `\includegraphics` -> needs a new slide
4. Any `\includegraphics` pointing to a nonexistent file -> broken reference

### Rule 6: Quiz Questions Must Reference Actual Content

**The catastrophic failure:** A lecture had 60% of quiz questions referencing scenarios, axes, and instruments that didn't exist in slides or charts. Students lose all trust.

**Verification checklist:**
- [ ] Every question references a concept in the .tex slides
- [ ] Every chart-based question uses ACTUAL axes/labels from chart.py
- [ ] Answer explanations cite specific slide content
- [ ] Zero references to content from drafts that didn't make it into final slides
- [ ] Questions test reasoning ("What would happen if...") not memorization ("What year was...")
- [ ] Even distribution across topics (e.g., 4 questions per topic for 20 questions across 5 topics)

**Root cause:** Quiz questions written from the lecture PLAN, not the final slides. Always write/review quiz AFTER finalizing slides.

### Rule 7: Cross-References and Real-World Anchors

```latex
% BAD
\item Gresham's Law applies to cryptocurrency markets

% GOOD
\item Gresham's Law (``bad money drives out good'') applies when
  exchange rates are fixed. In crypto there is no fixed rate, but
  the \textbf{analog} is similar: users spend stablecoins (whose
  value doesn't rise) and hoard Bitcoin (hoping it appreciates)
```

**Anchoring heuristics for BSc:**
- **Title slides** need a motivating hook question ("Can Bitcoin replace the dollar?")
- **Every lecture** should have at least one memorable real-world data point
- **Cross-reference** related lectures explicitly ("See L03 for how CBDCs address this")
- **Acknowledge** when an analogy breaks down -- students respect honesty
- **Simulated data caveats:** If a chart shows modeled data (not real), say so explicitly

---

## BSc-Specific Gotchas

**Gotcha 7: Quiz-Slide Drift**
Quiz questions written from the lecture PLAN reference content that changed or was cut. Always write quiz AFTER finalizing slides.

**Gotcha 8: Chart Annotation Language**
Use student-friendly terms in chart annotations ("Tipping point" not "Saddle-node bifurcation"). Chart.py annotations appear directly in the PDF -- they bypass all LaTeX accessibility layers.

**Gotcha 9: Trilemma/Axis Consistency**
When a chart uses specific axis labels, ALL downstream references (slides, quiz, exercises, glossary) must use the SAME labels. One mismatch propagates confusion everywhere.

**Gotcha 10: Order Book Step Functions**
Must use step functions (`ax.step()`), not line plots (`ax.plot()`). Continuous lines misrepresent discrete order books.

---

## Remediation Workflow (BSc Course)

When remediating existing BSc lectures:

1. **Analyze:** Read every slide, categorize issues by the 7 accessibility types
2. **Prioritize:** HIGH = missing definitions on core concepts, broken chart references, wrong quiz answers. MEDIUM = missing worked examples, chart-only slides. LOW = title hooks, cross-references.
3. **Fix surgically:** Add accessibility layers ON TOP of existing content. Never rewrite entire slides. Never remove academic rigor -- only add explanations.
4. **Verify:** Compile LaTeX, spot-check 10% of fixes across all categories, confirm quiz questions match actual content.

**Parallel execution pattern:** Assign one agent per lecture file. Zero file overlap guarantees no merge conflicts.
