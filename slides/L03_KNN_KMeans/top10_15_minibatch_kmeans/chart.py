"""Mini-Batch K-Means - Speed vs quality tradeoff compared to standard K-Means."""
import matplotlib.pyplot as plt
import numpy as np
import time
from pathlib import Path
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.datasets import make_blobs
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Mini-Batch K-Means: Speed vs Quality Tradeoff",
    "description": "Time and inertia comparison of KMeans vs MiniBatchKMeans across dataset sizes",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L03_KNN_KMeans/top10_15_minibatch_kmeans"
}


X_full, _ = make_blobs(n_samples=5000, centers=8, random_state=42)

sample_sizes = [100, 500, 1000, 2000, 5000]
times_km = []
times_mb = []
inertias_km = []
inertias_mb = []

for n in sample_sizes:
    X = X_full[:n]

    t0 = time.time()
    km = KMeans(n_clusters=8, random_state=42, n_init=10)
    km.fit(X)
    times_km.append(time.time() - t0)
    inertias_km.append(km.inertia_)

    t0 = time.time()
    mb = MiniBatchKMeans(n_clusters=8, random_state=42, n_init=10, batch_size=100)
    mb.fit(X)
    times_mb.append(time.time() - t0)
    inertias_mb.append(mb.inertia_)

fig, ax1 = plt.subplots(figsize=(10, 6))

# Time on primary y-axis
ln1 = ax1.plot(sample_sizes, times_km, color=MLRED, marker='o', markersize=8,
               linewidth=2.5, label='KMeans time', markeredgecolor='white')
ln2 = ax1.plot(sample_sizes, times_mb, color=MLBLUE, marker='s', markersize=8,
               linewidth=2.5, label='MiniBatch time', markeredgecolor='white')
ax1.set_xlabel('Number of Samples')
ax1.set_ylabel('Time (seconds)', color='black')
ax1.tick_params(axis='y')

# Inertia on secondary y-axis
ax2 = ax1.twinx()
ax2.grid(False)
ln3 = ax2.plot(sample_sizes, inertias_km, color=MLRED, marker='o', markersize=6,
               linewidth=1.5, linestyle='--', alpha=0.7, label='KMeans inertia')
ln4 = ax2.plot(sample_sizes, inertias_mb, color=MLBLUE, marker='s', markersize=6,
               linewidth=1.5, linestyle='--', alpha=0.7, label='MiniBatch inertia')
ax2.set_ylabel('Inertia', color='gray')
ax2.tick_params(axis='y', labelcolor='gray')
ax2.spines['top'].set_visible(False)

# Combined legend
lns = ln1 + ln2 + ln3 + ln4
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc='upper left', framealpha=0.9)

ax1.set_title('Mini-Batch K-Means: Speed vs Quality Tradeoff', fontweight='bold')
ax1.grid(True, alpha=0.3)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_15_minibatch_kmeans/chart.pdf")
