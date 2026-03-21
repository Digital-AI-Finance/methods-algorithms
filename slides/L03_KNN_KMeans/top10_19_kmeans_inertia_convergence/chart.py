"""K-Means Inertia Convergence - Inertia dropping over iterations."""
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
    "title": "K-Means Convergence: Inertia per Iteration",
    "description": "Tracking inertia across 15 manual K-Means iterations",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L03_KNN_KMeans/top10_19_kmeans_inertia_convergence"
}


X, _ = make_blobs(n_samples=500, centers=5, random_state=42)

# First run with max_iter=1 to get initial centers
km = KMeans(n_clusters=5, max_iter=1, n_init=1, init='random', random_state=42)
km.fit(X)

inertias = [km.inertia_]
centers = km.cluster_centers_.copy()

for i in range(14):
    km = KMeans(n_clusters=5, max_iter=1, n_init=1, init=centers, random_state=42)
    km.fit(X)
    inertias.append(km.inertia_)
    centers = km.cluster_centers_.copy()

iterations = list(range(1, len(inertias) + 1))

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(iterations, inertias, color=MLBLUE, marker='o', markersize=8,
        linewidth=2.5, markeredgecolor='white', markeredgewidth=1.5, zorder=5)

# Final inertia horizontal line
final_inertia = inertias[-1]
ax.axhline(y=final_inertia, color=MLORANGE, linestyle='--', linewidth=2, alpha=0.7,
           label=f'Converged inertia = {final_inertia:.0f}')

# Mark convergence region
converge_idx = None
for i in range(1, len(inertias)):
    if abs(inertias[i] - inertias[i-1]) / inertias[i-1] < 0.001:
        converge_idx = i
        break

if converge_idx:
    ax.axvspan(converge_idx + 1, len(inertias), alpha=0.1, color=MLGREEN)
    ax.annotate('Converged', (converge_idx + 1.5, inertias[converge_idx]),
                textcoords="offset points", xytext=(20, 20),
                fontsize=12, fontweight='bold', color=MLGREEN,
                arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=2))

ax.set_xlabel('Iteration')
ax.set_ylabel('Inertia')
ax.set_title('K-Means Convergence: Inertia per Iteration', fontweight='bold')
ax.legend(loc='upper right', framealpha=0.9)
ax.set_xticks(iterations)
ax.grid(True, alpha=0.3)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_19_kmeans_inertia_convergence/chart.pdf")
