# Plan: Generalize beamer-slide-restructure Skill

## Context

### Original Request
Transform the course-specific skill at `.omc/skills/beamer-slide-restructure.md` (508 lines, 7 parts) into a universal Beamer slide creation skill usable for ANY university course, ANY subject, ANY audience level, and ANY number of lectures. Additionally, enforce a hard requirement: every lecture MUST have a cartoon/comic at the beginning AND at the end.

### Source Analysis
The current skill was learned from restructuring L01 slides for an MSc Data Science "Methods and Algorithms" course. It contains:
- **Universal patterns** (Beamer formatting, three-zone architecture, chart creation, layout diversity) that apply to any academic slide deck
- **Course-specific patterns** (PMSP framework, L01-L06 topic guides, finance applications, ML chart types) that must be generalized or removed
- **Audience-specific patterns** (MSc-level assumptions like "Greek letters are fine after slide 1") that must become parameterized

### Reference Files
- Current skill: `D:\Joerg\Research\slides\Methods_and_Algorithms\.omc\skills\beamer-slide-restructure.md`
- Global skill copy: `C:\Users\OsterriederJRO\.claude\skills\omc-learned\beamer-slide-restructure.md`
- Companion BSc skill (to become overlay): `C:\Users\OsterriederJRO\.claude\skills\omc-learned\slide-creation.md`
- Beamer template: `D:\Joerg\Research\slides\Methods_and_Algorithms\templates\beamer_template.tex`
- Instructor guides: `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L0X_Topic\L0X_instructor_guide.md`

### Coexistence Architecture (Architect Recommendation)
The generalized `beamer-slide-restructure.md` becomes the **universal skill** with all shared infrastructure (three-zone architecture, layout diversity, chart creation, formatting). The BSc-focused `slide-creation.md` becomes a **slim overlay** (~250 lines) containing ONLY BSc-specific overrides (7 accessibility rules, no-Greek-letters intro, BSc preamble, quiz alignment). Shared triggers ("restructure slides", "create chart") belong to the universal skill only. The BSc overlay activates on BSc-specific triggers only ("assume no preknowledge", "beginner friendly", "BSc accessible", etc.).

---

## Work Objectives

### Core Objective
Rewrite `beamer-slide-restructure.md` as a generalized, parameterized skill that an agent with zero knowledge of the original course can apply to any university lecture series. Simultaneously, migrate topic-specific content to instructor guides, slim the BSc companion skill to an overlay, and deploy the skill to both local and global paths.

### Deliverables
1. Rewritten universal skill file at `.omc/skills/beamer-slide-restructure.md` (overwrite in place)
2. Global copy at `C:\Users\OsterriederJRO\.claude\skills\omc-learned\beamer-slide-restructure.md`
3. Slimmed overlay at `C:\Users\OsterriederJRO\.claude\skills\omc-learned\slide-creation.md`
4. Updated instructor guides (L01-L06) with "Slide Build Specification" sections
5. Same single-file format for skill, approximately 500-700 lines

### Definition of Done
- No references to L01-L06, finance, ML algorithms, PMSP, or "Methods and Algorithms"
- Parameterized placeholders for course name, audience level, subject domain, lecture count
- Cartoon/comic requirement at BOTH beginning AND end of every lecture
- Audience-level adaptation guidance (BSc through PhD) with chart density, appendix depth, and code expectations
- All universal Beamer patterns preserved
- Topic-specific content migrated to instructor guides (not lost)
- BSc overlay uses `extends: beamer-slide-restructure` convention
- An agent reading ONLY this skill can create slides for a philosophy course, a physics course, or a biology course

---

## Must Have / Must NOT Have

### MUST Have
- Three-zone architecture (Intro, Core, Appendix) -- universal
- Layout diversity rules (8+ patterns) -- universal
- Chart creation boilerplate (rcParams, colors, figsize, single figure) -- universal
- Chart-slide integration rules (widths, layouts) -- universal
- Beamer formatting rules (frame options, bottomnote, columns) -- universal
- Notation consistency rules -- universal
- Content triage decision table -- universal (but with generalized categories)
- Appendix mechanism with `\section*` -- universal
- Flowchart pattern code -- universal
- Gotchas section -- universal
- Plan checklist -- universal
- **NEW:** Cartoon/comic at beginning AND end of every lecture
- **NEW:** Audience-level parameter with specific adaptation rules (including chart density, appendix depth, code expectations)
- **NEW:** Subject-domain parameter with example applications
- **NEW:** Section structure templates with 6 framework options (PMSP, Conceptual, Case-Based, Custom, PBL, Flipped)
- **NEW:** Generalized chart type taxonomy (not ML-specific)
- **NEW:** Chart density governed by "1 per 4 slides" rule only (no separate chart count parameter)
- **NEW:** "Read instructor guide before restructuring" rule
- **NEW:** Instructor guide template for slide build specifications
- **NEW:** `extends:` convention for course overlays

### MUST NOT Have
- L01-L06 topic-specific adaptation section (Part 6 migrated to instructor guides)
- Finance application requirements (Section 9 removed entirely)
- PMSP section names hardcoded as the only option
- "MSc Data Science" hardcoded as audience
- References to specific ML algorithms (sigmoid, KNN, K-Means, Random Forest, PCA, t-SNE, RL)
- References to specific finance concepts (Basel, CAPM, yield curve, scorecards)
- References to `template_beamer_final.tex` (use "your course's Beamer template" instead)
- The global skill's BSc-specific patterns (those stay in the slimmed overlay)
- Dilbert as a recommended comic source (licensing issues)

---

## Task Flow and Dependencies

```
Task 1 (audit) --> Task 2 (skeleton) --> Task 3 (Part 1) --> Task 4 (Part 2) --> Task 5 (Part 3) --> Task 6 (Part 4) --> Task 7 (Part 5) --> Task 8 (Part 6) --> Task 9 (Part 7) --> Task 10 (assembly) --> Task 11 (verify)
                                                                                                                                                                                                                          |
Task 12 (migrate to instructor guides) -- can run in parallel with Tasks 3-9, must complete before Task 11
Task 13 (global copy) -- runs after Task 10
Task 14 (slim BSc overlay) -- runs after Task 10, before Task 11
```

