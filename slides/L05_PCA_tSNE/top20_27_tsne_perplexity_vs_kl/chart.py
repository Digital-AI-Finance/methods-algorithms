"""KL Divergence vs Perplexity in t-SNE - Shows how KL divergence varies with perplexity choice."""
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
    "title": "KL Divergence vs Perplexity in t-SNE",
    "description": "Line plot of final KL divergence vs perplexity with optimal point and recommended range.",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top20_27_tsne_perplexity_vs_kl"
}


np.random.seed(42)

X, y = make_blobs(n_samples=500, n_features=20, centers=5, cluster_std=1.5, random_state=42)

perplexities = list(range(5, 101, 5))
kl_divs = []

for p in perplexities:
    tsne = TSNE(perplexity=p, random_state=42, n_iter=1000)
    tsne.fit_transform(X)
    kl_divs.append(tsne.kl_divergence_)

kl_divs = np.array(kl_divs)
min_idx = np.argmin(kl_divs)

fig, ax = plt.subplots()

# Recommended range shading
ax.axvspan(20, 50, alpha=0.12, color=MLGREEN, label='Recommended range (20\u201350)')

# Line plot
ax.plot(perplexities, kl_divs, color=MLBLUE, linewidth=2.5, marker='o', markersize=6, zorder=3)

# Star at minimum
ax.plot(perplexities[min_idx], kl_divs[min_idx], marker='*', color=MLRED, markersize=20, zorder=4,
        label=f'Minimum KL = {kl_divs[min_idx]:.3f} (perp={perplexities[min_idx]})')

ax.set_xlabel('Perplexity')
ax.set_ylabel('Final KL Divergence')
ax.set_title('KL Divergence vs Perplexity in t-SNE')
ax.legend(loc='upper right', framealpha=0.9)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
