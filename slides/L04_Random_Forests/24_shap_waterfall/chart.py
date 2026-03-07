"""SHAP Waterfall: Why Was This Transaction Flagged?"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'SHAP Waterfall: Why Was This Transaction Flagged?',
    'description': 'Manual waterfall bar chart showing SHAP-style feature contributions for a fraud prediction',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/24_shap_waterfall'
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

features = ['Transaction Amount', 'Distance from Home', 'Frequency (24h)',
            'Time of Day', 'Merchant Category', 'Card Present', 'Customer Age']
shap_values = [+0.32, +0.18, +0.15, +0.08, -0.05, -0.03, -0.02]
base_value = 0.35

# Sort by absolute SHAP value descending (already ordered above)
# Build waterfall: accumulate from base
cumulative = base_value
starts = []
for sv in shap_values:
    starts.append(cumulative)
    cumulative += sv
final_prediction = cumulative

fig, ax = plt.subplots()

y_positions = np.arange(len(features))[::-1]

for i, (feat, sv, start) in enumerate(zip(features, shap_values, starts)):
    color = MLRED if sv > 0 else MLGREEN
    ax.barh(y_positions[i], sv, left=start, height=0.55, color=color, edgecolor='white', linewidth=0.5)
    # Value label
    label_x = start + sv / 2
    ax.text(label_x, y_positions[i], f'{sv:+.2f}', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')

    # Connector lines between bars
    if i < len(features) - 1:
        next_start = start + sv
        ax.plot([next_start, next_start], [y_positions[i] - 0.35, y_positions[i + 1] + 0.35],
                color='gray', linewidth=0.8, linestyle=':')

ax.set_yticks(y_positions)
ax.set_yticklabels(features)

# Base value line
ax.axvline(x=base_value, color='gray', linestyle='--', linewidth=1.2, alpha=0.6)
ax.text(base_value, y_positions[0] + 0.7, f'Base = {base_value:.2f}',
        ha='center', va='bottom', fontsize=11, color='gray')

# Final prediction line
ax.axvline(x=final_prediction, color='black', linestyle='-', linewidth=2.0)
ax.text(final_prediction, y_positions[-1] - 0.7, f'Prediction = {final_prediction:.2f}',
        ha='center', va='top', fontsize=12, fontweight='bold', color='black')

# Legend
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=MLRED, label='Increases fraud probability'),
                   Patch(facecolor=MLGREEN, label='Decreases fraud probability')]
ax.legend(handles=legend_elements, loc='lower right', framealpha=0.9)

ax.set_xlabel('Fraud Probability')
ax.set_title(CHART_METADATA['title'])
ax.set_xlim([0.15, 1.15])

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 24_shap_waterfall/chart.pdf")
