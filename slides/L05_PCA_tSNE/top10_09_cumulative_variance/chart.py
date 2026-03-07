"""Cumulative Explained Variance Ratio - Shows how many PCA components are needed to capture 90%/95% of variance."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.decomposition import PCA
from sklearn.datasets import make_classification

CHART_METADATA = {
    "title": "Cumulative Explained Variance Ratio",
    "description": "Step plot of cumulative variance with 90% and 95% threshold lines",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top10_09_cumulative_variance"
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

X, y = make_classification(n_samples=500, n_features=15, n_informative=8, random_state=42)

pca = PCA(n_components=15, random_state=42)
pca.fit(X)

cumulative = np.cumsum(pca.explained_variance_ratio_)
components = np.arange(1, 16)

fig, ax = plt.subplots()
ax.step(components, cumulative, where='mid', color=MLBLUE, linewidth=2.5, label='Cumulative variance')
ax.fill_between(components, cumulative, step='mid', alpha=0.2, color=MLBLUE)

ax.axhline(y=0.90, color=MLRED, linestyle='--', linewidth=1.5, alpha=0.8, label='90% threshold')
ax.axhline(y=0.95, color=MLRED, linestyle=':', linewidth=1.5, alpha=0.8, label='95% threshold')

n90 = np.argmax(cumulative >= 0.90) + 1
ax.axvline(x=n90, color=MLGREEN, linestyle='--', linewidth=1.5, alpha=0.8)
ax.annotate(f'{n90} components\nfor 90%', xy=(n90, 0.90), xytext=(n90 + 1.5, 0.78),
            fontsize=12, color=MLGREEN, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=1.5))

ax.set_xlabel('Number of Components')
ax.set_ylabel('Cumulative Explained Variance')
ax.set_title('Cumulative Explained Variance Ratio')
ax.set_xlim(0.5, 15.5)
ax.set_ylim(0, 1.05)
ax.set_xticks(components)
ax.legend(loc='center right', framealpha=0.9)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: top10_09_cumulative_variance/chart.pdf")
