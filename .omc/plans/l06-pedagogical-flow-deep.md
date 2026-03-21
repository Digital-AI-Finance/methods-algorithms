# L06 Pedagogical Flow Deep Check

## Analysis Summary

**Files analyzed:**
- `L06_overview.tex`: 24 slides (7 intro + 14 core + 3 wrap-up), 4 charts (01, 03, 05, 07)
- `L06_deepdive.tex`: 42 main + 10 appendix = 52 slides, 9 charts (02, 04, 06, 08, 09, 10, 11, 12, 13)

**Overall assessment:** Good. Recent fixes (MVF cosine sim slide, question titles at 90%/92%, DQN split, Skip-gram reorder) significantly improved flow. Remaining issues are P2-P3 level.

---

## Slide-by-Slide Flow Trace

### Overview Flow

| From | To | Transition | Verdict |
|------|----|-----------|---------|
| 3 (Comic) | 4 (Text Challenge) | General ML hook → specific problem | OK |
| 4 (Text) | 5 (Decision) | Parallel structure, both "Core question:" | OK |
| 5 (Decision) | 6 (Why Care) | Problem → motivation | OK |
| 6 (Why Care) | 7 (LOs) | Motivation → objectives | OK |
| 8 (Problem) | 9 (Chart 01) | Text problem → embedding visual | OK (MVF: M→V) |
| 9 (Chart) | 10 (Word2Vec) | Visual → explanation | OK (MVF: V→F) |
| 10 (Word2Vec) | 11 (Cosine Sim) | How to make embeddings → how to measure them | OK |
| 11 (Cosine) | 12 (Static/Contextual) | Similarity → limitations of static embeddings | OK |
| **12 (Contextual)** | **13 (RL Loop)** | **Embeddings → RL with NO transition signal** | **P2: ABRUPT** |
| 13 (RL Loop) | 14 (Q-learning) | Visual loop → formula | OK (MVF: V→F) |
| 14 (Q-learning) | 15 (Reward Curves) | Algorithm → evidence it works | OK |
| **15 (RL chart)** | **16 (Sentiment)** | **RL → Embeddings with NO transition signal** | **P2: ABRUPT** |
| 16 (Sentiment) | 17 (Trading) | Embedding app → RL app | OK (parallel) |
| 17 (Trading) | 18 (Comparison) | RL app → comparison table | OK |
| 18-21 | Practice/Summary | Standard wrap-up | OK |

### Deepdive Flow

| From | To | Transition | Verdict |
|------|----|-----------|---------|
| 5 (One-hot problem) | 6 (Skip-gram arch) | Problem → visual architecture | OK (MVF: M→V) |
| 6 (Architecture) | 7 (Objective) | Visual → formula | OK (MVF: V→F) |
| 7 (Objective) | 8 (Neg Sampling) | Softmax → why it's expensive → solution | OK |
| 8 (Neg Sampling) | 9 (NS Illustrated) | Formula → visual illustration | OK |
| 9 (NS Chart) | 10 (NS Algorithm) | Visual → implementation | OK |
| 10 (Algorithm) | 11 (Analogies) | Implementation → "what can embeddings do?" | OK |
| 11 (Analogies) | 12 (Analogy Chart) | Text → visual | OK |
| 12 (Chart) | 13 (Limitations) | Show → critique | OK |
| **13 (Limitations)** | **14 (Cosine Sim)** | Critique → formal similarity measure | **P2: OUT OF ORDER** |
| 14 (Cosine) | 15 (Pre-trained) | Measure → available models | OK |
| 15 (Pre-trained) | 16 (Static/Context) | Models → disambiguation | OK |
| 16 (Static/Context) | 17 (Finance Apps) | Theory → application | OK |
| 17 (Finance Apps) | 18 (Worked Example) | Applications → concrete example | OK |
| 18 (Embeddings) | 19 (RL Framework) | Section break, clean | OK |
| 19-23 (RL Theory) | Progressive disclosure | Each builds on previous | OK |
| 23 (TD) | 24 (Q-Learning) | Foundation → specific algorithm | OK |
| 24 (Q-Learning) | 25 (Worked Example) | Formula → concrete calculation | Excellent |
| 25-27 | Algorithm → visual | Implementation → visual result | OK |
| 27-29 | Q-values → exploration | See values → how to use them | OK |
| 29-34 | Trading application | Formulation → evaluation → results | OK |
| 34-36 | Tabular → DQN | Natural "what if states are continuous?" | OK |
| 36-42 | Practice → Summary | Standard wrap-up | OK |

