# Plan: Course Content Fixes (All 5 Priorities)

## Source
Ultra-deep content analysis identified 5 improvement priorities across the 6-lecture Methods and Algorithms MSc course.

---

## Fix 1: L06 Charts — Real Embeddings (CRITICAL)

### Problem
`01_word_embedding_space/chart.py` plots manually placed 2D coordinates for finance words. `02_similarity_heatmap/chart.py` uses a hand-crafted similarity matrix. Both are pedagogically dishonest for an MSc course.

### Approach
Use `gensim.downloader` to load `glove-wiki-gigaword-50` (50-dim, ~70MB download on first run).

### gensim Dependency
- **Uncomment** line 28 in `requirements.txt`: change `# gensim>=4.0.0` to `gensim>=4.0.0`
- First run downloads model to `~/gensim-data/`. Subsequent runs use cache.
- **Offline fallback**: Each chart.py will use a try/except: try loading gensim model, except fall back to saved numpy arrays in a `.npy` file shipped alongside chart.py. The executor must generate these cached arrays on first successful run.

### Charts to Refactor

**`slides/L06_Embeddings_RL/01_word_embedding_space/chart.py`**:
```python
import gensim.downloader as api
from sklearn.decomposition import PCA

try:
    model = api.load('glove-wiki-gigaword-50')
    words = ['stock', 'equity', 'share', 'bond', 'dividend',
             'risk', 'volatility', 'hedge', 'loss', 'exposure',
             'buy', 'sell', 'trade', 'invest', 'hold',
             'bullish', 'bearish', 'positive', 'negative', 'neutral']
    vectors = np.array([model[w] for w in words])
    pca = PCA(n_components=2, random_state=42)
    coords = pca.fit_transform(vectors)
    # Save cache for offline use
    np.save(Path(__file__).parent / 'embedding_cache.npy', coords)
except Exception:
    coords = np.load(Path(__file__).parent / 'embedding_cache.npy')
```
Keep same cluster coloring, annotation style, relationship arrows, CHART_METADATA.

**`slides/L06_Embeddings_RL/02_similarity_heatmap/chart.py`**:
```python
from sklearn.metrics.pairwise import cosine_similarity
try:
    model = api.load('glove-wiki-gigaword-50')
    words = ['stock', 'equity', 'bond', 'risk', 'volatility', 'buy', 'sell', 'bullish', 'bearish']
    vectors = np.array([model[w] for w in words])
    sim_matrix = cosine_similarity(vectors)
    np.save(Path(__file__).parent / 'similarity_cache.npy', sim_matrix)
except Exception:
    sim_matrix = np.load(Path(__file__).parent / 'similarity_cache.npy')
```

### Charts to Leave As-Is (8 of 10)
- `03_rl_loop` — Conceptual MDP diagram
- `04_q_learning_grid` — Grid Q-table visualization (custom, appropriate)
- `05_reward_curves` — Training curves (synthetic is fine)
- `06_policy_viz` — Policy arrows on grid
- `07_decision_flowchart` — Diagram
- `08_skipgram_architecture` — Architecture diagram
- `09_dqn_architecture` — Architecture diagram
- `10_negative_sampling` — Probability distribution illustration

### Verification
```bash
cd /d/Joerg/Research/slides/Methods_and_Algorithms
python slides/L06_Embeddings_RL/01_word_embedding_space/chart.py  # must produce chart.pdf
python slides/L06_Embeddings_RL/02_similarity_heatmap/chart.py   # must produce chart.pdf
# Verify gensim + sklearn used:
grep -l "gensim" slides/L06_Embeddings_RL/01_*/chart.py slides/L06_Embeddings_RL/02_*/chart.py
grep -l "sklearn" slides/L06_Embeddings_RL/01_*/chart.py slides/L06_Embeddings_RL/02_*/chart.py
```

---

## Fix 2: sklearn in L01, L02, L04 Charts (9 refactors)

### Problem
L01 (8 charts), L02 (7 charts), L04 (8 charts) never call sklearn. Charts are numpy-only illustrations.

### Approach
Refactor **3 charts per lecture** — only ones where the algorithm call is natural. Leave conceptual diagrams (flowcharts, FancyBboxPatch trees, sampling illustrations) untouched.

### L01 Charts to Refactor (3 of 8)

