"""Line chart comparing Gini impurity and scaled Entropy curves."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()


p = np.linspace(0.001, 0.999, 500)
gini = 2 * p * (1 - p)
entropy = (-p * np.log2(p) - (1 - p) * np.log2(1 - p)) * 0.5

fig, ax = plt.subplots()
ax.plot(p, gini, color=MLPURPLE, linewidth=2.5, label='Gini = 2p(1-p)')
ax.plot(p, entropy, color=MLORANGE, linewidth=2.5, linestyle='--',
        label='Entropy (scaled) = 0.5 H(p)')

# Peak annotation
ax.annotate("Both peak at p = 0.5", xy=(0.5, 0.5), xytext=(0.7, 0.45),
            fontsize=12, fontweight='bold', color=MLRED,
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=1.5),
            ha='center')

ax.text(0.15, 0.12, "Nearly identical\nranking of splits",
        fontsize=11, fontstyle='italic', color='gray',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.8))

ax.set_xlabel("Class Probability p")
ax.set_ylabel("Impurity Measure")
ax.set_title("Gini Impurity vs Scaled Entropy")
ax.legend(loc='upper right')
ax.set_xlim(0, 1)
ax.set_ylim(0, 0.55)

plt.tight_layout()
fig.savefig(Path(__file__).parent / "chart.pdf", bbox_inches='tight', facecolor='white')
plt.close(fig)
print("11_gini_vs_entropy/chart.pdf created")
