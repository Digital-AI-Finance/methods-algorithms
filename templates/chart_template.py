"""
Chart Template - Methods and Algorithms Course

Usage:
    Copy this file to your chart folder, rename to chart.py, and customize.

Chart requirements:
    - figsize=(10, 6) for Beamer compatibility
    - Font sizes scaled for 0.55-0.65 textwidth display
    - Output: chart.pdf in same directory
    - GitHub URL in bottom-right corner
"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# =============================================================================
# CHART CONFIGURATION
# =============================================================================

# Chart metadata (update for each chart)
CHART_METADATA = {
    "title": "Chart Title",
    "description": "Brief description of what this chart shows",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L01_Introduction_Linear_Regression/01_simple_regression"
}

# Font sizes scaled for Beamer display at 0.55-0.65 textwidth
plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 13,
    'ytick.labelsize': 13,
    'legend.fontsize': 13,
    'figure.figsize': (10, 6),
    'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# ML Color palette
COLORS = {
    'primary': '#3333B2',    # ML Purple
    'secondary': '#0066CC',  # ML Blue
    'accent': '#FF7F0E',     # ML Orange
    'success': '#2CA02C',    # ML Green
    'danger': '#D62728',     # ML Red
    'lavender': '#ADADE0',   # Light purple
    'gray': '#808080',       # Gray
}

# =============================================================================
# DATA GENERATION
# =============================================================================

np.random.seed(42)

# Example: Generate sample data
# Replace with your actual data generation
n_samples = 100
X = np.linspace(0, 10, n_samples)
y_true = 2 * X + 1
y_noisy = y_true + np.random.normal(0, 2, n_samples)

# =============================================================================
# CREATE FIGURE
# =============================================================================

fig, ax = plt.subplots(figsize=(10, 6))

# Example: Scatter plot with trend line
# Replace with your actual plotting code
ax.scatter(X, y_noisy, alpha=0.6, color=COLORS['secondary'], label='Data points', s=30)
ax.plot(X, y_true, color=COLORS['primary'], linewidth=2, label='True relationship')

# Labels and title
ax.set_xlabel('Feature X')
ax.set_ylabel('Target y')
ax.set_title('Example: Linear Regression Fit')
ax.legend(loc='upper left')

# Add GitHub URL in bottom-right
ax.text(0.99, 0.01, CHART_METADATA['url'],
        transform=ax.transAxes,
        fontsize=7,
        color='gray',
        ha='right',
        va='bottom',
        alpha=0.7)

# =============================================================================
# SAVE FIGURE
# =============================================================================

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

print(f"Chart saved to: {output_path}")
