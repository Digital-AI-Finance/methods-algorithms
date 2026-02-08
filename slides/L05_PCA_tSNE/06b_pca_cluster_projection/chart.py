"""PCA Cluster Projection - Runs ACTUAL sklearn PCA on MNIST digits.
Shows that PCA provides some but limited cluster separation."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits

CHART_METADATA = {
    'title': 'PCA Cluster Projection',
    'description': 'PCA 2D projection shows some cluster separation on digits data',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/06b_pca_cluster_projection'
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Color palette for 10 digit classes
colors = ['#3333B2', '#0066CC', '#FF7F0E', '#2CA02C', '#D62728',
          '#ADADE0', '#8B4513', '#FF69B4', '#808080', '#000000']

# Load ACTUAL high-dimensional data
digits = load_digits()
X, y = digits.data, digits.target

# Run ACTUAL PCA
pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X)

fig, ax = plt.subplots(figsize=(10, 6))

for digit in range(10):
    mask = y == digit
    ax.scatter(X_pca[mask, 0], X_pca[mask, 1], c=colors[digit], label=str(digit),
               s=15, alpha=0.6, edgecolors='none')

var1 = pca.explained_variance_ratio_[0] * 100
var2 = pca.explained_variance_ratio_[1] * 100
ax.set_title(f'PCA Projection of MNIST Digits\n(Some Separation -- {var1+var2:.1f}% Variance Explained)',
             fontsize=16, fontweight='bold')
ax.set_xlabel(f'PC1 ({var1:.1f}% var.)', fontweight='bold')
ax.set_ylabel(f'PC2 ({var2:.1f}% var.)', fontweight='bold')
ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', fontsize=11,
          title='Digit', title_fontsize=12, markerscale=2)
ax.grid(True, alpha=0.3)

for spine in ax.spines.values():
    spine.set_linewidth(1.5)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 06b_pca_cluster_projection/chart.pdf")