**`01_simple_regression/chart.py`** — Currently uses manual OLS formula (lines 37-40).
Replace with:
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X.reshape(-1, 1), y)
y_line = model.predict(X_line.reshape(-1, 1)) / 1000
# Use model.coef_[0] and model.intercept_ in legend label
```
Keep same scatter + line visual.

**`05_learning_curves/chart.py`** — Currently uses synthetic curve data.
Replace with:
```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import learning_curve
train_sizes, train_scores, val_scores = learning_curve(
    LinearRegression(), X.reshape(-1, 1), y, train_sizes=np.linspace(0.1, 1.0, 10),
    cv=5, scoring='neg_mean_squared_error', random_state=42)
```

**`06_regularization_comparison/chart.py`** — Currently uses synthetic coefficient paths.
Replace with:
```python
from sklearn.linear_model import Ridge, Lasso
alphas = np.logspace(-2, 3, 50)
ridge_coefs = [Ridge(alpha=a).fit(X_multi, y).coef_ for a in alphas]
lasso_coefs = [Lasso(alpha=a).fit(X_multi, y).coef_ for a in alphas]
```

Charts to leave as-is: `02_multiple_regression_3d` (numpy 3D surface), `03_residual_plots` (numpy residuals are fine), `04_gradient_descent` (conceptual step-by-step), `07_bias_variance` (conceptual), `08_decision_flowchart` (diagram).

### L02 Charts to Refactor (3 of 7)

**`02_decision_boundary/chart.py`** — Replace numpy sigmoid grid with:
```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, random_state=42)
clf = LogisticRegression(random_state=42).fit(X, y)
# Plot decision boundary using clf.predict on meshgrid
```

**`04_roc_curve/chart.py`** — Replace hand-crafted TPR/FPR with:
```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
clf = LogisticRegression(random_state=42).fit(X_train, y_train)
fpr, tpr, _ = roc_curve(y_test, clf.predict_proba(X_test)[:, 1])
```

**`06_confusion_matrix/chart.py`** — Replace hardcoded matrix with:
```python
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, clf.predict(X_test))
```

Charts to leave: `01_sigmoid_function` (math function plot), `03_log_loss` (math function), `05_precision_recall` (similar to ROC, 3 is enough), `07_decision_flowchart` (diagram).

### L04 Charts to Refactor (3 of 8)

**NOTE**: `01_decision_tree/chart.py` is a hand-drawn FancyBboxPatch conceptual tree diagram — NOT a boundary plot. Do NOT refactor it (it would destroy the conceptual visualization).

**`02_feature_importance/chart.py`** — Replace hardcoded bar values with:
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=500, n_features=8, n_informative=4, random_state=42)
rf = RandomForestClassifier(n_estimators=100, random_state=42).fit(X, y)
importances = rf.feature_importances_
```

**`04_oob_error/chart.py`** — Replace synthetic curve with:
```python
from sklearn.ensemble import RandomForestClassifier
oob_scores = []
n_trees_range = range(10, 201, 10)
for n in n_trees_range:
    rf = RandomForestClassifier(n_estimators=n, oob_score=True, random_state=42).fit(X, y)
    oob_scores.append(1 - rf.oob_score_)
```

**`06a_single_tree_variance/chart.py`** — Currently uses `interp1d` nearest-neighbor (lines 52-56) to simulate trees. Replace with real sklearn:
```python
from sklearn.tree import DecisionTreeRegressor
for i in range(7):
    idx = np.random.choice(n_train, n_train, replace=True)
    tree = DecisionTreeRegressor(max_depth=5, random_state=i)
    tree.fit(x_train[idx].reshape(-1, 1), y_train[idx])
    y_pred = tree.predict(x.reshape(-1, 1))
    ax.plot(x, y_pred, color=MLRED, alpha=0.4, linewidth=1.5)
```

Charts to leave: `01_decision_tree` (FancyBboxPatch conceptual diagram), `03_bootstrap` (FancyBboxPatch sampling diagram), `05_ensemble_voting` (conceptual), `06b_random_forest_variance` (partner to 06a, leave as comparison), `07_decision_flowchart` (diagram).

### Verification
```bash
cd /d/Joerg/Research/slides/Methods_and_Algorithms
# Run all 9 refactored charts
for f in \
    slides/L01_Introduction_Linear_Regression/01_simple_regression/chart.py \
    slides/L01_Introduction_Linear_Regression/05_learning_curves/chart.py \
    slides/L01_Introduction_Linear_Regression/06_regularization_comparison/chart.py \
    slides/L02_Logistic_Regression/02_decision_boundary/chart.py \
    slides/L02_Logistic_Regression/04_roc_curve/chart.py \
    slides/L02_Logistic_Regression/06_confusion_matrix/chart.py \
    slides/L04_Random_Forests/02_feature_importance/chart.py \
    slides/L04_Random_Forests/04_oob_error/chart.py \
    slides/L04_Random_Forests/06a_single_tree_variance/chart.py; do
    python "$f" && echo "PASS: $f" || echo "FAIL: $f"
done
```

