import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')
ax.grid(False)

def box(ax, cx, cy, w, h, label, sub='', ec=MLPURPLE, fc=MLLAVENDER,
        lw=2, fs=11, sub_fs=8.5):
    patch = FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                           boxstyle="round,pad=0.07",
                           edgecolor=ec, facecolor=fc, linewidth=lw, zorder=3)
    ax.add_patch(patch)
    ty = cy if not sub else cy + h * 0.15
    ax.text(cx, ty, label, ha='center', va='center',
            fontsize=fs, fontweight='bold', zorder=4)
    if sub:
        ax.text(cx, cy - h * 0.2, sub, ha='center', va='center',
                fontsize=sub_fs, color='#444444', zorder=4)

def arrow(ax, x0, y0, x1, y1, color='#555555', lw=2.0,
          style='-|>', ls='solid'):
    arr = FancyArrowPatch((x0, y0), (x1, y1),
                          arrowstyle=style, mutation_scale=14,
                          linewidth=lw, color=color,
                          linestyle=ls, zorder=2)
    ax.add_patch(arr)

# ── State input (top center) ───────────────────────────────────────────────
box(ax, 5.0, 5.2, 2.2, 0.6,
    'State  s',
    sub='[prices, RSI, position]',
    ec=MLPURPLE, fc=MLLAVENDER, fs=11, sub_fs=8.5)

# ── Actor branch (left) ───────────────────────────────────────────────────
box(ax, 2.8, 3.8, 1.6, 0.55, 'Actor',
    ec=MLBLUE, fc='#D0E8FF', fs=11)
box(ax, 2.8, 2.9, 1.6, 0.52, 'Policy  π(a|s)',
    ec=MLBLUE, fc='white', fs=10)
box(ax, 2.8, 1.9, 1.4, 0.48, 'Action',
    ec=MLGREEN, fc='#CCEECC', fs=10)

arrow(ax, 3.9, 4.9, 2.8, 4.08, color=MLPURPLE)   # State → Actor
arrow(ax, 2.8, 3.52, 2.8, 3.16, color=MLBLUE)    # Actor → Policy
arrow(ax, 2.8, 2.64, 2.8, 2.14, color=MLBLUE)    # Policy → Action

# ── Critic branch (right) ─────────────────────────────────────────────────
box(ax, 7.2, 3.8, 1.6, 0.55, 'Critic',
    ec=MLORANGE, fc='#FFE8CC', fs=11)
box(ax, 7.2, 2.9, 1.6, 0.52, 'Value  V(s)',
    ec=MLORANGE, fc='white', fs=10)
box(ax, 7.2, 1.9, 1.8, 0.48, 'Advantage  A = Q−V',
    ec=MLRED, fc='#FFD8D8', fs=9)

arrow(ax, 6.1, 4.9, 7.2, 4.08, color=MLPURPLE)   # State → Critic
arrow(ax, 7.2, 3.52, 7.2, 3.16, color=MLORANGE)   # Critic → V(s)
arrow(ax, 7.2, 2.64, 7.2, 2.14, color=MLORANGE)   # V(s) → Advantage

# ── Feedback: Advantage → Actor (curved, dashed) ──────────────────────────
# Go left from Advantage box bottom to Actor box right side
arrow(ax, 6.3, 1.9, 4.0, 2.9,
      color=MLRED, lw=2.2, ls='dashed')
ax.text(5.15, 2.55, 'policy gradient\nfeedback',
        ha='center', va='center', fontsize=8.5,
        color=MLRED, style='italic')

# ── Environment box (bottom center) ───────────────────────────────────────
box(ax, 5.0, 0.85, 2.4, 0.56, 'Environment',
    ec='#555555', fc='#EEEEEE', fs=10)

# Action → Environment
arrow(ax, 2.8, 1.66, 4.0, 1.0, color=MLGREEN, lw=2.0)
# Environment → reward annotation
ax.text(5.0, 0.28, 'reward  r,  next state  s′',
        ha='center', va='center', fontsize=9, color='#333333')
# Feedback arrows from Environment back up
arrow(ax, 6.0, 1.0, 7.2, 1.66, color='#777777', lw=1.8, ls='dashed')
ax.text(6.65, 1.4, 's′, r', ha='center', va='center',
        fontsize=8.5, color='#555555')

# ── Title ──────────────────────────────────────────────────────────────────
ax.text(5.0, 5.75, 'Actor-Critic Architecture for Trading',
        ha='center', va='center', fontsize=15, fontweight='bold')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=150)
plt.close()
print("Saved: 22_actor_critic_architecture/chart.pdf")
