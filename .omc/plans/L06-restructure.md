# L06 Restructure Plan: Embeddings & RL

**Plan ID:** L06-restructure
**Created:** 2026-02-13
**Revised:** 2026-02-13 (iteration 2 -- Critic fixes applied)
**Status:** READY FOR EXECUTION
**Base Path:** `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L06_Embeddings_RL`

---

## 1. Executive Summary

### What Changes

Restructure both L06 slide files to match the slide creation skill v3 architecture established in L05:

1. **L06_overview.tex**: Apply three-zone architecture (Introduction / Core Content PMSP / Wrap-Up), add XKCD opening image and closing text callback, relocate LOs to end of Zone 1, expand from 16 to 24 slides.

2. **L06_deepdive.tex**: Add `\appendix` + `\section*{Advanced Topics}` structure, add XKCD opening image and closing text callback, move derivations and proofs to appendix, expand from 33 to 50 slides (42 main + 8 appendix).

3. **Chart allocation**: Reassign the 10 available charts so each appears in exactly ONE file (currently all 7 used charts are duplicated in both files).

4. **Hostile review fixes preservation**: All content added during the hostile review fix phase (negative sampling, TD learning, worked examples, static vs. contextual embeddings, word analogy limitations, DQN loss, policy gradient details, statistical inference, backtesting, reward design) is already present in the current deepdive.tex and MUST be retained verbatim.

### Why

- L05 overview and deepdive already follow the v3 architecture and serve as the reference pattern
- The hostile review report (2026-02-06, score 35/100) identified structural issues including chart redundancy, missing XKCD, and no appendix -- many content fixes have since been applied but the structural framing has not
- Consistent slide architecture across all 6 lectures improves navigability for students and reduces cognitive load
- The three-zone architecture places LOs after the motivational hook, which is pedagogically superior to the current LO-first layout

### What Does NOT Change

- Lines 1-92 of both files (the standard beamer preamble) -- UNTOUCHED
- The `\institute{MSc Data Science}` line in both files -- ALREADY PRESENT
- All chart .py files and their outputs -- NO CHART CODE CHANGES
- All content from hostile review fixes -- PRESERVED IN FULL

---

## 2. XKCD Image Strategy

### Comics Selected

| Slot | Comic | Title | Rationale |
|------|-------|-------|-----------|
| Opening (both files) | XKCD #1838 | "Machine Learning" | Already referenced in L06 instructor guide; directly relevant to both embeddings and RL; the comic about "stirring the pile of linear algebra until it starts looking right" captures the lecture theme perfectly |
| Closing (both files) | XKCD #1838 callback | Text-only callback | No second XKCD image needed; use a text callback to the opening comic, adapted to the lecture content (same pattern as L05 which uses #2048 opening and #2400-inspired text closing) |

### Image File Requirements

**Action Required:** Create directory and download image.

```
mkdir slides/L06_Embeddings_RL/images/
```

Download XKCD #1838 from: `https://imgs.xkcd.com/comics/machine_learning.png`
Save as: `slides/L06_Embeddings_RL/images/1838_machine_learning.png`

### Attribution Format

Opening slide bottomnote (both files):
```latex
\bottomnote{XKCD \#1838 ``Machine Learning'' by Randall Munroe (CC BY-NC 2.5)}
```

Closing slide bottomnote (both files):
```latex
\bottomnote{Callback to XKCD \#1838 by Randall Munroe (CC BY-NC 2.5)}
```

---

## 3. Chart Allocation Table

**Rule:** Each chart in EXACTLY ONE file. Zero dual-assignment.

| # | Chart | File | Rationale |
|---|-------|------|-----------|
| 01 | `01_word_embedding_space` | **overview** | Visual hook for embeddings topic; no formulas needed |
| 02 | `02_similarity_heatmap` | **deepdive** | Accompanies cosine similarity derivation |
| 03 | `03_rl_loop` | **overview** | Conceptual RL introduction; no formulas needed |
| 04 | `04_q_learning_grid` | **deepdive** | Accompanies Q-learning worked example |
| 05 | `05_reward_curves` | **overview** | Visual RL results for overview audience |
| 06 | `06_policy_viz` | **deepdive** | Accompanies trading policy discussion |
| 07 | `07_decision_flowchart` | **overview** | Decision framework is an overview-level concern |
| 08 | `08_skipgram_architecture` | **deepdive** | Architecture diagram for Skip-gram theory |
| 09 | `09_dqn_architecture` | **deepdive** | DQN architecture for deep RL theory |
| 10 | `10_negative_sampling` | **deepdive** | Negative sampling illustration for theory section |

**Summary:** Overview gets 4 charts (01, 03, 05, 07). Deepdive gets 6 charts (02, 04, 06, 08, 09, 10).

**Verification:** 4 + 6 = 10. All 10 charts assigned. Zero overlap. Zero unassigned.

---

## 4. Overview Slide-by-Slide Specification (24 slides)

### Preamble (Lines 1-92): UNCHANGED

Lines 93-97 (title block): Keep as-is:
```latex
\title[L06: Embeddings \& RL]{L06: Embeddings \& RL}
\subtitle{Text Representations and Sequential Decision Making}
\author{Methods and Algorithms}
\institute{MSc Data Science}
\date{Spring 2026}
```

### ZONE 1: INTRODUCTION (7 slides, NO formulas, NO Greek letters)

Comment banner before Zone 1:
```latex
% ============================================================
% ZONE 1: INTRODUCTION (7 slides, NO formulas, NO Greek letters)
% ============================================================
```

**Slide 1: Title Page**
```
\begin{frame}
\titlepage
\end{frame}
```
- Standard title page, no modifications needed

**Slide 2: Outline**
```
\begin{frame}{Outline}
  \tableofcontents
\bottomnote{Three zones: Introduction, Core Content (PMSP), and Wrap-Up}
\end{frame}
```
- Add bottomnote matching L05 pattern

