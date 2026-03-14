"""Gaussian vs Student-t: The Heavy-Tail Advantage."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    "title": "Gaussian vs Student-t: The Heavy-Tail Advantage",
    "description": "Compares Gaussian and Student-t kernel tails, showing why Student-t solves the crowding problem",
    "url": "https://digital-ai-finance.github.io/methods-algorithms/slides/L05_PCA_tSNE/12_student_t_vs_gaussian"
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False
})

MLBlue = '#0066CC'
MLOrange = '#FF7F0E'

fig, ax = plt.subplots()

d = np.linspace(0, 6, 400)

gaussian = np.exp(-d**2 / 2)
student_t = 1.0 / (1.0 + d**2)

ax.plot(d, gaussian, color=MLBlue, linewidth=2.5, label='Gaussian (high-D)')
ax.plot(d, student_t, color=MLOrange, linewidth=2.5, label='Student-t (low-D)')

# Fill the area between curves for d > 1.5
mask = d >= 1.5
ax.fill_between(d[mask], gaussian[mask], student_t[mask],
                color=MLOrange, alpha=0.15)

# Annotate the shaded region
ax.annotate('Heavy tail:\nroom for moderate\ndistances',
            xy=(2.8, 0.10), fontsize=12, color=MLOrange,
            ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor=MLOrange, alpha=0.9))

ax.set_xlabel(r'Distance $\|y_i - y_j\|$')
ax.set_ylabel('Similarity Weight')
ax.set_title('Gaussian vs Student-t: The Heavy-Tail Advantage')
ax.set_xlim(0, 6)
ax.set_ylim(0, 1.05)
ax.legend(loc='upper right', fontsize=13)
ax.grid(True, alpha=0.3)

fig.text(0.99, 0.01, CHART_METADATA["url"],
         ha='right', va='bottom', fontsize=7, color='gray', alpha=0.6)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
