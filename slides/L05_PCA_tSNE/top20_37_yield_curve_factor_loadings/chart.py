"""Yield Curve PCA: Level, Slope, and Curvature Factors."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.decomposition import PCA
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Yield Curve PCA: Level, Slope, and Curvature Factors",
    "description": "PCA factor loadings from Nelson-Siegel simulated yield curves showing Level, Slope, and Curvature.",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top20_37_yield_curve_factor_loadings"
}


np.random.seed(42)

# Maturities in years
tau = np.array([0.25, 0.5, 1, 2, 3, 5, 7, 10, 20, 30])
maturity_labels = ['3M', '6M', '1Y', '2Y', '3Y', '5Y', '7Y', '10Y', '20Y', '30Y']
lam = 1.5
n_days = 500

# Nelson-Siegel model: y(tau) = b0 + b1*(1-exp(-tau/lam))/(tau/lam) + b2*((1-exp(-tau/lam))/(tau/lam) - exp(-tau/lam))
def nelson_siegel(tau, b0, b1, b2, lam):
    factor = (1 - np.exp(-tau / lam)) / (tau / lam)
    return b0 + b1 * factor + b2 * (factor - np.exp(-tau / lam))

# Generate 500 daily yield curves
b0_vals = np.random.normal(5, 0.3, n_days)
b1_vals = np.random.normal(-2, 0.2, n_days)
b2_vals = np.random.normal(1, 0.1, n_days)

yields = np.zeros((n_days, len(tau)))
for i in range(n_days):
    yields[i] = nelson_siegel(tau, b0_vals[i], b1_vals[i], b2_vals[i], lam)
    yields[i] += np.random.normal(0, 0.02, len(tau))

# PCA with 3 components
pca = PCA(n_components=3).fit(yields)

fig, ax = plt.subplots()
ax.plot(range(len(tau)), pca.components_[0], color=MLPURPLE, marker='o',
        linewidth=2.5, markersize=8, label='PC1 (Level)')
ax.plot(range(len(tau)), pca.components_[1], color=MLBLUE, marker='s',
        linewidth=2.5, markersize=8, label='PC2 (Slope)')
ax.plot(range(len(tau)), pca.components_[2], color=MLORANGE, marker='^',
        linewidth=2.5, markersize=8, label='PC3 (Curvature)')

ax.axhline(y=0, color='gray', linewidth=0.8, linestyle='-', alpha=0.5)
ax.set_xticks(range(len(tau)))
ax.set_xticklabels(maturity_labels)
ax.set_xlabel('Maturity')
ax.set_ylabel('Loading Magnitude')
ax.set_title('Yield Curve PCA: Level, Slope, and Curvature Factors')
ax.legend(frameon=True, fancybox=True, shadow=True)
ax.grid(True, alpha=0.3)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
