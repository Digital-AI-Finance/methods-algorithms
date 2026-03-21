# Plan: L06 Embeddings & RL Content Visual Improvements

## Context

### Original Request
Identify content gaps in L06 Embeddings & RL lectures and improve them with new charts and visuals.

### Research Findings

**Current inventory:** 7 lecture files, 15 numbered charts (01-15), plus 13 top10 charts. Total: 28 chart folders.

**Gap analysis across all 7 .tex files identified these unvisualized concepts:**

| Gap | Where Discussed (text only) | Impact |
|-----|-----------------------------|--------|
| FinBERT sentiment classification | L06_overview slide 16, L06_deepdive slide 18 | Finance application described with numbers but never shown as a chart |
| Static vs contextual embedding (polysemy) | L06c slides 13-15, L06_deepdive slide 16 | Central concept taught across 3 lectures but no comparative visualization |
| RLHF pipeline | L06e slide 8 | Key modern concept (how ChatGPT works) taught with bullet points only |
| Reward shaping impact (trading) | L06_deepdive slide 31, L06b slide 13 | top10_20_reward_shaping exists but is gridworld-specific; no trading-specific chart |

**Charts that exist but are underused:**
- `top10_20_reward_shaping` -- gridworld sparse-vs-shaped reward chart, referenced by zero .tex files. Best fit: L06b (teaches Q-learning on gridworld).

## Work Objectives

### Core Objective
Add 4 new charts to fill the highest-impact visual gaps, and integrate 1 existing unused chart into a pedagogically appropriate lecture.

### Deliverables
1. **4 new chart.py files** (folders 16-19) with generated chart.pdf
2. **1 existing chart integration** (top10_20_reward_shaping into L06b -- gridworld context matches)
3. **LaTeX slide additions** to insert each chart into the appropriate lecture(s)
4. **manifest.json updates** for new chart entries

### Definition of Done
- All 4 new chart.py scripts run without error and produce chart.pdf
- All modified .tex files compile with pdflatex (0 errors, 0 Overfull)
- Each chart serves exactly ONE clear pedagogical purpose
- Each chart appears in at least one lecture file
- **Every chart.py produces exactly ONE figure (NO subplots)** per CLAUDE.md rules

## Must Have / Must NOT Have

### Must Have
- Charts follow course standards: figsize=(10,6), dpi=150, font.size=14, ML color palette
- **Single figure per chart.py -- NO subplots** (CLAUDE.md rule)
- Each chart in own folder: `XX_name/chart.py` -> `chart.pdf`
- bottomnote on every new/modified slide
- No display math ($$) in new slides added to simple lectures (L06a-e)
- Finance context where applicable

### Must NOT Have
- No re-creation of any existing chart
- No new .tex lecture files
- No display math ($$) in the simple lectures (L06a-e)
- No more than 4 new charts (scope control)
- No changes to deepdive appendix slides
- No subplots in any chart.py

## Task Flow

```
T1 (new chart) ──┐
T2 (new chart) ──┤
T3 (new chart) ──┼── T5 (LaTeX integration for all) ── T6 (compile & verify) ── T7 (manifest)
T4 (new chart) ──┘
```

T1-T4 are independent (can run in parallel). T5 depends on T1-T4. T6 depends on T5. T7 depends on T6.

## Detailed TODOs

