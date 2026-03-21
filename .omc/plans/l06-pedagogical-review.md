# L06 Pedagogical Review: Hostile Review + Fix Plan

## Task
Apply the pedagogical review skill to L06 (Embeddings & RL). Score all 10 dimensions, identify issues by severity, and plan surgical fixes.

## Files Under Review
- `slides/L06_Embeddings_RL/L06_overview.tex` (24 slides: 7 intro + 14 core + 3 wrap-up)
- `slides/L06_Embeddings_RL/L06_deepdive.tex` (41 main + 10 appendix = 51 slides)
- 13 chart folders (01-13), plus 13 unused "top10" chart folders

---

## Phase 1: Hostile Review Scores

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | Learning Objectives | 9/10 | Bloom's 4-5 (Derive, Evaluate, Analyze, Critique). Identical in both decks. |
| 2 | Opening Engagement | 8/10 | XKCD #1838 comic + two "core question" motivation slides. Good. |
| 3 | Progressive Disclosure | 7/10 | Zone 1 clean (0 formulas). But overview slide 9 dumps 4 equations at once. |
| 4 | Formula Introduction (MVF) | **5/10** | **Worst dimension.** Overview slide 9 = classic formula dump. Deepdive puts formulas before visuals. |
| 5 | Term Definitions | 7/10 | Overview slide 9 uses symbols before they're defined on later slides. |
| 6 | Visual Quality | 8/10 | 13 charts, good density. Both decks share same opening XKCD. |
| 7 | Worked Examples | 8/10 | Good: FinBERT sentiment, Q-learning step-by-step. Missing: cosine similarity numerical walkthrough. |
| 8 | Domain Integration | 9/10 | Excellent: FinBERT, trading agents, EU AI Act, transaction costs, walk-forward validation. |
| 9 | Structural Clarity | 7/10 | DQN section has only 1 slide. Question-based titles only ~36% (target: ~80%). |
| 10 | Closing & Synthesis | 8/10 | Overview: TikZ toolkit comic. Deepdive: text-only closing (no visual). |
| | **AVERAGE** | **7.6 (B-)** | |

### Systemic Issues
- **MVF violation**: The overview "Key Equations" slide (slide 9) presents 4 formulas cold with no preceding motivation or visual. This is the worst formula dump in the entire course.
- **Question titles deficit**: Only ~5/14 overview core slides use question-based titles (~36% vs ~80% target).
- **Shared XKCD**: Both decks use identical XKCD #1838 for opening comic (other lectures differentiate).

---

## Phase 2: Issue Classification

### P1 - Structural (fix in current cycle)

