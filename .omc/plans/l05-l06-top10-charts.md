# Plan: Top 20 Essential Charts — L05 (PCA & t-SNE) and L06 (Embeddings & RL)

## Context

### Original Request
Create standalone "Top 20 Essential Charts" lectures for L05 and L06, following the exact same pattern established for L03 and L04. Each lecture: 9-10 reused existing charts + 11-13 new Python-generated charts = 20 total. Standalone Beamer .tex, all synthetic data, sklearn/numpy only.

### Established Pattern (from L03/L04)
- 27-slide Beamer lecture with 20 charts
- 3-part structure: Topic A Foundations → Topic B Foundations → Advanced Diagnostics → Summary
- Opening + closing XKCD cartoons with CC BY-NC 2.5 attribution
- Chart.py template: rcParams (font.size=14, figsize=(10,6), dpi=150), savefig dpi=300, ML colors, CHART_METADATA, URL figtext, random_state=42
- Reuse existing chart.pdf where the canonical visualization already exists
- Only create NEW chart.py for genuinely missing visualizations

---

## L05: PCA & t-SNE — Top 20 Essential Charts

### Existing Charts (12 folders)
| # | Folder | Description |
|---|--------|-------------|
| 01 | scree_plot | Explained variance per component (bar chart) |
| 02 | principal_components | 2D PCA projection with PC arrows |
| 03 | reconstruction | PCA reconstruction at different n_components |
| 04a | tsne_perplexity_5 | t-SNE with perplexity=5 |
| 04b | tsne_perplexity_30 | t-SNE with perplexity=30 |
| 04c | tsne_perplexity_100 | t-SNE with perplexity=100 |
| 05a | pca_swiss_roll | PCA on Swiss Roll (fails) |
| 05b | tsne_swiss_roll | t-SNE on Swiss Roll (succeeds) |
| 06a | original_clusters | Original 3D clusters |
| 06b | pca_cluster_projection | PCA 2D cluster projection |
| 06c | tsne_cluster_projection | t-SNE 2D cluster projection |
| 07 | decision_flowchart | PCA vs t-SNE decision flowchart |

### Top 10 Essential PCA/t-SNE Charts

| Rank | Chart | Why Essential | Source | Action |
|------|-------|---------------|--------|--------|
| C1 | Scree Plot | THE canonical PCA chart — eigenvalue magnitudes | 01_scree_plot | REUSE |
| C2 | PCA 2D Projection with PC arrows | Shows principal component directions on data | 02_principal_components | REUSE |
| C3 | PCA Reconstruction | Shows information loss at different n_components | 03_reconstruction | REUSE |
| C4 | t-SNE Perplexity Effect | The key t-SNE hyperparameter | 04b_tsne_perplexity_30 | REUSE |
| C5 | PCA on Swiss Roll (fails) | PCA's linear limitation | 05a_pca_swiss_roll | REUSE |
| C6 | t-SNE on Swiss Roll (succeeds) | t-SNE's non-linear strength | 05b_tsne_swiss_roll | REUSE |
| C7 | PCA Cluster Projection | Dimensionality reduction for visualization | 06b_pca_cluster_projection | REUSE |
| C8 | t-SNE Cluster Projection | Better cluster separation than PCA | 06c_tsne_cluster_projection | REUSE |
| C9 | Cumulative Explained Variance | The "how many components?" decision tool | None | **NEW** |
| C10 | PCA Biplot (scores + loadings) | Feature contribution visualization | None | **NEW** |

**Reuse: 8, New: 2**

### 10 Additional New Charts (A1-A10)

