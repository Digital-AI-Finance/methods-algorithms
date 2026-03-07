"""Kernel PCA on Concentric Circles - Linear PCA vs RBF Kernel PCA."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.decomposition import PCA, KernelPCA
from sklearn.datasets import make_circles

CHART_METADATA = {
    "title": "Linear vs Kernel PCA on Non-Linear Data",
    "description": "Comparison of linear PCA and RBF kernel PCA on concentric circles",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top10_12_kernel_pca"
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False,
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

X, y = make_circles(n_samples=400, factor=0.3, noise=0.05, random_state=42)

pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X)

kpca = KernelPCA(n_components=2, kernel='rbf', gamma=15, random_state=42)
X_kpca = kpca.fit_transform(X)

colors = [MLBLUE, MLORANGE]
labels = ['Inner circle', 'Outer circle']
fig, axes = plt.subplots(1, 2, figsize=(10, 6))

for cls in [0, 1]:
    mask = y == cls
    axes[0].scatter(X_pca[mask, 0], X_pca[mask, 1], c=colors[cls],
                    alpha=0.6, s=25, edgecolors='none', label=labels[cls])
    axes[1].scatter(X_kpca[mask, 0], X_kpca[mask, 1], c=colors[cls],
                    alpha=0.6, s=25, edgecolors='none', label=labels[cls])

axes[0].set_title('Linear PCA', fontsize=15)
axes[0].set_xlabel('PC1')
axes[0].set_ylabel('PC2')
axes[0].legend(loc='upper left', fontsize=11)

axes[1].set_title('Kernel PCA (RBF)', fontsize=15)
axes[1].set_xlabel('KPC1')
axes[1].set_ylabel('KPC2')
axes[1].legend(loc='upper left', fontsize=11)

fig.suptitle('Linear vs Kernel PCA on Non-Linear Data', fontsize=16, fontweight='bold', y=0.98)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout(rect=[0, 0.02, 1, 0.95])
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: top10_12_kernel_pca/chart.pdf")