Tasks 3-9 are sequential (each part builds on the previous).
Task 12 (instructor guide migration) is independent and can run in parallel with Tasks 3-9.
Tasks 13-14 depend on Task 10 (complete skill file must exist first).
Task 11 (verification) depends on ALL other tasks.

---

## Detailed TODOs

### Task 1: Line-by-Line Audit of Current Skill
**Agent:** executor (sonnet)
**Input:** Current skill file at `D:\Joerg\Research\slides\Methods_and_Algorithms\.omc\skills\beamer-slide-restructure.md`
**Output:** Audit saved to `D:\Joerg\Research\slides\Methods_and_Algorithms\.omc\plans\skill-generalization-audit.md`
**Action:** Read every line and classify each section/paragraph/table-row as:
- KEEP (universal, no changes needed)
- GENERALIZE (universal concept, but uses course-specific examples)
- REPLACE (course-specific, needs a parameterized alternative)
- REMOVE (purely course-specific, no general equivalent)
- MIGRATE (topic-specific content to move to instructor guides)

**Acceptance Criteria:** Written audit table covering all 508 lines, section by section. Output saved to `.omc/plans/skill-generalization-audit.md`.

### Task 2: Write the New Skill Skeleton (YAML Front Matter + Part Headings)
**Agent:** executor (sonnet)
**Action:** Write the new file structure with:

**YAML front matter changes:**
```yaml
---
id: beamer-slide-restructure
name: Universal Beamer Slide Restructure -- Structure, Content, Charts, Comics, Appendix
description: >
  Complete skill for restructuring university-level Beamer slides for any course
  and any subject. Covers three-zone architecture, audience-level adaptation
  (BSc/MSc/PhD), content depth scaling, chart creation (12 generalized types),
  domain application integration, comic/cartoon framing, notation consistency,
  flexible section frameworks (6 options), instructor guide integration, and
  topic-agnostic quality verification.
source: Generalized from MSc ML/finance restructure + hostile reviews (Feb 2026)
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
quality: v3 -- generalized from v2 course-specific skill
---
```

**New Part structure with full section numbering:**
```
# Universal Beamer Slide Restructure

## The Insight (generalized)
## Why This Matters (generalized)
## Recognition Pattern (generalized)

## PART 1: SLIDE STRUCTURE
  1. Three-Zone Architecture (kept, audience-adapted)
  2. The Intro Section (kept, with comic requirement)
  3. Section Framework Options (NEW -- 6 options replacing PMSP-only)
  4. Layout Diversity (kept as-is)
  5. The Appendix Mechanism (kept as-is)
  6. Content Triage Decision (generalized)

## PART 2: CONTENT DEPTH (generalized by audience level)
  7. Audience-Level Adaptation (NEW -- replaces MSc-only, includes chart density, appendix depth, code expectations)
  8. Content Depth Checklist (parameterized by level)
  9. Notation Consistency Rules (kept as-is)
  10. Domain Application Requirements (NEW -- replaces finance-only)
  11. Bottomnote Quality (kept as-is)

## PART 3: COMICS AND VISUAL FRAMING (NEW)
  12. Comic/Cartoon Placement Rules
  13. Comic Sources and Attribution
  14. Opening Comic Guidelines
  15. Closing Comic Guidelines

## PART 4: CHARTS (kept, generalized types)
  16. Chart Architecture (density-rule-only, no fixed counts)
  17. Chart Types Taxonomy (generalized 12-type from ML-specific)
  18. Chart.py Boilerplate (kept, URL generalized)
  19. Chart Rules (kept as-is)
  20. Color Convention (kept, with legacy naming note)
  21. Flowchart Pattern (kept as-is)
  22. Chart-Slide Integration (kept as-is)
  23. Chart Naming (kept as-is)

## PART 5: BEAMER FORMATTING (kept as-is)
  24. Frame Rules (kept as-is)
  25. Pseudocode Guidelines (kept, generalized)

## PART 6: PLAN CHECKLIST (generalized, numbered)
  26. Structure Checklist
  27. Content Depth Checklist
  28. Charts Checklist
  29. Domain Applications Checklist
  30. Comics Checklist
  31. Quality Checklist

## PART 7: GOTCHAS (kept + new gotchas)
  32. Gotchas 1-13 (numbered)

## APPENDICES
  A. Instructor Guide Template (for Slide Build Specification)
  B. Course Overlay Convention (extends: mechanism)
```

**Acceptance Criteria:** Skeleton file written with all part headings, section numbers through Parts 6-7, and appendices. Content is placeholder only.

### Task 3: Write PART 1 -- SLIDE STRUCTURE
**Agent:** executor (sonnet)
**Action:** Rewrite Part 1 with these specific changes:

**Section 1 (Three-Zone Architecture):** KEEP the zone structure. CHANGE the slide counts to be parameterized:
```
Overview file ({AUDIENCE_ADJUSTED} slides):
  INTRO (2-4 slides)  --> Problem motivation, where this fits, comic hook
  CORE (variable)     --> Formulas, examples, charts, evaluation
  CLOSING (3-5 slides) --> Exercises, decision guide, takeaways, closing comic

Deepdive file ({AUDIENCE_ADJUSTED} slides):
  MAIN BODY (variable) --> Derivations, proofs, algorithms, diagnostics
  \appendix
  APPENDIX (variable)  --> Pure theory, historical context, advanced proofs
```

Add an audience-scaling table:
```
| Audience  | Overview Slides | Deepdive Slides | Appendix Slides |
|-----------|----------------|-----------------|-----------------|
| BSc       | 25-35          | 20-30           | 3-6             |
| MSc       | 22-28          | 30-40           | 6-10            |
| PhD       | 15-22          | 35-50           | 10-15           |
```

