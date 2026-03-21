"""K-Means Failure Cases - K-Means on moons vs blobs showing when it fails."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.cluster import KMeans
from sklearn.datasets import make_moons, make_blobs
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "When K-Means Fails: Cluster Shape Matters",
    "description": "K-Means on make_moons (fails) vs make_blobs (succeeds) side-by-side",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L03_KNN_KMeans/top10_10_kmeans_failure_cases"
}


# Generate data
X_moons, y_moons = make_moons(n_samples=300, noise=0.1, random_state=42)
X_blobs, y_blobs = make_blobs(n_samples=300, centers=2, random_state=42)

# Fit K-Means
km_moons = KMeans(n_clusters=2, random_state=42, n_init=10)
km_blobs = KMeans(n_clusters=2, random_state=42, n_init=10)
labels_moons = km_moons.fit_predict(X_moons)
labels_blobs = km_blobs.fit_predict(X_blobs)

colors = [MLBLUE, MLORANGE]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))

# Left: moons (failure)
for i in range(2):
    mask = labels_moons == i
    ax1.scatter(X_moons[mask, 0], X_moons[mask, 1], c=colors[i],
                alpha=0.6, s=30, edgecolors='white', linewidth=0.3)
ax1.scatter(km_moons.cluster_centers_[:, 0], km_moons.cluster_centers_[:, 1],
            c=MLRED, marker='X', s=200, edgecolors='black', linewidth=1.5, zorder=5)
ax1.set_title('K-Means on Moons (Fails)', fontweight='bold', color=MLRED)
ax1.set_xlabel('Feature 1')
ax1.set_ylabel('Feature 2')

# Right: blobs (success)
for i in range(2):
    mask = labels_blobs == i
    ax2.scatter(X_blobs[mask, 0], X_blobs[mask, 1], c=colors[i],
                alpha=0.6, s=30, edgecolors='white', linewidth=0.3)
ax2.scatter(km_blobs.cluster_centers_[:, 0], km_blobs.cluster_centers_[:, 1],
            c=MLRED, marker='X', s=200, edgecolors='black', linewidth=1.5, zorder=5)
ax2.set_title('K-Means on Blobs (Succeeds)', fontweight='bold', color=MLGREEN)
ax2.set_xlabel('Feature 1')
ax2.set_ylabel('Feature 2')

fig.suptitle('When K-Means Fails: Cluster Shape Matters', fontsize=16, fontweight='bold', y=0.98)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_10_kmeans_failure_cases/chart.pdf")
