# Plan: L05 & L06 Deepdive Improvements

## Context

### Original Request
Fix 8 prioritized issues found by ultra-deep content analysis of L05 (PCA & t-SNE) and L06 (Embeddings & RL) deepdive slides. Only deepdive .tex files need modification; overviews are strong and untouched.

### Design Principle
Core concepts first, secondary material moves to appendix. The goal is NOT to show everything about a topic in the main body --- extended/secondary content belongs in the appendix.

### Research Findings
- **L05_deepdive.tex**: 1126 lines, 40 main slides + 8 appendix slides. 7 charts in main body.
- **L06_deepdive.tex**: 1053 lines, 42 main slides + 8 appendix slides. 6 charts in main body (10 total including top10_ charts not referenced in deepdive).
- L05 appendix starts at line 955 (`\appendix`), with slides A1-A8.
- L06 appendix starts at line 876 (`\appendix`), with slides A1-A8.
- L06 has existing `top10_08_word_analogy/chart.py` that already does the king-man+woman=queen visualization -- the new `11_word_analogy_arithmetic` chart must differ from this (or reuse it via renaming).
- L06 has existing `top10_09_epsilon_greedy/chart.py` that shows epsilon comparison in a 10-armed bandit -- the new `12_epsilon_decay` chart should show epsilon VALUE over episodes (decay curve), not reward curves.
- Chart style conventions: `plt.rcParams.update(...)` with font.size=14, figsize=(10,6), dpi=150, ML color palette (#3333B2, #0066CC, #FF7F0E, #2CA02C, #D62728, #ADADE0), `CHART_METADATA` dict, save to `chart.pdf`.

---

## Work Objectives

### Core Objective
Tighten the L05 and L06 deepdive slides by moving secondary content to appendix, adding charts to improve L06 density, removing style inconsistencies, and reducing overlap with overview slides.

### Deliverables
1. Modified `L05_deepdive.tex` with 1 slide moved to appendix
2. Modified `L06_deepdive.tex` with 2 slides moved to appendix, title fixes, columns layout, decision framework consolidation
3. 3 new chart.py files for L06 (word analogy arithmetic, epsilon decay, walk-forward timeline)
4. All new charts produce `chart.pdf` without errors
5. Updated `manifest.json` with 3 new chart entries

### Definition of Done
- Both .tex files compile with 0 errors and 0 Overfull warnings
- All new chart.py files run and produce chart.pdf
- L05 main body: 39 slides, appendix: 9 slides
- L06 main body: 41 slides, appendix: 10 slides (42 original - 2 moved - 2 consolidated + 3 new charts = 41)
- L06 chart density >= 1:5
- Zero content deleted (all moved slides preserved in appendix)
- manifest.json updated with 3 new chart entries

---

## Guardrails

### Must Have
- All moved slides appear in appendix with appropriate numbering
- Existing cross-references and section flow remain coherent
- New charts follow exact course standards (figsize, dpi, fonts, colors)
- Slide count comments updated throughout both files

### Must NOT Have
- No changes to overview files (L05_overview.tex, L06_overview.tex)
- No changes to existing chart.py files
- No deletion of content -- only moves and consolidation
- No changes to the preamble/template portions of either .tex file
- No changes to L01-L04 files

---

## Task Flow

```
TASK 1 (L05 tex edits)
    |
TASK 2 (L06 tex edits)  -- can run parallel with TASK 1
    |
TASK 3 (New L06 charts) -- can run parallel with TASKS 1-2
    |
TASK 4 (Verification)   -- depends on TASKS 1-3
```

---

## Detailed TODOs

### TASK 1: L05_deepdive.tex Edits
**File:** `D:/Joerg/Research/slides/Methods_and_Algorithms/slides/L05_PCA_tSNE/L05_deepdive.tex`

#### TODO 1.1: Rename slide 6 title (Priority 6)
- **Line 170:** Change `{Mathematical Foundation}` to `{Covariance Matrix and Eigendecomposition}`
- Acceptance: Frame title reads "Covariance Matrix and Eigendecomposition"

#### TODO 1.2: Move slide 16 (Statistical Inference for PCA) to appendix (Priority 2)
- **Cut lines 374-395** (the entire `% SLIDE 16: Statistical Inference for PCA` frame)
- **Insert** the cut frame into the appendix section, AFTER the current slide A7 (Trustworthiness and Continuity Metrics, ends ~line 1103) and BEFORE slide A8 (References and Further Reading)
- Rationale for appendix placement: Statistical inference methods (bootstrap, parallel analysis, cross-validation for DR) are methodological extensions that group logically near the Trustworthiness/Continuity metrics slide
- **Renumber** the inserted slide as A8, and renumber the old A8 (References) to A9

#### TODO 1.3: Renumber remaining main body slides after the move
- Old slide 17 (PCA Limitations, line 397) becomes slide 16
- Old slide 18 (t-SNE Core Idea) becomes slide 17
- Continue renumbering through slide 40 (References: Documentation) which becomes slide 39
- Each `% SLIDE NN:` comment must be updated

#### TODO 1.4: Update slide count comments
- **Line 102:** Change `% MAIN BODY (40 slides)` to `% MAIN BODY (39 slides)`
- **Line 953:** Change `% APPENDIX (8 slides)` to `% APPENDIX (9 slides)`

#### TODO 1.5: Verify section flow after move
- After removing slide 16, the flow becomes: slide 14 (Yield Curve Worked Example) -> slide 15 (Portfolio Risk Decomposition) -> slide 16 (PCA Limitations, was 17)
- This is clean: finance applications flow directly into limitations, which motivates t-SNE

**Acceptance criteria for TASK 1:**
- `pdflatex -interaction=nonstopmode L05_deepdive.tex` exits 0
- `grep -c "Overfull" L05_deepdive.log` returns 0
- Main body has exactly 39 `\begin{frame}` (including title page)
- Appendix has exactly 9 `\begin{frame}`

---

### TASK 2: L06_deepdive.tex Edits
**File:** `D:/Joerg/Research/slides/Methods_and_Algorithms/slides/L06_Embeddings_RL/L06_deepdive.tex`

**IMPORTANT:** Apply edits bottom-up (highest line numbers first) to avoid line-number drift.

**Execution order:** 2.1 (lines 735-794) → 2.2 (lines 696-713) → 2.3 (lines 680-694) → 2.5C (after line 644) → 2.5B (after line 580) → 2.5A (after line 260) → 2.4 (lines 142, 382) → 2.6 → 2.7

#### TODO 2.1: Consolidate Decision Framework slides 36-38 into 1-2 slides (Priority 8)
- **Current slides 36-38** (lines 735-794):
  - Slide 36: "When to Use What" (comparison table)
  - Slide 37: "Implementation" (library references)
  - Slide 38: "Practical Tips"
- **Action:** Merge slides 36 and 38 into ONE slide titled "Decision Framework and Best Practices"
  - Keep the comparison table from slide 36
  - Add deepdive-specific practical bullets below the table (from slide 38, but rewritten for deepdive level -- e.g., "Evaluate embedding quality via analogy task accuracy AND downstream task F1" instead of generic "start with pre-trained")
  - Remove slide 37 ("Implementation") entirely -- library references are in the References slides and the overview
- **Net effect:** 3 slides become 1, freeing 2 slots for new chart slides

#### TODO 2.2: Move slide 34 (Statistical Inference) to appendix (Priority 3)
- **Cut lines 696-713** (the entire `% Slide 34: Statistical Inference for Embeddings & RL` frame)
- **Insert** into appendix AFTER current A7 (SARSA vs Q-Learning, ends ~line 1036) and BEFORE A8 (References)
- **Renumber** as A8. Old A8 (References) becomes A9.

#### TODO 2.3: Move slide 33 (Policy Gradient Methods) to appendix (Priority 1)
- **Cut lines 680-694** (the entire `% Slide 33: Policy Gradient Methods` frame)
- **Insert** into appendix AFTER the newly placed Statistical Inference slide (now A8) -- so Policy Gradient becomes A9
- **Renumber** old A8 (References, now pushed) to A10
- **Fix section header:** After removing slide 33, the "Deep RL and Advanced Methods" section (line 655) contains only the DQN slide (32). Rename the section to: `\section{Deep Q-Networks}` on line ~655

#### TODO 2.4: Remove "Part 1/2:" title prefixes (Priority 5)
- **Slide 5 (line 142):** Change `{Part 1: Word Embeddings Introduction}` to `{Word Embeddings: The Representation Problem}`
- **Slide 18 (line 382):** Change `{Part 2: Reinforcement Learning Framework}` to `{The RL Framework}`

#### TODO 2.5: Add chart includes for new charts + columns layout (Priorities 4 & 7)
After the Decision Framework consolidation frees 2 slide slots, and after moving 2 slides to appendix frees 2 more conceptual slots, insert these new chart slides:

**New slide A: Word Analogy Arithmetic chart** (after current slide 11, Word Analogies)
- Insert a new frame after line 260 (end of slide 11):
```latex
%% Slide 12: Word Analogy Arithmetic (CHART 11)
\begin{frame}[t]{Word Analogy: Vector Arithmetic}
\begin{center}
\includegraphics[width=0.55\textwidth]{11_word_analogy_arithmetic/chart.pdf}
\end{center}
\bottomnote{Vector arithmetic in embedding space: relationships encoded as directions (PCA projection of 50-dim embeddings)}
\end{frame}
```

**New slide B: Epsilon Decay chart** (after current slide 27, Exploration vs Exploitation, using columns layout)
- Insert a new frame after line 580 (end of slide 27):
```latex
%% Slide XX: Epsilon Decay Schedule (CHART 12)
\begin{frame}[t]{Epsilon Decay Schedule}
\begin{columns}[T]
\begin{column}{0.55\textwidth}
\includegraphics[width=\textwidth]{12_epsilon_decay/chart.pdf}
\end{column}
\begin{column}{0.42\textwidth}
\textbf{Decay Strategies:}
\begin{itemize}
  \item \textbf{Linear:} $\epsilon_t = \epsilon_0 (1 - t/T)$
  \item \textbf{Exponential:} $\epsilon_t = \epsilon_0 \cdot \alpha^t$
  \item \textbf{Step:} Drop at fixed milestones
\end{itemize}
\vspace{0.3em}
\textbf{In finance:}
\begin{itemize}
  \item Early: explore diverse strategies
  \item Late: exploit best-found policy
\end{itemize}
\end{column}
\end{columns}
\bottomnote{Exponential decay ($\alpha = 0.995$) is the most common default; linear is simpler to tune}
\end{frame}
```

**New slide C: Walk-Forward Timeline chart** (after current slide 30, Backtesting RL Trading Strategies)
- Insert a new frame after line 644 (end of slide 30):
```latex
%% Slide XX: Walk-Forward Validation Timeline (CHART 13)
\begin{frame}[t]{Walk-Forward Validation Timeline}
\begin{center}
\includegraphics[width=0.65\textwidth]{13_walkforward_timeline/chart.pdf}
\end{center}
\bottomnote{Walk-forward: the gold standard for evaluating time-series strategies; never look ahead}
\end{frame}
```

#### TODO 2.6: Renumber ALL slides after all insertions/deletions
- Final main body count target: ~39 slides (42 original - 2 moved to appendix - 2 consolidated from Decision Framework + 3 new chart slides = 41; but consolidation removes 2 so: 42 - 2 - 2 + 3 = 41)
- Wait: 42 original, remove 2 to appendix = 40, remove 2 from consolidation = 38, add 3 charts = 41
- Final appendix count: 8 original + 2 moved = 10 slides
- Update ALL `%% Slide NN:` comments sequentially

#### TODO 2.7: Update header comments
- **Line 102:** Change `% MAIN BODY (42 slides)` to `% MAIN BODY (41 slides)`
- **Line ~873:** Change `% APPENDIX (8 slides)` to `% APPENDIX (10 slides)`

**Acceptance criteria for TASK 2:**
- `pdflatex -interaction=nonstopmode L06_deepdive.tex` exits 0
- `grep -c "Overfull" L06_deepdive.log` returns 0
- No "Part 1:" or "Part 2:" in any frame title
- At least 1 columns-layout frame in main body
- Appendix has exactly 10 `\begin{frame}`
- Section formerly called "Deep RL and Advanced Methods" is renamed

---

### TASK 3: Create New L06 Charts
**Base path:** `D:/Joerg/Research/slides/Methods_and_Algorithms/slides/L06_Embeddings_RL/`

#### TODO 3.1: Create `11_word_analogy_arithmetic/chart.py`
- **Create directory:** `11_word_analogy_arithmetic/`
- **Chart content:** Visualize king - man + woman = queen vector arithmetic in 2D
  - Use synthetic embeddings with clear gender and royalty semantic dimensions (similar approach to existing `top10_08_word_analogy/chart.py` but focused on the arithmetic operation)
  - Show: 4 key words (king, queen, man, woman) as labeled scatter points
  - Draw parallelogram: arrows showing king->queen is parallel to man->woman
  - Annotate with the equation: king - man + woman ~ queen
  - Lighter secondary words (prince, princess, boy, girl) to show the pattern generalizes
  - Use PCA to project from 50D to 2D
- **Style:** Standard rcParams, ML color palette, CHART_METADATA dict, output `chart.pdf`
- **Key difference from top10_08:** This chart emphasizes the parallelogram geometry and vector arithmetic; the top10 version is more of a general scatter. This chart should be cleaner with fewer annotations and more focus on the geometric relationship.
- Acceptance: `python chart.py` exits 0, `chart.pdf` exists

#### TODO 3.2: Create `12_epsilon_decay/chart.py`
- **Create directory:** `12_epsilon_decay/`
- **Chart content:** Epsilon value vs. episode number showing 3 decay strategies
  - X-axis: Episode (0 to 1000)
  - Y-axis: Epsilon value (0 to 1.0)
  - Three curves:
    - Linear decay: epsilon = max(eps_min, 1.0 - t/T) in MLBLUE
    - Exponential decay: epsilon = max(eps_min, 1.0 * 0.995^t) in MLORANGE
    - Step decay: drops at episode 200, 500, 800 in MLPURPLE
  - eps_min = 0.01 floor for all strategies
  - Horizontal dashed line at eps_min
  - Two shaded regions: "Exploration Phase" (left, light) and "Exploitation Phase" (right, light)
  - Legend in upper-right
- **Key difference from top10_09:** That chart shows REWARD curves over time for different fixed epsilon values; this chart shows the EPSILON VALUE itself decaying over episodes
- **Style:** Standard rcParams, ML color palette, CHART_METADATA dict, output `chart.pdf`
- Acceptance: `python chart.py` exits 0, `chart.pdf` exists

#### TODO 3.3: Create `13_walkforward_timeline/chart.py`
- **Create directory:** `13_walkforward_timeline/`
- **Chart content:** Walk-forward validation timeline diagram
  - 4-5 horizontal bars stacked vertically, each representing a fold
  - Each bar split into TRAIN (blue) and TEST (orange) segments
  - Fold 1: Train [2015-2017], Test [2017-2018]
  - Fold 2: Train [2016-2018], Test [2018-2019]
  - Fold 3: Train [2017-2019], Test [2019-2020]
  - Fold 4: Train [2018-2020], Test [2020-2021]
  - Y-axis labels: "Fold 1", "Fold 2", etc.
  - X-axis: Year (2015-2021)
  - Arrow annotation: "expanding window" along the left edge
  - Key insight annotation: "No look-ahead bias" with an arrow
- **Style:** Use broken_barh or barh for the timeline blocks. Standard rcParams, ML color palette, CHART_METADATA dict, output `chart.pdf`
- Acceptance: `python chart.py` exits 0, `chart.pdf` exists

**Acceptance criteria for TASK 3:**
- All 3 directories created with chart.py files
- All 3 chart.py files run without errors
- All 3 produce chart.pdf files
- Charts use correct figsize=(10,6), dpi=150, font.size=14, ML color palette

---

### TASK 4: Verification
**Depends on:** TASKS 1, 2, 3

#### TODO 4.1: Compile L05_deepdive.tex
- Run: `cd slides/L05_PCA_tSNE && pdflatex -interaction=nonstopmode L05_deepdive.tex`
- Verify: 0 errors, 0 Overfull warnings
- Count frames: 39 main + 9 appendix = 48 total

#### TODO 4.2: Compile L06_deepdive.tex
- Run: `cd slides/L06_Embeddings_RL && pdflatex -interaction=nonstopmode L06_deepdive.tex`
- Verify: 0 errors, 0 Overfull warnings
- Count frames: 41 main + 10 appendix = 51 total

#### TODO 4.3: Run all 3 new chart.py files
- `python slides/L06_Embeddings_RL/11_word_analogy_arithmetic/chart.py`
- `python slides/L06_Embeddings_RL/12_epsilon_decay/chart.py`
- `python slides/L06_Embeddings_RL/13_walkforward_timeline/chart.py`

#### TODO 4.4: Update manifest.json
- Add 3 new chart entries to the L06 `charts` array in `manifest.json`:
  - `{"path": "slides/L06_Embeddings_RL/11_word_analogy_arithmetic/chart.py", "status": "complete"}`
  - `{"path": "slides/L06_Embeddings_RL/12_epsilon_decay/chart.py", "status": "complete"}`
  - `{"path": "slides/L06_Embeddings_RL/13_walkforward_timeline/chart.py", "status": "complete"}`
- Per CLAUDE.md: "When adding new content: 1. Create the asset, 2. Update manifest.json"

#### TODO 4.5: Verify acceptance criteria
- [ ] L05 compiles clean (0 errors, 0 Overfull)
- [ ] L06 compiles clean (0 errors, 0 Overfull)
- [ ] All 3 chart.py files produce chart.pdf
- [ ] L05 main body: 39 slides, appendix: 9 slides
- [ ] L06 main body: 41 slides, appendix: 10 slides
- [ ] L06 chart density: 9 charts / 41 main body slides = 1:4.6 (meets target of >= 1:5; only main-body charts count toward density)
- [ ] No "Part X:" prefixes in L06 frame titles
- [ ] At least 1 columns-layout frame in L06 main body (epsilon decay slide)
- [ ] No content deleted -- all moved slides exist in appendix
- [ ] All slide numbering comments updated
- [ ] manifest.json updated with 3 new chart entries

---

## Commit Strategy

### Single commit after all changes verified:
```
L05/L06 deepdive: tighten main body, add L06 charts, consolidate framework

- L05: Move statistical inference slide to appendix (39 main + 9 appendix)
- L05: Rename "Mathematical Foundation" to specific title
- L06: Move policy gradient and statistical inference to appendix (10 appendix)
- L06: Add 3 new charts (word analogy, epsilon decay, walk-forward timeline)
- L06: Consolidate 3 decision framework slides into 1
- L06: Remove "Part 1/2:" title prefixes, add columns layout
- L06 chart density improved from 1:7 to 1:4.6
```

---

## Success Criteria

1. **Compilation:** Both .tex files compile with 0 errors and 0 Overfull warnings
2. **Charts:** All 3 new chart.py files run without errors and produce chart.pdf
3. **Slide counts:** L05 = 39+9, L06 = 41+10
4. **Chart density:** L06 >= 1:5 (9 charts in 41 main body slides = 1:4.6)
5. **Content integrity:** No content deleted; all moved slides in appendix
6. **Style consistency:** No "Part X:" prefixes; at least 1 columns layout in L06
7. **Section coherence:** "Deep RL and Advanced Methods" renamed after slide removal

---

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Moving slides breaks section flow | Verified post-move flow in task descriptions above |
| New chart slides cause Overfull | Use standard chart widths (0.55 or 0.65\textwidth) |
| Existing top10_08 word analogy chart overlap | New chart emphasizes parallelogram geometry; top10 is a different visual |
| Appendix ordering not logical | Grouped by topic: L05 inference near trustworthiness; L06 statistical inference and policy gradient placed after SARSA (RL methods grouped together) |
| Decision framework consolidation loses content | Only removing library references (available in References slides); practical tips merged |