**Section 2 (Intro Section):** KEEP the 2-4 slide rule. ADD the opening comic requirement:
- Slide 1: Frame the problem with a COMIC/CARTOON (not just "compelling visual")
- Explicitly state: "Every lecture MUST open with a relevant comic"

GENERALIZE the audience assumptions:
- Replace "MSc Data Science. They know what ML is" with a parameterized rule:
  - BSc: Define all terms, no prerequisites assumed, 3-4 intro slides
  - MSc: Assume foundational knowledge, Greek letters OK after slide 1, 2-3 intro slides
  - PhD: Assume deep background, jump to frontier quickly, 2 intro slides

**Section 3 (Section Framework):** REPLACE PMSP with a menu of 6 frameworks:
```
Option A: PMSP (Problem-Method-Solution-Practice) -- for applied/methods courses
Option B: Conceptual (Motivation-Theory-Evidence-Implications) -- for theory courses
Option C: Case-Based (Context-Challenge-Analysis-Resolution) -- for case study courses
Option D: Custom (user defines sections) -- for anything else
Option E: PBL (Scenario-Investigation-Synthesis-Reflection) -- for problem-based learning courses
Option F: Flipped (Pre-Work Recap-Guided Practice-Application-Debrief) -- for flipped classroom courses
```
Each option gets a section template with slide allocations.

**Section 4 (Layout Diversity):** KEEP as-is (the layout table is already universal). REMOVE reference to `template_beamer_final.tex` -- replace with "Map from your course's Beamer template."

**Section 5 (Appendix Mechanism):** KEEP as-is (LaTeX code is universal).

**Section 6 (Content Triage):** GENERALIZE the table:
- Replace "finance applications" with "domain applications"
- Replace specific test names (Breusch-Pagan, Shapiro-Wilk) with "formal statistical tests (domain-specific)"
- Replace "CAPM origin, MLE connection" with "historical context, theoretical connections"

**Acceptance Criteria:** Part 1 is fully written. No references to L01-L06, finance, ML, MSc-only, PMSP-only, or `template_beamer_final.tex`. Six framework options present.

### Task 4: Write PART 2 -- CONTENT DEPTH
**Agent:** executor (sonnet)
**Action:** Rewrite Part 2 with these specific changes:

**Section 7 (Audience-Level Adaptation) -- NEW:** Replace the MSc-only depth assumptions with a comprehensive multi-tier table covering ALL dimensions including those flagged as missing:

```
| Dimension              | BSc                          | MSc                           | PhD                          |
|------------------------|------------------------------|-------------------------------|------------------------------|
| Prerequisite check     | Define ALL terms             | Assume foundations            | Assume deep background       |
| Notation entry         | Plain English first, then    | Greek from slide 2            | Full notation from slide 1   |
|                        | symbols gradually            |                               |                              |
| Proof depth            | Show intuition, skip proofs  | Show 2+ key derivations       | Show all proofs, discuss     |
|                        |                              |                               | limitations                  |
| Worked examples        | 2+ per section, simple       | 1+ per section, realistic     | Optional, focus on edge      |
|                        | numbers                      | data                          | cases                        |
| Domain applications    | Real-world analogies         | Industry worked examples      | Research frontiers            |
| Exercises              | Guided, scaffolded           | Open-ended, multi-step        | Research-oriented            |
| Intro length           | 3-4 slides                   | 2-3 slides                    | 2 slides                     |
| Chart density          | 1 per 4 slides (governing    | 1 per 4 slides (governing     | 1 per 4 slides (governing    |
|                        | rule); prefer intuitive viz  | rule); mix intuitive +        | rule); favor diagnostic +    |
|                        |                              | diagnostic                    | research-frontier viz        |
| Appendix depth         | Light (3-6 slides):          | Moderate (6-10 slides):       | Heavy (10-15 slides):        |
|                        | optional proofs, further     | proofs, convergence theory,   | full proofs, open problems,  |
|                        | reading only                 | historical context            | alternative formulations     |
| Code/implementation    | Full walkthrough with        | Pseudocode + sklearn/library  | Pseudocode only; assume      |
|                        | comments, copy-paste ready   | snippets, not hand-held       | students implement from spec |
```

**Derived chart density examples (from the "1 per 4 slides" governing rule):**
```
| File Length    | Minimum Charts | Example                              |
|---------------|----------------|--------------------------------------|
| 15-20 slides  | 4-5 charts     | BSc overview, PhD overview           |
| 22-28 slides  | 6-7 charts     | MSc overview                         |
| 30-40 slides  | 8-10 charts    | MSc deepdive, PhD deepdive           |
| 40-50 slides  | 10-13 charts   | PhD deepdive with appendix visuals   |
```

**Relaxation note:** For derivation-heavy sections, 1 chart per 5 slides is acceptable IF equations serve a single continuous proof. However, 4+ consecutive formula slides with no chart MUST trigger adding a visualization.

**Section 8 (Content Depth Checklist):** KEEP the checklist structure. PARAMETERIZE by audience level:
- BSc: 0 derivations required, 2+ intuitive explanations, 2+ worked examples
- MSc: 2+ derivations, 1+ inference, 1+ worked example, diagnostics
- PhD: 3+ derivations/proofs, convergence analysis, open problems

Replace "Example (L01)" column with "Example" using generic subjects.

**Section 9 (Notation Consistency):** KEEP as-is -- already universal.

