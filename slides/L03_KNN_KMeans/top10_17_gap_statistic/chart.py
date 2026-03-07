"""Gap Statistic - Finding optimal number of clusters using gap statistic."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

CHART_METADATA = {
    "title": "Gap Statistic: Finding the Optimal Number of Clusters",
    "description": "Gap statistic with reference distributions for k=1..10",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L03_KNN_KMeans/top10_17_gap_statistic"
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False,
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

X, _ = make_blobs(n_samples=300, centers=4, random_state=42)

ks = range(1, 11)
n_refs = 20

log_w_data = []
log_w_refs = []
log_w_ref_stds = []

# Bounding box for uniform reference data
x_min, x_max = X.min(axis=0), X.max(axis=0)

for k in ks:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X)
    log_w_data.append(np.log(km.inertia_))

    ref_inertias = []
    for r in range(n_refs):
        rng = np.random.RandomState(r + k * 100)
        X_ref = rng.uniform(x_min, x_max, size=X.shape)
        km_ref = KMeans(n_clusters=k, random_state=42, n_init=10)
        km_ref.fit(X_ref)
        ref_inertias.append(np.log(km_ref.inertia_))

    log_w_refs.append(np.mean(ref_inertias))
    log_w_ref_stds.append(np.std(ref_inertias))

gap = np.array(log_w_refs) - np.array(log_w_data)
gap_stds = np.array(log_w_ref_stds)

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(list(ks), gap, color=MLBLUE, alpha=0.7, edgecolor='white',
              yerr=gap_stds, capsize=5, error_kw={'color': 'gray', 'linewidth': 1.5})

# Highlight optimal k
optimal_k = np.argmax(gap) + 1
bars[optimal_k - 1].set_color(MLRED)
bars[optimal_k - 1].set_alpha(1.0)
ax.annotate(f'Optimal k={optimal_k}', (optimal_k, gap[optimal_k - 1]),
            textcoords="offset points", xytext=(20, 10), ha='left',
            fontsize=13, fontweight='bold', color=MLRED,
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=2))

ax.set_xlabel('Number of Clusters (k)')
ax.set_ylabel('Gap Statistic')
ax.set_title('Gap Statistic: Finding the Optimal Number of Clusters', fontweight='bold')
ax.set_xticks(list(ks))
ax.grid(True, alpha=0.3, axis='y')

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: top10_17_gap_statistic/chart.pdf")
