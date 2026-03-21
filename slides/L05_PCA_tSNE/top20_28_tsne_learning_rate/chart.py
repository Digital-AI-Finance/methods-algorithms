"""t-SNE at Optimal Learning Rate (200) - Shows well-separated clusters with failure mode annotations."""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.manifold import TSNE
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "t-SNE at Optimal Learning Rate (200)",
    "description": "Scatter of t-SNE with lr=200 showing well-separated clusters, annotated with failure modes at other learning rates.",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top20_28_tsne_learning_rate"
}


np.random.seed(42)

X, y = make_blobs(n_samples=400, n_features=15, centers=4, cluster_std=1.0, random_state=42)

tsne = TSNE(learning_rate=200, random_state=42, perplexity=30, n_iter=1000)
X_emb = tsne.fit_transform(X)

cluster_colors = [MLBLUE, MLORANGE, MLGREEN, MLPURPLE]

fig, ax = plt.subplots()

for i in range(4):
    mask = y == i
    ax.scatter(X_emb[mask, 0], X_emb[mask, 1], c=cluster_colors[i], s=30,
               alpha=0.7, edgecolors='white', linewidths=0.3, label=f'Cluster {i+1}')

ax.set_title('t-SNE at Optimal Learning Rate (200)')
ax.set_xlabel('t-SNE Dimension 1')
ax.set_ylabel('t-SNE Dimension 2')

# Failure mode annotations
bbox_props = dict(boxstyle='round,pad=0.4', facecolor='#FFF3CD', edgecolor=MLORANGE, alpha=0.9)
ax.annotate('lr = 10: compressed ball\n(gradient too small)',
            xy=(0.02, 0.98), xycoords='axes fraction', fontsize=11,
            va='top', ha='left', bbox=bbox_props)

bbox_props2 = dict(boxstyle='round,pad=0.4', facecolor='#F8D7DA', edgecolor=MLRED, alpha=0.9)
ax.annotate('lr = 2000: exploded scatter\n(gradient too large)',
            xy=(0.98, 0.98), xycoords='axes fraction', fontsize=11,
            va='top', ha='right', bbox=bbox_props2)

bbox_props3 = dict(boxstyle='round,pad=0.4', facecolor='#D4EDDA', edgecolor=MLGREEN, alpha=0.9)
ax.annotate('lr = 200: well-separated clusters',
            xy=(0.5, 0.02), xycoords='axes fraction', fontsize=11,
            va='bottom', ha='center', bbox=bbox_props3)

ax.legend(loc='lower right', framealpha=0.9, fontsize=11)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
