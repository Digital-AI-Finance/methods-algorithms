"""High-D Before/After PCA - 10 features compressed to 2 components"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from pathlib import Path

CHART_METADATA = {
    "title": "10 Features Compressed to 2 Components",
    "description": "PCA projection of 10-feature synthetic data with 3 clusters",
    "url": "https://digital-ai-finance.github.io/methods-algorithms/slides/L05_PCA_tSNE/08_high_dim_before_after"
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLLAVENDER = '#ADADE0'

np.random.seed(42)

# Generate 10-feature data with 3 clusters
X, y = make_blobs(n_samples=300, n_features=10, centers=3, random_state=42)
X_scaled = StandardScaler().fit_transform(X)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

total_var = sum(pca.explained_variance_ratio_) * 100
var1 = pca.explained_variance_ratio_[0] * 100
var2 = pca.explained_variance_ratio_[1] * 100

fig, ax = plt.subplots(figsize=(10, 6))
colors = [MLBLUE, MLORANGE, MLGREEN]
labels = ['Cluster A', 'Cluster B', 'Cluster C']
for i in range(3):
    mask = y == i
    ax.scatter(X_pca[mask, 0], X_pca[mask, 1], c=colors[i], label=labels[i],
               alpha=0.6, s=40, edgecolors='white', linewidths=0.5)

ax.set_xlabel(f'PC1 ({var1:.1f}% variance)')
ax.set_ylabel(f'PC2 ({var2:.1f}% variance)')
ax.set_title('10 Features Compressed to 2 Components')
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

# Annotation box
textstr = f'Original: 10 features | After PCA: 2 components | Variance kept: {total_var:.0f}%'
ax.annotate(textstr, xy=(0.5, 0.02), xycoords='axes fraction', ha='center',
            fontsize=11, bbox=dict(boxstyle='round,pad=0.4', facecolor=MLLAVENDER, alpha=0.3))

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
