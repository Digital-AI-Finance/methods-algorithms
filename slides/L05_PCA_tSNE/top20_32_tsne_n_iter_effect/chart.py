"""Trustworthiness vs Number of t-SNE Iterations - Effect of iteration count."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_blobs
from sklearn.manifold import TSNE, trustworthiness
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Trustworthiness vs Number of t-SNE Iterations",
    "description": "Line plot showing how trustworthiness changes with t-SNE iteration count, with recommended range highlighted.",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top20_32_tsne_n_iter_effect"
}


np.random.seed(42)

# Data: 4 blobs in 15D, 400 samples
X, y = make_blobs(n_samples=400, n_features=15, centers=4, random_state=42)

n_iters = [250, 300, 400, 500, 750, 1000, 1500, 2000]
trust_scores = []

for n in n_iters:
    emb = TSNE(n_components=2, n_iter=n, random_state=42).fit_transform(X)
    t_score = trustworthiness(X, emb, n_neighbors=10)
    trust_scores.append(t_score)

fig, ax = plt.subplots()

# Shaded recommended band
ax.axvspan(500, 1000, alpha=0.12, color=MLGREEN, label='Recommended range (500-1000)')

# Main line
ax.plot(n_iters, trust_scores, 'o-', color=MLPURPLE, linewidth=2.5, markersize=8, zorder=5)

# Find plateau: where improvement < 0.5% over previous
plateau_idx = None
for i in range(1, len(trust_scores)):
    if (trust_scores[i] - trust_scores[i - 1]) < 0.005:
        plateau_idx = i
        break

if plateau_idx is not None:
    ax.plot(n_iters[plateau_idx], trust_scores[plateau_idx], '*', color=MLORANGE,
            markersize=20, zorder=6, label=f'Plateau at n_iter={n_iters[plateau_idx]}')

ax.set_xlabel('Number of t-SNE Iterations (n_iter)')
ax.set_ylabel('Trustworthiness (k=10)')
ax.set_ylim(0.7, 1.0)
ax.set_title('Trustworthiness vs Number of t-SNE Iterations')
ax.legend(loc='lower right', framealpha=0.9)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
