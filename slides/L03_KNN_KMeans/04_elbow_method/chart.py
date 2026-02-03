"""Elbow Method - Choosing optimal K"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    "title": "Elbow Method",
    "description": "WCSS vs K for optimal cluster selection",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L03_KNN_KMeans/04_elbow_method"
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

# Compute inertia for different K
from sklearn.cluster import KMeans

K_range = range(1, 11)
inertias = []

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(K_range, inertias, 'o-', color=MLBLUE, linewidth=2, markersize=10)

# Highlight elbow point
elbow_k = 3
ax.scatter([elbow_k], [inertias[elbow_k-1]], c=MLRED, s=200, zorder=5,
           edgecolors='black', linewidth=2)
ax.annotate('Elbow Point\n(Optimal K=3)', xy=(elbow_k, inertias[elbow_k-1]),
            xytext=(elbow_k+1.5, inertias[elbow_k-1]+100),
            fontsize=12, arrowprops=dict(arrowstyle='->', color='black'),
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))

# Add shaded region
ax.axvspan(2.5, 3.5, alpha=0.2, color=MLGREEN)

ax.set_xlabel('Number of Clusters (K)')
ax.set_ylabel('Within-Cluster Sum of Squares (Inertia)')
ax.set_title('Elbow Method for Optimal K Selection')
ax.set_xticks(K_range)
ax.grid(True, alpha=0.3)

# Add interpretation
ax.text(7, inertias[2], 'Diminishing returns\nafter K=3', fontsize=11,
        color='gray', ha='left')

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 04_elbow_method/chart.pdf")
