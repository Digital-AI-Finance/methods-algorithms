"""Scatter plot showing XOR-like pattern with linear vs DT boundaries."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()


rng = np.random.RandomState(42)
n = 50
std = 0.6

# Class 0: clusters at (1,1) and (4,4)
c0a = rng.randn(n, 2) * std + np.array([1, 1])
c0b = rng.randn(n, 2) * std + np.array([4, 4])
# Class 1: clusters at (1,4) and (4,1)
c1a = rng.randn(n, 2) * std + np.array([1, 4])
c1b = rng.randn(n, 2) * std + np.array([4, 1])

X0 = np.vstack([c0a, c0b])
X1 = np.vstack([c1a, c1b])

fig, ax = plt.subplots()
ax.scatter(X0[:, 0], X0[:, 1], c=MLBLUE, edgecolors='white', linewidth=0.5,
           s=40, label='Class 0 (Repay)', zorder=3)
ax.scatter(X1[:, 0], X1[:, 1], c=MLORANGE, edgecolors='white', linewidth=0.5,
           s=40, label='Class 1 (Default)', zorder=3)

# Diagonal line (linear boundary fails)
ax.plot([0, 5], [0, 5], '--', color='gray', linewidth=2, alpha=0.7,
        label='Linear boundary fails')

# Axis-aligned DT splits
ax.axvline(2.5, color=MLGREEN, linestyle=':', linewidth=2, alpha=0.8,
           label='DT splits here')
ax.axhline(2.5, color=MLGREEN, linestyle=':', linewidth=2, alpha=0.8)

ax.set_xlabel("Income (normalized)")
ax.set_ylabel("Credit Score (normalized)")
ax.set_title("Non-Linearly Separable Classes")
ax.legend(loc='center right', fontsize=11)
ax.set_xlim(-1, 6)
ax.set_ylim(-1, 6)

plt.tight_layout()
fig.savefig(Path(__file__).parent / "chart.pdf", bbox_inches='tight', facecolor='white')
plt.close(fig)
print("12_nonlinear_classes/chart.pdf created")
