"""PCA Mini-Example: 5 Data Points in 2D"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "PCA Mini-Example: 5 Data Points in 2D",
    "description": "Visual companion for the PCA by Hand worked example",
    "url": "https://digital-ai-finance.github.io/methods-algorithms/slides/L05_PCA_tSNE/10_pca_mini_example"
}


fig, ax = plt.subplots()

# Data points
points = np.array([[1, 2], [3, 4], [5, 6], [2, 3], [4, 5]], dtype=float)
mean = points.mean(axis=0)  # (3, 4)

# PC directions
pc1_dir = np.array([1 / np.sqrt(2), 1 / np.sqrt(2)])
pc2_dir = np.array([-1 / np.sqrt(2), 1 / np.sqrt(2)])

# --- Draw projections (dashed lines perpendicular to PC1) ---
for pt in points:
    diff = pt - mean
    proj_scalar = np.dot(diff, pc1_dir)
    proj_point = mean + proj_scalar * pc1_dir
    ax.plot([pt[0], proj_point[0]], [pt[1], proj_point[1]],
            color='gray', linestyle='--', linewidth=1.0, alpha=0.6, zorder=1)

# --- PC1 arrow ---
pc1_length = 2.5
ax.annotate(
    '', xy=mean + pc1_length * pc1_dir, xytext=mean - pc1_length * pc1_dir,
    arrowprops=dict(arrowstyle='->', color=MLORANGE, lw=2.5)
)
# PC1 label offset slightly above the arrowhead
label_pc1 = mean + (pc1_length + 0.25) * pc1_dir
ax.text(label_pc1[0], label_pc1[1] - 0.25, r'PC1 ($\lambda_1$=5, 100%)',
        color=MLORANGE, fontsize=12, ha='center', va='bottom', fontweight='bold')

# --- PC2 arrow ---
pc2_length = 1.0
ax.annotate(
    '', xy=mean + pc2_length * pc2_dir, xytext=mean - pc2_length * pc2_dir,
    arrowprops=dict(arrowstyle='->', color=MLBLUE, lw=1.8, alpha=0.5)
)
# PC2 label
label_pc2 = mean + (pc2_length + 0.25) * pc2_dir
ax.text(label_pc2[0] - 0.1, label_pc2[1], r'PC2 ($\lambda_2$=0)',
        color=MLBLUE, fontsize=12, ha='right', va='center', alpha=0.7)

# --- Original data points ---
ax.scatter(points[:, 0], points[:, 1], s=120, color=MLPURPLE, zorder=4,
           label='Data points')

# --- Mean point ---
ax.scatter(mean[0], mean[1], s=200, color=MLRED, marker='*', zorder=5,
           label='Mean (3, 4)')

# --- Coordinate labels for each point ---
offsets = [(0.12, 0.12), (0.12, 0.12), (0.12, 0.12), (-0.35, 0.12), (0.12, 0.12)]
for pt, (dx, dy) in zip(points, offsets):
    ax.text(pt[0] + dx, pt[1] + dy, f'({int(pt[0])},{int(pt[1])})',
            fontsize=11, color=MLPURPLE, va='bottom')

# --- Formatting ---
ax.set_aspect('equal')
ax.set_title('PCA Mini-Example: Finding the Best Direction', fontsize=16)
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.grid(True, alpha=0.3)
ax.legend(loc='upper left', fontsize=12)

# URL watermark
fig.text(0.99, 0.01, CHART_METADATA["url"],
         ha='right', va='bottom', fontsize=7, color='gray', alpha=0.6)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