| # | Folder | Description | sklearn Usage |
|---|--------|-------------|---------------|
| A1 | top10_11_scaling_effect | PCA with vs without StandardScaler on same data | PCA.fit_transform (x2) |
| A2 | top10_12_kernel_pca | Kernel PCA on concentric circles (linear PCA fails, RBF succeeds) | KernelPCA.fit_transform + PCA |
| A3 | top10_13_tsne_iterations | t-SNE at n_iter=50, 250, 1000 (convergence snapshots) | TSNE.fit_transform (x3) |
| A4 | top10_14_explained_var_heatmap | Component-feature loading heatmap (which features load where) | PCA.fit |
| A5 | top10_15_pca_denoising | Noisy signal → PCA reconstruct → denoised (3 lines) | PCA.fit_transform + inverse_transform |
| A6 | top10_16_tsne_distance_preservation | Original pairwise distances vs t-SNE distances (scatter) | TSNE.fit_transform |
| A7 | top10_17_pca_vs_tsne_runtime | Wall-clock time comparison at different n_samples | PCA + TSNE timed |
| A8 | top10_18_intrinsic_dimensionality | Explained variance ratio with "knee" detection for optimal dims | PCA.fit |
| A9 | top10_19_pca_whitening | PCA with whiten=True: original → PCA → whitened (3 scatter panels) | PCA(whiten=True) — **1x3 subplot exception** |
| A10 | top10_20_tsne_perplexity_grid | 2x2 grid: perplexity=[5,15,30,100] on make_blobs — **2x2 subplot exception** | TSNE (x4) |

**Total L05: 8 reused + 12 new = 20 charts**

### Subplot Exceptions (L05)
- A9 (whitening): `fig, axes = plt.subplots(1, 3, figsize=(10, 6))` — pedagogical: showing transformation stages
- A10 (perplexity grid): `fig, axes = plt.subplots(2, 2, figsize=(10, 6))` — pedagogical: comparing hyperparameter values

### L05 Lecture Structure (L05_pca_tsne_top10.tex, 27 slides)

```
Slide 1:  Title — "PCA & t-SNE: The Essential Visuals"
Slide 2:  Opening XKCD (#2048, images/2048_curve_fitting.png)
Slide 3:  Learning Objectives (3 bullets)
Slide 4:  Table of Contents
          --- PART 1: PCA FOUNDATIONS (7 charts) ---
          \section{PCA Foundations}
Slide 5:  C1 — Scree Plot (REUSE 01)
Slide 6:  C9 — Cumulative Explained Variance (NEW top10_09)
Slide 7:  C2 — PCA 2D Projection (REUSE 02)
Slide 8:  C10 — PCA Biplot (NEW top10_10)
Slide 9:  A4 — Loading Heatmap (NEW top10_14)
Slide 10: C3 — PCA Reconstruction (REUSE 03)
Slide 11: A1 — Scaling Effect (NEW top10_11)
          --- TRANSITION ---
Slide 12: "From Linear to Non-Linear" transition
          --- PART 2: t-SNE & NON-LINEAR (6 charts) ---
          \section{t-SNE and Non-Linear Methods}
Slide 13: C4 — t-SNE Perplexity=30 (REUSE 04b)
Slide 14: A10 — Perplexity Grid (NEW top10_20, 2x2)
Slide 15: A3 — t-SNE Iterations (NEW top10_13)
Slide 16: C5 — PCA on Swiss Roll (REUSE 05a)
Slide 17: C6 — t-SNE on Swiss Roll (REUSE 05b)
Slide 18: A2 — Kernel PCA (NEW top10_12)
          --- PART 3: COMPARISON & ADVANCED (7 charts) ---
          \section{Comparison and Advanced Topics}
Slide 19: C7 — PCA Cluster Projection (REUSE 06b)
Slide 20: C8 — t-SNE Cluster Projection (REUSE 06c)
Slide 21: A6 — Distance Preservation (NEW top10_16)
Slide 22: A7 — Runtime Comparison (NEW top10_17)
Slide 23: A5 — PCA Denoising (NEW top10_15)
Slide 24: A9 — PCA Whitening (NEW top10_19, 1x3)
Slide 25: A8 — Intrinsic Dimensionality (NEW top10_18)
          --- CLOSING ---
          \section{Summary}
Slide 26: Summary checklist (two-column, 10 items each)
Slide 27: Closing XKCD (#2400, images/2400_statistics.png)
```

