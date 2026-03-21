"""Outlier Influence on PCA Directions."""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Outlier Influence on PCA Directions",
    "description": "2D scatter showing how outliers shift PC1 direction with angular deviation.",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top20_24_robust_pca_outlier_influence"
}


np.random.seed(42)

# Clean data: 300 bivariate normal
X_clean = np.random.multivariate_normal([0, 0], [[4, 2], [2, 1.5]], size=300)

# Outliers
X_outliers = np.random.multivariate_normal([8, -3], [[0.3, 0], [0, 0.3]], size=15)

# Contaminated data
X_contaminated = np.vstack([X_clean, X_outliers])

# PCA on clean
pca_clean = PCA(n_components=2).fit(X_clean)
pc1_clean = pca_clean.components_[0]

# PCA on contaminated
pca_contam = PCA(n_components=2).fit(X_contaminated)
pc1_contam = pca_contam.components_[0]

# Angular deviation
cos_angle = np.clip(np.abs(np.dot(pc1_clean, pc1_contam)), -1, 1)
angle_deg = np.degrees(np.arccos(cos_angle))

# Ensure arrows point in similar general direction for visual clarity
if np.dot(pc1_clean, pc1_contam) < 0:
    pc1_contam = -pc1_contam

fig, ax = plt.subplots()

# Plot clean points
ax.scatter(X_clean[:, 0], X_clean[:, 1], c=MLBLUE, alpha=0.3, s=20,
           label='Clean data (n=300)', zorder=2)

# Plot outliers
ax.scatter(X_outliers[:, 0], X_outliers[:, 1], c=MLRED, alpha=0.8, s=50,
           marker='x', linewidths=2, label='Outliers (n=15)', zorder=3)

# Arrow scale
arrow_len = 4.0
mean_clean = X_clean.mean(axis=0)
mean_contam = X_contaminated.mean(axis=0)

# PC1 direction arrows from data mean
ax.annotate('', xy=mean_clean + arrow_len * pc1_clean,
            xytext=mean_clean,
            arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=3),
            zorder=4)
ax.annotate('', xy=mean_contam + arrow_len * pc1_contam,
            xytext=mean_contam,
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=3),
            zorder=4)

# Labels for arrows
ax.text(mean_clean[0] + arrow_len * pc1_clean[0] + 0.3,
        mean_clean[1] + arrow_len * pc1_clean[1] + 0.3,
        'PC1 (clean)', color=MLGREEN, fontsize=12, fontweight='bold', zorder=5)
ax.text(mean_contam[0] + arrow_len * pc1_contam[0] + 0.3,
        mean_contam[1] + arrow_len * pc1_contam[1] - 0.5,
        'PC1 (contaminated)', color=MLRED, fontsize=12, fontweight='bold', zorder=5)

# Draw arc to show angular deviation
arc_radius = 2.5
angle_clean = np.degrees(np.arctan2(pc1_clean[1], pc1_clean[0]))
angle_contam = np.degrees(np.arctan2(pc1_contam[1], pc1_contam[0]))
arc_center = (mean_clean + mean_contam) / 2

from matplotlib.patches import Arc
arc = Arc(arc_center, 2 * arc_radius, 2 * arc_radius,
          angle=0, theta1=min(angle_clean, angle_contam),
          theta2=max(angle_clean, angle_contam),
          color=MLPURPLE, linewidth=2, linestyle='--', zorder=4)
ax.add_patch(arc)

# Label the angle
mid_angle = np.radians((angle_clean + angle_contam) / 2)
label_x = arc_center[0] + (arc_radius + 0.5) * np.cos(mid_angle)
label_y = arc_center[1] + (arc_radius + 0.5) * np.sin(mid_angle)
ax.text(label_x, label_y, f'$\\Delta\\theta = {angle_deg:.1f}°$',
        color=MLPURPLE, fontsize=13, fontweight='bold',
        ha='center', va='center', zorder=5,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=MLPURPLE, alpha=0.9))

ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_title('Outlier Influence on PCA Directions')
ax.legend(loc='lower left')

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray',
            ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
