"""Rolling PCA for Portfolio Risk Regime Detection."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.decomposition import PCA
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Rolling PCA for Portfolio Risk Regime Detection",
    "description": "Time series of rolling PC1 explained variance ratio detecting crisis regimes in correlated stock returns.",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top20_40_portfolio_risk_pca_monitoring"
}


np.random.seed(42)

n_days = 1000
n_stocks = 10
window = 250

# Generate returns with regime-dependent correlation
returns = np.zeros((n_days, n_stocks))

for day in range(n_days):
    if 500 <= day < 750:
        # Crisis regime: high correlation, high volatility
        corr_val = 0.8
        vol = 0.02
    else:
        # Normal regime: low correlation, normal volatility
        corr_val = 0.3
        vol = 0.01

    corr_matrix = np.full((n_stocks, n_stocks), corr_val)
    np.fill_diagonal(corr_matrix, 1.0)
    L = np.linalg.cholesky(corr_matrix)
    returns[day] = vol * (L @ np.random.randn(n_stocks))

# Rolling PCA: compute PC1 explained variance ratio for each 250-day window
rolling_days = []
rolling_var_ratio = []

for end in range(window, n_days):
    start = end - window
    window_data = returns[start:end]
    pca = PCA(n_components=1).fit(window_data)
    rolling_days.append(end)
    rolling_var_ratio.append(pca.explained_variance_ratio_[0])

rolling_days = np.array(rolling_days)
rolling_var_ratio = np.array(rolling_var_ratio)

fig, ax = plt.subplots()

# Shade crisis period
ax.axvspan(500, 750, color=MLRED, alpha=0.1, label='Crisis Period')

# Plot rolling variance ratio
ax.plot(rolling_days, rolling_var_ratio, color=MLPURPLE, linewidth=2, label='PC1 Variance Ratio')

# Threshold lines
ax.axhline(y=0.5, color=MLORANGE, linewidth=1.5, linestyle='--', alpha=0.7, label='50% Threshold')
ax.axhline(y=0.7, color=MLRED, linewidth=1.5, linestyle='--', alpha=0.7, label='70% Threshold')

ax.set_xlabel('Trading Day')
ax.set_ylabel('PC1 Explained Variance Ratio')
ax.set_title('Rolling PCA for Portfolio Risk Regime Detection')
ax.set_ylim(0.3, 0.9)
ax.set_xlim(250, 1000)
ax.legend(frameon=True, fancybox=True, shadow=True, loc='upper left')
ax.grid(True, alpha=0.3)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
