"""PCA Loadings Heatmap - Component-feature loading heatmap showing feature contributions."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.decomposition import PCA
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "PCA Loadings: Feature Contributions per Component",
    "description": "Heatmap of PCA component loadings with annotated values",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top10_14_explained_var_heatmap"
}


feature_names = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8']
X, y = make_classification(n_samples=300, n_features=8, n_informative=5, random_state=42)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=5, random_state=42)
pca.fit(X_scaled)

loadings = pca.components_
pc_labels = [f'PC{i+1}' for i in range(5)]

fig, ax = plt.subplots()
vmax = np.abs(loadings).max()
im = ax.imshow(loadings, cmap='RdBu_r', aspect='auto', vmin=-vmax, vmax=vmax)
ax.grid(False)

ax.set_xticks(range(len(feature_names)))
ax.set_xticklabels(feature_names)
ax.set_yticks(range(len(pc_labels)))
ax.set_yticklabels(pc_labels)

for i in range(loadings.shape[0]):
    for j in range(loadings.shape[1]):
        color = 'white' if abs(loadings[i, j]) > vmax * 0.6 else 'black'
        ax.text(j, i, f'{loadings[i, j]:.2f}', ha='center', va='center',
                fontsize=10, color=color)

ax.set_title('PCA Loadings: Feature Contributions per Component')
cbar = plt.colorbar(im, ax=ax, shrink=0.8)
cbar.set_label('Loading Value', fontsize=12)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_14_explained_var_heatmap/chart.pdf")
