import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')
ax.grid(False)

# ── Background zones ───────────────────────────────────────────────────────
online_bg = FancyBboxPatch((0.2, 0.8), 4.3, 4.8,
                           boxstyle="round,pad=0.1",
                           edgecolor=MLBLUE, facecolor='#D8EEFF',
                           linewidth=2.0, zorder=1)
ax.add_patch(online_bg)

offline_bg = FancyBboxPatch((5.5, 0.8), 4.3, 4.8,
                            boxstyle="round,pad=0.1",
                            edgecolor=MLORANGE, facecolor='#FFF0D8',
                            linewidth=2.0, zorder=1)
ax.add_patch(offline_bg)

# ── Zone headers ───────────────────────────────────────────────────────────
ax.text(2.35, 5.35, 'Online RL', ha='center', va='center',
        fontsize=14, fontweight='bold', color=MLBLUE)
ax.text(7.65, 5.35, 'Offline RL', ha='center', va='center',
        fontsize=14, fontweight='bold', color=MLORANGE)

# ── Online RL: Agent ↔ Environment circles ─────────────────────────────────
def draw_circle_node(ax, cx, cy, r, label, ec, fc):
    circ = Circle((cx, cy), r, edgecolor=ec, facecolor=fc, linewidth=2, zorder=3)
    ax.add_patch(circ)
    ax.text(cx, cy, label, ha='center', va='center',
            fontsize=11, fontweight='bold', zorder=4)

draw_circle_node(ax, 1.4, 3.1, 0.55, 'Agent',       MLBLUE,   '#AACFEE')
draw_circle_node(ax, 3.3, 3.1, 0.55, 'Env',         '#555555', '#DDDDDD')

# Bidirectional arrows
arr_fwd = FancyArrowPatch((1.95, 3.3), (2.75, 3.3),
                          arrowstyle='-|>', mutation_scale=14,
                          linewidth=2.0, color=MLBLUE, zorder=2)
ax.add_patch(arr_fwd)
arr_bwd = FancyArrowPatch((2.75, 2.9), (1.95, 2.9),
                          arrowstyle='-|>', mutation_scale=14,
                          linewidth=2.0, color='#555555', zorder=2)
ax.add_patch(arr_bwd)
ax.text(2.35, 3.5, 'action', ha='center', va='bottom', fontsize=8.5, color=MLBLUE)
ax.text(2.35, 2.65, 'reward, s′', ha='center', va='top', fontsize=8.5, color='#555555')

# Online labels
ax.text(2.35, 1.95, 'Live interaction', ha='center', va='center',
        fontsize=10, color=MLBLUE, fontweight='bold')
ax.text(2.35, 1.55, 'Explore freely', ha='center', va='center',
        fontsize=9.5, color='#335588')

# ── Offline RL: Dataset → Agent (one-way) ─────────────────────────────────
# Dataset "drum" icon using two rounded rectangles
db_box = FancyBboxPatch((5.9, 2.6), 1.2, 0.9,
                        boxstyle="round,pad=0.08",
                        edgecolor=MLORANGE, facecolor='#FFE0A0',
                        linewidth=2, zorder=3)
ax.add_patch(db_box)
ax.text(6.5, 3.07, 'Dataset', ha='center', va='center',
        fontsize=10, fontweight='bold', zorder=4)
ax.text(6.5, 2.77, '(fixed)', ha='center', va='center',
        fontsize=8.5, color='#666666', zorder=4)

draw_circle_node(ax, 8.6, 3.05, 0.55, 'Agent', MLORANGE, '#FFD8AA')

arr_off = FancyArrowPatch((7.1, 3.05), (8.05, 3.05),
                          arrowstyle='-|>', mutation_scale=14,
                          linewidth=2.5, color=MLORANGE, zorder=2)
ax.add_patch(arr_off)
ax.text(7.57, 3.3, 'learn from\nbatch', ha='center', va='bottom',
        fontsize=8.5, color=MLORANGE)

# No-exploration cross mark
ax.plot([7.2, 7.95], [2.5, 2.5], color=MLRED, linewidth=2.5, zorder=3)
ax.text(7.57, 2.3, 'No new interactions', ha='center', va='top',
        fontsize=8.5, color=MLRED)

# Offline labels
ax.text(7.25, 1.95, 'Fixed dataset', ha='center', va='center',
        fontsize=10, color=MLORANGE, fontweight='bold')
ax.text(7.25, 1.55, 'No exploration', ha='center', va='center',
        fontsize=9.5, color='#885533')

# ── Center "vs" divider ────────────────────────────────────────────────────
ax.plot([4.9, 4.9], [0.9, 5.5], color='#888888',
        linewidth=1.8, linestyle='--', zorder=2)
ax.text(4.9, 3.1, 'vs', ha='center', va='center',
        fontsize=15, fontweight='bold', color='#555555',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#888888'))

# ── Bottom annotation ──────────────────────────────────────────────────────
ax.text(5.0, 0.4,
        'Finance: Live trading data is expensive and risky  →  Offline RL preferred for initial training',
        ha='center', va='center', fontsize=9.5, color='#333333',
        style='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFFFDD', edgecolor='#CCCC88'))

# ── Title ──────────────────────────────────────────────────────────────────
ax.text(5.0, 5.75, 'Online vs Offline Reinforcement Learning',
        ha='center', va='center', fontsize=15, fontweight='bold')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=150)
plt.close()
print("Saved: 23_offline_vs_online_rl/chart.pdf")
