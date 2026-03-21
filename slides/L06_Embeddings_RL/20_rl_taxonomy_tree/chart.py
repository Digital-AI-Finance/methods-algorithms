import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Nodes covered in course get MLORANGE highlight
COURSE_NODES = {'Q-Learning', 'DQN', 'PPO'}

def draw_node(ax, x, y, label, w=1.3, h=0.38, highlight=False):
    fc = MLORANGE if highlight else MLLAVENDER
    ec = MLRED if highlight else MLPURPLE
    lw = 2.2 if highlight else 1.5
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                         boxstyle="round,pad=0.05",
                         edgecolor=ec, facecolor=fc, linewidth=lw, zorder=3)
    ax.add_patch(box)
    fw = 'bold' if highlight else 'normal'
    fs = 9.5 if highlight else 9
    ax.text(x, y, label, ha='center', va='center', fontsize=fs,
            fontweight=fw, zorder=4)

def draw_arrow(ax, x0, y0, x1, y1):
    arr = FancyArrowPatch((x0, y0), (x1, y1), arrowstyle='-|>',
                          mutation_scale=12, linewidth=1.4,
                          color='#555555', zorder=2)
    ax.add_patch(arr)

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')
ax.grid(False)

# ── Layer 0: root ──────────────────────────────────────────────────────────
draw_node(ax, 5.0, 5.5, 'RL Methods', w=1.6, h=0.42)

# ── Layer 1: Model-Free / Model-Based ──────────────────────────────────────
draw_node(ax, 3.0, 4.5, 'Model-Free',  w=1.5, h=0.38)
draw_node(ax, 7.8, 4.5, 'Model-Based', w=1.5, h=0.38)

draw_arrow(ax, 4.2, 5.28, 3.0, 4.69)
draw_arrow(ax, 5.8, 5.28, 7.8, 4.69)

# ── Layer 2 (Model-Free): Value-Based / Policy-Based / Actor-Critic ────────
mf_l2 = [(1.2, 3.5, 'Value-Based'), (3.0, 3.5, 'Policy-Based'), (4.8, 3.5, 'Actor-Critic')]
for x2, y2, lbl in mf_l2:
    draw_node(ax, x2, y2, lbl, w=1.4, h=0.38)
    draw_arrow(ax, 3.0, 4.31, x2, 3.69)

# ── Layer 2 (Model-Based): Dyna / MBPO / MuZero ───────────────────────────
mb_l2 = [(6.9, 3.5, 'Dyna'), (7.8, 3.5, 'MBPO'), (8.7, 3.5, 'MuZero')]
for x2, y2, lbl in mb_l2:
    draw_node(ax, x2, y2, lbl, w=1.15, h=0.38, highlight=(lbl in COURSE_NODES))
    draw_arrow(ax, 7.8, 4.31, x2, 3.69)

# ── Layer 3: leaf nodes ────────────────────────────────────────────────────
vb_leaves = [(0.5, 2.4, 'Q-Learning'), (1.2, 2.4, 'DQN'), (1.9, 2.4, 'Double DQN')]
pb_leaves = [(2.3, 2.4, 'REINFORCE'), (3.0, 2.4, 'PPO'), (3.7, 2.4, 'TRPO')]
ac_leaves = [(4.1, 2.4, 'A2C'), (4.8, 2.4, 'A3C'), (5.5, 2.4, 'SAC')]

for grp, parent_x, parent_y in [
    (vb_leaves, 1.2, 3.31),
    (pb_leaves, 3.0, 3.31),
    (ac_leaves, 4.8, 3.31),
]:
    for x3, y3, lbl in grp:
        draw_node(ax, x3, y3, lbl, w=0.95, h=0.36, highlight=(lbl in COURSE_NODES))
        draw_arrow(ax, parent_x, parent_y, x3, 2.58)

# ── Legend ─────────────────────────────────────────────────────────────────
for xleg, yleg, fc, ec, lbl in [
    (0.5, 1.4, MLORANGE, MLRED, 'Covered in this course'),
    (0.5, 1.0, MLLAVENDER, MLPURPLE, 'Other methods'),
]:
    leg_box = FancyBboxPatch((xleg, yleg - 0.18), 0.5, 0.36,
                             boxstyle="round,pad=0.04",
                             edgecolor=ec, facecolor=fc, linewidth=1.5)
    ax.add_patch(leg_box)
    ax.text(xleg + 0.65, yleg, lbl, va='center', fontsize=9)

# ── Title ──────────────────────────────────────────────────────────────────
ax.text(5.0, 0.35, 'RL Method Taxonomy', ha='center', va='center',
        fontsize=15, fontweight='bold')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=150)
plt.close()
print("Saved: 20_rl_taxonomy_tree/chart.pdf")
