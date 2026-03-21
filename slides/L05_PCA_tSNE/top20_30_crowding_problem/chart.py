"""The Crowding Problem: Gaussian vs Student-t Kernels - Compares kernel tails to illustrate the crowding solution."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "The Crowding Problem: Gaussian vs Student-t Kernels",
    "description": "Overlaid curves of Gaussian and Student-t kernels showing heavier tails that alleviate crowding.",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top20_30_crowding_problem"
}


np.random.seed(42)

x = np.linspace(0, 5, 200)

# Gaussian kernel (unnormalized similarity)
q_gauss_raw = np.exp(-x ** 2)
q_gauss = q_gauss_raw / q_gauss_raw.sum()

# Student-t kernel (1 degree of freedom)
q_t_raw = (1 + x ** 2) ** (-1)
q_t = q_t_raw / q_t_raw.sum()

fig, ax = plt.subplots()

ax.plot(x, q_gauss, color=MLBLUE, linewidth=2.5, linestyle='--', label='Gaussian kernel', zorder=3)
ax.plot(x, q_t, color=MLORANGE, linewidth=2.5, linestyle='-', label="Student-t kernel (df=1)", zorder=3)

# Fill between in tail region where t > gauss
mask = (x >= 1.0) & (x <= 3.0)
ax.fill_between(x[mask], q_gauss[mask], q_t[mask], alpha=0.25, color=MLORANGE, zorder=2)

# Annotate crowding zone
mid_x = 2.0
mid_y = (q_t[np.argmin(np.abs(x - mid_x))] + q_gauss[np.argmin(np.abs(x - mid_x))]) / 2
ax.annotate('Crowding zone\nGaussian drops to zero,\nbut Student-t retains mass',
            xy=(mid_x, mid_y), xytext=(3.2, max(q_t) * 0.55),
            fontsize=11, ha='left',
            arrowprops=dict(arrowstyle='->', color='gray', lw=1.5),
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFF3CD', edgecolor=MLORANGE, alpha=0.9))

ax.set_xlabel('Pairwise Distance in Embedding Space')
ax.set_ylabel('Kernel Value (normalized)')
ax.set_title('The Crowding Problem: Gaussian vs Student-t Kernels')
ax.legend(loc='upper right', framealpha=0.9)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
