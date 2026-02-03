"""Reconstruction Error - Comparing different numbers of components"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Reconstruction Error',
    'description': 'Error vs number of components showing diminishing returns',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/03_reconstruction'
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
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLORANGE = '#FF7F0E'

np.random.seed(42)

# Simulated reconstruction error data
n_features = 20
n_components = np.arange(1, n_features + 1)

# Reconstruction error decreases as we add components
# Error = sum of discarded eigenvalues
eigenvalues = np.array([5, 3, 2, 1.5, 1, 0.8, 0.6, 0.5, 0.4, 0.35,
                        0.3, 0.25, 0.2, 0.18, 0.15, 0.12, 0.1, 0.08, 0.06, 0.05])
total_variance = eigenvalues.sum()
reconstruction_error = [(total_variance - eigenvalues[:k].sum()) / total_variance * 100
                        for k in n_components]

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(n_components, reconstruction_error, 'o-', color=MLBLUE,
        linewidth=2.5, markersize=8)

# Highlight key points
ax.scatter([3], [reconstruction_error[2]], c=MLGREEN, s=200, zorder=5,
           marker='*', label=f'k=3: {reconstruction_error[2]:.1f}% error')
ax.scatter([5], [reconstruction_error[4]], c=MLORANGE, s=200, zorder=5,
           marker='*', label=f'k=5: {reconstruction_error[4]:.1f}% error')

# Threshold lines
ax.axhline(y=10, color='gray', linestyle='--', alpha=0.5)
ax.text(19, 11, '10% error', fontsize=10, color='gray')

ax.axhline(y=5, color='gray', linestyle='--', alpha=0.5)
ax.text(19, 6, '5% error', fontsize=10, color='gray')

ax.set_xlabel('Number of Components (k)', fontweight='bold')
ax.set_ylabel('Reconstruction Error (%)', fontweight='bold')
ax.set_title('PCA Reconstruction Error vs Number of Components',
             fontsize=16, fontweight='bold')
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 21)
ax.set_ylim(0, 70)

# Add annotation about trade-off
ax.annotate('Diminishing returns\nafter k=5', xy=(8, reconstruction_error[7]),
            xytext=(12, 35), fontsize=10,
            arrowprops=dict(arrowstyle='->', color='gray'),
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 03_reconstruction/chart.pdf")