**Slide 3: Opening Comic (XKCD #1838)**
```
\begin{frame}[t]{When All You Have Is Linear Algebra...}
\vspace{0.3em}
\begin{center}
\includegraphics[height=0.70\textheight]{images/1838_machine_learning.png}
\end{center}
\vspace{0.2em}
\begin{center}
\textit{``You pour the data into this big pile of linear algebra,
then collect the answers on the other side.''}
\end{center}
\bottomnote{XKCD \#1838 ``Machine Learning'' by Randall Munroe (CC BY-NC 2.5)}
\end{frame}
```
- Frame title is a thematic hook, not the comic title
- Image centered at 0.70\textheight (matching L05 pattern)
- Quote from the comic below the image
- CC BY-NC 2.5 attribution in bottomnote

**Slide 4: The Text Data Challenge**
- Content: Financial news, reports, social media contain valuable signals; text is unstructured -- how to feed it to ML models?; need to capture semantic meaning ("bullish" similar to "positive")
- Bottomnote: "Embeddings turn text into numbers that ML models can process"
- NO formulas, NO Greek letters
- Source: adapted from current overview slide "The Business Problem" (lines 122-136), embeddings half only

**Slide 5: The Sequential Decision Challenge**
- Content: Trading requires sequences of buy/sell/hold decisions; actions have delayed consequences (profit realized later); classic problem: explore new strategies or exploit known ones?
- Bottomnote: "Reinforcement learning: learning from trial and error with delayed rewards"
- NO formulas, NO Greek letters
- Source: adapted from current overview slide "The Business Problem" (lines 122-136), RL half only
- Rationale: Splitting the current combined slide into two separate motivation slides gives each topic proper space

**Slide 6: Why Banks and Asset Managers Care**
- Content: Highlight with finance-specific use cases for both topics
  - Embeddings: sentiment analysis for trading signals, document similarity for compliance, entity recognition for news feeds
  - RL: algorithmic trading, portfolio rebalancing, optimal execution
- Bottomnote: "Both techniques address real problems in quantitative finance and risk management"
- NO formulas, NO Greek letters
- NEW SLIDE: fills the finance-hook role that Zone 1 requires (matching L05 slide 6 "Why Banks Care")

**Slide 7: Learning Objectives**
- Content: Preserve the existing 4 LOs verbatim from current overview (lines 112-120):
  1. Derive the Skip-Gram objective and analyze the negative sampling approximation
  2. Evaluate static vs. contextual embeddings for domain-specific NLP tasks (e.g., FinBERT)
  3. Analyze the convergence properties of Q-learning and the role of the exploration-exploitation tradeoff
  4. Critique RL-based trading strategies and their limitations (transaction costs, non-stationarity, overfitting)
- Add: `\textbf{Finance Application:} Sentiment analysis (FinBERT), algorithmic trading (Q-learning)`
- Bottomnote: `Bloom's taxonomy levels 4--5: Analyze, Evaluate, Derive, Critique`
- POSITION: End of Zone 1 (after motivation), matching L05 pattern

### ZONE 2: CORE CONTENT (14 slides, PMSP sections)

Comment banner:
```latex
% ============================================================
% ZONE 2: CORE CONTENT (14 slides, PMSP sections)
% ============================================================
```

#### \section{Problem}

**Slide 8: The Business Problem**
- Content: Combine the two challenges into a problem statement:
  - Text data: one-hot encoding wastes dimensions, loses semantics; "king" and "queen" equally distant from "car"
  - Sequential decisions: supervised learning needs labels, but trading provides only delayed profit/loss signals
- Bottomnote: "Embeddings solve the text problem; RL solves the sequential decision problem"
- Source: adapted from current overview "Why Is This Hard?" (lines 138-149) and deepdive "Part 1" (lines 112-127)

**Slide 9: Key Equations**
- Content: Preserve the current "Key Equations" slide content (lines 153-174) with all four formulas:
  - Skip-Gram Objective
  - Cosine Similarity
  - Bellman Equation
  - TD Update (Q-Learning)
- Bottomnote: "These four equations are the mathematical backbone of this lecture"
- Source: current overview lines 153-174 -- PRESERVE VERBATIM

#### \section{Method}

**Slide 10: Word Embedding Space (CHART 01)**
- Content: Chart 01_word_embedding_space at 0.65\textwidth
- Bottomnote: "Similar words cluster together in embedding space"
- Source: current overview lines 176-181

**Slide 11: From Words to Vectors**
- Content: Explain the core idea of embeddings conceptually:
  - Distributional hypothesis: "You shall know a word by the company it keeps" (Firth, 1957)
  - Dense vectors (50-300 dimensions) vs. sparse one-hot
  - Word2Vec learns embeddings by predicting context from target
- Bottomnote: "Word2Vec: the breakthrough that made word embeddings practical (Mikolov et al., 2013)"
- NEW SLIDE: bridges the chart to the equation; the overview currently jumps from chart to chart without explanation

**Slide 12: Static vs. Contextual Embeddings**
- Content: Key distinction at overview level (no formulas):
  - Static (Word2Vec, GloVe): one fixed vector per word; "bank" same in all contexts
  - Contextual (BERT, FinBERT): different vectors based on sentence; "bank" differs in "river bank" vs. "bank account"
  - State-of-the-art: contextual models solve polysemy
- Bottomnote: "Static: one meaning per word. Contextual: meaning adapts to context."
- Source: deepdive lines 280-297 (simplified for overview)

**Slide 13: RL: Agent-Environment Loop (CHART 03)**
- Content: Chart 03_rl_loop at 0.55\textwidth
- Additional text: Key components listed (Agent, Environment, State, Action, Reward) -- 5 bullets max
- Bottomnote: "Agent takes actions, receives rewards, learns optimal policy"
- Source: current overview lines 190-195, enhanced with component list from deepdive lines 342-358

**Slide 14: Q-Learning at a Glance**
- Content: The Q-learning update rule (already in slide 9 equations), but now with a brief conceptual explanation:
  - Q(s,a) = expected total reward from state s, action a
  - Update: blend old estimate with new information (learning rate alpha)
  - Exploration vs exploitation: epsilon-greedy strategy
- Bottomnote: "Q-learning: the foundation of value-based reinforcement learning"
- Source: condensed from deepdive Q-learning slides

#### \section{Solution}

**Slide 15: Learning Progress (CHART 05)**
- Content: Chart 05_reward_curves at 0.65\textwidth
- Bottomnote: "RL agents improve through exploration and exploitation over many episodes"
- Source: current overview lines 206-211

**Slide 16: Embeddings in Finance: Sentiment Analysis**
- Content: The worked sentiment example, simplified for overview level:
  - Task: classify "Fed signals rate hike" as positive or negative
  - Method: compare sentence embedding to sentiment anchors via cosine similarity
  - Result: negative sentiment (rate hikes = tighter policy)
  - Real-world: FinBERT for production (up to 87% accuracy, Araci 2019)
- Bottomnote: "Simplified example --- real embeddings are 300-768 dimensions"
- Source: deepdive lines 317-337 (abbreviated)

**Slide 17: RL in Finance: Trading Agents**
- Content: Overview-level summary of RL for trading:
  - State: price history, portfolio, technical indicators
  - Action: buy, sell, hold
  - Reward: profit/loss minus transaction costs
  - Challenge: non-stationary markets, overfitting, partial observability
- Bottomnote: "RL for trading is an active research area; not a solved problem"
- Source: deepdive lines 537-553 (condensed)

**Slide 18: Comparison Table (Condensed)**
- Content: Condensed 3-row comparison table for overview audience:
  - Row 1: Input -- Text data vs. Sequential decisions
  - Row 2: Learns -- Semantic representations vs. Optimal policy
  - Row 3: Finance Use -- Sentiment analysis vs. Trading strategies
- Bottomnote: "Both transform complex inputs into learnable representations"
- NOTE: This is the CONDENSED version (3 rows). The deepdive slide 36 has the FULL version (6 rows). This avoids verbatim duplication between the two files.
- Source: deepdive lines 684-701 (abbreviated to 3 key rows)

#### \section{Practice}

**Slide 19: Decision Framework (CHART 07)**
- Content: Chart 07_decision_flowchart at 0.55\textwidth
- Bottomnote: "Embeddings for text, RL for sequential decisions with delayed rewards"
- Source: current overview lines 235-240

**Slide 20: Practical Tips**
- Content: Concise practical guidance for both topics:
  - Embeddings: start with pre-trained, fine-tune if needed; check domain match; visualize with t-SNE
  - RL: start simple (tabular Q-learning before DQN); reward shaping is crucial; normalize observations
- Bottomnote: "Both domains: start simple, iterate, validate thoroughly"
- Source: deepdive lines 726-742 (condensed)

**Slide 21: Hands-on Exercise**
- Content: Preserve existing hands-on content (lines 222-231):
  - Exercise 1: Explore word embeddings with Word2Vec
  - Exercise 2: Implement basic Q-learning
  - Exercise 3: Apply RL to a simple trading environment
  - Colab link
- Bottomnote: "Notebooks available on the course GitHub page --- see the L06 folder"

### ZONE 3: WRAP-UP (3 slides)

Comment banner:
```latex
% ============================================================
% ZONE 3: WRAP-UP (3 slides)
% ============================================================
```

#### \section{Summary}

**Slide 22: Key Takeaways**
- Content:
  - Embeddings: dense vector representations capture semantic similarity; use pre-trained (Word2Vec, GloVe, FinBERT)
  - RL: agent learns from environment interaction; Q-learning (tabular) and DQN (deep)
  - Finance: sentiment analysis with embeddings, trading strategies with RL
  - Key insight: different tools for different problems --- embeddings for text, RL for sequential decisions
- Bottomnote: "Course complete! Apply these methods in your capstone project"
- Source: deepdive lines 744-761 (adapted)

**Slide 23: Closing Comic (XKCD #1838 Text Callback)**
```
\begin{frame}[t]{Closing Thought}
\vspace{2em}
\begin{center}
\Large\textit{``We poured financial news into a pile of linear algebra}

\textit{and got sentiment scores on the other side.}

\vspace{0.5em}

\textit{Then we poured the sentiment scores into a reinforcement learner}

\textit{and got a trading strategy on the other side.}

\vspace{0.5em}

\textit{The strategy said: `Buy and hold.'\,''}
\end{center}

\vspace{1em}
\begin{center}
\normalsize --- Adapted from XKCD \#1838 ``Machine Learning'' by Randall Munroe
\end{center}
\bottomnote{Callback to XKCD \#1838 by Randall Munroe (CC BY-NC 2.5)}
\end{frame}
```
- Text-only callback referencing the opening comic's "pile of linear algebra" theme
- Punchline ties both lecture topics together with a wry finance ending
- Pattern: matches L05 closing (text adaptation of opening comic)

**Slide 24: References**
- Content: Keep Mikolov et al. (2013), Sutton & Barto (2018), Jurafsky & Martin (2024)
- REMOVE: James et al. (ISLR) -- not relevant to L06 (hostile review Mo3)
- ADD: Araci (2019) for FinBERT
- Bottomnote: "Sutton \& Barto: the definitive RL textbook (free at incompleteideas.net)"
- Source: current overview lines 244-251, corrected per hostile review

---

## 5. Deepdive Slide-by-Slide Specification (50 slides: 42 main + 8 appendix)

### Preamble (Lines 1-92): UNCHANGED

Lines 93-97 (title block): Keep as-is:
```latex
\title[L06: Embeddings \& RL Deep Dive]{L06: Embeddings \& RL}
\subtitle{Deep Dive: Theory, Implementation, and Applications}
\author{Methods and Algorithms}
\institute{MSc Data Science}
\date{Spring 2026}
```

### MAIN BODY (42 slides)

Comment banner:
```latex
% ============================================================
% MAIN BODY (42 slides)
% ============================================================
```

**Slide 1: Title Page** -- standard titlepage

**Slide 2: Outline** -- \tableofcontents

**Slide 3: Opening Comic (XKCD #1838)**
```
\begin{frame}{Pouring Data into Linear Algebra}
\begin{center}
\includegraphics[height=0.65\textheight]{images/1838_machine_learning.png}
\end{center}
\bottomnote{XKCD \#1838 ``Machine Learning'' by Randall Munroe (CC BY-NC 2.5)}
\end{frame}
```
- Matches L05 deepdive pattern (slide 3 opening comic)

**Slide 4: Learning Objectives**
- Content: Use the same 4 LOs listed in Overview Slide 7:
  1. Derive the Skip-Gram objective and analyze the negative sampling approximation
  2. Evaluate static vs. contextual embeddings for domain-specific NLP tasks (e.g., FinBERT)
  3. Analyze the convergence properties of Q-learning and the role of the exploration-exploitation tradeoff
  4. Critique RL-based trading strategies and their limitations (transaction costs, non-stationarity, overfitting)
- Add Finance Applications bullet list below (matching L05 deepdive slide 4 pattern)
- Bottomnote: `Bloom's Levels 4--5: Analyze, Evaluate, Derive, Critique`
- Source: current deepdive lines 111-127 -- CONTENT PRESERVED but reframe to match L05 format

#### \section{Word Embeddings}

**Slide 5: Part 1: Word Embeddings Introduction**
- Content: PRESERVE current deepdive lines 112-127 (one-hot encoding problem, dense embedding solution, Firth quote)
- Bottomnote: "You shall know a word by the company it keeps -- Firth, 1957"

**Slide 6: Word2Vec: Skip-gram**
- Content: PRESERVE current deepdive lines 131-144 (softmax objective, training procedure)
- Source: lines 131-144

**Slide 7: Skip-gram: Computational Challenge**
- Content: PRESERVE current deepdive lines 146-166 (intractability of full softmax, negative sampling solution, SGNS objective)
- This is a HOSTILE REVIEW FIX (C1) -- MUST PRESERVE
- Source: lines 146-166

**Slide 8: Negative Sampling Illustrated (CHART 10)**
- Content: PRESERVE current deepdive lines 168-173 (chart 10_negative_sampling)
- Chart at 0.55\textwidth
- Source: lines 168-173

**Slide 9: Skip-gram Architecture (CHART 08)**
- Content: PRESERVE current deepdive lines 175-180 (chart 08_skipgram_architecture)
- Chart at 0.55\textwidth
- Source: lines 175-180

**Slide 10: Skip-Gram with Negative Sampling: Algorithm**
- Content: PRESERVE current deepdive lines 182-201 (SGNS pseudocode -- algorithmic environment)
- This is a HOSTILE REVIEW FIX (M4) and INSTRUCTOR GUIDE requirement -- MUST PRESERVE
- Source: lines 182-201

**Slide 11: Word Analogies**
- Content: PRESERVE current deepdive lines 210-228 (king-man+woman=queen, finance examples, how it works)
- Bottomnote: "Embeddings capture relational structure, not just similarity"
- Source: lines 210-228
- NOTE: This slide replaces the former "Word Embedding Space" chart slide. Chart 01 is now overview-only; this slot uses the existing word analogies content instead.

**Slide 12: Word Analogy Limitations**
- Content: PRESERVE current deepdive lines 230-245 (success rates 40-70%, evaluation methodology, bias, finance concern)
- This is a HOSTILE REVIEW FIX (M2) -- MUST PRESERVE
- Source: lines 230-245

**Slide 13: Similarity Measures (CHART 02)**
- Content: PRESERVE current deepdive lines 247-262 (cosine similarity formula + chart 02_similarity_heatmap)
- Chart at 0.45\textwidth (with formula text above)
- PRESERVE: line 254 already reads "1=same direction" (hostile review Mi3 was already applied)
- Source: lines 247-262

**Slide 14: Pre-trained Embeddings**
- Content: PRESERVE current deepdive lines 264-278 (Word2Vec, GloVe, FastText, FinBERT, BioBERT)
- PRESERVE: line 274 already reads "FinBERT: BERT further pre-trained on financial corpora" (hostile review Mo1 was already applied)
- Source: lines 264-278

**Slide 15: Static vs Contextual Embeddings**
- Content: PRESERVE current deepdive lines 280-297 (static vs contextual distinction, "bank" example, polysemy)
- This is a HOSTILE REVIEW FIX (M5) -- MUST PRESERVE
- Source: lines 280-297

**Slide 16: Embeddings in Finance**
- Content: PRESERVE current deepdive lines 299-315 (applications list, sentence embeddings, averaging limitation)
- Source: lines 299-315

**Slide 17: Finance Example: Embedding-Based Sentiment**
- Content: PRESERVE current deepdive lines 317-337 (worked sentiment example with cosine similarity)
- This is a HOSTILE REVIEW FIX (C2 partial) -- MUST PRESERVE
- Source: lines 317-337

#### \section{Reinforcement Learning Framework}

**Slide 18: Part 2: Reinforcement Learning Framework**
- Content: PRESERVE bullet content from current deepdive lines 342-358 (key components: Agent, Environment, State, Action, Reward)
- REMOVE the chart reference (chart 03 is now overview-only)
- REPLACE chart with a text-based description of the RL loop using a bullet cycle:
  ```
  Agent observes State -> Agent selects Action -> Environment transitions ->
  Environment emits Reward -> Agent updates -> (repeat)
  ```
  Format as a centered, compact bullet list (NOT TikZ -- avoids compilation risk).
- Source: lines 342-358, but without \includegraphics for chart 03

**Slide 19: Markov Decision Process**
- Content: PRESERVE current deepdive lines 360-375 (MDP tuple, Markov property)
- PRESERVE: line 367 already reads "$\gamma \in [0,1)$: Discount factor (or $\gamma \in [0,1]$ for episodic tasks)" (hostile review Mo4 was already applied)
- Source: lines 360-375

**Slide 20: Policy and Value Functions**
- Content: PRESERVE current deepdive lines 377-394 (policy, V-function, Q-function)
- Source: lines 377-394

**Slide 21: Bellman Equation**
- Content: PRESERVE current deepdive lines 396-413 (optimal Q-function, interpretation, optimal policy)
- Source: lines 396-413

**Slide 22: Temporal Difference Learning**
- Content: PRESERVE current deepdive lines 415-429 (TD(0) update, TD error, comparison to MC and DP)
- This is a HOSTILE REVIEW FIX (M3) -- MUST PRESERVE
- Source: lines 415-429

#### \section{Q-Learning and Trading}

**Slide 23: Q-Learning Algorithm**
- Content: PRESERVE current deepdive lines 431-449 (update rule, informal algorithm)
- FIX: Add convergence conditions (Robbins-Monro) to bottomnote (hostile review M9)
- Source: lines 431-449

**Slide 24: Q-Learning: Worked Example**
- Content: PRESERVE current deepdive lines 451-473 (trading scenario worked example)
- This is a HOSTILE REVIEW FIX (M8) -- MUST PRESERVE
- Source: lines 451-473

**Slide 25: Q-Learning Algorithm: Pseudocode**
- Content: PRESERVE current deepdive lines 475-495 (formal pseudocode)
- This is an INSTRUCTOR GUIDE requirement -- MUST PRESERVE
- Source: lines 475-495

**Slide 26: Q-Values Visualization (CHART 04)**
- Content: PRESERVE current deepdive lines 497-504 (chart 04_q_learning_grid)
- Chart at 0.50\textwidth
- Source: lines 497-504

**Slide 27: Exploration vs Exploitation**
- Content: PRESERVE current deepdive lines 506-527 (epsilon-greedy, decay)
- Source: lines 506-527

**Slide 28: RL for Trading**
- Content: PRESERVE current deepdive lines 537-553 (state/action/reward formulation, challenges)
- Source: lines 537-553
- NOTE: This replaces the former "Learning Curves" chart slide. Chart 05 is now overview-only; we shift the RL-for-Trading content forward to fill this slot because the reward curves chart was illustrative but not essential to the deepdive narrative when the worked Q-learning example (slide 24) already demonstrates learning.

**Slide 29: Trading Reward Function Design**
- Content: PRESERVE current deepdive lines 555-576 (reward with transaction costs, state features, alternative rewards)
- This is a HOSTILE REVIEW FIX (C2 partial) -- MUST PRESERVE
- Source: lines 555-576

**Slide 30: Backtesting RL Trading Strategies**
- Content: PRESERVE current deepdive lines 578-596 (walk-forward validation, honest evaluation, "if it beats buy-and-hold..." )
- This is a HOSTILE REVIEW FIX content -- MUST PRESERVE
- Source: lines 578-596

**Slide 31: Trading Policy (CHART 06)**
- Content: PRESERVE current deepdive lines 598-603 (chart 06_policy_viz)
- Chart at 0.65\textwidth
- Source: lines 598-603

#### \section{Deep RL and Advanced Methods}

**Slide 32: Deep Q-Networks (DQN) (CHART 09)**
- Content: PRESERVE current deepdive lines 605-624 (DQN idea, loss function, experience replay, target network, chart 09_dqn_architecture)
- This is a HOSTILE REVIEW FIX (M7) -- MUST PRESERVE (DQN loss function was added)
- Source: lines 605-624

**Slide 33: Policy Gradient Methods**
- Content: PRESERVE current deepdive lines 626-639 (policy gradient theorem, REINFORCE, Actor-Critic, PPO)
- This is a HOSTILE REVIEW FIX (M6) -- MUST PRESERVE (advantage function was added)
- Source: lines 626-639

**Slide 34: Statistical Inference for Embeddings & RL**
- Content: PRESERVE current deepdive lines 641-657 (bootstrap cosine similarity, permutation test, Q-value confidence, off-policy evaluation)
- This is a HOSTILE REVIEW FIX (C4) -- MUST PRESERVE
- Source: lines 641-657

#### \section{Practice}

**Slide 35: Hands-on Exercise**
- Content: PRESERVE current deepdive lines 661-670 (exercises + Colab link)
- Source: lines 661-670

#### \section{Decision Framework}

**Slide 36: When to Use What (Full Comparison Table)**
- Content: PRESERVE the FULL 6-row comparison table from current deepdive lines 684-701 (Aspect/Embeddings/RL table with all 6 rows: Input, Learns, Output, Training Signal, Finance Use, Key Challenge)
- NOTE: This is the FULL version (6 rows). The overview slide 18 has the CONDENSED version (3 rows). This differentiation avoids verbatim duplication between the two files.
- Source: lines 675-701

**Slide 37: Implementation**
- Content: PRESERVE current deepdive lines 706-724 (Python libraries for embeddings and RL)
- Source: lines 706-724

**Slide 38: Practical Tips**
- Content: PRESERVE current deepdive lines 726-742 (embeddings tips, RL tips)
- Source: lines 726-742

#### \section{Summary}

**Slide 39: Key Takeaways / Summary**
- Content: PRESERVE current deepdive lines 744-761 (summary of both topics)
- Source: lines 744-761

**Slide 40: Closing Comic (XKCD #1838 Text Callback)**
```
\begin{frame}[t]{Closing Thought}
\vspace{2em}
\begin{center}
\Large\textit{``After six lectures of methods and algorithms,}

\textit{we've learned the most important lesson:}

\vspace{0.5em}

\textit{pour the data into the right pile of linear algebra,}

\textit{and the answers will come out the other side.}

\vspace{0.5em}

\textit{The hard part is knowing which pile.'\,''}
\end{center}

\vspace{1em}
\begin{center}
\normalsize --- Adapted from XKCD \#1838 ``Machine Learning'' by Randall Munroe
\end{center}
\bottomnote{Callback to XKCD \#1838 by Randall Munroe (CC BY-NC 2.5). Course complete!}
\end{frame}
```
- Text callback reflecting on the entire course arc (L06 is the final lecture)
- Different text from the overview closing to avoid verbatim repetition

**Slide 41: References (Embeddings)**
- Content: Embeddings references from current deepdive lines 766-772 (Mikolov, Pennington, Devlin, Levy & Goldberg, Bolukbasi)
- Source: lines 764-772

**Slide 42: References (RL and Finance)**
- Content: RL and finance references from current deepdive lines 774-787 (Sutton & Barto, Mnih, Schulman, Watkins & Dayan, Liu et al., Araci)
- Source: lines 774-788
- Split into two reference slides to avoid overflow (current single slide has 11 entries)

### APPENDIX (8 slides)

```latex
% ============================================================
% APPENDIX (8 slides)
% ============================================================
\appendix
\section*{Advanced Topics}
```

**Slide A1: Appendix Divider**
```
\begin{frame}
\begin{center}
\vspace{2cm}
{\Huge \textcolor{mlpurple}{Appendix}}

\vspace{0.5cm}
{\Large Advanced Topics and Proofs}

\vspace{0.5cm}
{\normalsize Supplementary material for self-study and reference}
\end{center}
\bottomnote{Appendix slides are not covered in lecture --- provided for advanced students and exam preparation.}
\end{frame}
```
- Matches L05 appendix divider pattern exactly

**Slide A2: Skip-Gram Objective Derivation**
- Content: Full derivation of the Skip-gram objective from first principles
  - Maximum likelihood estimation on context-target pairs
  - Log-likelihood simplification
  - Connection to cross-entropy loss
- Bottomnote: "The Skip-gram objective is a discriminative model of word-context co-occurrence"
- Source: INSTRUCTOR GUIDE "Appendix Content: Skip-gram objective derivation"

**Slide A3: Negative Sampling Theory**
- Content: Full derivation of the negative sampling objective
  - From Noise Contrastive Estimation (NCE)
  - Why the 3/4 power for the noise distribution
  - Convergence to implicit matrix factorization (Levy & Goldberg, 2014)
- Bottomnote: "Negative sampling implicitly factorizes a shifted PMI matrix (Levy \& Goldberg, 2014)"
- Source: INSTRUCTOR GUIDE "Appendix Content: Negative sampling theory"

**Slide A4: Bellman Equation Convergence**
- Content: Formal convergence proof for Q-learning
  - Robbins-Monro conditions: $\sum \alpha_t = \infty$, $\sum \alpha_t^2 < \infty$
  - Contraction mapping argument for the Bellman operator
  - Why fixed alpha does not guarantee convergence in theory
  - Reference: Watkins & Dayan (1992)
- Bottomnote: "Q-learning converges to $Q^*$ under Robbins-Monro conditions and infinite exploration (Watkins \& Dayan, 1992)"
- Source: INSTRUCTOR GUIDE "Appendix Content: Bellman equation convergence"

**Slide A5: DQN Architecture Details**
- Content: Detailed DQN architecture and training procedure
  - Experience replay buffer: circular buffer of (s,a,r,s') tuples, uniform sampling
  - Target network: $\theta^- \leftarrow \theta$ every C steps (or soft update $\theta^- \leftarrow \tau\theta + (1-\tau)\theta^-$)
  - Double DQN: use online network for action selection, target network for evaluation
  - Dueling DQN: separate value and advantage streams
- Bottomnote: "Mnih et al. (2015): DQN achieved human-level play on 29/49 Atari games"
- Source: INSTRUCTOR GUIDE "Appendix Content: DQN architecture details"

**Slide A6: Word Embedding Bias and Fairness**
- Content: Deeper treatment of bias in embeddings
  - Bolukbasi et al. (2016): man:programmer :: woman:homemaker
  - Debiasing techniques: hard debiasing (projection), counterfactual augmentation
  - Finance implications: biased embeddings in credit scoring, hiring, customer segmentation
  - Regulatory considerations: EU AI Act, model fairness audits
- Bottomnote: "Embedding bias is a compliance risk in regulated financial services"

**Slide A7: SARSA vs Q-Learning**
- Content: On-policy vs off-policy comparison
  - SARSA update: $Q(s,a) \leftarrow Q(s,a) + \alpha[r + \gamma Q(s', a') - Q(s,a)]$ where $a'$ is the action actually taken
  - Q-learning uses $\max_{a'}$ (off-policy); SARSA uses actual $a'$ (on-policy)
  - SARSA is safer (accounts for exploration cost); Q-learning learns the greedy policy
  - Example: cliff-walking domain
- Bottomnote: "SARSA: on-policy learns a safer path; Q-learning: off-policy learns the optimal path"

**Slide A8: References and Further Reading**
- Content: Advanced references for appendix topics
  - Levy & Goldberg (2014): Neural Word Embedding as Implicit Matrix Factorization
  - Bolukbasi et al. (2016): Debiasing Word Embeddings
  - Watkins & Dayan (1992): Q-Learning convergence
  - van Hasselt et al. (2016): Double DQN
  - Wang et al. (2016): Dueling DQN
  - Sutton & Barto (2018): Chapters 6 (TD Learning) and 16 (Applications)
- Bottomnote: "All appendix references are freely available online"

---

## 6. Hostile Review Fixes Preservation Checklist

Every content fix from the hostile review that is already present in the current deepdive.tex MUST be retained in the restructured version. This checklist maps each fix to its location in both the current file and the plan.

| Fix ID | Description | Current Location (deepdive) | Plan Location | Status |
|--------|-------------|----------------------------|---------------|--------|
| C1 | Negative sampling formula + explanation | Lines 146-166 | Deepdive Slide 7 | PRESERVE |
| C2a | Worked sentiment example (embeddings) | Lines 317-337 | Deepdive Slide 17 | PRESERVE |
| C2b | Trading reward function with transaction costs | Lines 555-576 | Deepdive Slide 29 | PRESERVE |
| C3 | Policy viz relabeled (bottomnote updated) | Line 602 | Deepdive Slide 31 | PRESERVE |
| C4 | Statistical inference section | Lines 641-657 | Deepdive Slide 34 | PRESERVE |
| M1 | Chart redundancy elimination | N/A (structural) | Chart allocation table | NEW |
| M2 | Word analogy limitations + bias | Lines 230-245 | Deepdive Slide 12 | PRESERVE |
| M3 | TD learning slide added | Lines 415-429 | Deepdive Slide 22 | PRESERVE |
| M4 | SGNS pseudocode added | Lines 182-201 | Deepdive Slide 10 | PRESERVE |
| M5 | Static vs contextual embeddings | Lines 280-297 | Deepdive Slide 15 | PRESERVE |
| M6 | Policy gradient expanded (advantage function) | Lines 626-639 | Deepdive Slide 33 | PRESERVE |
| M7 | DQN loss function added | Lines 605-624 | Deepdive Slide 32 | PRESERVE |
| M8 | Q-learning worked numerical example | Lines 451-473 | Deepdive Slide 24 | PRESERVE |
| M9 | Q-learning convergence (Robbins-Monro in bottomnote) | Lines 431-449 | Deepdive Slide 23 | FIX (not yet in file) |
| Mo1 | FinBERT "further pre-trained" | Line 274 | Deepdive Slide 14 | PRESERVE (already applied in current file) |
| Mo4 | Gamma range episodic vs continuing | Line 367 | Deepdive Slide 19 | PRESERVE (already applied in current file) |
| Mo7 | Averaging destroys word order | Lines 310-311 | Deepdive Slide 16 | PRESERVE |
| Mi3 | "1=same direction" not "1=identical" | Line 254 | Deepdive Slide 13 | PRESERVE (already applied in current file) |
| Mo8 | Add XKCD image | N/A | Slides 3, 40 (deepdive); Slides 3, 23 (overview) | NEW |

**PRESERVE** = content already exists in current file, keep it verbatim
**PRESERVE (already applied in current file)** = hostile review fix was already applied; executor must not re-apply or alter
**FIX** = content exists but needs minor correction per hostile review (not yet applied)
**NEW** = new structural element not yet in file

---

## 7. Task List for Implementation

### Task 1: Create images directory and download XKCD #1838
- Create `slides/L06_Embeddings_RL/images/` directory
- Download `https://imgs.xkcd.com/comics/machine_learning.png` to `images/1838_machine_learning.png`
- Verify the file exists and is a valid PNG

### Task 2: Restructure L06_overview.tex
- Preserve lines 1-92 (preamble) UNCHANGED
- Preserve lines 93-97 (title block) UNCHANGED
- Rewrite lines 99-253 following the Zone 1/2/3 specification above (24 slides)
- Charts used: 01, 03, 05, 07 ONLY
- Add zone comment banners matching L05 pattern
- Add XKCD #1838 at slide 3 (image) and slide 23 (text callback)
- Move LOs to slide 7 (end of Zone 1)
- Remove ISLR from references
- Add Araci (2019) to references
- Overview comparison table (slide 18) uses condensed 3-row version

### Task 3: Restructure L06_deepdive.tex
- Preserve lines 1-92 (preamble) UNCHANGED
- Preserve lines 93-97 (title block) UNCHANGED
- Rewrite lines 99-791 following the Main Body + Appendix specification above (42 main + 8 appendix = 50 slides)
- Charts used: 02, 04, 06, 08, 09, 10 ONLY
- Remove all references to charts 01, 03, 05, 07
- Add XKCD #1838 at slide 3 (image) and slide 40 (text callback)
- Add `\appendix` + `\section*{Advanced Topics}` after slide 42
- Add appendix divider + 7 appendix content slides + appendix references
- Apply M9 hostile review fix only (Robbins-Monro convergence conditions in bottomnote for slide 23)
- Mo1, Mo4, Mi3 are already applied in the current file -- PRESERVE them as-is, do NOT re-apply
- PRESERVE all hostile review content fixes verbatim (see checklist above)
- Split references into two slides to prevent overflow
- Deepdive comparison table (slide 36) uses full 6-row version
- Slide 18 (RL Framework) uses text-based loop description (bullet list), NOT TikZ

### Task 4: Update instructor guide
- Verify current timing is correct (it already sums to 185 min = 180 min + 5 min buffer)
- Update slide counts to reflect new totals: deepdive ~42 frames (was ~35), overview ~24 frames (was ~15)
- Update the "Slides" row in Session Overview table accordingly

### Task 5: Compile and verify
- Compile both .tex files with pdflatex
- Check for zero Overfull warnings
- Verify page counts (overview ~24, deepdive ~50)
- Run verification protocol (section 9 below)

---

## 8. Architect Verification Checklist (21 points)

Post-implementation, verify ALL of the following:

### Structural Compliance
- [ ] 1. L06_overview.tex has three zone comment banners matching L05 format
- [ ] 2. L06_overview.tex Zone 1 has exactly 7 slides (title, outline, XKCD, 3 motivation, LOs)
- [ ] 3. L06_overview.tex Zone 2 has ~14 slides with \section{Problem}, \section{Method}, \section{Solution}, \section{Practice}
- [ ] 4. L06_overview.tex Zone 3 has exactly 3 slides (takeaways, closing comic, references)
- [ ] 5. L06_deepdive.tex has `\appendix` command followed by `\section*{Advanced Topics}`
- [ ] 6. L06_deepdive.tex appendix has divider slide matching L05 pattern
- [ ] 7. L06_deepdive.tex main body has 42 slides before appendix
- [ ] 8. L06_deepdive.tex appendix has 8 slides

### XKCD Compliance
- [ ] 9. `images/1838_machine_learning.png` exists in L06 directory
- [ ] 10. L06_overview.tex slide 3 includes XKCD image with CC BY-NC 2.5 attribution
- [ ] 11. L06_overview.tex closing slide has text callback to XKCD #1838
- [ ] 12. L06_deepdive.tex slide 3 includes XKCD image with CC BY-NC 2.5 attribution
- [ ] 13. L06_deepdive.tex closing slide has text callback to XKCD #1838

### Chart Allocation Compliance
- [ ] 14. L06_overview.tex references ONLY charts 01, 03, 05, 07
- [ ] 15. L06_deepdive.tex references ONLY charts 02, 04, 06, 08, 09, 10
- [ ] 16. Zero charts appear in both files (grep verification)

### Preamble and Metadata Compliance
- [ ] 17. Lines 1-92 of both files are IDENTICAL to current versions (preamble untouched)
- [ ] 18. `\institute{MSc Data Science}` present in both files

### Content Preservation
- [ ] 19. ALL hostile review fix items from checklist (section 6) are present in the restructured files
- [ ] 20. SGNS pseudocode (algorithmic environment) present in deepdive
- [ ] 21. Q-learning pseudocode (algorithmic environment) present in deepdive

---

## 9. Grep-Based Verification Protocol

Run these commands after implementation to verify structural compliance:

```bash
# ---- CHART ALLOCATION ----

# Overview should reference ONLY charts 01, 03, 05, 07
grep -n "includegraphics" slides/L06_Embeddings_RL/L06_overview.tex
# Expected: 01_word_embedding_space, 03_rl_loop, 05_reward_curves, 07_decision_flowchart, images/1838_machine_learning.png
# MUST NOT contain: 02_, 04_, 06_, 08_, 09_, 10_

# Deepdive should reference ONLY charts 02, 04, 06, 08, 09, 10
grep -n "includegraphics" slides/L06_Embeddings_RL/L06_deepdive.tex
# Expected: 02_similarity_heatmap, 04_q_learning_grid, 06_policy_viz, 08_skipgram_architecture, 09_dqn_architecture, 10_negative_sampling, images/1838_machine_learning.png
# MUST NOT contain: 01_, 03_, 05_, 07_

# Zero dual-assignment check (should return empty)
for chart in 01 02 03 04 05 06 07 08 09 10; do
  ov=$(grep -c "${chart}_" slides/L06_Embeddings_RL/L06_overview.tex)
  dd=$(grep -c "${chart}_" slides/L06_Embeddings_RL/L06_deepdive.tex)
  if [ "$ov" -gt 0 ] && [ "$dd" -gt 0 ]; then
    echo "DUAL ASSIGNMENT: chart $chart in BOTH files"
  fi
done

# ---- ZONE ARCHITECTURE (Overview) ----
grep -n "ZONE" slides/L06_Embeddings_RL/L06_overview.tex
# Expected: 3 zone banners (ZONE 1, ZONE 2, ZONE 3)

# ---- APPENDIX (Deepdive) ----
grep -n "appendix\|Advanced Topics" slides/L06_Embeddings_RL/L06_deepdive.tex
# Expected: \appendix and \section*{Advanced Topics}

# ---- XKCD ----
grep -n "1838\|xkcd\|XKCD\|Randall Munroe" slides/L06_Embeddings_RL/L06_overview.tex
grep -n "1838\|xkcd\|XKCD\|Randall Munroe" slides/L06_Embeddings_RL/L06_deepdive.tex
# Expected: at least 2 occurrences in each file (opening + closing)

# ---- XKCD IMAGE ----
ls slides/L06_Embeddings_RL/images/1838_machine_learning.png
# Expected: file exists

# ---- HOSTILE REVIEW FIXES ----
# C1: Negative sampling
grep -n "negative sampling\|Negative Sampling\|SGNS" slides/L06_Embeddings_RL/L06_deepdive.tex
# Expected: multiple occurrences

# C4: Statistical inference
grep -n "bootstrap\|confidence\|permutation\|inference" slides/L06_Embeddings_RL/L06_deepdive.tex
# Expected: at least 3 occurrences

# M3: TD learning
grep -n "Temporal Difference\|TD(0)\|TD Error" slides/L06_Embeddings_RL/L06_deepdive.tex
# Expected: at least 2 occurrences

# M5: Static vs contextual
grep -n "Static.*Contextual\|static.*contextual\|BERT.*context" slides/L06_Embeddings_RL/L06_deepdive.tex
# Expected: at least 2 occurrences

# M7: DQN loss
grep -n "L(.*theta\|target.*network\|experience.*replay" slides/L06_Embeddings_RL/L06_deepdive.tex
# Expected: at least 2 occurrences

# M8: Worked example
grep -n "3\.19\|Worked Example\|worked example" slides/L06_Embeddings_RL/L06_deepdive.tex
# Expected: at least 1 occurrence (the Q-value 3.19 from the worked example)

# ---- PREAMBLE INTEGRITY ----
# Lines 1-92 should be identical between current and new versions
# (Compare with diff after implementation)

# ---- INSTITUTE LINE ----
grep "MSc Data Science" slides/L06_Embeddings_RL/L06_overview.tex
grep "MSc Data Science" slides/L06_Embeddings_RL/L06_deepdive.tex
# Expected: present in both

# ---- SLIDE COUNT ----
grep -c "begin{frame" slides/L06_Embeddings_RL/L06_overview.tex
# Expected: 24

grep -c "begin{frame" slides/L06_Embeddings_RL/L06_deepdive.tex
# Expected: 50 (42 main + 8 appendix)

# ---- NO ISLR IN OVERVIEW ----
grep "James\|ISLR\|Introduction to Statistical Learning" slides/L06_Embeddings_RL/L06_overview.tex
# Expected: no matches (removed per hostile review Mo3)

# ---- LEARNING OBJECTIVES POSITION (Overview) ----
# LOs should appear AFTER the XKCD slide and motivation slides
grep -n "Learning Objectives" slides/L06_Embeddings_RL/L06_overview.tex
# Expected: appears after line ~40 (not at line ~10 which would be too early)
```

---

## 10. Commit Strategy

### Single commit after all changes:

```
Restructure L06 slides to v3 architecture with three-zone overview and appendix deepdive

- Apply three-zone architecture to overview (7 intro / 14 PMSP / 3 wrap-up = 24 slides)
- Add appendix section to deepdive (42 main + 8 appendix = 50 slides)
- Add XKCD #1838 opening image and closing text callback to both files
- Eliminate chart dual-assignment: overview gets 4 charts, deepdive gets 6 charts
- Preserve all hostile review content fixes (negative sampling, TD learning, worked examples, etc.)
- Add appendix slides: Skip-gram derivation, neg. sampling theory, Bellman convergence, DQN details, bias/fairness, SARSA comparison
- Minor fixes: Robbins-Monro convergence in Q-learning bottomnote, remove ISLR reference
```

---

## 11. Arithmetic Verification

| File | Breakdown | Total |
|------|-----------|-------|
| Overview | 7 (Zone 1) + 14 (Zone 2) + 3 (Zone 3) | **24** |
| Deepdive main | Slides 1-42 (title through references) | **42** |
| Deepdive appendix | Slides A1-A8 (divider through appendix refs) | **8** |
| Deepdive total | 42 + 8 | **50** |
| Charts overview | 01, 03, 05, 07 | **4** |
| Charts deepdive | 02, 04, 06, 08, 09, 10 | **6** |
| Charts total | 4 + 6 | **10** |
| Dual assignment | 0 | **PASS** |

---

## 12. Success Criteria

The restructure is COMPLETE when ALL of the following are true:

1. L06_overview.tex compiles with zero Overfull warnings and produces 24 slides
2. L06_deepdive.tex compiles with zero Overfull warnings and produces 50 slides (42 main + 8 appendix)
3. All 21 architect verification checklist items pass
4. All grep verification commands produce expected output
5. Zero chart dual-assignment (each of 10 charts in exactly one file)
6. All hostile review fix items preserved in the restructured files (see checklist section 6)
7. XKCD #1838 image file exists in images/ directory
8. Both files have XKCD opening (image) AND closing (text callback)
9. Lines 1-92 of both files are byte-identical to current versions

---

## Revision History

| Iteration | Date | Changes |
|-----------|------|---------|
| 1 | 2026-02-13 | Initial plan |
| 2 | 2026-02-13 | Applied Critic feedback: B1 (corrected slide count 42 main + 8 appendix = 50), B2 (cleaned up slide 28 dual specification), B3 (chose text-only for slide 18 RL loop, no TikZ), N1 (updated Task 4 to verify timing rather than fix it), N2 (differentiated comparison tables: 3-row condensed in overview vs 6-row full in deepdive), N4 (removed redundant chart 07 explanation at slide 36), N5 (listed the 4 LOs explicitly for deepdive slide 4), N6 (changed Mo1, Mo4, Mi3 from FIX to PRESERVE since already applied in current file) |

---

*Plan generated by Prometheus (Planner Agent)*
*Revised after Critic review (iteration 2)*
