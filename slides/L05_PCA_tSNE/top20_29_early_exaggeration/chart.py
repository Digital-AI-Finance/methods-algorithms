"""t-SNE Without Early Exaggeration - Shows poorly separated clusters when early exaggeration is disabled."""
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
    "title": "t-SNE Without Early Exaggeration",
    "description": "Scatter of t-SNE with early_exaggeration=1 showing overlapping clusters due to disabled exaggeration.",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top20_29_early_exaggeration"
}


np.random.seed(42)

X, y = make_blobs(n_samples=500, n_features=20, centers=5, cluster_std=1.5, random_state=42)

tsne = TSNE(early_exaggeration=1, random_state=42, n_iter=1000, perplexity=30)
X_emb = tsne.fit_transform(X)

cluster_colors = [MLBLUE, MLORANGE, MLGREEN, MLPURPLE, MLRED]

fig, ax = plt.subplots()

for i in range(5):
    mask = y == i
    ax.scatter(X_emb[mask, 0], X_emb[mask, 1], c=cluster_colors[i], s=30,
               alpha=0.6, edgecolors='white', linewidths=0.3, label=f'Cluster {i+1}')

ax.set_title('t-SNE Without Early Exaggeration (factor = 1)')
ax.set_xlabel('t-SNE Dimension 1')
ax.set_ylabel('t-SNE Dimension 2')

# Annotation
bbox_props = dict(boxstyle='round,pad=0.5', facecolor='#FFF3CD', edgecolor=MLORANGE, alpha=0.95)
annotation_text = ('Without early exaggeration, clusters\n'
                   'remain tangled. Default (12\u00d7) pushes\n'
                   'clusters apart in early iterations.')
ax.annotate(annotation_text,
            xy=(0.02, 0.02), xycoords='axes fraction', fontsize=12,
            va='bottom', ha='left', bbox=bbox_props)

ax.legend(loc='upper right', framealpha=0.9, fontsize=11)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
