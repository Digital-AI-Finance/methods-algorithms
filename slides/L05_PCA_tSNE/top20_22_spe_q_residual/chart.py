"""SPE/Q-Residual Statistic for Anomaly Detection."""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "SPE/Q-Residual Statistic for Anomaly Detection",
    "description": "Bar chart of SPE values with 95% threshold, green normal vs red anomalies.",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top20_22_spe_q_residual"
}


np.random.seed(42)

# 200 points in 10D with 3 true components
n_samples = 200
n_features = 10
n_true = 3

# Generate low-rank structure + noise
latent = np.random.randn(n_samples, n_true)
loadings = np.random.randn(n_true, n_features)
X = latent @ loadings + 0.5 * np.random.randn(n_samples, n_features)

# Inject 8 sensor drift anomalies (large values in features 7-10)
anomaly_idx = np.random.choice(n_samples, 8, replace=False)
X[anomaly_idx, 7:10] += np.random.uniform(8, 12, size=(8, 3))

# PCA with 3 components
pca = PCA(n_components=3)
scores = pca.fit_transform(X)
X_reconstructed = pca.inverse_transform(scores)

# SPE = sum of squared residuals per row
residuals = X - X_reconstructed
spe = np.sum(residuals**2, axis=1)

# Pick 50 random samples, sort descending
sample_idx = np.random.choice(n_samples, 50, replace=False)
spe_subset = spe[sample_idx]
sort_order = np.argsort(spe_subset)[::-1]
spe_sorted = spe_subset[sort_order]

# 95% threshold from the non-anomaly distribution
normal_mask = np.ones(n_samples, dtype=bool)
normal_mask[anomaly_idx] = False
threshold_95 = np.percentile(spe[normal_mask], 95)

fig, ax = plt.subplots()

colors = [MLRED if v > threshold_95 else MLGREEN for v in spe_sorted]
bars = ax.bar(range(len(spe_sorted)), spe_sorted, color=colors, edgecolor='white',
              linewidth=0.3, width=0.85)

ax.axhline(y=threshold_95, color=MLPURPLE, linestyle='--', linewidth=2,
           label=f'95% threshold = {threshold_95:.1f}')

ax.set_xlabel('Sample (sorted by SPE)')
ax.set_ylabel('SPE / Q-Residual')
ax.set_title('SPE/Q-Residual Statistic for Anomaly Detection')
ax.legend(loc='upper right')

# Custom legend entries for bar colors
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=MLGREEN, label='Normal'),
    Patch(facecolor=MLRED, label='Anomaly (exceeds threshold)'),
    plt.Line2D([0], [0], color=MLPURPLE, linestyle='--', linewidth=2,
               label=f'95% threshold = {threshold_95:.1f}'),
]
ax.legend(handles=legend_elements, loc='upper right')

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray',
            ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