---

## Fix 3: Mini-Lectures for L01, L05, L06

### Problem
L01, L05, L06 have zero supplementary materials. L02/L03/L04 all have mini-lectures.

### Files to Create (4 new .tex files)

#### `slides/L01_Introduction_Linear_Regression/L01_linreg_mini.tex`
- **10 slides**: Title, XKCD `1725_linear_regression.png`, intuition scatter, OLS formula, residuals, R-squared, gradient descent idea, regularization overview, practice problem, summary
- **Charts**: `01_simple_regression/chart.pdf`, `03_residual_plots/chart.pdf`
- **XKCD**: `images/1725_linear_regression.png` (opening)

#### `slides/L05_PCA_tSNE/L05_pca_mini.tex`
- **10 slides**: Title, XKCD `2048_curve_fitting.png`, why reduce dimensions, PCA intuition (variance direction), eigenvalues/scree, t-SNE intuition (neighborhoods), perplexity, PCA vs t-SNE comparison, finance application, summary
- **Charts**: `01_scree_plot/chart.pdf`, `02_principal_components/chart.pdf`
- **XKCD**: `images/2048_curve_fitting.png` (opening)

#### `slides/L06_Embeddings_RL/L06_embeddings_mini.tex`
- **10 slides**: Title, XKCD `1838_machine_learning.png`, words as vectors, similarity, analogies, Word2Vec skip-gram idea, finance embeddings, limitations, practice question, summary
- **Charts**: `01_word_embedding_space/chart.pdf`, `02_similarity_heatmap/chart.pdf`
- **XKCD**: `images/1838_machine_learning.png` (opening)

#### `slides/L06_Embeddings_RL/L06_rl_mini.tex`
- **10 slides**: Title, XKCD `1838_machine_learning.png` (same image, different caption), agent/environment loop, reward, states/actions, Q-table idea, epsilon-greedy, trading example, Q-learning pseudocode, summary
- **Charts**: `03_rl_loop/chart.pdf`, `04_q_learning_grid/chart.pdf`
- **XKCD**: `images/1838_machine_learning.png` (only one available for L06)

### Template
Use the Beamer preamble from `slides/L02_Logistic_Regression/L02_logreg_mini.tex` as template (it has the full Madrid 8pt 16:9 preamble with `\bottomnote{}` command defined).

### Compilation and Deployment
```bash
# Compile each (from their respective directories)
cd slides/L01_Introduction_Linear_Regression && pdflatex -interaction=nonstopmode L01_linreg_mini.tex
cd slides/L05_PCA_tSNE && pdflatex -interaction=nonstopmode L05_pca_mini.tex
cd slides/L06_Embeddings_RL && pdflatex -interaction=nonstopmode L06_embeddings_mini.tex
cd slides/L06_Embeddings_RL && pdflatex -interaction=nonstopmode L06_rl_mini.tex

# Copy to docs
cp slides/L01_.../L01_linreg_mini.pdf docs/slides/pdf/
cp slides/L05_.../L05_pca_mini.pdf docs/slides/pdf/
cp slides/L06_.../L06_embeddings_mini.pdf docs/slides/pdf/
cp slides/L06_.../L06_rl_mini.pdf docs/slides/pdf/
```

### GH Pages Update
**Hero PDF count**: Currently shows `14` but 22 PDFs exist. After adding 4 new = 26 total. Update to `26`.

**Add mini-lecture cards** to L01, L05, L06 sections in `docs/index.html`:
- L01 section: add `<a class="ccard" href="slides/pdf/L01_linreg_mini.pdf" download>...Linear Regression Mini-Lecture...</a>`
- L05 section: add `<a class="ccard" href="slides/pdf/L05_pca_mini.pdf" download>...PCA Mini-Lecture...</a>`
- L06 section: add 2 cards for embeddings mini and RL mini

### manifest.json
Do NOT change the manifest.json schema. The infrastructure tooling reads `assets.overview_slides` and `assets.deepdive_slides` as singular objects. Mini-lectures are supplementary materials discovered via GH Pages, not tracked in the manifest (same pattern as L03 notebooks decision).

### Verification
```bash
# All 4 must compile with 0 Overfull
for f in L01_linreg_mini L05_pca_mini L06_embeddings_mini L06_rl_mini; do
    grep -c "Overfull" temp_compile_output  # after compilation
done
```

