import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')
ax.grid(False)

# ── Zone background rectangles ─────────────────────────────────────────────
zones = [
    (0.15, 0.5, 3.0, 5.0, MLLAVENDER,  '#EEEEFF', 'Multi-Armed\nBandit'),
    (3.45, 0.5, 3.0, 5.0, '#88AACC',   '#D8EEFF', 'Contextual\nBandit'),
    (6.75, 0.5, 3.1, 5.0, '#55AA55',   '#D8F0D8', 'Full MDP'),
]
for x0, y0, w, h, ec, fc, _ in zones:
    bg = FancyBboxPatch((x0, y0), w, h,
                        boxstyle="round,pad=0.1",
                        edgecolor=ec, facecolor=fc, linewidth=2, zorder=1)
    ax.add_patch(bg)

# ── Zone titles ────────────────────────────────────────────────────────────
ax.text(1.65, 5.25, 'Multi-Armed Bandit',
        ha='center', va='center', fontsize=11, fontweight='bold', color=MLPURPLE)
ax.text(4.95, 5.25, 'Contextual Bandit',
        ha='center', va='center', fontsize=11, fontweight='bold', color=MLBLUE)
ax.text(8.30, 5.25, 'Full MDP',
        ha='center', va='center', fontsize=11, fontweight='bold', color=MLGREEN)

# ── helpers ────────────────────────────────────────────────────────────────
def node(ax, cx, cy, r, label, ec, fc, fs=9.5):
    circ = Circle((cx, cy), r, edgecolor=ec, facecolor=fc, linewidth=2, zorder=3)
    ax.add_patch(circ)
    ax.text(cx, cy, label, ha='center', va='center',
            fontsize=fs, fontweight='bold', zorder=4)

def farrow(ax, x0, y0, x1, y1, color, lw=1.8, style='-|>'):
    arr = FancyArrowPatch((x0, y0), (x1, y1),
                          arrowstyle=style, mutation_scale=12,
                          linewidth=lw, color=color, zorder=2)
    ax.add_patch(arr)

# ── Zone 1: Multi-Armed Bandit ─────────────────────────────────────────────
node(ax, 1.65, 3.5, 0.42, 'State', MLPURPLE, MLLAVENDER, fs=9)

# Three arms fanning out
arm_angles = [135, 90, 45]
arm_labels = ['R₁', 'R₂', 'R₃']
arm_colors = [MLRED, MLORANGE, MLGREEN]
for angle, rlbl, color in zip(arm_angles, arm_labels, arm_colors):
    rad = np.radians(angle)
    ex = 1.65 + 1.05 * np.cos(rad)
    ey = 3.5  + 1.05 * np.sin(rad)
    farrow(ax, 1.65 + 0.42*np.cos(rad), 3.5 + 0.42*np.sin(rad),
           ex, ey, color=color, lw=2.0)
    ax.text(ex, ey, rlbl, ha='center', va='center',
            fontsize=10, fontweight='bold', color=color,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                      edgecolor=color, linewidth=1.5))

ax.text(1.65, 1.2, '1 state,  k arms', ha='center', va='center',
        fontsize=9, color=MLPURPLE, fontstyle='italic')

# ── Zone 2: Contextual Bandit ─────────────────────────────────────────────
s_xs = [4.3, 4.95, 5.6]
s_ys = [3.9, 3.2, 3.75]
for i, (sx, sy) in enumerate(zip(s_xs, s_ys)):
    node(ax, sx, sy, 0.30, f's{i+1}', '#88AACC', '#D0E8FF', fs=8.5)
    # Arrow to action and reward
    ax.annotate('', xy=(sx + 0.45, sy - 0.0),
                xytext=(sx + 0.30, sy),
                arrowprops=dict(arrowstyle='->', color=MLBLUE, lw=1.5))
    ax.text(sx + 0.65, sy, f'r{i+1}', ha='center', va='center',
            fontsize=9, color=MLBLUE, fontweight='bold')

ax.text(4.95, 1.2, 'Multiple states,\nno transitions',
        ha='center', va='center', fontsize=9, color=MLBLUE, fontstyle='italic')

# ── Zone 3: Full MDP ───────────────────────────────────────────────────────
# s → action → s' → reward loop
mx_s,  my_s  = 7.55, 3.9
mx_sp, my_sp = 9.05, 3.9
mx_r,  my_r  = 8.30, 2.6

node(ax, mx_s,  my_s,  0.38, 's',   '#55AA55', '#CCF0CC', fs=10)
node(ax, mx_sp, my_sp, 0.38, "s'",  '#55AA55', '#CCF0CC', fs=10)
node(ax, mx_r,  my_r,  0.32, 'r',   MLRED,     '#FFCCCC', fs=10)

# s --(a)--> s'
farrow(ax, mx_s + 0.38, my_s, mx_sp - 0.38, my_sp, color=MLGREEN, lw=2.0)
ax.text(8.30, my_s + 0.28, 'action a', ha='center', va='bottom',
        fontsize=8.5, color=MLGREEN)

# s' --> r
farrow(ax, mx_sp - 0.15, my_sp - 0.35, mx_r + 0.25, my_r + 0.2,
       color=MLRED, lw=1.8)

# r --> s (loop back)
farrow(ax, mx_r - 0.25, my_r + 0.2, mx_s + 0.1, my_s - 0.35,
       color='#777777', lw=1.8)
ax.text(7.6, 2.6, 'transition', ha='center', va='center',
        fontsize=8, color='#555555', fontstyle='italic')

ax.text(8.30, 1.2, 'States + transitions',
        ha='center', va='center', fontsize=9, color=MLGREEN, fontstyle='italic')

# ── Large arrows between zones ─────────────────────────────────────────────
farrow(ax, 3.15, 3.1, 3.45, 3.1, color='#444444', lw=3.0, style='-|>')
ax.text(3.3, 3.45, 'Add\nstates', ha='center', va='bottom',
        fontsize=8.5, fontweight='bold', color='#333333')

farrow(ax, 6.45, 3.1, 6.75, 3.1, color='#444444', lw=3.0, style='-|>')
ax.text(6.6, 3.45, 'Add\ntransitions', ha='center', va='bottom',
        fontsize=8.5, fontweight='bold', color='#333333')

# ── Title ──────────────────────────────────────────────────────────────────
ax.text(5.0, 5.75, 'From Bandits to MDPs: Increasing Complexity',
        ha='center', va='center', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=150)
plt.close()
print("Saved: 24_bandit_to_mdp_progression/chart.pdf")
