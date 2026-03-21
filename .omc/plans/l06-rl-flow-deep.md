# L06 RL Pedagogical Flow Deep Check

## Scope

RL-specific analysis of:
- **Overview:** Slides 5, 8, 13-15, 17 (RL content)
- **Deepdive:** Slides 19-36 (RL Framework + Q-Learning + DQN sections)
- **Appendix:** A4, A5, A7, A9 (RL appendix slides)

---

## RL Slide-by-Slide Flow Trace

### Deepdive RL Theory (Slides 19-23)

| From | To | Transition | Verdict |
|------|----|-----------|---------|
| 19 (Components) | 20 (MDP) | Informal components → formal tuple | OK |
| 20 (MDP) | 21 (Policy/Value) | Framework → what we optimize | OK |
| 21 (V, Q) | 22 (Bellman) | Value definitions → recursive structure | Excellent |
| 22 (Bellman) | 23 (TD) | Theory → practical learning method | OK, bridge bullet on 23 |

### Deepdive Q-Learning (Slides 24-29)

| From | To | Transition | Verdict |
|------|----|-----------|---------|
| 23 (TD) | 24 (Q-learning) | Last bullet: "TD applied to Q-function" → Q-learning | Excellent handoff |
| 24 (Formula) | 25 (Worked example) | Abstract → concrete numbers | Excellent MVF |
| 25 (Example) | 26 (Pseudocode) | Understanding → implementation | OK |
| 26 (Pseudocode) | 27 (Chart 04) | Code → visual result | OK |
| 27 (Visual) | 28 (Exploration) | Q-values → how to use them | OK |
| **28 (ε-greedy)** | **29 (Decay schedule)** | Strategy → decay implementation | **P2: α COLLISION** |

### Deepdive Trading (Slides 30-34)

| From | To | Transition | Verdict |
|------|----|-----------|---------|
| 29 (Decay) | 30 (Trading) | Theory → application domain | OK |
| 30 (Formulation) | 31 (Reward design) | What → how | OK |
| 31 (Reward) | 32 (Backtesting) | Design → evaluation | OK |
| 32 (Backtesting) | 33 (Chart 13) | Text → visual | OK |
| 33 (Timeline) | 34 (Chart 06) | Evaluation method → result | OK |

### Deepdive DQN (Slides 35-36)

| From | To | Transition | Verdict |
|------|----|-----------|---------|
| 34 (Policy) | 35 (DQN motivation) | Tabular limits → function approx | OK |
| 35 (DQN loss) | 36 (DQN stability) | Loss → innovations | OK, but θ⁻ forward ref |

---

## Issues Found

### P2: Should Fix (1 issue)

#### Issue 1: α symbol collision — learning rate vs. decay rate

- **Location:** `L06_deepdive.tex` slide 29, line 597
- **Text:** `\item \textbf{Exponential:} $\epsilon_t = \epsilon_0 \cdot \alpha^t$`
- **Also:** Line 608 bottomnote: `Exponential decay ($\alpha = 0.995$)`
- **Problem:** On slides 23-26, $\alpha$ is established as the learning rate ($\alpha = 0.1$ in the worked example on slide 25). Three slides later on slide 29, $\alpha$ is reused as the exponential decay rate ($\alpha = 0.995$). Students who just learned $\alpha$ = learning rate will be confused.
- **Fix:** Replace $\alpha$ with $\beta$ (decay rate) on slide 29:
  - Line 597: `$\epsilon_t = \epsilon_0 \cdot \beta^t$`
  - Line 608: `Exponential decay ($\beta = 0.995$) is the most common default; linear is simpler to tune`

### P3: Nice to Fix (3 issues)

#### Issue 2: $R_{t+1}$ notation appears without connecting to $r$

