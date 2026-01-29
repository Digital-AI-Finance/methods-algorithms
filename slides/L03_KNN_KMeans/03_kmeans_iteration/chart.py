"""K-Means Iteration - Clustering process visualization"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    "title": "K-Means Clustering",
    "description": "Converged solution with cluster assignments",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L03_KNN_KMeans/03_kmeans_iteration"
}

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

# Run K-Means manually for visualization
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=42, n_init=1, max_iter=10)
kmeans.fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

fig, ax = plt.subplots(figsize=(10, 6))

colors = [MLRED, MLGREEN, MLBLUE]
for i, color in enumerate(colors):
    cluster_points = X[labels == i]
    ax.scatter(cluster_points[:, 0], cluster_points[:, 1], c=color, s=60,
               alpha=0.7, edgecolors='white', linewidth=0.5)

# Plot centroids
for i, (centroid, color) in enumerate(zip(centroids, colors)):
    ax.scatter(centroid[0], centroid[1], c=color, s=300, marker='X',
               edgecolors='black', linewidth=2, zorder=5)
    ax.annotate(f'C{i+1}', xy=(centroid[0], centroid[1]),
                xytext=(centroid[0]+0.3, centroid[1]+0.3),
                fontsize=12, fontweight='bold')

# Draw lines from points to centroids (for a few points)
for i, color in enumerate(colors):
    cluster_points = X[labels == i][:5]
    for point in cluster_points:
        ax.plot([point[0], centroids[i][0]], [point[1], centroids[i][1]],
                color=color, alpha=0.3, linewidth=1)

ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_title('K-Means Clustering: Converged Solution (K=3)')
ax.grid(True, alpha=0.3)

# Add legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor=MLRED,
           markersize=10, label='Cluster 1'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=MLGREEN,
           markersize=10, label='Cluster 2'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=MLBLUE,
           markersize=10, label='Cluster 3'),
    Line2D([0], [0], marker='X', color='w', markerfacecolor='gray',
           markersize=12, markeredgecolor='black', label='Centroids')
]
ax.legend(handles=legend_elements, loc='upper right')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 03_kmeans_iteration/chart.pdf")
