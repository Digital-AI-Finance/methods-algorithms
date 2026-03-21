"""PCA on Stock Returns: Revealing the Market Factor."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.decomposition import PCA

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "PCA on Stock Returns: Revealing the Market Factor",
    "description": "Horizontal bar chart of PC1 loadings across 12 stocks from 3 sectors, revealing the market factor.",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top20_38_portfolio_factor_decomposition"
}


np.random.seed(42)

n_days = 500
n_stocks = 12

# Stock labels and sector assignments
labels = ['BANK_A', 'BANK_B', 'BANK_C', 'BANK_D',
          'TECH_A', 'TECH_B', 'TECH_C', 'TECH_D',
          'OIL_A', 'OIL_B', 'OIL_C', 'OIL_D']
sector_colors = [MLPURPLE]*4 + [MLBLUE]*4 + [MLORANGE]*4
sector_names = ['Banking', 'Tech', 'Energy']

# Factor model: r_i = beta_market * F_market + beta_sector * F_sector + epsilon
F_market = np.random.normal(0, 0.01, n_days)
F_banking = np.random.normal(0, 0.005, n_days)
F_tech = np.random.normal(0, 0.005, n_days)
F_energy = np.random.normal(0, 0.005, n_days)

# Market betas
beta_market = np.array([0.8, 0.9, 1.0, 1.2,    # Banking
                        1.0, 1.2, 1.3, 1.5,     # Tech
                        0.6, 0.7, 0.8, 1.0])    # Energy

returns = np.zeros((n_days, n_stocks))
for i in range(n_stocks):
    returns[:, i] = beta_market[i] * F_market
    if i < 4:
        returns[:, i] += F_banking
    elif i < 8:
        returns[:, i] += F_tech
    else:
        returns[:, i] += F_energy
    returns[:, i] += np.random.normal(0, 0.005, n_days)

# PCA
pca = PCA(n_components=1).fit(returns)
pc1_loadings = pca.components_[0]

# Ensure loadings are positive (PC1 = market factor, should be positive)
if np.mean(pc1_loadings) < 0:
    pc1_loadings = -pc1_loadings

fig, ax = plt.subplots()
y_pos = np.arange(n_stocks)
bars = ax.barh(y_pos, pc1_loadings, color=sector_colors, edgecolor='white', height=0.7)

ax.set_yticks(y_pos)
ax.set_yticklabels(labels)
ax.set_xlabel('PC1 Loading (Market Factor)')
ax.set_title('PCA on Stock Returns: Revealing the Market Factor')
ax.axvline(x=0, color='gray', linewidth=0.8, alpha=0.5)
ax.invert_yaxis()

# Legend for sectors
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=MLPURPLE, label='Banking'),
                   Patch(facecolor=MLBLUE, label='Tech'),
                   Patch(facecolor=MLORANGE, label='Energy')]
ax.legend(handles=legend_elements, frameon=True, fancybox=True, shadow=True, loc='lower right')
ax.grid(True, alpha=0.3, axis='x')

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