**P1.1: Overview slide 9 "Key Equations" is a formula dump**
- 4 equations (Skip-Gram, Cosine Sim, Bellman, TD Update) presented cold in rapid succession
- Violates MVF protocol: no motivation, no visual before any formula
- Violates progressive disclosure: terms used before defined ($w_t$, $c$, $\gamma$, $\alpha$, $Q^*$, $s'$)
- **Fix**: DELETE this slide entirely. The formulas appear naturally later:
  - Skip-Gram is covered on slides 11 (overview "From Words to Vectors")
  - Cosine similarity can get its own mini-slide in Method section
  - Bellman/Q-learning are covered on slide 14 (overview "Q-Learning at a Glance")
  - This removes the formula dump without losing any content

**P1.2: Deepdive Skip-Gram visual comes AFTER formula**
- Slide 6: Skip-gram formula (softmax equation)
- Slide 8: Negative sampling chart (chart 10)
- Slide 9: Skip-gram architecture chart (chart 08)
- The architecture diagram should come BEFORE the formula (MVF: Visualize before Formalize)
- **Fix**: Reorder deepdive slides 6-9:
  - Current: 6(formula) → 7(neg sampling challenge) → 8(neg sampling chart) → 9(architecture chart)
  - Proposed: current-9(architecture chart) → current-6(formula) → current-7(neg sampling challenge) → current-8(neg sampling chart)
  - This makes the visual precede the formula

### P2 - Pedagogical Flow (fix in current cycle)

**P2.1: Question-based titles - overview**
Convert these declarative titles to questions (~80% target):

| Current (Declarative) | Proposed (Question) | Slide |
|------------------------|---------------------|-------|
| "The Business Problem" | "Why Can't Machines Read Text?" | 8 |
| "Key Equations" | DELETE (see P1.1) | 9 |
| "From Words to Vectors" | "How Do We Turn Words Into Numbers?" | 11 |
| "Static vs. Contextual Embeddings" | "Does 'Bank' Always Mean the Same Thing?" | 12 |
| "Q-Learning at a Glance" | "How Does an Agent Learn from Rewards?" | 14 |
| "Learning Progress" | "Does the Agent Actually Improve?" | 15 |
| "Embeddings vs. Reinforcement Learning" | "Embeddings vs. RL: When Do You Use Which?" | 18 |
| "Practical Tips" | "What Are the Common Pitfalls?" | 20 |
| "Hands-on Exercise" | "Can You Build It Yourself?" | 21 |

**Convention**: Chart-only slides (containing only `\includegraphics` with no bullet text) are excluded from the question-title denominator.

**Post-fix overview core zone count** (after deleting slide 9, adding cosine sim slide):
- Core zone: 14 slides (8-21, with slide 9 replaced by cosine sim slide)
- Chart-only slides (excluded): slide 10 (Word Embedding Space), slide 15 (Learning Progress), slide 19 (Decision Framework) = 3
- Content slides in denominator: 14 - 3 = 11
- After converting 8 titles (slide 9 deleted, 8 remaining from table above): 8/11 = 73%
- Need 1 more conversion to reach 80%: "Embeddings in Finance: Sentiment Analysis" (slide 16) → "How Can Embeddings Detect Market Sentiment?"
- **Final: 9/11 = 82%** (meets ≥80% target)

**P2.2: Add cosine similarity motivation + mini-example to overview**
- After deleting slide 9, add a brief cosine similarity slide in the Method section (between current slides 11 and 12)
- Content: "How Do We Measure Word Similarity?" with:
  - Plain English: "Cosine similarity measures the angle between two vectors"
  - Simple 2D visual analogy: two arrows, angle between them
  - Formula: $\text{sim}(u,v) = \frac{u \cdot v}{\|u\|\|v\|}$
  - Numeric mini-example: Given $u = [3, 4]$ and $v = [4, 3]$, compute: dot=24, $\|u\|=5$, $\|v\|=5$, $\text{sim} = 24/25 = 0.96$ (clean integers, verifiable arithmetic)
- This follows MVF: motivate (why measure similarity?) → visualize (angle diagram) → formalize (formula + numbers)

**P2.3: Deepdive DQN section too thin (1 slide)**
- Slide 35 crams DQN loss function + experience replay + target network + chart into one slide
- **Fix**: Split into 2 slides:
  - Slide 35a: "Why Do We Need Deep Q-Networks?" - motivation (tabular Q fails with large state spaces) + the core idea (neural net approximates Q) + DQN loss formula
  - Slide 35b: "How Does DQN Stay Stable?" - experience replay + target network (the two key innovations) + chart 09

**P2.4: Question-based titles - deepdive**
Convert key declarative titles (target ~80% of content slides):

| Current | Proposed | Slide |
|---------|----------|-------|
| "Word Embeddings: The Representation Problem" | "Why Can't One-Hot Vectors Capture Meaning?" | 5 |
| "Word2Vec: Skip-gram" | "How Does Skip-Gram Learn Word Meaning?" | 6 |
| "Skip-gram: Computational Challenge" | "Why Is Full Softmax Too Expensive?" | 7 |
| "Word Analogies" | "Can Vectors Solve Analogies?" | 11 |
| "Word Analogy Limitations" | "When Do Word Analogies Fail?" | 13 |
| "Pre-trained Embeddings" | "Should You Train Your Own Embeddings?" | 15 |
| "Static vs Contextual Embeddings" | "Does Context Change a Word's Meaning?" | 16 |
| "Embeddings in Finance" | "How Do Banks Use Word Embeddings?" | 17 |
| "The RL Framework" | "What Are the Building Blocks of RL?" | 19 |
| "Markov Decision Process" | "What Makes a Problem Markovian?" | 20 |
| "Policy and Value Functions" | "How Do We Measure a Strategy's Worth?" | 21 |
| "Bellman Equation" | "Why Is the Bellman Equation Recursive?" | 22 |
| "Temporal Difference Learning" | "Can We Learn Without Waiting for the End?" | 23 |
| "Q-Learning Algorithm" | "How Does Q-Learning Find the Best Action?" | 24 |
| "Exploration vs Exploitation" | "Explore or Exploit: How Do You Choose?" | 28 |
| "RL for Trading" | "Can an Algorithm Learn to Trade?" | 30 |
| "Backtesting RL Trading Strategies" | "How Do You Know Your RL Strategy Works?" | 32 |
| "Skip-Gram with Negative Sampling: Algorithm" | "How Does Negative Sampling Work in Practice?" | 10 |
| "Similarity Measures" | "How Do We Measure Closeness in Vector Space?" | 14 |
| "Finance Example: Embedding-Based Sentiment" | "How Would You Classify This Headline?" | 18 |
| "Q-Learning: Worked Example" | "What Happens in One Q-Learning Update?" | 25 |
| "Trading Reward Function Design" | "How Do You Design the Right Reward Signal?" | 31 |
| "Deep Q-Networks (DQN)" | "What If the State Space Is Too Large for a Table?" | 35 |

**Note**: Slide numbers in this table refer to PRE-reorder numbering (before Step 5). After Step 5 reorders slides 6-9, slides 6-9 shift but all other slide numbers remain unchanged since the total count stays the same.

**Post-fix deepdive count**:
- Total main content slides (excluding title, outline, comic, LOs, hands-on, decision framework table, takeaways, closing, 2x references): ~31 content slides
- Chart-only slides (excluded from denominator): slides 8, 9, 12, 27, 29, 33, 34 = 7
- Content slides in denominator: 31 - 7 = 24
- Conversions: 17 (original) + 6 (added above) = 23
- **Final: 23/24 = 96%** (far exceeds ≥80% target)

### P3 - Engagement (fix if time permits)

**P3.1: Both decks use identical XKCD #1838 opening**
- Other lectures differentiate: e.g., L01 overview has different comic than L01 deepdive
- **Fix**: Keep XKCD #1838 for overview. For deepdive, either:
  - (a) Use XKCD #2173 "Trained a Neural Net" or another relevant XKCD, OR
  - (b) Keep the same XKCD but change the framing title to make it a different pedagogical point (currently: overview = "When All You Have Is Linear Algebra...", deepdive = "Pouring Data into Linear Algebra" -- these are already different, which is acceptable)
  - **Decision**: Option (b) is acceptable. The titles already differentiate. LOW priority. SKIP.

**P3.2: Deepdive closing is text-only (no visual)**
- Slide 39 is a text-based callback to XKCD #1838 (no actual image)
- Overview slide 23 has a TikZ comic -- good
- **Fix**: Add a simple TikZ visual to the deepdive closing OR include the XKCD image. Since this is the LAST lecture of the course, a course-recap visual would be impactful.
- **Decision**: Convert deepdive slide 39 to include a small TikZ illustration alongside the text. Reuse the overview's "ML Toolkit" TikZ concept but simplified.

### P4 - Polish

**P4.1: Deepdive slide 10 uses manual bottomnote**
- Lines 234-238 manually construct the bottomnote instead of using `\bottomnote{}`
- **Fix**: Replace manual construction with `\bottomnote{Mikolov et al.\ (2013). Distributed representations of words and phrases. NeurIPS, 3111--3119.}`

**P4.2: Overview slide 2 bottomnote is meta-commentary**
- "Three zones: Introduction, Core Content (PMSP), and Wrap-Up" -- this is about the SLIDE STRUCTURE, not content
- Students don't need to know about zones
- **Fix**: Change to content-relevant note: "Two topics today: text embeddings and reinforcement learning"

---

## Phase 3: Fix Plan (Execution Steps)

### Step 1: Overview - Delete "Key Equations" slide 9 (P1.1)
- **File**: `L06_overview.tex`
- **Action**: Remove lines 212-236 (the entire slide 9 frame)
- **Verify**: Overview now has 23 slides (was 24). Slide numbering shifts down by 1 for all subsequent slides.
- **Side effect**: The Bellman and Q-learning equations now only appear on slide 13 (renumbered from 14) "Q-Learning at a Glance" which already has good context. Skip-Gram already appears on slide 10 (renumbered from 11). Cosine similarity will be covered by new slide (Step 2).

### Step 2: Overview - Add cosine similarity MVF slide (P2.2)
- **File**: `L06_overview.tex`
- **Action**: Insert new slide after current slide 11 (which becomes slide 10 after Step 1) "From Words to Vectors"
- **Content**: "How Do We Measure Word Similarity?"
  - 1 sentence motivation
  - TikZ: two vectors with angle θ
  - Cosine similarity formula
  - Numeric example: $u=[3, 4]$, $v=[4, 3]$, dot=24, $\|u\|=\|v\|=5$, $\text{sim}=24/25=0.96$ (clean integers)
  - Bottomnote
- **Verify**: Overview back to 24 slides. Net: replaced formula dump with focused MVF slide.

### Step 3: Overview - Convert declarative titles to questions (P2.1)
- **File**: `L06_overview.tex`
- **Action**: Replace 9 frame titles per the table in P2.1
- **Verify**: Count question-mark titles in core zone. Target: ≥80%.

### Step 4: Overview - Fix outline bottomnote (P4.2)
- **File**: `L06_overview.tex`
- **Action**: Change bottomnote on slide 2 from "Three zones..." to "Two topics today: text embeddings and reinforcement learning"

### Step 5: Deepdive - Reorder Skip-Gram visual before formula (P1.2)
- **File**: `L06_deepdive.tex`
- **Action**: Move current slide 9 (Skip-gram Architecture, chart 08) to become the NEW slide 6, pushing current slides 6-8 down by one position.
- **New order**: 5(Representation Problem) → 6(Architecture chart) → 7(Skip-gram formula) → 8(Computational Challenge) → 9(Negative Sampling chart)
- **Verify**: Visual now precedes formula (MVF: Visualize → Formalize).
- **CRITICAL DEPENDENCY**: This reorder changes slide numbering for slides 6-9 ONLY. The P2.4 title-conversion table uses PRE-reorder numbering. After this step, old slide 6 becomes new slide 7, old slide 7 becomes new slide 8, old slide 8 becomes new slide 9, and old slide 9 becomes new slide 6. Step 7 (title conversions) must use the actual frame titles (not slide numbers) to locate the correct frames. All slides outside the 6-9 range are unaffected.

### Step 6: Deepdive - Split DQN into 2 slides (P2.3)
- **File**: `L06_deepdive.tex`
- **Action**: Replace current slide 35 with two slides:
  - Slide 35a: "Why Do We Need Deep Q-Networks?" -- Motivation (tabular fails at scale) + core idea + DQN loss formula
  - Slide 35b: "How Does DQN Stay Stable?" -- Experience replay + target network + chart 09
- **Verify**: Deepdive now has 42 main slides (was 41). Within budget.

### Step 7: Deepdive - Convert declarative titles to questions (P2.4)
- **File**: `L06_deepdive.tex`
- **Action**: Replace 23 frame titles per the table in P2.4 (17 original + 6 added per Critic feedback)
- **IMPORTANT**: Use frame title text (not slide numbers) to locate frames, since Step 5 shifted slides 6-9.
- **Verify**: Count question-mark titles in content slides (excluding chart-only). Target: ≥80%. Expected: 23/24 = 96%.

### Step 8: Deepdive - Fix manual bottomnote on slide 10 (P4.1)
- **File**: `L06_deepdive.tex`
- **Action**: Replace lines 234-238 (manual bottomnote) with `\bottomnote{Mikolov et al.\ (2013). Distributed representations of words and phrases. \textit{NeurIPS}, 3111--3119.}`

### Step 9: Deepdive - Add visual to closing slide (P3.2)
- **File**: `L06_deepdive.tex`
- **Action**: Add a small TikZ illustration to slide 39 (closing thought). Keep the existing text but add a simple visual element (e.g., small robot/figure with a speech bubble to match the overview's pattern).

### Step 10: Compile and verify
- Compile both files with `pdflatex -interaction=nonstopmode`
- Check: 0 errors, 0 Overfull hbox warnings
- Verify slide counts: Overview ~24, Deepdive ~42 main + 10 appendix

---

## Phase 4: Acceptance Criteria

| # | Criterion | How to Verify |
|---|-----------|---------------|
| 1 | No formula dump in overview | Slide 9 "Key Equations" is gone; each formula has MVF context |
| 2 | Cosine similarity has MVF treatment in overview | New slide with motivation + visual + formula + example |
| 3 | Question-based titles ≥80% in both decks | Count titles with "?" in core zones |
| 4 | Deepdive architecture visual precedes Skip-Gram formula | Slide order check |
| 5 | DQN has 2 slides in deepdive | Section check |
| 6 | Manual bottomnote fixed | Grep for manual rule construction |
| 7 | Both PDFs compile clean | 0 errors, 0 Overfull |
| 8 | Slide counts within budget | Overview ≤26, Deepdive main ≤45 |
| 9 | Deepdive closing has visual element | Visual inspection |

---

## Phase 5: Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Deleting slide 9 loses important equations | Verified: all 4 equations appear elsewhere in both decks |
| Reordering deepdive slides breaks cross-references | No internal cross-references in affected slides |
| New cosine similarity slide causes overflow | Use TikZ (compact) + keep to 3-4 bullets |
| DQN split creates redundancy with appendix A5 | A5 covers extensions (Double DQN, Dueling); main slides cover basics only |
| Title changes break TOC | Section markers are separate from frame titles; TOC unaffected |

---

## Summary

**Current**: 7.6/10 (B-)
**Projected after fixes**: ~8.3/10 (B+)

Estimated post-fix scores: LOs 9, Opening 8, Progressive Disclosure 8, MVF 7.5, Term Definitions 8, Visual Quality 8.5, Worked Examples 8.5, Domain Integration 9, Structural Clarity 8.5, Closing 8.5 = 83.5/100.

**10 execution steps**, touching 2 files. No chart changes needed. No new charts. Pure LaTeX edits.