**Section 10 (Domain Application Requirements) -- NEW:** Replace the finance-specific Section 9 with:
```
Each lecture needs 2-3 slides of genuine domain application:

Rules:
- At least 1 application must include a worked numerical example with realistic data
- Generic one-liners ("[method] is used in [domain]") do NOT count
- The overview gets the intuitive application; the deepdive gets the mathematical detail
- Applications should demonstrate WHY the method matters for the course's target audience
- Non-quantitative courses may substitute timelines, concept maps, or formatted text for charts where a data visualization would be forced or artificial

Example domains (adapt to your course):
| Domain     | Application Style                                    |
|------------|------------------------------------------------------|
| Finance    | Risk models, portfolio optimization, fraud detection |
| Healthcare | Diagnostic models, survival analysis, drug discovery |
| Physics    | Simulation, signal processing, particle classification|
| Humanities | Text analysis, network graphs, sentiment mining      |
| Engineering| Control systems, quality assurance, predictive maint.|
```

**Section 11 (Bottomnote Quality):** KEEP as-is -- already universal.

**Acceptance Criteria:** Part 2 fully written. Audience level is parameterized with ALL dimensions (including chart density, appendix depth, code expectations). Derived chart density table present. No finance-specific or ML-specific content.

### Task 5: Write PART 3 -- COMICS AND VISUAL FRAMING (NEW)
**Agent:** executor (sonnet)
**Action:** Write the entirely new Part 3:

**Section 12 (Comic/Cartoon Placement Rules):**
```
HARD RULE: Every lecture MUST have a cartoon/comic in TWO positions:
1. OPENING: Slide 1 or 2 of the Intro section (sets the tone, engages audience)
2. CLOSING: Final content slide before References (sends students off with a smile)

The opening comic FRAMES the lecture's problem.
The closing comic REFLECTS on the lecture's key insight or common pitfall.
```

**Section 13 (Comic Sources and Attribution):**
```
| Source          | License              | Attribution Format                                    |
|-----------------|----------------------|-------------------------------------------------------|
| XKCD            | CC BY-NC 2.5         | \bottomnote{XKCD \#NNN by Randall Munroe (CC BY-NC 2.5)} |
| PhD Comics      | Permission required  | \bottomnote{PhD Comics by Jorge Cham, used with permission} |
| The Oatmeal     | Link-back required   | \bottomnote{The Oatmeal by Matthew Inman, theoatmeal.com}  |
| xkcd-style DIY  | Original work        | \bottomnote{Original illustration}                         |
| Instructor-made | Original work        | No attribution needed                                      |
| AI-generated    | Varies by tool       | \bottomnote{Generated with [tool name]}                    |

PREFERRED: XKCD (free, high quality, math/science/tech focus, CC licensed)
FALLBACK for non-STEM: PhD Comics (academia universal), instructor-made cartoons

NOTE: Syndicated comics (Dilbert, Calvin and Hobbes, etc.) require commercial licensing
for educational slide use. Verify your institution's licensing agreements before including.
```

**Section 14 (Opening Comic Guidelines):**
```
Purpose: Hook attention, frame the lecture's central question
Placement: Slide 1 (after title) or Slide 2
Layout: Layout 8 (mixed media) -- image + 2-3 framing bullets, OR full-width image

Rules:
- The comic MUST relate to the lecture topic (not just "funny")
- Add 1-2 bullets below explaining the connection to today's topic
- Bottomnote includes attribution AND "This is the problem we solve today"
- Image width: 0.45\textwidth (with text) or 0.55\textwidth (standalone)

Selection criteria:
- Does this comic make the lecture's central question obvious?
- Would a student who sees ONLY this slide know what the lecture is about?
- Is it appropriate for the audience level and institutional context?
```

**Section 15 (Closing Comic Guidelines):**
```
Purpose: Reinforce the key takeaway with humor, memorable exit
Placement: Last content slide (before References) or second-to-last
Layout: Same as opening -- Layout 8 or full-width

Rules:
- The comic MUST relate to the lecture's conclusion or a common mistake
- Add 1-2 bullets: "Now you know why..." or "The takeaway: ..."
- Bottomnote: attribution + cross-reference to next lecture

Selection criteria:
- Does this comic reference something the students NOW understand?
- Does it reinforce the key insight or warn against a common pitfall?
- Would students share this comic after class? (engagement test)

Closing comic categories:
| Category          | When to Use                    | Example Angle                |
|-------------------|--------------------------------|------------------------------|
| "Now you know"    | After teaching a concept       | Comic about the concept      |
| "Common mistake"  | After a nuanced method         | Comic about doing it wrong   |
| "Real-world irony"| After applied content          | Comic about practice vs theory|
| "What's next"     | When next lecture builds on this| Teaser for next topic        |
```

**Acceptance Criteria:** Part 3 is fully written. Comic placement is a HARD rule, not optional. Attribution table covers major sources with licensing caveat for syndicated comics. Both opening and closing have clear guidelines.

### Task 6: Write PART 4 -- CHARTS
**Agent:** executor (sonnet)
**Action:** Rewrite Part 4 with these specific changes:

**Section 16 (Chart Architecture):** Density-rule-only approach (Architect recommendation). No separate chart count parameters. KEEP the two-file split. State the governing rule clearly:

```
GOVERNING RULE: Minimum 1 chart per 4 slides in each file.

This is the ONLY chart count rule. Do not memorize fixed counts.
Derive minimums from your slide count:

| File Length    | Minimum Charts | Typical Lecture Type                 |
|---------------|----------------|--------------------------------------|
| 15-20 slides  | 4-5 charts     | BSc overview, PhD overview           |
| 22-28 slides  | 6-7 charts     | MSc overview                         |
| 30-40 slides  | 8-10 charts    | MSc deepdive, PhD deepdive           |
| 40-50 slides  | 10-13 charts   | PhD deepdive with appendix visuals   |

Relaxation: For derivation-heavy sections, 1 per 5 slides is acceptable
if equations serve a single continuous proof. But 4+ consecutive formula
slides with no chart --> MUST add a visualization.
```

KEEP the role table but GENERALIZE examples:

