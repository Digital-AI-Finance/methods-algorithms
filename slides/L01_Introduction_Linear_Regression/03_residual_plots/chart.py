"""Residual Analysis - Residuals vs Fitted Values"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# QuantLet branding metadata
CHART_METADATA = {
    "title": "Residual Analysis",
    "description": "Residuals vs fitted values diagnostic plot",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L01_Introduction_Linear_Regression/03_residual_plots"
}

# Chart settings for Beamer
plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150
})

# Colors
MLPURPLE = '#3333B2'
MLORANGE = '#FF7F0E'
MLBLUE = '#0066CC'
MLRED = '#D62728'

# Generate synthetic data with good residuals
np.random.seed(42)
n = 80
X = np.random.uniform(50, 200, n)
true_slope = 2000
true_intercept = 50000
noise = np.random.normal(0, 25000, n)
y = true_intercept + true_slope * X + noise

# Fit model
slope = np.sum((X - X.mean()) * (y - y.mean())) / np.sum((X - X.mean())**2)
intercept = y.mean() - slope * X.mean()
y_pred = intercept + slope * X
residuals = y - y_pred

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Residual plot
ax.scatter(y_pred/1000, residuals/1000, c=MLBLUE, alpha=0.7, s=60)
ax.axhline(y=0, color=MLRED, linestyle='--', linewidth=2, label='Zero line')

# Add reference bands
ax.axhline(y=2*np.std(residuals)/1000, color='gray', linestyle=':', alpha=0.5)
ax.axhline(y=-2*np.std(residuals)/1000, color='gray', linestyle=':', alpha=0.5)

# Labels
ax.set_xlabel('Fitted Values (thousands $)')
ax.set_ylabel('Residuals (thousands $)')
ax.set_title('Residual Analysis: Checking Model Assumptions')
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

# Add annotation
ax.annotate('Residuals should be\nrandomly scattered\naround zero',
            xy=(300, 40), fontsize=11, color='gray',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 03_residual_plots/chart.pdf")
