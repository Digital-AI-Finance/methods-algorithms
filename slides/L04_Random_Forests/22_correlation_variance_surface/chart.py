"""Ensemble Variance: Correlation vs Number of Trees"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Ensemble Variance: Correlation vs Number of Trees',
    'description': 'Heatmap of the ensemble variance formula Var/sigma^2 = rho + (1-rho)/B',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/22_correlation_variance_surface'
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

B = np.arange(1, 501)
rho = np.linspace(0.0, 1.0, 200)
B_grid, rho_grid = np.meshgrid(B, rho)

# Ensemble variance formula: Var/sigma^2 = rho + (1 - rho) / B
variance = rho_grid + (1 - rho_grid) / B_grid

fig, ax = plt.subplots()

pcm = ax.pcolormesh(B_grid, rho_grid, variance, cmap='YlOrRd', shading='auto', vmin=0, vmax=1)
cbar = fig.colorbar(pcm, ax=ax, label=r'Var / $\sigma^2$')

contour_levels = [0.1, 0.2, 0.5, 0.8]
cs = ax.contour(B_grid, rho_grid, variance, levels=contour_levels, colors='black', linewidths=1.0, linestyles='--')
ax.clabel(cs, inline=True, fontsize=11, fmt='%.1f')

# Sweet spot rectangle: rho < 0.2, B > 100
from matplotlib.patches import Rectangle
rect = Rectangle((100, 0.0), 400, 0.2, linewidth=2, edgecolor=MLGREEN, facecolor=MLGREEN,
                 alpha=0.25, linestyle='-', zorder=5)
ax.add_patch(rect)
ax.annotate('Sweet spot:\nlow correlation,\nmany trees',
            xy=(300, 0.10), fontsize=11, color='black', fontweight='bold',
            ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=MLGREEN, alpha=0.9))

ax.set_xlabel('Number of Trees (B)')
ax.set_ylabel(r'Pairwise Correlation ($\rho$)')
ax.set_title(CHART_METADATA['title'])

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 22_correlation_variance_surface/chart.pdf")