### T1: Chart 16 -- FinBERT Sentiment Bar Chart
**Folder:** `16_finbert_sentiment_bars/chart.py`
**What:** Horizontal grouped bar chart showing cosine similarity scores of 5 financial headlines against positive/negative sentiment anchors. Each headline gets two bars (positive similarity, negative similarity) with the higher one in a bolder color. Headlines: "Fed signals rate hike" (negative), "Revenue beats expectations" (positive), "CEO steps down amid probe" (negative), "Dividend increased 20%" (positive), "Markets remain volatile" (neutral).
**Why:** L06_overview slide 16 and L06_deepdive slide 18 both walk through a sentiment classification example with numbers but never show it visually. Students see "sim = 0.61" but have no chart to anchor the concept.
**Target lectures:** L06a (after slide 13 "Why Bankers Care About Embeddings"), L06_overview (after slide 16)
**Acceptance criteria:**
- Single figure, NO subplots
- 5 headlines on y-axis, each with 2 horizontal bars (positive/negative similarity)
- Color: MLGreen for "Positive Similarity" bars, MLRed for "Negative Similarity" bars
- Clear legend: "Positive Similarity" / "Negative Similarity"
- Title: "FinBERT Sentiment: Cosine Similarity to Sentiment Anchors"
- Simulated but realistic cosine similarity values (0.1-0.8 range)
- figsize=(10,6), dpi=150, font.size=14

### T2: Chart 17 -- Static vs Contextual Embedding (Polysemy Viz)
**Folder:** `17_static_vs_contextual_embedding/chart.py`
**What:** Single scatter plot showing an embedding space with ~15 words. Most words sit in domain clusters (finance, nature). The key: "bank" appears ONCE in the static representation (single marker at a midpoint between finance and nature clusters) but is annotated with arrows showing it SHOULD split into two locations: "bank (financial)" near the finance cluster and "bank (river)" near the nature cluster. Uses a single 2D scatter plot with annotations -- NOT two panels.
**Why:** Polysemy is the central motivation for the static-to-contextual transition taught in L06c. It is discussed on 3+ slides but never shown as a data visualization.
**Target lectures:** L06c (after slide 13 "But Wait --- One Word, Many Meanings!"), L06_deepdive (after slide 16)
**Design (single-figure, no subplots):**
- One scatter plot with ~15 labeled word points
- Domain clusters: MLBlue=finance (money, loan, stock, investment, portfolio, deposit), MLGreen=nature (river, water, fish, tree, lake, stream)
- "bank" plotted ONCE at midpoint between clusters with a LARGE marker and different shape (star)
- Two dashed arrows from "bank" to where it SHOULD be: one arrow to finance cluster labeled "bank (money)", one to nature cluster labeled "bank (river)"
- Subtitle or annotation: "Static embeddings: 1 point. Contextual: 2 points (based on meaning)"
- Uses synthetic but pedagogically clear coordinates
**Acceptance criteria:**
- Single figure, NO subplots
- "bank" is visually prominent (star marker, larger size)
- Two dashed arrows clearly show the split
- Domain clusters are color-coded
- figsize=(10,6), dpi=150, font.size=14

### T3: Chart 18 -- RLHF Pipeline Diagram
**Folder:** `18_rlhf_pipeline/chart.py`
**What:** Three-stage pipeline diagram showing the RLHF process using matplotlib boxes and arrows (same approach as existing `14_rag_pipeline_flow/chart.py`). Stages: (1) Supervised Fine-Tuning of base LLM, (2) Reward Model training from human rankings, (3) PPO Optimization against reward model.
**Why:** L06e slide 8 teaches RLHF as a numbered list. This is the most important modern RL application (how ChatGPT works) and it deserves a visual pipeline diagram.
**Target lectures:** L06e (after slide 8 "RLHF --- How ChatGPT Learned to Be Helpful"). NOT in deepdive appendix (per constraint).
**Design (follows 14_rag_pipeline_flow precedent):**
- Horizontal flow: 3 rounded boxes connected by arrows
- Box 1 (MLPurple): "Stage 1: Supervised Fine-Tuning" / subtitle: "Train on text corpus"
- Box 2 (MLBlue): "Stage 2: Reward Model" / subtitle: "Humans rank outputs"
- Box 3 (MLOrange): "Stage 3: PPO Optimization" / subtitle: "RL fine-tunes LLM"
- Output arrow: "Aligned LLM"
- Data inputs as small labels below each box
- Clean, readable at 0.65\textwidth in Beamer
**Acceptance criteria:**
- Single figure, NO subplots
- 3 stages with clear labels and subtitles
- Arrows showing directional flow
- Uses FancyBboxPatch or similar for rounded boxes (see 14_rag_pipeline_flow for pattern)
- figsize=(10,6), dpi=150, font.size=14

