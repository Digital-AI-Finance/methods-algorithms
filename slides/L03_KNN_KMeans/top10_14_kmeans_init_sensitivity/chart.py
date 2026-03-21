"""K-Means Initialization Sensitivity - Random vs K-Means++ inertia distributions."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Initialization Sensitivity: Random vs K-Means++",
    "description": "Histogram of inertias for 50 random vs 50 k-means++ initializations",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L03_KNN_KMeans/top10_14_kmeans_init_sensitivity"
}


X, _ = make_blobs(n_samples=500, centers=5, random_state=42)

inertias_random = []
inertias_pp = []

for i in range(50):
    km_rand = KMeans(n_clusters=5, init='random', n_init=1, random_state=i)
    km_rand.fit(X)
    inertias_random.append(km_rand.inertia_)

    km_pp = KMeans(n_clusters=5, init='k-means++', n_init=1, random_state=i)
    km_pp.fit(X)
    inertias_pp.append(km_pp.inertia_)

fig, ax = plt.subplots(figsize=(10, 6))

bins = np.linspace(min(min(inertias_random), min(inertias_pp)) * 0.95,
                   max(max(inertias_random), max(inertias_pp)) * 1.05, 25)

ax.hist(inertias_random, bins=bins, alpha=0.5, color=MLRED, label='Random init', edgecolor='white')
ax.hist(inertias_pp, bins=bins, alpha=0.5, color=MLBLUE, label='K-Means++', edgecolor='white')

# Mean lines
mean_rand = np.mean(inertias_random)
mean_pp = np.mean(inertias_pp)
ax.axvline(mean_rand, color=MLRED, linestyle='--', linewidth=2.5,
           label=f'Random mean = {mean_rand:.0f}')
ax.axvline(mean_pp, color=MLBLUE, linestyle='--', linewidth=2.5,
           label=f'K-Means++ mean = {mean_pp:.0f}')

ax.set_xlabel('Inertia')
ax.set_ylabel('Count')
ax.set_title('Initialization Sensitivity: Random vs K-Means++', fontweight='bold')
ax.legend(loc='upper right', framealpha=0.9)
ax.grid(True, alpha=0.3, axis='y')

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_14_kmeans_init_sensitivity/chart.pdf")
