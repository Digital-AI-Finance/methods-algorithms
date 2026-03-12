"""
Chart: Epsilon Decay Strategies for Exploration
Shows linear, exponential, and step decay of epsilon over 1000 episodes
with exploration/exploitation shaded regions.
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------
CHART_METADATA = {
    "title": "Epsilon Decay Strategies for Exploration",
    "description": (
        "Three epsilon-greedy decay schedules (linear, exponential, step) "
        "plotted over 1000 training episodes with exploration/exploitation phases highlighted."
    ),
    "url": "https://digital-ai-finance.github.io/methods-algorithms/slides/L06_Embeddings_RL/12_epsilon_decay",
}

# ---------------------------------------------------------------------------
# Style
# ---------------------------------------------------------------------------
plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False
})

MLPURPLE = '#3333B2'
MLBLUE   = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN  = '#2CA02C'
MLRED    = '#D62728'

# ---------------------------------------------------------------------------
# Decay curves
# ---------------------------------------------------------------------------
T       = 1000
eps_min = 0.01
eps_start = 1.0
t = np.arange(0, T + 1)

# Linear decay
linear = np.maximum(eps_min, eps_start - t / T)

# Exponential decay
exponential = np.maximum(eps_min, eps_start * (0.995 ** t))

# Step decay: start at 1.0, drop at 200, 500, 800
step = np.ones(T + 1) * eps_start
step[200:] = 0.5
step[500:] = 0.2
step[800:] = eps_min
step = np.maximum(step, eps_min)

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, ax = plt.subplots()

# Shaded phases
ax.axvspan(0,   500, alpha=0.08, color=MLBLUE,  label='_nolegend_')
ax.axvspan(500, T,   alpha=0.08, color=MLGREEN, label='_nolegend_')

# Phase labels
ax.text(125, 0.92, 'Exploration Phase', fontsize=12, color=MLBLUE,
        ha='center', va='center', alpha=0.75)
ax.text(750, 0.92, 'Exploitation Phase', fontsize=12, color=MLGREEN,
        ha='center', va='center', alpha=0.75)

# Epsilon minimum floor line
ax.axhline(eps_min, color='#888888', linewidth=1.2, linestyle='--', zorder=1)
ax.text(T + 5, eps_min + 0.01, r'$\varepsilon_{\min} = 0.01$',
        fontsize=11, color='#666666', va='bottom')

# Decay curves
ax.plot(t, linear,      color=MLBLUE,   linewidth=2.5, label='Linear decay',      zorder=3)
ax.plot(t, exponential, color=MLORANGE, linewidth=2.5, label='Exponential decay', zorder=3)
ax.plot(t, step,        color=MLPURPLE, linewidth=2.5, label='Step decay',        zorder=3)

# ---------------------------------------------------------------------------
# Axes, legend, labels
# ---------------------------------------------------------------------------
ax.set_xlim(0, T)
ax.set_ylim(-0.02, 1.05)
ax.set_xlabel('Episode')
ax.set_ylabel('Epsilon (ε)')
ax.set_title('Epsilon Decay Strategies for Exploration')
ax.legend(loc='upper right', framealpha=0.85)
ax.grid(alpha=0.3)

# URL watermark
ax.text(0.99, 0.01, CHART_METADATA["url"],
        transform=ax.transAxes, fontsize=7, color='#AAAAAA',
        ha='right', va='bottom')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