### XKCD Images (L05)
- Opening: `images/2048_curve_fitting.png` (exists)
- Closing: `images/2400_statistics.png` (exists)

---

## L06: Embeddings & RL — Top 20 Essential Charts

### Existing Charts (10 folders)
| # | Folder | Description |
|---|--------|-------------|
| 01 | word_embedding_space | 2D word embedding projection |
| 02 | similarity_heatmap | Cosine similarity matrix heatmap |
| 03 | rl_loop | RL agent-environment loop diagram |
| 04 | q_learning_grid | Q-values in gridworld |
| 05 | reward_curves | Training reward convergence |
| 06 | policy_viz | Optimal policy arrows in grid |
| 07 | decision_flowchart | Embeddings vs RL flowchart |
| 08 | skipgram_architecture | Skip-gram neural network diagram |
| 09 | dqn_architecture | DQN architecture diagram |
| 10 | negative_sampling | Negative sampling visualization |

### Top 10 Essential Embeddings & RL Charts

| Rank | Chart | Why Essential | Source | Action |
|------|-------|---------------|--------|--------|
| C1 | Word Embedding Space (2D) | THE canonical embedding visual | 01_word_embedding_space | REUSE |
| C2 | Cosine Similarity Heatmap | Understanding embedding relationships | 02_similarity_heatmap | REUSE |
| C3 | Skip-gram Architecture | How embeddings are learned | 08_skipgram_architecture | REUSE |
| C4 | Negative Sampling | Training efficiency visualization | 10_negative_sampling | REUSE |
| C5 | Q-Learning Grid | The heart of RL: state values | 04_q_learning_grid | REUSE |
| C6 | Reward Curves | Training convergence | 05_reward_curves | REUSE |
| C7 | Policy Visualization | Learned behavior | 06_policy_viz | REUSE |
| C8 | Word Analogy Arithmetic | The "king - man + woman = queen" chart | None | **NEW** |
| C9 | Epsilon-Greedy Exploration | Exploration vs exploitation tradeoff | None | **NEW** |
| C10 | Embedding Dimension Effect | How many dimensions are needed? | None | **NEW** |

**Reuse: 7, New: 3**

### 10 Additional New Charts (A1-A10)

| # | Folder | Description | Implementation |
|---|--------|-------------|----------------|
| A1 | top10_11_word_frequency_rank | Zipf's law: word frequency vs rank (log-log) | numpy only (synthetic word freq) |
| A2 | top10_12_context_window | Effect of context window size on embedding quality | Synthetic similarity score vs window size |
| A3 | top10_13_embedding_neighbors | Query word + top-5 nearest neighbors in 2D | PCA on synthetic embeddings |
| A4 | top10_14_qvalue_convergence | Q-value convergence over episodes for one state-action | numpy Q-learning simulation |
| A5 | top10_15_state_action_heatmap | Full Q-table heatmap (states x actions) | numpy Q-learning, imshow |
| A6 | top10_16_bandit_regret | Multi-armed bandit cumulative regret curves (3 strategies) | numpy simulation |
| A7 | top10_17_td_learning_update | TD(0) value estimates converging over episodes | numpy TD simulation |
| A8 | top10_18_embedding_pca_variance | PCA on synthetic embeddings: variance per component | PCA.fit on synthetic embeddings |
| A9 | top10_19_gridworld_trajectory | RL agent path through gridworld (optimal vs random) | numpy simulation, arrows on grid |
| A10 | top10_20_reward_shaping | Effect of reward shaping: sparse vs shaped reward curves | numpy simulation |

**Total L06: 7 reused + 13 new = 20 charts**

### L06 Note on Dependencies
L06 charts use numpy-only RL simulations (no gym/gymnasium dependency). Embeddings use synthetic vectors, not real word2vec/GloVe (no gensim dependency). All charts stay within numpy + matplotlib + sklearn.