```
| Role       | Overview Example             | Deepdive Example                  |
|------------|------------------------------|-----------------------------------|
| Concept    | Core relationship scatter    | Multi-dimensional surface         |
| Diagnostic | Residual/error patterns      | Statistical test visualization    |
| Algorithm  | Process result               | Convergence/iteration tracking    |
| Evaluation | Performance curves           | Cross-validation error curves     |
| Comparison | Method A vs B (intuitive)    | Parameter sensitivity analysis    |
| Tradeoff   | Bias-variance / precision-recall | Confidence/uncertainty bands  |
| Decision   | Flowchart                    | (not needed in deepdive)          |
```

**Section 17 (Chart Types Taxonomy):** REPLACE the ML-specific 10-type table with a generalized 12-type taxonomy:

```
| Type                  | Description                          | Use When                          | matplotlib Pattern          |
|-----------------------|--------------------------------------|-----------------------------------|-----------------------------|
| Scatter + Fit         | Data points + model overlay          | Showing model fit to data         | ax.scatter() + ax.plot()    |
| Decision/Region Map   | Colored regions showing boundaries   | Classification or segmentation    | ax.contourf() + scatter     |
| Metric Curves         | Parameter vs performance metric      | Tuning, evaluation                | ax.plot() + fill_between    |
| Evaluation Curves     | ROC, PR, lift, calibration           | Model assessment                  | ax.plot() with reference    |
| Heatmap/Matrix        | 2D grid with color intensity         | Confusion, correlation, distance  | ax.imshow() + annotations   |
| Iterative Process     | Algorithm convergence over steps     | Optimization, iterative methods   | Arrows + contour background |
| Cluster/Group Viz     | Points colored by group membership   | Clustering, segmentation          | ax.scatter(c=labels)        |
| Dimensionality Reduc. | 2D projection of high-dim data       | Visualization of complex data     | ax.scatter() with colormap  |
| Structure Diagram     | Trees, networks, architectures       | Hierarchical/graph structures     | matplotlib.patches + arrows |
| Flowchart             | Decision guide (EVERY lecture)       | Method selection, troubleshooting | FancyBboxPatch + arrows     |
| Bar/Distribution      | Frequency, comparison across groups  | Categorical data, distributions   | ax.bar() or ax.hist()       |
| Time Series           | Values over time with annotations    | Temporal patterns, trends         | ax.plot() + ax.axvspan()    |
```

**Sections 18-23:** KEEP as-is. The chart.py boilerplate, chart rules, color convention, flowchart pattern, chart-slide integration, and chart naming are all already universal.

Specific changes within these sections:
- **Section 18 (Boilerplate):** Remove the URL pointing to the specific GitHub repo -- replace with `"url": "https://[COURSE_REPO]/slides/LXX_Topic/XX_name"`.
- **Section 20 (Color Convention):** Add a note: "NOTE: The MLPURPLE/MLBLUE/etc. names are legacy from the original ML course. They are semantic color names (primary, secondary, contrast, good, bad, neutral) that work for any subject. Renaming is optional -- the hex values and semantic roles are what matter."

**Acceptance Criteria:** Part 4 fully written. Chart density governed by "1 per 4" rule only, no separate count parameters. Derived example table present. Chart types are subject-agnostic. No references to specific ML algorithms or specific finance charts. Color naming note present.

### Task 7: Write PART 5 -- BEAMER FORMATTING
**Agent:** executor (sonnet)
**Action:** Minimal changes:

**Section 24 (Frame Rules):** KEEP as-is. Already universal. Remove any reference to `template_beamer_final.tex`.

**Section 25 (Pseudocode Guidelines):** KEEP the algorithmic environment. GENERALIZE the parenthetical:
- Change "(L02-L06)" to "(when the lecture includes algorithms or formal procedures)"
- Change "empty clusters, ties, division by zero" to "edge cases specific to the algorithm (empty sets, ties, division by zero, boundary conditions)"

**Acceptance Criteria:** Part 5 written. No lecture-number references. No template file references.

### Task 8: Write PART 6 -- PLAN CHECKLIST
**Agent:** executor (sonnet)
**Action:** REWRITE the checklist with generalized categories. Use numbered sections (26-31) so Task 10 assembly has unambiguous references:

```
### 26. Structure
- [ ] Slide-by-slide spec with layout, content, chart ref, bottomnote
- [ ] Section framework chosen and applied (PMSP, Conceptual, Case-Based, PBL, Flipped, or Custom)
- [ ] Intro is 2-4 slides (audience-adjusted)
- [ ] `\appendix` + `\section*` in deepdive (if deepdive exists)
- [ ] Slide count arithmetic verified

### 27. Content Depth
- [ ] Derivations/proofs appropriate for audience level (see depth table)
- [ ] Worked numerical examples appropriate for audience level
- [ ] Diagnostics/evaluation in deepdive MAIN body (not appendix)
- [ ] Notation table with no symbol collisions

### 28. Charts
- [ ] Chart allocation table (each chart in exactly ONE file)
- [ ] Minimum 1 chart per 4 slides in each file (governing rule)
- [ ] No chart dual-assignment across files

### 29. Domain Applications
- [ ] 2-3 domain application slides with worked example
- [ ] Applications are genuine (not generic one-liners)

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
```

**Acceptance Criteria:** Checklist has numbered sections (26-31). No course-specific items. Comics section is new and mandatory. Instructor guide check present. Six framework options listed.

### Task 9: Write PART 7 -- GOTCHAS
**Agent:** executor (sonnet)
**Action:** KEEP all 10 existing gotchas (they are mostly universal). GENERALIZE where needed. Number them as section 32:

Changes to existing gotchas:
- Gotcha 5: Change "NEVER copy from `template_beamer_final.tex`" to "NEVER copy preamble from template files. Preserve existing preamble byte-for-byte."
- Gotcha 7: Change "2-4 slides for MSc" to "2-4 slides (adjust by audience level: BSc may need 3-4, PhD may need only 2)"
- Gotcha 9: Change "residual plots, ROC, confusion matrix" to "basic diagnostics (method-appropriate)" and "Breusch-Pagan, Shapiro-Wilk" to "formal statistical tests"

