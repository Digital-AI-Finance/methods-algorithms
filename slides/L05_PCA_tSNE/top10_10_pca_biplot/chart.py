"""PCA Biplot - Scores (data points in PC1-PC2 space) plus loading arrows (feature contributions)."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.decomposition import PCA
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler

CHART_METADATA = {
    "title": "PCA Biplot: Scores and Loadings",
    "description": "Scatter of PCA scores with overlaid feature loading arrows",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top10_10_pca_biplot"
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

feature_names = ['Revenue', 'Cost', 'Growth', 'Risk', 'Volume', 'Rating']
X, y = make_classification(n_samples=200, n_features=6, n_informative=4, random_state=42)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=2, random_state=42)
scores = pca.fit_transform(X_scaled)

fig, ax = plt.subplots()

colors = [MLBLUE, MLORANGE]
labels = ['Class 0', 'Class 1']
for cls in [0, 1]:
    mask = y == cls
    ax.scatter(scores[mask, 0], scores[mask, 1], c=colors[cls], alpha=0.5,
               s=30, label=labels[cls], edgecolors='none')

loadings = pca.components_.T
scale = np.abs(scores).max() * 0.8 / np.abs(loadings).max()

for i, name in enumerate(feature_names):
    ax.annotate('', xy=(loadings[i, 0] * scale, loadings[i, 1] * scale), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color=MLRED, lw=2))
    offset_x = 0.3 if loadings[i, 0] >= 0 else -0.3
    offset_y = 0.3 if loadings[i, 1] >= 0 else -0.3
    ax.text(loadings[i, 0] * scale + offset_x, loadings[i, 1] * scale + offset_y,
            name, fontsize=11, fontweight='bold', color=MLRED, ha='center', va='center')

ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%} variance)')
ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%} variance)')
ax.set_title('PCA Biplot: Scores and Loadings')
ax.axhline(0, color='gray', linewidth=0.5, alpha=0.5)
ax.axvline(0, color='gray', linewidth=0.5, alpha=0.5)
ax.legend(loc='upper left', framealpha=0.9)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: top10_10_pca_biplot/chart.pdf")
