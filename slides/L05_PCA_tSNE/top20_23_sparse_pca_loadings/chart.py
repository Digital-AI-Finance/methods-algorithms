"""Sparse PCA vs Standard PCA Loadings."""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_classification
from sklearn.decomposition import SparsePCA
from sklearn.preprocessing import StandardScaler
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Sparse PCA vs Standard PCA Loadings",
    "description": "Horizontal bar chart of SparsePCA PC1 loadings across 15 features.",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top20_23_sparse_pca_loadings"
}


np.random.seed(42)

# Generate classification data
X, y = make_classification(n_samples=500, n_features=15, n_informative=5,
                           n_redundant=3, n_classes=2, random_state=42)
X = StandardScaler().fit_transform(X)

# Sparse PCA
spca = SparsePCA(n_components=1, alpha=1.0, random_state=42)
spca.fit(X)
loadings = spca.components_[0]

# Feature labels
features = [f'Feature_{i+1:02d}' for i in range(15)]

# Sort by absolute loading for display
sort_idx = np.argsort(np.abs(loadings))
loadings_sorted = loadings[sort_idx]
features_sorted = [features[i] for i in sort_idx]

# Color by sign
colors = [MLBLUE if v >= 0 else MLORANGE for v in loadings_sorted]

fig, ax = plt.subplots()

ax.barh(range(len(loadings_sorted)), loadings_sorted, color=colors,
        edgecolor='white', linewidth=0.3, height=0.7)

ax.set_yticks(range(len(features_sorted)))
ax.set_yticklabels(features_sorted)
ax.set_xlabel('Sparse PCA Loading (PC1)')
ax.set_title('Sparse PCA Loadings ($\\alpha=1.0$)')
ax.axvline(x=0, color='gray', linewidth=0.8, linestyle='-')

# Legend for sign colors
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=MLBLUE, label='Positive loading'),
    Patch(facecolor=MLORANGE, label='Negative loading'),
]
ax.legend(handles=legend_elements, loc='lower right')

# Count zero loadings
n_zero = np.sum(np.abs(loadings) < 1e-6)
ax.annotate(f'{n_zero} of 15 loadings = 0\n(sparsity enforced)',
            xy=(0.97, 0.05), xycoords='axes fraction', ha='right', va='bottom',
            fontsize=11, color='gray', style='italic')

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray',
            ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
