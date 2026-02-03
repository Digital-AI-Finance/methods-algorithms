"""Silhouette Analysis - Cluster quality visualization"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    "title": "Silhouette Analysis",
    "description": "Cluster cohesion and separation quality",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L03_KNN_KMeans/05_silhouette"
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

np.random.seed(42)

# Generate clustered data
n_per_cluster = 50
c1 = np.random.randn(n_per_cluster, 2) * 0.6 + np.array([-2, 2])
c2 = np.random.randn(n_per_cluster, 2) * 0.6 + np.array([2, 2])
c3 = np.random.randn(n_per_cluster, 2) * 0.6 + np.array([0, -1])
X = np.vstack([c1, c2, c3])

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples

# Fit K-Means
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = kmeans.fit_predict(X)

# Compute silhouette scores
silhouette_avg = silhouette_score(X, labels)
sample_silhouette_values = silhouette_samples(X, labels)

fig, ax = plt.subplots(figsize=(10, 6))

colors = [MLRED, MLGREEN, MLBLUE]
y_lower = 10

for i in range(3):
    cluster_silhouette_values = sample_silhouette_values[labels == i]
    cluster_silhouette_values.sort()

    size_cluster_i = cluster_silhouette_values.shape[0]
    y_upper = y_lower + size_cluster_i

    ax.fill_betweenx(np.arange(y_lower, y_upper),
                     0, cluster_silhouette_values,
                     facecolor=colors[i], edgecolor=colors[i], alpha=0.7)

    ax.text(-0.05, y_lower + 0.5 * size_cluster_i, f'Cluster {i+1}',
            fontsize=11, fontweight='bold')

    y_lower = y_upper + 10

# Average line
ax.axvline(x=silhouette_avg, color='black', linestyle='--', linewidth=2,
           label=f'Average silhouette = {silhouette_avg:.3f}')

ax.set_xlabel('Silhouette Coefficient')
ax.set_ylabel('Samples (grouped by cluster)')
ax.set_title('Silhouette Plot for K-Means Clustering (K=3)')
ax.set_xlim([-0.1, 1])
ax.set_yticks([])
ax.legend(loc='upper right')

# Add interpretation
interpretation = ('Silhouette Score:\n'
                  '  1.0 = Perfect separation\n'
                  '  0.0 = Overlapping clusters\n'
                  ' -1.0 = Wrong cluster')
ax.text(0.65, 30, interpretation, fontsize=10,
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 05_silhouette/chart.pdf")