ADD new gotchas:
- Gotcha 11: **Missing closing comic.** Opening comic is natural; closing comic gets forgotten. Build it into the plan from the start.
- Gotcha 12: **Audience level drift.** A BSc lecture that slips into MSc notation mid-deck loses students. A PhD lecture that over-explains basics wastes time. Pick a level and hold it.
- Gotcha 13: **Generic domain applications.** "This method is used in [field]" is not an application. A worked example with realistic numbers IS an application.

**Acceptance Criteria:** 13 gotchas total under section 32. No course-specific references. No template file references.

### Task 10: Assemble the Complete Skill File
**Agent:** executor (sonnet)
**Action:** Combine all parts into a single coherent `.md` file:

1. Write the opening sections (The Insight, Why This Matters, Recognition Pattern) with generalized language
2. Assemble Parts 1-7 in order with consistent section numbering (1-32 for main sections)
3. Write Appendix A: Instructor Guide Template (slide build specification format)
4. Write Appendix B: Course Overlay Convention (extends: mechanism)
5. Verify internal cross-references (section numbers match)
6. Verify no orphaned references to L01-L06, finance, ML, PMSP-only, or "Methods and Algorithms"
7. Save to `D:\Joerg\Research\slides\Methods_and_Algorithms\.omc\skills\beamer-slide-restructure.md`

**The Insight** (rewritten):
```
Good academic slides need FOUR things working together: (1) structure -- zones that
progress from engagement to rigor, (2) content depth -- matched to audience level
with proofs, examples, and domain applications, (3) visual density -- charts in BOTH
overview AND deepdive, governed by a minimum of 1 chart per 4 slides, and (4)
framing -- comics/cartoons that open and close every lecture to engage and reinforce.
Structure alone is necessary but not sufficient.
```

**Why This Matters** (rewritten):
```
Hostile reviews of academic slides consistently score low for content gaps (insufficient
depth, missing domain applications, no worked examples), NOT structural issues. A
perfectly structured slide deck with shallow content still fails. And a rigorous deck
without engagement hooks loses students in the first five minutes. The opening comic
earns attention; the closing comic cements memory.
```

**Recognition Pattern** (rewritten):
```
Apply when restructuring ANY university lecture, or when:
- Slides need a beginner-friendly intro followed by rigorous core
- Slides use only 2-3 layout patterns (needs visual variety)
- Advanced proofs clutter the main slide count (needs appendix)
- Deepdive is a wall of equations with no charts
- Domain applications are generic one-liners
- Lectures lack opening or closing engagement hooks (comics/cartoons)
- Content depth is mismatched to audience level

IMPORTANT: Before restructuring any lecture, read the instructor guide
(if one exists) for topic-specific build specifications, required derivations,
mandatory charts, and domain application requirements.
```

**Appendix A: Instructor Guide Template**
```
Add a "Slide Build Specification" section to each LXX_instructor_guide.md:

## Slide Build Specification

### Required Content
- Intro key formula: [formula in simple notation]
- Must-have derivations: [list of proofs/derivations for deepdive]
- Must-have charts: [list of chart types with descriptions]
- Required domain applications: [specific worked examples]

### Chart Requirements
- [Chart name]: [description, which file (overview/deepdive)]
- ...

### Pseudocode Requirements
- [Algorithm name]: [key edge cases to handle]
- ...

### Appendix Content
- [Topic]: [what goes in appendix vs main body]
- ...
```

**Appendix B: Course Overlay Convention**
```
A course-specific skill can EXTEND this universal skill using the overlay pattern:

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

The overlay file should contain ONLY:
1. Course-specific preamble (if different from universal patterns)
2. Course-specific accessibility rules (e.g., BSc no-Greek-letters rule)
3. Course-specific quality checks (e.g., quiz alignment)
4. Course-specific audience assumptions

The overlay should NOT duplicate:
- Three-zone architecture (use universal)
- Layout diversity rules (use universal)
- Chart creation boilerplate (use universal)
- Comic/cartoon rules (use universal)
- Beamer formatting rules (use universal)
```

**PMSP verification scan guidance** (for use in Task 11):
The verification scan should check that all 6 framework options (PMSP, Conceptual, Case-Based, PBL, Flipped, Custom) appear within 20 lines of each other, making them grep-able as a block.

**Acceptance Criteria:** Complete file saved. Single markdown file. No course-specific content. Internally consistent section numbering (1-32 + appendices A-B). Instructor guide template present. Overlay convention present.

### Task 11: Verification Scan
**Agent:** executor (sonnet)
**Depends on:** Tasks 10, 12, 13, 14 (all must complete first)
**Action:** Run a final verification across ALL deliverables:

**A. Universal skill verification (`.omc/skills/beamer-slide-restructure.md`):**

1. Search for these terms (should find ZERO matches):
   - "L01", "L02", "L03", "L04", "L05", "L06"
   - "Linear Regression" (as a required topic)
   - "Logistic Regression", "KNN", "K-Means", "Random Forest", "PCA", "t-SNE", "Embeddings", "RL"
   - "Basel", "CAPM", "yield curve", "scorecard", "fraud"
   - "Methods and Algorithms"
   - "MSc Data Science" (as the only audience)
   - "PMSP" (as the only section framework -- it should appear as ONE of 6 options)
   - "template_beamer_final.tex"
   - "Dilbert" (removed per licensing)

2. Search for these terms (should find 1+ matches each):
   - "BSc", "MSc", "PhD" (all three audience levels present)
   - "comic" or "cartoon" (in Parts 1, 3, 6, 7)
   - "domain application" (replacing "finance application")
   - "audience level" (parameterization present)
   - "PMSP" as one option among: "Conceptual", "Case-Based", "PBL", "Flipped", "Custom" (all 6 within 20 lines)
   - "instructor guide" (read-before-restructuring rule present)
   - "extends:" (overlay convention present)
   - "1 per 4 slides" or "1 chart per 4 slides" (governing density rule)

