"""Yield Curve PCA Factor Loadings - Level, Slope, Curvature"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from pathlib import Path

CHART_METADATA = {
    "title": "Yield Curve PCA: What the Three Factors Look Like",
    "description": "Factor loadings of first 3 PCA components across 5 maturities",
    "url": "https://digital-ai-finance.github.io/methods-algorithms/slides/L05_PCA_tSNE/09_yield_curve_factors"
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False
})

MLPURPLE = '#3333B2'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'

np.random.seed(42)

maturities = ['1Y', '2Y', '5Y', '10Y', '30Y']
# Correlation matrix mimicking yield curve behavior
corr = np.array([
    [1.0, 0.95, 0.85, 0.75, 0.65],
    [0.95, 1.0, 0.92, 0.82, 0.72],
    [0.85, 0.92, 1.0, 0.93, 0.83],
    [0.75, 0.82, 0.93, 1.0, 0.94],
    [0.65, 0.72, 0.83, 0.94, 1.0],
])
vols = np.array([0.08, 0.07, 0.06, 0.05, 0.04])
cov = np.outer(vols, vols) * corr
X = np.random.multivariate_normal(np.zeros(5), cov, 500)

pca = PCA(n_components=3)
pca.fit(X)

fig, ax = plt.subplots(figsize=(10, 6))
x_pos = np.arange(len(maturities))
width = 0.25

bars1 = ax.bar(x_pos - width, pca.components_[0], width, color=MLPURPLE, label=f'PC1 "Level" ({pca.explained_variance_ratio_[0]*100:.0f}%)', alpha=0.85)
bars2 = ax.bar(x_pos, pca.components_[1], width, color=MLORANGE, label=f'PC2 "Slope" ({pca.explained_variance_ratio_[1]*100:.0f}%)', alpha=0.85)
bars3 = ax.bar(x_pos + width, pca.components_[2], width, color=MLGREEN, label=f'PC3 "Curvature" ({pca.explained_variance_ratio_[2]*100:.0f}%)', alpha=0.85)

ax.set_xlabel('Maturity')
ax.set_ylabel('Loading (Eigenvector Value)')
ax.set_title('Yield Curve PCA: What the Three Factors Look Like')
ax.set_xticks(x_pos)
ax.set_xticklabels(maturities)
ax.legend(loc='upper left', fontsize=11)
ax.axhline(y=0, color='gray', linewidth=0.8, linestyle='-')
ax.grid(True, alpha=0.3, axis='y')

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