### T4: Chart 19 -- Reward Shaping Comparison (Trading)
**Folder:** `19_reward_shaping_trading/chart.py`
**What:** Single-plot line chart with two overlaid curves comparing RL agent training under different reward functions for a trading task. Curve 1: Raw P&L reward (high variance, slow convergence). Curve 2: Risk-adjusted reward using Sharpe-like metric (lower variance, faster convergence). Both curves on the same axes with legend.
**Why:** L06_deepdive slide 31 discusses reward function design but never shows the impact visually. L06b slide 13 warns "reward design is tricky." Students need to SEE that reward function choice dramatically affects learning quality. This chart is trading-specific, complementing the existing gridworld top10_20_reward_shaping chart.
**Target lectures:** L06b (after slide 13 "Three Things to Watch Out For"), L06_deepdive (after slide 31 "How Do You Design the Right Reward Signal?")
**Design (single figure, no subplots -- like top10_20 pattern):**
- Single axes, two overlaid curves with rolling-average smoothing
- Curve 1 (MLRed, linewidth=2.5): "Raw P&L Reward" -- high variance, slow convergence
- Curve 2 (MLGreen, linewidth=2.5): "Risk-Adjusted Reward (Sharpe)" -- lower variance, faster convergence
- Shaded confidence bands around each curve (alpha=0.15)
- X-axis: "Training Episode" (0-1000), Y-axis: "Cumulative Reward"
- Title: "Reward Shaping: Impact on Trading Agent Learning"
- Synthetic but realistic training data (sigmoid + noise, different parameters for each curve)
**Acceptance criteria:**
- Single figure, NO subplots
- Two distinct curves with clear legend
- Shaded confidence bands
- Trading-specific axis labels and title
- figsize=(10,6), dpi=150, font.size=14

### T5: LaTeX Integration (all charts into target lectures)
**What:** Add new \frame{} slides to the target lectures for each new chart + integrate existing top10_20. Each new slide must include:
- Frame title (question-based per course convention)
- \includegraphics with chart.pdf at 0.55-0.65\textwidth
- 2-3 compactlist bullet points
- \bottomnote{}
- NO display math ($$) in simple lectures (L06a-e)

**Target file modifications:**

| File | Chart | Insert After | Notes |
|------|-------|-------------|-------|
| L06a_embeddings_simple.tex | 16_finbert_sentiment_bars | slide 13 ("Why Bankers Care") | +1 slide |
| L06b_rl_simple.tex | 19_reward_shaping_trading | slide 13 ("Three Things to Watch") | +1 slide |
| L06b_rl_simple.tex | top10_20_reward_shaping | slide 14 (after new chart 19) | +1 slide (gridworld matches L06b content) |
| L06c_embeddings_llm_simple.tex | 17_static_vs_contextual | slide 13 ("One Word, Many Meanings") | +1 slide |
| L06e_modern_rl_simple.tex | 18_rlhf_pipeline | slide 8 ("RLHF") | +1 slide |
| L06_overview.tex | 16_finbert_sentiment_bars | slide 16 ("How Can Embeddings Detect Sentiment?") | +1 slide |
| L06_deepdive.tex | 17_static_vs_contextual | slide 16 ("Does Context Change Meaning?") | +1 slide |
| L06_deepdive.tex | 19_reward_shaping_trading | slide 31 ("Reward Signal Design") | +1 slide |

**Total: +8 slides across 6 files**