3. Count total lines -- should be 500-700 (estimated: ~650 given new Part 3, expanded tables, 6 frameworks, 2 appendices, 3 extra gotchas).

4. Verify the YAML triggers include both old and new generic triggers but NOT BSc-specific triggers.

**B. Global copy verification:**
- `C:\Users\OsterriederJRO\.claude\skills\omc-learned\beamer-slide-restructure.md` is byte-identical to local copy.

**C. BSc overlay verification (`slide-creation.md`):**
- Contains `extends: beamer-slide-restructure` in YAML front matter
- Is approximately 250 lines (not 935)
- Contains the 7 BSc accessibility rules
- Does NOT contain three-zone architecture, layout diversity, chart boilerplate, or other shared content
- Triggers are BSc-specific only (no "restructure slides", "create chart", etc.)

**D. Instructor guide verification:**
- All 6 instructor guides (L01-L06) contain a "Slide Build Specification" section
- Each specification includes required derivations, charts, and domain applications migrated from old Part 6

**Acceptance Criteria:** All zero-match terms return zero. All required-match terms return 1+. Line count in range. Global copy matches. BSc overlay is slim. Instructor guides are updated.

### Task 12: Migrate Topic-Specific Content to Instructor Guides
**Agent:** executor (sonnet)
**Can run in parallel with:** Tasks 3-9
**Input:** Part 6 of the current skill (lines 443-484) + existing instructor guides
**Action:** For each of L01-L06, add a "Slide Build Specification" section to the existing instructor guide:

**L01 (`D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L01_Introduction_Linear_Regression\L01_instructor_guide.md`):**
Add before "Post-Session Notes":
```markdown
## Slide Build Specification

### Required Content
- Intro key formula: `y = a + bx` (then switch to beta notation)
- Must-have derivations: OLS normal equation, gradient descent gradient computation
- Must-have inference: t-test for coefficients, F-test for model

### Chart Requirements
- Regression surfaces (deepdive)
- QQ-plot (deepdive)
- Confidence bands (deepdive)
- CV error curve (deepdive)

### Domain Applications
- House price valuation for banks (worked numerical example)
- CAPM beta estimation

### Appendix Content
- Gauss-Markov proof
- MLE connection
- Convergence theory
```

**L02 (`D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L02_Logistic_Regression\L02_instructor_guide.md`):**
```markdown
## Slide Build Specification

### Required Content
- Intro key formula: `P(Y=1) = 1/(1+e^{-z})` (sigmoid)
- Must-have derivations: MLE derivation, Newton-Raphson
- Must-have inference: Wald/LR/Score tests, multiclass (softmax)

### Chart Requirements
- Sigmoid curve (overview)
- Decision boundary (overview)
- ROC curve (overview/deepdive)
- PR curve (deepdive)
- Confusion matrix (overview)
- Calibration plot (deepdive)

### Domain Applications
- Credit scoring / PD estimation (worked example)
- Basel II/III scorecards
- Class imbalance in fraud -- MUST discuss for ANY classification task

### Appendix Content
- Newton-Raphson convergence
- Multinomial logit theory
```

**L03 (`D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L03_KNN_KMeans\L03_instructor_guide.md`):**
```markdown
## Slide Build Specification

### Required Content
- Intro key visual: Nearest neighbor intuition (show k=1,3,7 effect)
- Must-have derivations: Distance metric proofs, K-Means convergence, curse of dimensionality
- Must-have pseudocode: KNN with tie-breaking, K-Means with empty cluster handling

### Chart Requirements
- KNN boundaries (overview)
- Distance heatmap (deepdive)
- K-Means iteration (overview)
- Elbow plot (overview)
- Silhouette plot (deepdive)
- Voronoi diagram (deepdive)

### Domain Applications
- Customer segmentation (RFM) (worked example)
- Fraud anomaly detection via clustering

### Appendix Content
- Distance metric proofs
- K-Means convergence proof
- Empty cluster handling edge cases
```

**L04 (`D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L04_Random_Forests\L04_instructor_guide.md`):**
```markdown
## Slide Build Specification

### Required Content
- Intro key visual: Ensemble voting (wisdom of crowds)
- Must-have derivations: Gini/entropy derivation, bagging variance reduction proof, boosting loss minimization, SHAP
- Must-have pseudocode: RF with bootstrap, AdaBoost/XGBoost update

### Chart Requirements
- Decision tree visualization (overview)
- Feature importance bar chart (overview)
- Bootstrap illustration (overview)
- OOB error convergence (deepdive)
- Ensemble voting diagram (overview)
- Variance reduction curve (deepdive)

### Domain Applications
- Fraud detection with class imbalance (worked example) -- MUST discuss class imbalance
- Credit risk feature importance

### Appendix Content
- Gini derivation from first principles
- Bagging variance reduction proof
- XGBoost objective function
```

**L05 (`D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L05_PCA_tSNE\L05_instructor_guide.md`):**
```markdown
## Slide Build Specification

### Required Content
- Intro key visual: 3D to 2D projection
- Must-have derivations: Eigenvalue derivation from covariance matrix, SVD connection, t-SNE gradient, perplexity math
- No pseudocode needed (PCA is a closed-form computation)

### Chart Requirements
- Scree plot (overview)
- PC loadings (deepdive)
- Reconstruction visualization (deepdive)
- t-SNE perplexity comparison (deepdive)
- Swiss roll projection (overview)

### Domain Applications
- Yield curve PCA: first 3 PCs = level/slope/curvature (worked example)
- Portfolio risk decomposition
- t-SNE for market regime detection

### Appendix Content
- Full eigenvalue derivation
- SVD-PCA equivalence proof
- t-SNE gradient derivation
```

