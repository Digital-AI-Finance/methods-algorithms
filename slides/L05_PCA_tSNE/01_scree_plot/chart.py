"""Scree Plot - Variance explained by principal components"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Scree Plot',
    'description': 'Eigenvalue magnitudes and cumulative variance explained',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/01_scree_plot'
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

# Simulated eigenvalues (variance explained)
n_components = 10
eigenvalues = np.array([4.5, 2.8, 1.5, 0.8, 0.5, 0.35, 0.25, 0.15, 0.1, 0.07])
variance_explained = eigenvalues / eigenvalues.sum()
cumulative_variance = np.cumsum(variance_explained)

fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart for individual variance
x = np.arange(1, n_components + 1)
bars = ax1.bar(x, variance_explained * 100, color=MLBLUE, alpha=0.7,
               edgecolor='black', linewidth=1, label='Individual')
ax1.set_xlabel('Principal Component', fontweight='bold')
ax1.set_ylabel('Variance Explained (%)', color=MLBLUE, fontweight='bold')
ax1.tick_params(axis='y', labelcolor=MLBLUE)
ax1.set_xticks(x)

# Line chart for cumulative variance
ax2 = ax1.twinx()
ax2.plot(x, cumulative_variance * 100, 'o-', color=MLRED, linewidth=2.5,
         markersize=8, label='Cumulative')
ax2.set_ylabel('Cumulative Variance (%)', color=MLRED, fontweight='bold')
ax2.tick_params(axis='y', labelcolor=MLRED)

# Mark 80% and 95% thresholds
ax2.axhline(y=80, color='gray', linestyle='--', alpha=0.5)
ax2.axhline(y=95, color='gray', linestyle='--', alpha=0.5)
ax2.text(9.5, 81, '80%', fontsize=10, color='gray')
ax2.text(9.5, 96, '95%', fontsize=10, color='gray')

# Find elbow point
ax1.axvline(x=3, color=MLGREEN, linestyle='--', alpha=0.7)
ax1.annotate('Elbow', xy=(3, variance_explained[2]*100),
             xytext=(4.5, variance_explained[2]*100 + 5),
             arrowprops=dict(arrowstyle='->', color=MLGREEN),
             fontsize=11, color=MLGREEN)

# Legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='center right')

ax1.set_title('Scree Plot: Variance Explained by Principal Components',
              fontsize=16, fontweight='bold')
ax1.set_ylim(0, 50)
ax2.set_ylim(0, 105)
ax1.grid(True, alpha=0.3, axis='y')

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 01_scree_plot/chart.pdf")
