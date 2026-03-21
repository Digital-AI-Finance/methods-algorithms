import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle, FancyArrowPatch

ROWS = 4
COLS = 12
CELL = 0.75   # cell size in data units

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-0.2, COLS * CELL + 0.4)
ax.set_ylim(-0.5, ROWS * CELL + 0.7)
ax.axis('off')
ax.grid(False)

# ── Draw grid cells ────────────────────────────────────────────────────────
for r in range(ROWS):
    for c in range(COLS):
        x = c * CELL
        y = r * CELL

        # Determine fill color
        if r == 0 and c == 0:
            fc = '#90EE90'   # start: light green
            ec = MLGREEN
            lw = 2.5
        elif r == 0 and c == COLS - 1:
            fc = '#90EE90'   # goal: light green
            ec = MLGREEN
            lw = 2.5
        elif r == 0 and 1 <= c <= COLS - 2:
            fc = '#FFAAAA'   # cliff cells: light red
            ec = MLRED
            lw = 1.5
        else:
            fc = '#F5F5F5'
            ec = '#AAAAAA'
            lw = 0.8

        rect = Rectangle((x, y), CELL, CELL,
                          facecolor=fc, edgecolor=ec, linewidth=lw, zorder=1)
        ax.add_patch(rect)

# ── Labels in special cells ────────────────────────────────────────────────
ax.text(0.5 * CELL, 0.5 * CELL, 'S', ha='center', va='center',
        fontsize=13, fontweight='bold', color=MLGREEN, zorder=3)
ax.text((COLS - 0.5) * CELL, 0.5 * CELL, 'G', ha='center', va='center',
        fontsize=13, fontweight='bold', color=MLGREEN, zorder=3)
ax.text(5.5 * CELL, 0.5 * CELL, 'CLIFF  −100', ha='center', va='center',
        fontsize=9, fontweight='bold', color=MLRED, zorder=3)

# ── Q-Learning path: hug the cliff (row 0, from col 0 → col 11) ───────────
# Walk right along bottom row; drawn as polyline
ql_xs = [(c + 0.5) * CELL for c in range(COLS)]
ql_ys = [0.5 * CELL] * COLS
ax.plot(ql_xs, ql_ys, color=MLORANGE, linewidth=3.5, zorder=4,
        solid_capstyle='round', label='Q-Learning (optimal)')

# ── SARSA path: go up, across top, back down ──────────────────────────────
sarsa_xs = (
    [0.5 * CELL] * (ROWS - 1) +                              # up from row 0 to row 3
    [(c + 0.5) * CELL for c in range(COLS)] +                 # across top row
    [(COLS - 0.5) * CELL] * (ROWS - 1)                        # down to row 0
)
sarsa_ys = (
    [(r + 0.5) * CELL for r in range(ROWS - 1)] +             # up
    [(ROWS - 0.5) * CELL] * COLS +                            # across
    [(r + 0.5) * CELL for r in range(ROWS - 2, -1, -1)]       # down
)
ax.plot(sarsa_xs, sarsa_ys, color=MLBLUE, linewidth=3.5, zorder=4,
        solid_capstyle='round', label='SARSA (safe)')

# ── Directional arrowheads on paths ───────────────────────────────────────
# Q-Learning: midpoint arrow
mid = COLS // 2
arr_ql = FancyArrowPatch((ql_xs[mid - 1], ql_ys[mid - 1]),
                          (ql_xs[mid], ql_ys[mid]),
                          arrowstyle='-|>', mutation_scale=16,
                          linewidth=0, color=MLORANGE, zorder=5)
ax.add_patch(arr_ql)

# SARSA: midpoint on top row
top_mid = ROWS - 1 + COLS // 2
arr_sa = FancyArrowPatch((sarsa_xs[top_mid - 1], sarsa_ys[top_mid - 1]),
                          (sarsa_xs[top_mid], sarsa_ys[top_mid]),
                          arrowstyle='-|>', mutation_scale=16,
                          linewidth=0, color=MLBLUE, zorder=5)
ax.add_patch(arr_sa)

# ── Annotations ───────────────────────────────────────────────────────────
ax.text(5.5 * CELL, (ROWS - 0.15) * CELL + 0.05,
        '−1 per step', ha='center', va='bottom',
        fontsize=10, color=MLBLUE, fontweight='bold')

ax.text(5.5 * CELL, -0.35,
        '−100 if cliff', ha='center', va='bottom',
        fontsize=10, color=MLRED, fontweight='bold')

# ── Legend ─────────────────────────────────────────────────────────────────
legend_patches = [
    mpatches.Patch(color=MLBLUE,   label='SARSA path (safe, row 3)'),
    mpatches.Patch(color=MLORANGE, label='Q-Learning path (optimal, hugs cliff)'),
    mpatches.Patch(color='#FFAAAA', edgecolor=MLRED, linewidth=1.5,
                   label='Cliff cells (−100 reward)'),
]
ax.legend(handles=legend_patches, loc='upper right',
          fontsize=9, framealpha=0.9)

# ── Title ──────────────────────────────────────────────────────────────────
ax.set_title('Cliff Walking: SARSA (Safe) vs Q-Learning (Optimal)',
             fontsize=14, fontweight='bold', pad=8)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=150)
plt.close()
print("Saved: 21_sarsa_vs_qlearning_cliff/chart.pdf")
