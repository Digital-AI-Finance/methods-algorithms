"""KL Divergence: Asymmetric Penalty for different p values."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "KL Divergence: Asymmetric Penalty",
    "description": "Shows how KL divergence penalizes asymmetrically -- high p with low q produces a huge penalty",
    "url": "https://digital-ai-finance.github.io/methods-algorithms/slides/L05_PCA_tSNE/13_kl_divergence_asymmetry"
}

MLPurple = '#3333B2'
MLBlue = '#0066CC'
MLOrange = '#FF7F0E'
MLRed = '#D62728'

fig, ax = plt.subplots()

q = np.linspace(0.01, 1.0, 300)

for p, color, label in [
    (0.80, MLRed,    'p = 0.8 (true neighbors)'),
    (0.30, MLOrange, 'p = 0.3 (moderate)'),
    (0.05, MLBlue,   'p = 0.05 (distant)'),
]:
    kl_penalty = p * np.log(p / q)
    ax.plot(q, kl_penalty, color=color, linewidth=2.5, label=label)

# Annotate the high-p line at low q
ax.annotate('Neighbors torn apart\n$\\rightarrow$ BIG penalty',
            xy=(0.05, 0.8 * np.log(0.8 / 0.05)),
            xytext=(0.25, 2.8),
            fontsize=12, color=MLRed,
            arrowprops=dict(arrowstyle='->', color=MLRed, lw=2),
            ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor=MLRed, alpha=0.9))

ax.set_xlabel(r'Map similarity $q_{ij}$')
ax.set_ylabel(r'KL Penalty: $p \cdot \log(p/q)$')
ax.set_title('KL Divergence: Asymmetric Penalty')
ax.set_xlim(0, 1.0)
ax.set_ylim(bottom=0)
ax.legend(loc='upper right', fontsize=13)
ax.grid(True, alpha=0.3)

fig.text(0.99, 0.01, CHART_METADATA["url"],
         ha='right', va='bottom', fontsize=7, color='gray', alpha=0.6)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