- **Location:** `L06_deepdive.tex` slide 21, lines 433 and 438
- **Problem:** Slide 19 introduces lowercase $r$ as "Reward: Feedback signal". Slide 20 introduces $R(s,a,s')$ as "Reward function". Slide 21 uses $R_{t+1}$ as a random variable in the summation. The relationship between these three R/r notations is never stated.
- **Fix:** Add a parenthetical on slide 21 after the Value Function heading. Change line 431 from `\textbf{Value Function:}` to `\textbf{Value Function} (where $R_{t+1}$ is the reward received at step $t{+}1$):`

#### Issue 3: θ⁻ used in DQN loss before definition

- **Location:** `L06_deepdive.tex` slide 35, line 711
- **Problem:** The DQN loss function uses $\theta^-$ (target network parameters) but target networks aren't explained until slide 36. One-slide gap.
- **Fix:** Add a brief inline note on slide 35 after the loss function. After line 712 (closing `\]`), add: `where $\theta^-$ are frozen target-network weights (explained next slide).`

#### Issue 4: RL theory section has 8 slides without a visual

- **Location:** `L06_deepdive.tex` slides 19-26
- **Problem:** No chart or diagram appears between slide 18 (last embedding slide) and slide 27 (Q-values grid). This is 8 consecutive slides of text/formulas. The "1 chart per 4 slides" density guideline suggests at least one visual.
- **Assessment:** This matches standard RL textbook presentation (Sutton & Barto Ch. 3-6 are formula-heavy). The worked example on slide 25 provides concrete grounding. The overview already provided the RL loop visual (chart 03). Upgrading to a mandatory fix would require adding a TikZ MDP transition diagram to slide 20, which is nontrivial.
- **Fix (optional):** On slide 19, convert the text-based RL loop into a simple TikZ circular diagram. However, this is cosmetic and the current text chain is functional. **Defer unless user requests it.**

### Verified Clean (no RL issues)

| Check | Result |
|-------|--------|
| Progressive disclosure | Building Blocks → MDP → V/Q → Bellman → TD → Q-learning → Trading → DQN. Textbook order. |
| Q-learning MVF | Formula (24) → Worked Example (25) → Pseudocode (26) → Q-Values Visual (27). Excellent. |
| ε-greedy MVF | Dilemma text (28) → Formal formula (28) → Decay chart (29). Good. |
| DQN MVF | Problem/Loss (35) → Architecture+Innovations+Chart (36). Good. |
| Trading flow | Formulation (30) → Reward design (31) → Backtesting (32) → Timeline visual (33) → Policy visual (34). Excellent. |
| α definition | Now properly introduced in TD heading (slide 23, line 465) from previous fix. |
| ε definition | Now properly expanded on slide 24 (line 497) from previous fix. |
| γ definition | Properly introduced on slide 20 (line 413). |
| Overview RL flow | Components (13) → Q-learning (14) → Evidence (15) → Trading (17). Appropriate for overview depth. |
| Appendix RL | A4 (Convergence), A5 (DQN details), A7 (SARSA vs Q), A9 (Policy Gradient). Self-contained. |

---

## Execution Steps

### Step 1: Fix α symbol collision on slide 29

- **File:** `L06_deepdive.tex`
- **Line 597:** Change `$\epsilon_t = \epsilon_0 \cdot \alpha^t$` to `$\epsilon_t = \epsilon_0 \cdot \beta^t$`
- **Line 608:** Change `Exponential decay ($\alpha = 0.995$)` to `Exponential decay ($\beta = 0.995$)`

### Step 2: Add $R_{t+1}$ parenthetical on slide 21

- **File:** `L06_deepdive.tex`
- **Line 431:** Change `\textbf{Value Function:}` to `\textbf{Value Function} ($R_{t+1}$: reward at step $t{+}1$):`

### Step 3: Add θ⁻ inline note on slide 35

- **File:** `L06_deepdive.tex`
- **After line 712** (the `\]` closing the loss function), add:
  `where $\theta^-$ are frozen target-network weights (see next slide).`

### Step 4: Compile and verify

- Compile `L06_deepdive.tex` with pdflatex
- Verify 0 errors, 0 Overfull
- Verify page count remains 52

---

## Acceptance Criteria

1. P2 issue addressed: α → β in epsilon decay formula and bottomnote (slide 29)
2. P3 issues addressed: $R_{t+1}$ parenthetical (slide 21), θ⁻ note (slide 35)
3. Deepdive compiles cleanly: 0 errors, 0 Overfull
4. Page count stable: 52 pages
5. No new symbol collisions or term-before-use violations introduced
6. Overview unchanged (no RL issues found in overview)
