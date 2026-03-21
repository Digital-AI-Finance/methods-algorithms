"""KNN Weighted vs Uniform - Comparing uniform and distance-weighted KNN decision boundaries."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "KNN: Uniform vs Distance-Weighted Voting (k=15)",
    "description": "Two KNN classifiers on make_moons comparing uniform and distance-weighted boundaries",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L03_KNN_KMeans/top10_11_knn_weighted_vs_uniform"
}


# Generate data
X, y = make_moons(n_samples=300, noise=0.3, random_state=42)

# Fit both models
knn_uniform = KNeighborsClassifier(n_neighbors=15, weights='uniform')
knn_distance = KNeighborsClassifier(n_neighbors=15, weights='distance')
knn_uniform.fit(X, y)
knn_distance.fit(X, y)

# Create mesh for decision boundaries
h = 0.02
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
grid = np.c_[xx.ravel(), yy.ravel()]

Z_distance = knn_distance.predict(grid).reshape(xx.shape)
Z_uniform = knn_uniform.predict(grid).reshape(xx.shape)

fig, ax = plt.subplots(figsize=(10, 6))

# Distance-weighted: filled contour
from matplotlib.colors import ListedColormap
cmap_light = ListedColormap([MLBLUE + '33', MLORANGE + '33'])
ax.contourf(xx, yy, Z_distance, alpha=0.25, cmap=cmap_light, levels=1)

# Uniform: contour lines only
ax.contour(xx, yy, Z_uniform, levels=[0.5], colors='gray', linestyles='dashed', linewidths=2)

# Scatter data points
scatter_colors = [MLBLUE, MLORANGE]
for cls in [0, 1]:
    mask = y == cls
    ax.scatter(X[mask, 0], X[mask, 1], c=scatter_colors[cls],
               alpha=0.6, s=30, edgecolors='white', linewidth=0.3)

# Legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color=MLBLUE, linewidth=0, marker='s', markersize=12,
           markerfacecolor=MLBLUE, alpha=0.3, label='Distance-weighted boundary'),
    Line2D([0], [0], color='gray', linewidth=2, linestyle='dashed',
           label='Uniform boundary'),
]
ax.legend(handles=legend_elements, loc='upper right', framealpha=0.9)

ax.set_title('KNN: Uniform vs Distance-Weighted Voting (k=15)', fontweight='bold')
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_11_knn_weighted_vs_uniform/chart.pdf")
