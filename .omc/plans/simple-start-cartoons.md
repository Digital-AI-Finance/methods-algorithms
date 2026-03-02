# Plan: Ensure Simple Start + Cartoons

## Task Summary

Ensure the course starts very simply with accessible examples and visuals, and deploy cartoon images across the 6 overview lectures.

## Current State

### Cartoon Inventory (Overview Lectures Only)

| Lecture | Opening | Mid | Closing | Images |
|---------|---------|-----|---------|--------|
| L01 | #1725 (image) | #2048 (image) | #605 (image) | 3 |
| L02 | #1132 (image) | — | text-only callback | 1 |
| L03 | #1838 (image) | — | text-only callback | 1 |
| L04 | #1885 (image) | — | #1838 (image) | 2 |
| L05 | #2048 (image) | — | text-only callback | 1 |
| L06 | #1838 (image) | — | text-only callback | 1 |
| **Total** | | | | **9** |

**Unique XKCD images:** 6 (#605, #1132, #1725, #1838, #1885, #2048)

### Target State

Every overview lecture gets both opening AND closing cartoon images. This brings the total to 13 cartoon placements using 8 unique XKCD comics. The user's "10 cartoon" request is met and exceeded because: (a) we do not remove existing images, (b) each lecture deserves both an opening and closing visual, and (c) having 13 placements with 8 unique comics provides variety while allowing thematic reuse of #1838 as the course's recurring motif.

| Lecture | Opening | Mid | Closing | Total |
|---------|---------|-----|---------|-------|
| L01 | #1725 | #2048 | #605 | 3 |
| L02 | #1132 | — | #1132 (image) | 2 |
| L03 | #1838 | — | #2731 (image) | 2 |
| L04 | #1885 | — | #1838 | 2 |
| L05 | #2048 | — | #2400 (image) | 2 |
| L06 | #1838 | — | #1838 (image) | 2 |
| **Total** | | | | **13** |

**All 8 image files already exist on disk. No downloads needed.**

---

## Execution Order

**Execute in this order to avoid slide-number conflicts:**

1. **Part 2 first** (L01 simplicity edits) — modifies existing slides, no slide additions
2. **Part 3 second** (worked example audit) — may add content to existing slides (NO new slides allowed)
3. **Part 1 last** (cartoon closings) — replaces existing closing frames, no slide count changes

---

## Part 1: Deploy Cartoon Closing Images (4 tasks)

All 4 tasks replace existing text-only closing frames with image+text layouts. No new slides are added; existing slide 23 frames are edited in-place.

### Task 1.1: Add XKCD #1132 closing image to L02 overview

**File:** `slides/L02_Logistic_Regression/L02_overview.tex`
**Slide:** 23 (line ~639, closing comic)
**Image:** `images/1132_frequentist_bayesian.png` (exists)

Replace the entire closing frame (from `\begin{frame}[t]{Until Next Time...}` to its `\end{frame}`) with:

```latex
\begin{frame}[t]{Until Next Time...}
\begin{columns}[T]
\column{0.45\textwidth}
\includegraphics[width=\textwidth]{images/1132_frequentist_bayesian.png}
\column{0.50\textwidth}
\vspace{1em}
\textit{``Is the sun going to explode?''}\\[0.5em]
Now you have the tools to answer with a probability, not just yes/no.

\vspace{1em}
\textbf{Next Session:} L03 -- KNN \& K-Means (from parametric to non-parametric)
\end{columns}
\bottomnote{XKCD \#1132 by Randall Munroe (CC BY-NC 2.5) -- classification is about probabilities, not certainties}
\end{frame}
```

### Task 1.2: Add XKCD #2731 closing image to L03 overview

**File:** `slides/L03_KNN_KMeans/L03_overview.tex`
**Slide:** 23 (line ~520, closing comic)
**Image:** `images/2731_kmeans_clustering.png` (exists)

Replace the entire closing frame with:

```latex
\begin{frame}[t]{Until Next Time...}
\begin{columns}[T]
\column{0.45\textwidth}
\includegraphics[width=\textwidth]{images/2731_kmeans_clustering.png}
\column{0.50\textwidth}
\vspace{1em}
\textit{``Even K-Means would struggle to cluster the ways students misuse K-Means.''}\\[0.5em]
With KNN and K-Means, you can now classify the known and discover the unknown.

\vspace{1em}
\textbf{Next Session:} L04 -- Random Forests (from distance-based to tree-based methods)
\end{columns}
\bottomnote{XKCD \#2731 by Randall Munroe (CC BY-NC 2.5) -- clustering is easy, knowing when to cluster is the hard part}
\end{frame}
```

### Task 1.3: Add XKCD #2400 closing image to L05 overview

**File:** `slides/L05_PCA_tSNE/L05_overview.tex`
**Slide:** 23 (line ~397, closing comic)
**Image:** `images/2400_statistics.png` (exists)

Replace the entire closing frame with:

```latex
\begin{frame}[t]{Closing Thought}
\begin{columns}[T]
\column{0.45\textwidth}
\includegraphics[width=\textwidth]{images/2400_statistics.png}
\column{0.50\textwidth}
\vspace{1em}
\textit{``We reduced our 100-dimensional portfolio to 3 principal components.\\[0.3em]
The fourth component? That's just noise\ldots\ probably.''}

\vspace{1em}
\textbf{Next Session:} L06 -- Embeddings \& RL
\end{columns}
\bottomnote{XKCD \#2400 ``Statistics'' by Randall Munroe (CC BY-NC 2.5)}
\end{frame}
```

### Task 1.4: Add XKCD #1838 closing image to L06 overview

**File:** `slides/L06_Embeddings_RL/L06_overview.tex`
**Slide:** 23 (line ~453, closing comic)
**Image:** `images/1838_machine_learning.png` (exists)

Replace the entire closing frame with:

```latex
\begin{frame}[t]{Closing Thought}
\begin{columns}[T]
\column{0.40\textwidth}
\includegraphics[width=\textwidth]{images/1838_machine_learning.png}
\column{0.55\textwidth}
\vspace{1em}
\Large\textit{``We poured financial news into a pile of linear algebra and got sentiment scores on the other side.''}

\vspace{0.5em}
\normalsize You now have the toolkit: regression, classification, clustering, ensembles, dimensionality reduction, embeddings, and RL.
\end{columns}
\bottomnote{XKCD \#1838 by Randall Munroe (CC BY-NC 2.5). Course complete!}
\end{frame}
```

---

## Part 2: Ensure Simple Start (2 tasks)

### Task 2.1: Simplify L01 Learning Objectives

**File:** `slides/L01_Introduction_Linear_Regression/L01_overview.tex`
**Slide:** 4 (line ~157, Learning Objectives)

The current LOs use jargon ("OLS estimator", "Gauss-Markov assumptions", "gradient descent convergence") on the very first content slide. Rewrite with simpler TARGET descriptions while preserving Bloom level 4 verbs (Derive, Analyze, Evaluate, Compare).

Replace the entire `\begin{enumerate}...\end{enumerate}` block (lines 160-165) with:

```latex
  \begin{enumerate}
    \item \textbf{Derive} the best-fit line formula and explain why it minimizes prediction errors
    \item \textbf{Analyze} how a computer iteratively improves its predictions (gradient descent)
    \item \textbf{Evaluate} model quality using diagnostic plots and metrics ($R^2$, RMSE)
    \item \textbf{Compare} Ridge vs.\ Lasso regularization and select the right one for a given problem
  \end{enumerate}
```

**Bloom level check:** All 4 verbs remain at Bloom 4+ (Derive=L4, Analyze=L4, Evaluate=L5, Compare=L4). The change simplifies the TARGETS, not the cognitive level.

### Task 2.2: Add reassurance to L01 Road Map slide

**File:** `slides/L01_Introduction_Linear_Regression/L01_overview.tex`
**Slide:** 10 (line ~334, Road Map for Today)

After the `\end{enumerate}` on this slide, add:

```latex
\vspace{0.5em}
\textit{Don't worry if some formulas look unfamiliar --- we build up step by step, and the intuition matters more than memorizing equations.}
```

---

## Part 3: Worked Example Audit (1 task, bounded)

### Task 3.1: Verify formula slides have worked examples

**Scope:** Check L02, L03, L05, L06 overview files only (L01 and L04 already verified in prior audits).

**Definition:** A "worked example" is a 1-2 line numeric substitution showing concrete numbers plugged into the formula (e.g., "If income=50k and debt=10k, then P(default) = 0.23").

**Rules:**
- Add examples to EXISTING slides only — do NOT create new slides
- At most 1 new worked example per lecture (keep scope bounded)
- If multiple formula slides lack examples, choose the FIRST formula slide in the lecture
- Format: add a `\textbf{Example:}` block with 1-2 lines of arithmetic after the formula

**Files and priority formula slides:**
- `L02_overview.tex` — Slide 8 (sigmoid function): add numeric example like "If z=0, sigmoid(0)=0.5; if z=2, sigmoid(2)=0.88"
- `L03_overview.tex` — first distance/similarity formula slide: add numeric example
- `L05_overview.tex` — first PCA/eigenvalue slide: add numeric example
- `L06_overview.tex` — first embedding similarity slide: add numeric example

---

## Verification

1. Compile all 6 overview .tex files: `pdflatex -interaction=nonstopmode LXX_overview.tex`
2. Grep for "Overfull" in compilation output — must be 0
3. Count `\includegraphics.*images/` references in overview files — must be ≥ 13
4. Verify each overview has both opening AND closing cartoon images (not text-only)

## Acceptance Criteria

- [ ] Every overview lecture has opening AND closing cartoon image (13 total placements)
- [ ] 8 unique XKCD images used across overview lectures
- [ ] L01 learning objectives use accessible language with Bloom 4+ verbs preserved
- [ ] L01 has reassurance text on Road Map slide
- [ ] At most 4 worked examples added (one per unchecked lecture: L02, L03, L05, L06)
- [ ] All 6 overview PDFs compile with 0 Overfull warnings
- [ ] No new slides added (total slide count unchanged in each file)