---

## Issues Found

### P2: Should Fix (4 issues)

#### Issue 1: Overview mentions DQN in two places, but DQN is never taught in overview
- **Location A:** `L06_overview.tex` line 438 (slide 22, Key Takeaways)
- **Text A:** "Q-learning and DQN provide practical algorithms for value-based control"
- **Location B:** `L06_overview.tex` line 401 (slide 20, What Are the Common Pitfalls?)
- **Text B:** "Start simple: tabular Q-learning before DQN or policy gradient"
- **Problem:** DQN is only covered in the deepdive (slides 35-36). Students seeing the overview alone encounter an unexplained term twice.
- **Fix A:** Change line 438 to "Q-learning provides a practical algorithm for value-based control"
- **Fix B:** Change line 401 to "Start simple: tabular Q-learning before more advanced methods"

#### Issue 2: Deepdive cosine similarity defined AFTER conceptual use
- **Location:** `L06_deepdive.tex` slide 14 (line 285)
- **Problem:** "Similar vectors" concept used in slide 5 (line 153: "Similar words → similar vectors"), slide 11 (vector arithmetic implying similarity), and slide 13 (evaluation methodology). Formal cosine similarity definition only at slide 14.
- **Analysis:** Moving slide 14 earlier would break the Skip-gram → Negative Sampling → Analogies narrative. Better to add a parenthetical forward-reference.
- **Fix:** On slide 5, line 153, change "Similar words $\rightarrow$ similar vectors" to "Similar words $\rightarrow$ similar vectors (via cosine similarity---defined later)"

#### Issue 3: Deepdive $\epsilon$-greedy forward reference
- **Location:** `L06_deepdive.tex` slide 24, line 496
- **Problem:** "Choose action $a$ ($\epsilon$-greedy)" is mentioned in Q-learning algorithm but not explained until slide 28 (4 slides later).
- **Fix:** Expand the parenthetical on line 496 from "($\epsilon$-greedy)" to "($\epsilon$-greedy: random with prob.\ $\epsilon$, greedy otherwise)"

#### Issue 4: Overview topic transitions between embeddings and RL are abrupt
- **Location:** `L06_overview.tex` slides 12→13 and 15→16
- **Problem:** No textual bridge when switching between embedding and RL content. The \section{Method} header covers both topics, making the transition invisible.
- **Fix (slide 12→13):** Slide 12 is already dense (2 sections, 5 bullets). Instead of adding body text, embed the transition in the bottomnote. Change `\bottomnote{Static: one meaning per word. Contextual: meaning adapts to context.}` to `\bottomnote{Static: one meaning per word. Contextual: meaning adapts to context. Next: sequential decisions.}`
- **Fix (slide 15→16):** Add at the start of slide 16 body: `\textit{Returning to embeddings---}` before "Worked Example"

### P3: Nice to Fix (3 issues)

#### Issue 5: Deepdive $\sigma$ (sigmoid) used without definition
- **Location:** `L06_deepdive.tex` slide 8, line 196
- **Problem:** Negative sampling formula uses $\log \sigma(...)$ without defining $\sigma$ as sigmoid.
- **Fix:** After the negative sampling formula (line 197), add: "where $\sigma(x) = 1/(1+e^{-x})$ is the sigmoid function."

#### Issue 6: Deepdive $f(w)$ used without definition in pseudocode
- **Location:** `L06_deepdive.tex` slide 10, line 224
- **Problem:** "$P_n(w) \propto f(w)^{3/4}$" uses $f(w)$ without defining it.
- **Fix:** Change line 224 to: `\STATE Sample $w_n \sim P_n(w) \propto f(w)^{3/4}$ \COMMENT{$f(w)$: word frequency}`

