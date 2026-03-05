"""Grouped bar chart: Gini impurity before and after a split."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False,
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

labels = [
    "Parent\n100 applicants\n60 repay, 40 default",
    "Left Child\n40 applicants\n(70/30)",
    "Right Child\n60 applicants\n(90/10)",
    "Weighted\nAverage",
]
values = [0.48, 0.42, 0.18, 0.276]
colors = [MLPURPLE, MLBLUE, MLBLUE, MLGREEN]

fig, ax = plt.subplots()
x = np.arange(len(labels))
bars = ax.bar(x, values, width=0.55, color=colors, edgecolor='white', linewidth=1.2)

for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.012,
            f"G = {val:.3f}" if val != 0.276 else f"{val:.3f}",
            ha='center', va='bottom', fontsize=12, fontweight='bold')

# Arrow showing impurity reduction
ax.annotate(
    "Impurity Reduction = 0.204",
    xy=(3, 0.276), xytext=(0, 0.48),
    fontsize=12, fontweight='bold', color=MLRED,
    arrowprops=dict(arrowstyle='->', color=MLRED, lw=2),
    ha='center', va='bottom',
)

ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=11)
ax.set_ylabel("Gini Impurity")
ax.set_title("Gini Impurity: Before vs After Split")
ax.set_ylim(0, 0.58)

plt.tight_layout()
fig.savefig(Path(__file__).parent / "chart.pdf", bbox_inches='tight')
plt.close(fig)
print("08_gini_split/chart.pdf created")
