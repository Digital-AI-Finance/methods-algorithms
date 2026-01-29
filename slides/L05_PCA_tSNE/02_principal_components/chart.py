"""Principal Components Visualization - 2D projection of portfolio data"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Principal Components',
    'description': 'PC vectors visualized on correlated asset returns scatter',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/02_principal_components'
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLORANGE = '#FF7F0E'

np.random.seed(42)

# Generate correlated asset returns data
n_samples = 200
mean = [0, 0]
cov = [[1, 0.7], [0.7, 1]]  # Correlated
X = np.random.multivariate_normal(mean, cov, n_samples)

# Compute principal components
from numpy.linalg import eig
cov_matrix = np.cov(X.T)
eigenvalues, eigenvectors = eig(cov_matrix)

# Sort by eigenvalue
idx = eigenvalues.argsort()[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

fig, ax = plt.subplots(figsize=(10, 6))

# Plot data points
ax.scatter(X[:, 0], X[:, 1], c=MLBLUE, alpha=0.5, s=40, label='Asset returns')

# Plot principal component directions
origin = np.mean(X, axis=0)
for i, (val, vec) in enumerate(zip(eigenvalues, eigenvectors.T)):
    scale = np.sqrt(val) * 2
    color = MLRED if i == 0 else MLORANGE
    ax.annotate('', xy=origin + vec * scale, xytext=origin,
                arrowprops=dict(arrowstyle='->', color=color, lw=3))
    ax.text(origin[0] + vec[0] * scale * 1.1,
            origin[1] + vec[1] * scale * 1.1,
            f'PC{i+1} ({eigenvalues[i]/sum(eigenvalues)*100:.0f}%)',
            fontsize=12, fontweight='bold', color=color)

ax.set_xlabel('Asset 1 Returns', fontweight='bold')
ax.set_ylabel('Asset 2 Returns', fontweight='bold')
ax.set_title('Principal Components of Correlated Asset Returns',
             fontsize=16, fontweight='bold')
ax.axhline(y=0, color='gray', linestyle='-', alpha=0.3)
ax.axvline(x=0, color='gray', linestyle='-', alpha=0.3)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.legend(loc='upper left')

# Add annotation
ax.text(0.02, 0.02, 'PC1: Market factor\nPC2: Idiosyncratic',
        transform=ax.transAxes, fontsize=10, verticalalignment='bottom',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 02_principal_components/chart.pdf")
