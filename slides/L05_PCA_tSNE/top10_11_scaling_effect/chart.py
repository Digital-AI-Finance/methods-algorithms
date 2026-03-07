"""Scaling Effect on PCA - Compares PCA with and without StandardScaler."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.decomposition import PCA
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler

CHART_METADATA = {
    "title": "The Impact of Feature Scaling on PCA",
    "description": "Side-by-side PCA projections with and without standard scaling",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top10_11_scaling_effect"
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

X, y = make_classification(n_samples=300, n_features=5, n_informative=3, random_state=42)
X[:, 0] *= 1000  # scale imbalance

pca_raw = PCA(n_components=2, random_state=42)
scores_raw = pca_raw.fit_transform(X)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pca_scaled = PCA(n_components=2, random_state=42)
scores_scaled = pca_scaled.fit_transform(X_scaled)

colors = [MLBLUE, MLORANGE]
fig, axes = plt.subplots(1, 2, figsize=(10, 6))

for cls in [0, 1]:
    mask = y == cls
    axes[0].scatter(scores_raw[mask, 0], scores_raw[mask, 1], c=colors[cls],
                    alpha=0.6, s=25, edgecolors='none', label=f'Class {cls}')
    axes[1].scatter(scores_scaled[mask, 0], scores_scaled[mask, 1], c=colors[cls],
                    alpha=0.6, s=25, edgecolors='none', label=f'Class {cls}')

axes[0].set_title('Without Scaling', fontsize=15)
axes[0].set_xlabel('PC1')
axes[0].set_ylabel('PC2')
axes[0].legend(loc='upper left', fontsize=11)

axes[1].set_title('With Scaling', fontsize=15)
axes[1].set_xlabel('PC1')
axes[1].set_ylabel('PC2')
axes[1].legend(loc='upper left', fontsize=11)

fig.suptitle('The Impact of Feature Scaling on PCA', fontsize=16, fontweight='bold', y=0.98)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout(rect=[0, 0.02, 1, 0.95])
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: top10_11_scaling_effect/chart.pdf")
