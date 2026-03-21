"""Intrinsic Dimensionality - Bar chart with cumulative overlay and elbow detection."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.decomposition import PCA
from sklearn.datasets import make_classification
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Intrinsic Dimensionality: Finding the Elbow",
    "description": "Individual variance bars with cumulative line and elbow marker",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top10_18_intrinsic_dimensionality"
}


X, y = make_classification(n_samples=500, n_features=20, n_informative=5, random_state=42)

pca = PCA(n_components=20, random_state=42)
pca.fit(X)

var_ratio = pca.explained_variance_ratio_
cumulative = np.cumsum(var_ratio)
components = np.arange(1, 21)

fig, ax1 = plt.subplots()
ax1.bar(components, var_ratio, color=MLBLUE, alpha=0.6, label='Individual variance')

ax2 = ax1.twinx()
ax2.grid(False)
ax2.plot(components, cumulative, 'o-', color=MLRED, linewidth=2.5, markersize=5, label='Cumulative')

elbow = np.argmax(var_ratio < 0.05) + 1
if var_ratio[elbow - 1] >= 0.05:
    elbow = len(var_ratio)

ax1.axvline(x=elbow, color=MLGREEN, linestyle='--', linewidth=2, alpha=0.8)
ax1.annotate(f'Elbow at PC{elbow}\n(var < 5%)', xy=(elbow, var_ratio[elbow - 1]),
             xytext=(elbow + 3, var_ratio[0] * 0.6),
             fontsize=12, color=MLGREEN, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=1.5))

ax1.set_xlabel('Principal Component')
ax1.set_ylabel('Explained Variance Ratio', color=MLBLUE)
ax2.set_ylabel('Cumulative Variance', color=MLRED)
ax1.set_title('Intrinsic Dimensionality: Finding the Elbow')
ax1.set_xticks(components[::2])

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='center right', framealpha=0.9)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_18_intrinsic_dimensionality/chart.pdf")
