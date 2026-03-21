"""PCA vs t-SNE Runtime Comparison - Wall-clock time at different sample sizes."""
import matplotlib.pyplot as plt
import numpy as np
import time
from pathlib import Path
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.datasets import make_blobs
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "PCA vs t-SNE: Runtime Comparison",
    "description": "Log-scale time comparison across sample sizes",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top10_17_pca_vs_tsne_runtime"
}


sample_sizes = [100, 500, 1000, 2000, 5000]
pca_times = []
tsne_times = []

X_full, _ = make_blobs(n_samples=5000, n_features=50, centers=5, random_state=42)

for n in sample_sizes:
    X = X_full[:n]

    start = time.time()
    PCA(n_components=2, random_state=42).fit_transform(X)
    pca_times.append(time.time() - start)

    start = time.time()
    TSNE(n_components=2, perplexity=min(30, n // 4), random_state=42,
         learning_rate='auto').fit_transform(X)
    tsne_times.append(time.time() - start)

fig, ax = plt.subplots()
ax.plot(sample_sizes, pca_times, 'o-', color=MLBLUE, linewidth=2.5, markersize=8, label='PCA')
ax.plot(sample_sizes, tsne_times, 's-', color=MLORANGE, linewidth=2.5, markersize=8, label='t-SNE')

ax.set_xlabel('Number of Samples')
ax.set_ylabel('Time (seconds)')
ax.set_title('PCA vs t-SNE: Runtime Comparison')
ax.set_yscale('log')
ax.legend(loc='upper left', framealpha=0.9, fontsize=13)
ax.grid(True, alpha=0.3, which='both')

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_17_pca_vs_tsne_runtime/chart.pdf")