**Acceptance criteria:**
- All new frames have question-based titles
- bottomnote on every new slide
- Chart widths: 0.55\textwidth (with text) or 0.65\textwidth (chart-only)
- No display math in L06a, L06b, L06c, L06e files
- Frame numbering consistent (no gaps)

### T6: Compile and Verify
**What:** Run pdflatex on all 6 modified .tex files and verify clean compilation.
**Acceptance criteria:**
- All 6 files compile with 0 errors: L06a, L06b, L06c, L06e, L06_overview, L06_deepdive
- `grep -c "Overfull" *.log` returns 0 for each file
- Move aux files: `mkdir -p temp && mv *.aux *.log *.nav *.out *.snm *.toc temp/`

### T7: Update manifest.json
**What:** Add entries for 4 new charts (16-19) to the L06 section of manifest.json with status "complete".
**Acceptance criteria:**
- 4 new chart entries in manifest.json under L06
- Status: "complete" for all
- Paths match actual folder names: 16_finbert_sentiment_bars, 17_static_vs_contextual_embedding, 18_rlhf_pipeline, 19_reward_shaping_trading

## Commit Strategy

1. **Commit 1:** New chart.py files (T1-T4) -- "Add 4 new L06 charts: finbert sentiment, polysemy viz, rlhf pipeline, reward shaping"
2. **Commit 2:** LaTeX integration (T5) + compilation (T6) + manifest (T7) -- "Integrate 5 charts into L06 lectures (+8 slides across 6 files)"

## Success Criteria

1. 4 new chart.py scripts each produce a clean chart.pdf (single figure, no subplots)
2. 1 existing chart (top10_20_reward_shaping) is now referenced in L06b (gridworld context matches)
3. All 6 modified .tex files compile with 0 errors and 0 Overfull warnings
4. Each new chart fills a documented pedagogical gap (not decorative)
5. Total new slides added: 8 across 6 files
6. manifest.json reflects the 4 new charts

## Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| FinBERT chart bars too small for 5 headlines | Medium | Readability | Use horizontal bars, increase figsize height if needed |
| Polysemy chart annotations overlap | Medium | Readability | Use adjustText library or manual coordinate tuning |
| RLHF pipeline too cluttered at 0.65\textwidth | Medium | Readability | Follow 14_rag_pipeline_flow pattern (5 boxes worked); 3 boxes is simpler |
| Reward shaping curves look too similar to top10_20 | Low | Confusion | Different context (trading vs gridworld), different axis labels, different title |
| Adding 2 slides to L06b pushes total over comfortable limit | Low | Overflow | L06b has 17 slides currently; 19 slides is still under the 20-26 range |

## Critic Issue Resolution Log

**Iteration 1 → 2 fixes applied:**

| Issue | Resolution |
|-------|-----------|
| Charts 17 and 19 specified "two panels" violating NO SUBPLOTS rule | **Fixed:** Chart 17 redesigned as single scatter with annotation arrows. Chart 19 redesigned as single plot with two overlaid curves (like top10_20 pattern). |
| "No appendix changes" contradicted T3 targeting deepdive appendix | **Fixed:** Removed deepdive appendix target from T3. RLHF chart now targets L06e only. |
| T5 inserted gridworld chart into trading-focused deepdive slide 31 | **Fixed:** T5 now targets L06b (which teaches Q-learning on gridworld). top10_20's gridworld content matches L06b's pedagogical context. |
| Task flow diagram omitted T8 | **Fixed:** Renamed T6→T5 (merged integration), T7→T6 (compile), T8→T7 (manifest). Diagram updated. |
| T6 and T7 had duplicate acceptance criteria | **Fixed:** T5 owns LaTeX editing, T6 owns compilation verification. No overlap. |
| Chart 18 could be TikZ instead of matplotlib | **Decision:** Keep as matplotlib per 14_rag_pipeline_flow precedent. Box-and-arrow diagrams work in matplotlib and maintain consistency with existing pipeline chart. |