### L06 Lecture Structure (L06_embeddings_rl_top10.tex, 27 slides)

```
Slide 1:  Title — "Embeddings & RL: The Essential Visuals"
Slide 2:  Opening XKCD (#1838, images/1838_machine_learning.png)
Slide 3:  Learning Objectives (3 bullets)
Slide 4:  Table of Contents
          --- PART 1: EMBEDDINGS (7 charts) ---
          \section{Word Embeddings}
Slide 5:  C1 — Word Embedding Space (REUSE 01)
Slide 6:  C2 — Similarity Heatmap (REUSE 02)
Slide 7:  C3 — Skip-gram Architecture (REUSE 08)
Slide 8:  C4 — Negative Sampling (REUSE 10)
Slide 9:  C8 — Word Analogy Arithmetic (NEW top10_08)
Slide 10: C10 — Embedding Dimension Effect (NEW top10_10)
Slide 11: A3 — Embedding Nearest Neighbors (NEW top10_13)
          --- TRANSITION ---
Slide 12: "From Representation to Action" transition
          --- PART 2: REINFORCEMENT LEARNING (6 charts) ---
          \section{Reinforcement Learning}
Slide 13: C5 — Q-Learning Grid (REUSE 04)
Slide 14: C6 — Reward Curves (REUSE 05)
Slide 15: C7 — Policy Visualization (REUSE 06)
Slide 16: C9 — Epsilon-Greedy Exploration (NEW top10_09)
Slide 17: A4 — Q-Value Convergence (NEW top10_14)
Slide 18: A9 — Gridworld Trajectory (NEW top10_19)
          --- PART 3: ADVANCED TOPICS (7 charts) ---
          \section{Advanced Topics}
Slide 19: A1 — Word Frequency / Zipf's Law (NEW top10_11)
Slide 20: A2 — Context Window Effect (NEW top10_12)
Slide 21: A8 — Embedding PCA Variance (NEW top10_18)
Slide 22: A5 — State-Action Q-Table Heatmap (NEW top10_15)
Slide 23: A6 — Multi-Armed Bandit Regret (NEW top10_16)
Slide 24: A7 — TD Learning Updates (NEW top10_17)
Slide 25: A10 — Reward Shaping Comparison (NEW top10_20)
          --- CLOSING ---
          \section{Summary}
Slide 26: Summary checklist (two-column, 10 items each)
Slide 27: Closing XKCD (#1838, images/1838_machine_learning.png)
```

### XKCD Images (L06)
- Opening: `images/1838_machine_learning.png` (exists)
- Closing: `images/1838_machine_learning.png` (same image — only 1 XKCD available for L06)

**Note:** L06 only has one XKCD image. Using same image for opening and closing is acceptable — or closing can be omitted/replaced with a text-only summary slide. Plan uses it for both as the simplest option.

---

## Shared Specifications

### Chart.py Template (both L05 and L06)

All new chart.py files MUST follow the exact template:
- `CHART_METADATA` dict with title, description, url
- `plt.rcParams.update({font.size: 14, axes.labelsize: 14, axes.titlesize: 16, ...})`
- `figure.figsize: (10, 6)`, `figure.dpi: 150`
- `savefig(dpi=300, bbox_inches='tight')`
- ML colors: MLPURPLE=#3333B2, MLBLUE=#0066CC, MLORANGE=#FF7F0E, MLGREEN=#2CA02C, MLRED=#D62728
- `random_state=42` on all sklearn objects and np.random.seed(42)
- URL figtext at bottom-right
- Dependencies: numpy, matplotlib, scikit-learn ONLY
- Output: `chart.pdf` in same directory

### .tex Template
- Beamer: Madrid theme, 8pt, 16:9
- Full preamble with ML color definitions (copy from L04_dt_rf_top10.tex)
- Chart widths: 0.65\textwidth (chart-only), 0.55\textwidth (with text)
- Max 3-4 bullets per slide
- Every content frame has `\bottomnote{}`
- `[t]` option on all content frames

