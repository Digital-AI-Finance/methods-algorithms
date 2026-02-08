"""Original Clusters - MNIST digits shown in first 2 raw dimensions.
Demonstrates that high-dimensional data looks overlapped in raw feature space."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import load_digits

CHART_METADATA = {
    'title': 'Original Clusters',
    'description': 'High-dimensional digit data (showing 2 of 64 dimensions)',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/06a_original_clusters'
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Color palette for 10 digit classes
colors = ['#3333B2', '#0066CC', '#FF7F0E', '#2CA02C', '#D62728',
          '#ADADE0', '#8B4513', '#FF69B4', '#808080', '#000000']

# Load ACTUAL high-dimensional data
digits = load_digits()
X, y = digits.data, digits.target

fig, ax = plt.subplots(figsize=(10, 6))

# Show first 2 raw pixel features -- clusters heavily overlap
for digit in range(10):
    mask = y == digit
    ax.scatter(X[mask, 0], X[mask, 1], c=colors[digit], label=str(digit),
               s=15, alpha=0.5, edgecolors='none')

ax.set_title('Raw Pixel Features of MNIST Digits\n(2 of 64 Dimensions -- Classes Overlap)',
             fontsize=16, fontweight='bold')
ax.set_xlabel('Pixel Feature 1', fontweight='bold')
ax.set_ylabel('Pixel Feature 2', fontweight='bold')
ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', fontsize=11,
          title='Digit', title_fontsize=12, markerscale=2)
ax.grid(True, alpha=0.3)

for spine in ax.spines.values():
    spine.set_linewidth(1.5)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 06a_original_clusters/chart.pdf")
