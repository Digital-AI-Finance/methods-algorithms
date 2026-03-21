"""The Polysemy Problem: Why Static Embeddings Fail -- single scatter plot."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()


# Finance cluster
finance_words = {
    'money': (2.1, 3.2), 'loan': (2.5, 2.8), 'stock': (1.8, 3.5),
    'investment': (2.3, 3.8), 'portfolio': (2.7, 3.5), 'deposit': (2.0, 2.5),
}

# Nature cluster
nature_words = {
    'river': (7.2, 3.0), 'water': (7.5, 3.4), 'fish': (7.8, 2.7),
    'tree': (7.0, 3.6), 'lake': (7.3, 2.3), 'stream': (7.6, 3.8),
}

fig, ax = plt.subplots(figsize=(10, 6))

# Plot finance cluster
fx = [v[0] for v in finance_words.values()]
fy = [v[1] for v in finance_words.values()]
ax.scatter(fx, fy, c=MLBLUE, s=80, zorder=3, alpha=0.85)
for word, (x, y) in finance_words.items():
    ax.annotate(word, (x, y), textcoords='offset points', xytext=(0, 10),
                ha='center', fontsize=10, color=MLBLUE)

# Plot nature cluster
nx = [v[0] for v in nature_words.values()]
ny = [v[1] for v in nature_words.values()]
ax.scatter(nx, ny, c=MLGREEN, s=80, zorder=3, alpha=0.85)
for word, (x, y) in nature_words.items():
    ax.annotate(word, (x, y), textcoords='offset points', xytext=(0, 10),
                ha='center', fontsize=10, color=MLGREEN)

# "bank" as large star at midpoint
ax.scatter(4.8, 3.1, c=MLORANGE, s=300, marker='*', zorder=5, edgecolors='black', linewidths=0.5)
ax.annotate('bank', (4.8, 3.1), textcoords='offset points', xytext=(0, 14),
            ha='center', fontsize=12, fontweight='bold', color=MLORANGE)

# Dashed arrows from "bank" to contextual positions (labels at midpoints)
arrow_style = dict(arrowstyle='->', lw=1.8, linestyle='dashed')
ax.annotate('', xy=(2.4, 3.0), xytext=(4.8, 3.1),
            arrowprops=dict(**arrow_style, color=MLBLUE))
ax.text(3.6, 3.45, 'bank (money)', fontsize=9, fontweight='bold',
        color=MLBLUE, ha='center', va='bottom',
        bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none', alpha=0.8))
ax.annotate('', xy=(7.1, 2.8), xytext=(4.8, 3.1),
            arrowprops=dict(**arrow_style, color=MLGREEN))
ax.text(5.95, 2.6, 'bank (river)', fontsize=9, fontweight='bold',
        color=MLGREEN, ha='center', va='top',
        bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none', alpha=0.8))

# Light dashed ellipses around clusters
from matplotlib.patches import Ellipse
ell_finance = Ellipse((2.3, 3.15), 1.8, 2.0, fill=False,
                       edgecolor=MLBLUE, linestyle='--', linewidth=1.2, alpha=0.5)
ell_nature = Ellipse((7.4, 3.1), 1.8, 2.2, fill=False,
                      edgecolor=MLGREEN, linestyle='--', linewidth=1.2, alpha=0.5)
ax.add_patch(ell_finance)
ax.add_patch(ell_nature)

# Cluster labels
ax.text(2.3, 1.7, 'Finance', ha='center', fontsize=11, fontweight='bold',
        color=MLBLUE, alpha=0.7)
ax.text(7.4, 1.5, 'Nature', ha='center', fontsize=11, fontweight='bold',
        color=MLGREEN, alpha=0.7)

# Title
ax.set_title('The Polysemy Problem: Why Static Embeddings Fail',
             fontsize=16, fontweight='bold', pad=14)

# Subtitle annotation
ax.text(5.0, 0.7, 'Static: 1 vector for "bank".  Contextual (BERT): different vectors based on meaning.',
        ha='center', fontsize=11, color='#555555', style='italic')

# Clean up axes
ax.set_xlim(0.5, 9.0)
ax.set_ylim(0.3, 4.8)
ax.set_xticks([])
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.tight_layout()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chart.pdf')
plt.savefig(out, bbox_inches='tight', pad_inches=0.1, facecolor='white')
plt.close()
print(f'Saved: {out}')