#### Issue 7: Deepdive $\alpha$ (learning rate) first appears without introduction
- **Location:** `L06_deepdive.tex` slide 23, line 466
- **Problem:** TD(0) formula uses $\alpha$ without first defining it as the learning rate.
- **Fix:** Change line 464 from `\textbf{TD(0) Update Rule} --- learn from each transition:` to `\textbf{TD(0) Update Rule} (learning rate $\alpha \in (0,1]$) --- learn from each transition:`

### Verified Clean (no action needed)

| Check | Result |
|-------|--------|
| MVF on core formulas | All main derivations properly motivated (Skip-gram: M→V→F via slides 5→6→7; Q-learning: slides 22→23→24→25; Cosine sim overview: full MVF with TikZ) |
| Chart dual-allocation | All 13 charts in exactly ONE file |
| Zone 1 Greek-free | Confirmed (overview slides 1-7) |
| Question-title coverage | Overview 90% (9/10 core), Deepdive 92% (24/26 core) - both above 80% |
| Opening/closing cartoons | Both files: XKCD #1838 opening + TikZ robot closing |
| Appendix markers | `\appendix` + `\section*` correct |
| Cross-file narrative arc | Overview = "why + high-level how"; Deepdive = "theory + implementation + applications" |
| Chart 03 absence in deepdive | Intentional --- overview provides the visual, deepdive goes straight to formalism for students who've already seen the loop |

---

## Execution Steps

### Step 1: Fix overview DQN forward references (2 locations)
- **File:** `L06_overview.tex`
- **Line 438 (slide 22 takeaways):** "Q-learning and DQN provide practical algorithms for value-based control" → "Q-learning provides a practical algorithm for value-based control"
- **Line 401 (slide 20 pitfalls):** "Start simple: tabular Q-learning before DQN or policy gradient" → "Start simple: tabular Q-learning before more advanced methods"

### Step 2: Add cosine similarity forward-reference in deepdive
- **File:** `L06_deepdive.tex`, line 153
- **Change:** "Similar words $\rightarrow$ similar vectors" → "Similar words $\rightarrow$ similar vectors (via cosine similarity---defined later)"

### Step 3: Expand $\epsilon$-greedy parenthetical in deepdive
- **File:** `L06_deepdive.tex`, line 496
- **Change:** "($\epsilon$-greedy)" → "($\epsilon$-greedy: random with prob.\ $\epsilon$, best otherwise)"

### Step 4: Add topic transition signals in overview slides 12 and 16
- **File:** `L06_overview.tex`
- **Slide 12 (line 273):** Change `\bottomnote{Static: one meaning per word. Contextual: meaning adapts to context.}` to `\bottomnote{Static: one meaning per word. Contextual: meaning adapts to context. Next: sequential decisions.}` (safe: fits in bottomnote, no overflow risk)
- **Slide 16 (line ~329):** After the frame title line, add: `\textit{Returning to embeddings---}` before "Worked Example"

### Step 5: Define $\sigma$ in deepdive negative sampling
- **File:** `L06_deepdive.tex`, line ~197
- **After** the negative sampling formula block, add a line: `where $\sigma(x) = 1/(1+e^{-x})$ is the sigmoid function.`

### Step 6: Define $f(w)$ in deepdive pseudocode
- **File:** `L06_deepdive.tex`, line 224
- **Change:** Add `\COMMENT{$f(w)$: word frequency}` at the end of the sampling line

### Step 7: Define $\alpha$ in deepdive TD slide
- **File:** `L06_deepdive.tex`, line 464
- **Change:** "TD(0) Update Rule --- learn from each transition:" → "TD(0) Update Rule (learning rate $\alpha \in (0,1]$) --- learn from each transition:"

### Step 8: Compile and verify
- Compile both files with pdflatex
- Verify 0 errors, 0 Overfull
- Verify page counts remain stable (overview ~24, deepdive ~52)

---

## Acceptance Criteria

1. All 4 P2 issues addressed (Steps 1-4)
2. All 3 P3 issues addressed (Steps 5-7)
3. Both files compile cleanly: 0 errors, 0 Overfull warnings
4. No new term-before-use violations introduced
5. Page counts stable (overview 24, deepdive 52 +/- 1)
6. No content removed beyond the DQN references in overview takeaways (line 438) and pitfalls (line 401)
