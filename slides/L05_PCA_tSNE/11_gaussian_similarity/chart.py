"""Gaussian Kernel: Distance to Similarity for different sigma values."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Gaussian Kernel: Distance to Similarity",
    "description": "Shows how the Gaussian kernel converts distances to similarity probabilities for different sigma values",
    "url": "https://digital-ai-finance.github.io/methods-algorithms/slides/L05_PCA_tSNE/11_gaussian_similarity"
}

MLPurple = '#3333B2'
MLBlue = '#0066CC'
MLOrange = '#FF7F0E'
MLGreen = '#2CA02C'
MLRed = '#D62728'
MLGray = '#7F7F7F'

fig, ax = plt.subplots()

d = np.linspace(0, 5, 300)

for sigma, color, label in [
    (0.5, MLPurple, r'$\sigma = 0.5$ (tight)'),
    (1.0, MLBlue,   r'$\sigma = 1.0$ (default)'),
    (2.0, MLOrange, r'$\sigma = 2.0$ (wide)'),
]:
    similarity = np.exp(-d**2 / (2 * sigma**2))
    ax.plot(d, similarity, color=color, linewidth=2.5, label=label)

# Vertical annotation lines
ax.axvline(x=1.0, color=MLGray, linestyle='--', linewidth=1.2, alpha=0.7)
ax.text(1.05, 0.92, 'nearby', fontsize=12, color=MLGray, ha='left', va='top')

ax.axvline(x=3.0, color=MLGray, linestyle='--', linewidth=1.2, alpha=0.7)
ax.text(3.05, 0.92, 'far away', fontsize=12, color=MLGray, ha='left', va='top')

ax.set_xlabel(r'Distance $\|x_i - x_j\|$')
ax.set_ylabel(r'Similarity $p(j|i)$')
ax.set_title(r'Gaussian Kernel: Distance $\rightarrow$ Similarity')
ax.set_xlim(0, 5)
ax.set_ylim(0, 1.05)
ax.legend(loc='upper right', fontsize=13)
ax.grid(True, alpha=0.3)

fig.text(0.99, 0.01, CHART_METADATA["url"],
         ha='right', va='bottom', fontsize=7, color='gray', alpha=0.6)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
