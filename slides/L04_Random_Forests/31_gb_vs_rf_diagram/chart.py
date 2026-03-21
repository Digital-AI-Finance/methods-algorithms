import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    'title': 'Random Forest vs Gradient Boosting',
    'description': 'Conceptual diagram comparing parallel tree building (RF) with sequential residual fitting (GBM)',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/31_gb_vs_rf_diagram'
}

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')
ax.grid(False)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# ---- Helper ----
def draw_box(ax, cx, cy, w, h, label, facecolor, fontsize=11, textcolor='white'):
    x0, y0 = cx - w / 2, cy - h / 2
    patch = FancyBboxPatch((x0, y0), w, h,
                           boxstyle='round,pad=0.15',
                           facecolor=facecolor, edgecolor='white',
                           linewidth=1.5, zorder=3)
    ax.add_patch(patch)
    ax.text(cx, cy, label, ha='center', va='center',
            fontsize=fontsize, color=textcolor, fontweight='bold', zorder=4)

def draw_arrow(ax, x1, y1, x2, y2, color):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=2.0),
                zorder=2)

# ============================================================
# LEFT: Random Forest (MLBLUE)
# ============================================================
rf_color = MLBLUE
rf_light = '#CCE0FF'
rf_cx = 2.5

# Title label
ax.text(rf_cx, 9.5, 'Random Forest', ha='center', va='center',
        fontsize=14, color=rf_color, fontweight='bold')

# Training Data
draw_box(ax, rf_cx, 8.5, 3.0, 0.7, 'Training Data', rf_color, fontsize=11)

# Three tree boxes (parallel)
tree_xs = [1.2, 2.5, 3.8]
tree_y = 6.8
for tx in tree_xs:
    draw_box(ax, tx, tree_y, 0.9, 0.65, 'Tree', rf_light, fontsize=10, textcolor=rf_color)
    draw_arrow(ax, rf_cx, 8.15, tx, tree_y + 0.33, rf_color)

# Average / Vote box
draw_box(ax, rf_cx, 5.3, 2.8, 0.7, 'Average / Vote', rf_color, fontsize=11)
for tx in tree_xs:
    draw_arrow(ax, tx, tree_y - 0.33, rf_cx, 5.65, rf_color)

# Prediction
draw_box(ax, rf_cx, 4.0, 2.2, 0.65, 'Prediction', '#1a53a0', fontsize=11)
draw_arrow(ax, rf_cx, 4.95, rf_cx, 4.33, rf_color)

# "Parallel" label
ax.text(rf_cx, 3.1, '[ Independent / Parallel ]', ha='center',
        fontsize=10, color=rf_color, style='italic')

# ============================================================
# RIGHT: Gradient Boosting (MLORANGE)
# ============================================================
gb_color = MLORANGE
gb_light = '#FFE0B0'
gb_cx = 7.5

ax.text(gb_cx, 9.5, 'Gradient Boosting', ha='center', va='center',
        fontsize=14, color=gb_color, fontweight='bold')

# Training Data
draw_box(ax, gb_cx, 8.5, 3.0, 0.7, 'Training Data', gb_color,
         fontsize=11, textcolor='white')

# Sequential chain: Tree1 -> Residuals -> Tree2 -> Residuals -> Tree3
chain_y_start = 7.4
step = 0.9
items = ['Tree 1', 'Residuals', 'Tree 2', 'Residuals', 'Tree 3']
item_colors = [gb_light, '#FFEEDD', gb_light, '#FFEEDD', gb_light]
item_tcolor = [gb_color, '#AA5500', gb_color, '#AA5500', gb_color]
chain_ys = [chain_y_start - i * step for i in range(len(items))]

draw_arrow(ax, gb_cx, 8.15, gb_cx, chain_ys[0] + 0.33, gb_color)

for i, (label, cy, fc, tc) in enumerate(zip(items, chain_ys, item_colors, item_tcolor)):
    draw_box(ax, gb_cx, cy, 2.2, 0.6, label, fc, fontsize=10, textcolor=tc)
    if i < len(items) - 1:
        draw_arrow(ax, gb_cx, cy - 0.30, gb_cx, chain_ys[i + 1] + 0.30, gb_color)

# Scaled Sum
sum_y = chain_ys[-1] - 0.85
draw_box(ax, gb_cx, sum_y, 2.4, 0.65, 'Scaled Sum', gb_color,
         fontsize=11, textcolor='white')
draw_arrow(ax, gb_cx, chain_ys[-1] - 0.30, gb_cx, sum_y + 0.33, gb_color)

# Prediction
pred_y = sum_y - 0.95
draw_box(ax, gb_cx, pred_y, 2.2, 0.65, 'Prediction', '#CC5500',
         fontsize=11, textcolor='white')
draw_arrow(ax, gb_cx, sum_y - 0.33, gb_cx, pred_y + 0.33, gb_color)

# "Sequential" label
ax.text(gb_cx, pred_y - 0.6, '[ Sequential / Boosting ]', ha='center',
        fontsize=10, color=gb_color, style='italic')

# ============================================================
# Dividing line
# ============================================================
ax.axvline(5.0, color='#CCCCCC', linewidth=1.5, linestyle='--', zorder=1)

# Title
ax.set_title('Random Forest vs Gradient Boosting', fontsize=16, fontweight='bold', pad=4)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