### Subplot Exceptions
Only these charts use subplots (pedagogical justification required):
- L05 A9 (whitening): 1x3 — shows original → PCA → whitened transformation stages
- L05 A10 (perplexity grid): 2x2 — comparing hyperparameter values
- All subplots keep figsize=(10, 6)

---

## File Structure

```
slides/L05_PCA_tSNE/
  L05_pca_tsne_top10.tex                    # NEW standalone lecture
  top10_09_cumulative_variance/chart.py      # NEW
  top10_10_pca_biplot/chart.py               # NEW
  top10_11_scaling_effect/chart.py           # NEW
  top10_12_kernel_pca/chart.py               # NEW
  top10_13_tsne_iterations/chart.py          # NEW
  top10_14_explained_var_heatmap/chart.py    # NEW
  top10_15_pca_denoising/chart.py            # NEW
  top10_16_tsne_distance_preservation/chart.py # NEW
  top10_17_pca_vs_tsne_runtime/chart.py      # NEW
  top10_18_intrinsic_dimensionality/chart.py # NEW
  top10_19_pca_whitening/chart.py            # NEW
  top10_20_tsne_perplexity_grid/chart.py     # NEW

slides/L06_Embeddings_RL/
  L06_embeddings_rl_top10.tex                # NEW standalone lecture
  top10_08_word_analogy/chart.py             # NEW
  top10_09_epsilon_greedy/chart.py           # NEW
  top10_10_embedding_dimensions/chart.py     # NEW
  top10_11_word_frequency_rank/chart.py      # NEW
  top10_12_context_window/chart.py           # NEW
  top10_13_embedding_neighbors/chart.py      # NEW
  top10_14_qvalue_convergence/chart.py       # NEW
  top10_15_state_action_heatmap/chart.py     # NEW
  top10_16_bandit_regret/chart.py            # NEW
  top10_17_td_learning_update/chart.py       # NEW
  top10_18_embedding_pca_variance/chart.py   # NEW
  top10_19_gridworld_trajectory/chart.py     # NEW
  top10_20_reward_shaping/chart.py           # NEW
```

---

## Task Flow

```
Phase 1: Create L05 chart.py files (12 new) and run to generate chart.pdf
Phase 2: Create L06 chart.py files (13 new) and run to generate chart.pdf
Phase 3: Create L05_pca_tsne_top10.tex
Phase 4: Create L06_embeddings_rl_top10.tex
Phase 5: Compile both .tex files (0 errors, 0 Overfull)
Phase 6: Update manifest.json (add chart entries + tex entries for both L05 and L06)
Phase 7: Architect verification
Phase 8: Commit and push
```

Phases 1+2 can run in parallel. Phases 3+4 can run in parallel.

---

## Definition of Done

| Criterion | L05 | L06 |
|-----------|-----|-----|
| New chart.py files created | 12 | 13 |
| All chart.pdf generated | 12 | 13 |
| Reused chart.pdf paths valid | 8 | 7 |
| .tex compiles clean | 0 err, 0 Overfull, 27 pages | 0 err, 0 Overfull, 27 pages |
| Every slide has \bottomnote{} | Yes | Yes |
| manifest.json updated | Charts + tex entry | Charts + tex entry |
| Template compliance | rcParams, ML colors, CHART_METADATA | rcParams, ML colors, CHART_METADATA |
| Dependencies | numpy, matplotlib, sklearn only | numpy, matplotlib, sklearn only |
| Architect verified | APPROVED | APPROVED |

---

## Commit Strategy

**Single commit:** "Add standalone top-20 charts lectures for L05 (PCA/t-SNE) and L06 (Embeddings/RL)"
- Files: 25 new chart folders, 2 new .tex files, 2 new .pdf files, manifest.json update