---

## Fix 4: Notebook Exercise Solutions (L02, L06)

### Problem
L02 notebook has 2 exercises with `# TODO: Implement` stubs. L06 has 3 exercises with no solution code.

### L02 Solutions

**Exercise 1: Implement Accuracy from Scratch** (notebook line ~437):
```python
def accuracy_from_scratch(y_true, y_pred):
    """Calculate accuracy without sklearn."""
    correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
    return correct / len(y_true)

acc_manual = accuracy_from_scratch(y_test, y_pred)
print(f"Manual accuracy: {acc_manual:.4f}")
print(f"sklearn accuracy: {accuracy_score(y_test, y_pred):.4f}")
```

**Exercise 2: Handle Class Imbalance** (notebook line ~458):
```python
from sklearn.linear_model import LogisticRegression

clf_balanced = LogisticRegression(class_weight='balanced', random_state=42, max_iter=1000)
clf_balanced.fit(X_train_scaled, y_train)
y_pred_balanced = clf_balanced.predict(X_test_scaled)
print("With class_weight='balanced':")
print(classification_report(y_test, y_pred_balanced))
print(f"\nDefault accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Balanced accuracy: {accuracy_score(y_test, y_pred_balanced):.4f}")
```

### L06 Solutions

**IMPORTANT**: L06 exercises depend on Fix 1 (real embeddings). After Fix 1, the notebook must also switch from simulated embeddings to gensim. The exercise solutions assume real pretrained embeddings are available.

**Exercise 1: Word Analogies** (notebook line ~658):
```python
def analogy(model, a, b, c, topn=5):
    """Find d such that a:b :: c:d using vector arithmetic."""
    # d = c + (b - a)
    result = model.most_similar(positive=[c, b], negative=[a], topn=topn)
    return result

# Finance analogies
print("stock - equity + debt =", analogy(model, 'equity', 'stock', 'debt'))
print("bull - buy + sell =", analogy(model, 'buy', 'bull', 'sell'))
print("risk - loss + profit =", analogy(model, 'loss', 'risk', 'profit'))
```
Note: uses gensim model's `most_similar()` method. Words like 'debt', 'bull', 'profit' exist in glove-wiki-gigaword-50.

**Exercise 2: Epsilon Decay** (notebook line ~677):
```python
epsilon = 1.0
epsilon_min = 0.01
decay_rate = 0.995
rewards_decay = []

for episode in range(500):
    state = 0
    total_reward = 0
    for step in range(100):
        if np.random.random() < epsilon:
            action = np.random.choice(n_actions)  # explore
        else:
            action = np.argmax(Q[state])  # exploit
        next_state = get_next_state(state, action)
        reward = get_reward(state, action)
        Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
        state = next_state
        total_reward += reward
    epsilon = max(epsilon_min, epsilon * decay_rate)
    rewards_decay.append(total_reward)

plt.plot(rewards_decay, alpha=0.3, color=ML_BLUE)
plt.plot(pd.Series(rewards_decay).rolling(20).mean(), color=ML_ORANGE, linewidth=2)
plt.title('Q-Learning with Epsilon Decay')
plt.xlabel('Episode'); plt.ylabel('Total Reward')
plt.grid(True, alpha=0.3); plt.show()
```

**Exercise 3: More Complex State** (notebook line ~695):
```python
# Extend 4-state linear grid to 8-state grid with obstacle
# States: 0-7 in a line, state 3 is obstacle (negative reward), state 7 is goal
n_states_complex = 8
n_actions_complex = 2  # left, right
Q_complex = np.zeros((n_states_complex, n_actions_complex))
rewards_complex = np.zeros(n_states_complex)
rewards_complex[7] = 10.0   # goal
rewards_complex[3] = -5.0   # obstacle

for episode in range(1000):
    state = 0
    for step in range(50):
        if np.random.random() < 0.1:
            action = np.random.choice(n_actions_complex)
        else:
            action = np.argmax(Q_complex[state])
        next_state = max(0, min(7, state + (1 if action == 1 else -1)))
        reward = rewards_complex[next_state]
        Q_complex[state, action] += 0.1 * (reward + 0.9 * np.max(Q_complex[next_state]) - Q_complex[state, action])
        state = next_state
        if state == 7:
            break

print("Learned Q-table (8 states):")
print(pd.DataFrame(Q_complex, columns=['Left', 'Right'],
                   index=[f'State {i}{"(obstacle)" if i==3 else "(goal)" if i==7 else ""}' for i in range(8)]))
```

