"""2D Partial Dependence: Feature Interaction"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import partial_dependence

CHART_METADATA = {
    'title': '2D Partial Dependence: Feature Interaction',
    'description': 'Contour plot of joint partial dependence for two features',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/top10_17_2d_pdp_contour'
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False,
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

feature_names = ['Amount', 'Frequency', 'Distance', 'Time', 'Device']
X, y = make_classification(n_samples=1000, n_features=5, n_informative=3, random_state=42)

clf = RandomForestClassifier(n_estimators=200, random_state=42)
clf.fit(X, y)

pdp_result = partial_dependence(clf, X, features=[0, 1], kind='average')
pd_values = pdp_result['average'][0]
grid_0 = pdp_result['grid_values'][0]
grid_1 = pdp_result['grid_values'][1]

XX, YY = np.meshgrid(grid_0, grid_1)

fig, ax = plt.subplots(figsize=(10, 6))

contour = ax.contourf(XX, YY, pd_values.T, levels=20, cmap='RdYlBu_r', alpha=0.9)
cbar = plt.colorbar(contour, ax=ax, shrink=0.8)
cbar.set_label('Partial Dependence', fontsize=13)

ax.contour(XX, YY, pd_values.T, levels=10, colors='k', linewidths=0.3, alpha=0.4)

ax.set_xlabel(f"{feature_names[0]}")
ax.set_ylabel(f"{feature_names[1]}")
ax.set_title("2D Partial Dependence: Feature Interaction", fontsize=16, fontweight='bold')

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: top10_17_2d_pdp_contour/chart.pdf")