**L06 (`D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L06_Embeddings_RL\L06_instructor_guide.md`):**
```markdown
## Slide Build Specification

### Required Content
- Intro key visual: Word analogy (king - man + woman = queen)
- Must-have derivations: Skip-gram objective, negative sampling, Bellman equation derivation, DQN architecture
- Must-have pseudocode: Q-learning with epsilon-greedy, skip-gram training loop

### Chart Requirements
- Embedding space visualization (overview)
- Similarity heatmap (deepdive)
- RL loop diagram (overview)
- Q-learning grid (deepdive)
- Reward curves (deepdive)
- Policy visualization (deepdive)

### Domain Applications
- Financial NLP sentiment analysis (worked example)
- Algorithmic trading with RL

### Appendix Content
- Skip-gram objective derivation
- Negative sampling theory
- Bellman equation convergence
- DQN architecture details
```

**Acceptance Criteria:** All 6 instructor guides have "Slide Build Specification" sections. Content is migrated faithfully from Part 6 of the current skill. No content is lost. Existing instructor guide content is preserved (new section added, nothing removed).

### Task 13: Copy Completed Skill to Global Path
**Agent:** executor-low (haiku)
**Depends on:** Task 10
**Action:** Copy the completed universal skill from `D:\Joerg\Research\slides\Methods_and_Algorithms\.omc\skills\beamer-slide-restructure.md` to `C:\Users\OsterriederJRO\.claude\skills\omc-learned\beamer-slide-restructure.md`.
**Acceptance Criteria:** Global copy is byte-identical to local copy.

### Task 14: Slim BSc Overlay (`slide-creation.md`)
**Agent:** executor (sonnet)
**Depends on:** Task 10
**Input:** Current `C:\Users\OsterriederJRO\.claude\skills\omc-learned\slide-creation.md` (935 lines)
**Action:** Rewrite `slide-creation.md` as a slim overlay (~250 lines) containing ONLY BSc-specific content:

**New YAML front matter:**
```yaml
---
id: slide-creation
extends: beamer-slide-restructure
name: BSc Digital Finance Slide Overlay
description: >
  BSc-specific overrides for the Economics of Digital Finance course.
  Extends the universal beamer-slide-restructure skill with 7 accessibility
  rules, BSc intro conventions, BSc preamble, and quiz alignment checks.
  For shared infrastructure (three-zone architecture, layout diversity,
  chart creation, comic rules, formatting), see beamer-slide-restructure.
source: 191-issue BSc remediation across 8 Digital Finance lectures (Feb 2026)
triggers:
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
quality: high (Critic 2 iterations + 191 issues remediated) -- slimmed to overlay v1
---
```

**Content to KEEP (BSc-specific only, ~250 lines):**
1. BSc-specific preamble (Part 0 sections 0.1-0.3 -- the exact LaTeX preamble for this course)
2. BSc intro rules: No Greek letters, no matrix notation, everyday examples first, 8-10 slide intro
3. The 7 content accessibility rules (Part 2 sections 2.1-2.7) -- these are BSc-specific intensity
4. Quiz-slide alignment checks (Rule 2.6)
5. BSc-specific gotchas (7, 8, 9, 10 -- quiz drift, chart annotations, trilemma consistency, order book step functions)
6. Title block pattern with BSc course info

**Content to REMOVE (now in universal skill):**
- Three-zone architecture (Part 1 section 1.1)
- Layout diversity (Part 1 section 1.3)
- Content triage (Part 1 section 1.4)
- Appendix mechanism (Part 1 section 1.5)
- Beamer formatting rules (Part 1 section 1.6)
- Chart architecture, types, boilerplate, rules, colors, flowcharts, naming, integration (all of Part 3)
- Plan checklist (Part 4 section 4.1)
- Post-execution verification (Part 4 section 4.3)
- Universal gotchas (1-6 -- chart dual-assignment, slide count, section*, overfull, preamble, merging)

**Add at the top of the overlay:**
```
NOTE: This is a COURSE OVERLAY. It extends the universal `beamer-slide-restructure`
skill. For shared infrastructure (three-zone architecture, layout diversity, chart
creation, comic rules, formatting, gotchas 1-6), refer to that skill.

This overlay adds BSc-specific rules that override or supplement the universal defaults.
```

**Acceptance Criteria:** File is approximately 250 lines. Contains `extends: beamer-slide-restructure` in YAML. Contains BSc accessibility rules. Does NOT duplicate universal content. Triggers are BSc-specific only (shared triggers removed).

---

## Commit Strategy

Single commit after Task 11 verification passes:
```
Generalize beamer-slide-restructure skill for any university course

Replace course-specific content (L01-L06, finance, PMSP-only) with
parameterized templates supporting any subject, audience level (BSc/MSc/PhD),
and lecture count. Add mandatory opening+closing comic requirement.
Migrate topic-specific content to instructor guides. Slim BSc slide-creation
skill to overlay. Deploy to both local and global skill paths.
```

---

## Success Criteria

1. **Universality Test:** An agent given ONLY this skill and asked to create slides for "BSc Introduction to Philosophy, Lecture 3: Ethics of AI" can produce a valid plan without needing any other context.

2. **Backward Compatibility Test:** An agent given this skill + the L04 instructor guide and asked to create slides for "MSc Methods and Algorithms, L04: Random Forests" produces output at least as good as the old skill would have (the old topic-specific guidance now lives in the instructor guide).

3. **Comic Enforcement Test:** Every plan generated from this skill includes opening AND closing comics for every lecture, with attribution.

4. **Audience Scaling Test:** The same agent using this skill produces noticeably different intro lengths, notation entry points, proof depths, chart densities, appendix depths, and code expectations for BSc vs PhD.

5. **No Content Loss Test:** Every line of Part 6 (L01-L06 topic guides) from the old skill exists in an instructor guide's "Slide Build Specification" section.

6. **Overlay Test:** An agent triggered by "BSc accessible" activates the slim overlay. An agent triggered by "restructure slides" activates the universal skill. No trigger collision between the two.

7. **Global Deployment Test:** The universal skill at the global path matches the local copy exactly.
