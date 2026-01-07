"""Voronoi Diagram - K-Means decision regions"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from scipy.spatial import Voronoi

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

np.random.seed(42)

# Generate clustered data
n_per_cluster = 40
c1 = np.random.randn(n_per_cluster, 2) * 0.6 + np.array([-2, 2])
c2 = np.random.randn(n_per_cluster, 2) * 0.6 + np.array([2, 2])
c3 = np.random.randn(n_per_cluster, 2) * 0.6 + np.array([0, -1])
X = np.vstack([c1, c2, c3])

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = kmeans.fit_predict(X)
centroids = kmeans.cluster_centers_

fig, ax = plt.subplots(figsize=(10, 6))

# Create mesh for decision boundary visualization
h = 0.05
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

colors = [MLRED, MLGREEN, MLBLUE]
ax.contourf(xx, yy, Z, levels=[-0.5, 0.5, 1.5, 2.5], colors=colors, alpha=0.15)
ax.contour(xx, yy, Z, levels=[0.5, 1.5], colors='gray', linestyles='-', linewidths=2)

# Plot data points
for i, color in enumerate(colors):
    cluster_points = X[labels == i]
    ax.scatter(cluster_points[:, 0], cluster_points[:, 1], c=color, s=60,
               alpha=0.8, edgecolors='white', linewidth=0.5)

# Plot centroids
for i, (centroid, color) in enumerate(zip(centroids, colors)):
    ax.scatter(centroid[0], centroid[1], c=color, s=300, marker='X',
               edgecolors='black', linewidth=2, zorder=5)

ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_title('K-Means Voronoi Regions (Decision Boundaries)')
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.grid(True, alpha=0.3)

# Add annotation
ax.text(0.02, 0.98, 'Each point assigned to\nnearest centroid', transform=ax.transAxes,
        fontsize=11, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 06_voronoi/chart.pdf")
