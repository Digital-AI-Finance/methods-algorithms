"""Simple Linear Regression - Scatter plot with fitted line"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Chart settings for Beamer (scaled up for 70% display)
plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150
})

# Colors
MLPURPLE = '#3333B2'
MLORANGE = '#FF7F0E'
MLBLUE = '#0066CC'

# Generate synthetic data
np.random.seed(42)
n = 50
X = np.random.uniform(50, 200, n)  # House size (sqm)
true_slope = 2000
true_intercept = 50000
noise = np.random.normal(0, 30000, n)
y = true_intercept + true_slope * X + noise  # House price

# Fit linear regression
X_mean = X.mean()
y_mean = y.mean()
slope = np.sum((X - X_mean) * (y - y_mean)) / np.sum((X - X_mean)**2)
intercept = y_mean - slope * X_mean

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Scatter plot
ax.scatter(X, y/1000, c=MLBLUE, alpha=0.7, s=60, label='Data points')

# Regression line
X_line = np.linspace(40, 210, 100)
y_line = (intercept + slope * X_line) / 1000
ax.plot(X_line, y_line, c=MLORANGE, linewidth=3, label=f'Fit: y = {intercept/1000:.0f}k + {slope:.0f}x')

# Labels
ax.set_xlabel('House Size (sqm)')
ax.set_ylabel('Price (thousands $)')
ax.set_title('Simple Linear Regression: House Price vs Size')
ax.legend(loc='lower right')
ax.grid(True, alpha=0.3)

# Axis limits
ax.set_xlim(40, 210)
ax.set_ylim(0, 550)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 01_simple_regression/chart.pdf")