### Verification
```bash
jupyter nbconvert --to notebook --execute notebooks/L02_logistic_regression.ipynb --output /dev/null 2>&1 && echo "L02: PASS"
jupyter nbconvert --to notebook --execute notebooks/L06_embeddings_rl.ipynb --output /dev/null 2>&1 && echo "L06: PASS"
```

---

## Fix 5: L01 Overview Learning Objectives

### Problem
`L01_overview.tex` is the only overview without a Learning Objectives frame. L02-L06 all have one.

### Fix
Add this frame to `L01_overview.tex` after the opening XKCD comic frame. Copy EXACT text from `L01_deepdive.tex` lines 155-168:

```latex
\begin{frame}[t]{Learning Objectives}
  By the end of this session, you will be able to:

  \begin{enumerate}
    \item \textbf{Derive} the OLS estimator and prove its optimality under Gauss-Markov assumptions
    \item \textbf{Analyze} gradient descent convergence and evaluate learning rate selection
    \item \textbf{Evaluate} regression diagnostics to identify assumption violations
    \item \textbf{Compare} regularization strategies (Ridge, Lasso, Elastic Net) for different problem structures
  \end{enumerate}

  \vspace{0.5em}
  \textbf{Finance Applications:} Property valuation, asset pricing (CAPM)

  \bottomnote{Foundation for all supervised learning methods}
\end{frame}
```

### Verification
```bash
cd slides/L01_Introduction_Linear_Regression
pdflatex -interaction=nonstopmode L01_overview.tex 2>&1 | grep -c "Overfull"
# Must be 0
```

---

## Execution Order

| Phase | Fix | Dependencies | Files Changed |
|:---:|------|------------|:---:|
| 1 | Fix 5: L01 LOs | None | 1 .tex |
| 2 | Fix 1: L06 real embeddings | gensim uncommented in requirements.txt | 2 chart.py + requirements.txt |
| 3 | Fix 2: sklearn in L01/L02/L04 | None | 9 chart.py |
| 4 | Fix 4: Notebook exercises | Fix 1 done (L06 needs real embeddings) | 2 .ipynb |
| 5 | Fix 3: Mini-lectures | Fixes 1-2 done (charts referenced) | 4 .tex + compile + deploy |
| 6 | GH Pages deploy | All fixes done | docs/index.html + PDF copies |

---

## Acceptance Criteria

1. `requirements.txt` line 28: `gensim>=4.0.0` (uncommented)
2. `slides/L06_.../01_word_embedding_space/chart.py` uses `gensim.downloader` + `sklearn.decomposition.PCA` with offline fallback — produces chart.pdf
3. `slides/L06_.../02_similarity_heatmap/chart.py` uses `gensim.downloader` + `cosine_similarity` with offline fallback — produces chart.pdf
4. L01 charts `01`, `05`, `06` contain `from sklearn` imports and `.fit()` calls — all produce chart.pdf
5. L02 charts `02`, `04`, `06` contain `from sklearn` imports — all produce chart.pdf
6. L04 charts `02`, `04`, `06a` contain `from sklearn` imports and `.fit()` calls — all produce chart.pdf
7. L04 `01_decision_tree/chart.py` is NOT modified (conceptual diagram)
8. All 11 refactored chart.py files produce chart.pdf without errors
9. `L01_overview.tex` contains Learning Objectives frame matching deepdive LOs exactly (Derive, Analyze, Evaluate, Compare)
10. `L01_overview.tex` compiles with 0 Overfull warnings
11. `notebooks/L02_logistic_regression.ipynb` exercises have solution code (no TODO stubs remaining)
12. `notebooks/L06_embeddings_rl.ipynb` exercises have solution code using gensim pretrained embeddings
13. Both notebooks execute top-to-bottom without errors
14. 4 mini-lecture .tex files exist: `L01_linreg_mini`, `L05_pca_mini`, `L06_embeddings_mini`, `L06_rl_mini`
15. All 4 mini-lectures compile with 0 Overfull warnings, each ~10 slides
16. All new PDFs copied to `docs/slides/pdf/` (26 total PDFs in docs)
17. `docs/index.html` hero PDF count updated to `26`
18. `docs/index.html` has mini-lecture cards in L01, L05, L06 sections
19. `manifest.json` NOT modified (same rationale as L03 notebooks)
20. Updated chart PNGs copied to `docs/slides/images/` for L06 embedding charts

---

PLAN_READY: .omc/plans/course-content-fixes.md
