"""FinBERT Sentiment: Cosine Similarity to Sentiment Anchors -- horizontal grouped bar chart."""
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()


# Data sorted: positive-dominant at top, negative-dominant at bottom
headlines = [
    "CEO steps down amid probe",
    "Fed signals rate hike",
    "Markets remain volatile",
    "Revenue beats expectations",
    "Dividend increased 20%",
]
pos_sim = [0.15, 0.22, 0.38, 0.68, 0.72]
neg_sim = [0.73, 0.65, 0.41, 0.21, 0.18]

y = np.arange(len(headlines))
bar_h = 0.35

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(y + bar_h / 2, pos_sim, bar_h, color=MLGREEN, label='Positive Similarity', zorder=3)
ax.barh(y - bar_h / 2, neg_sim, bar_h, color=MLRED, label='Negative Similarity', zorder=3)

ax.set_yticks(y)
ax.set_yticklabels(headlines, fontsize=12)
ax.set_xlabel('Cosine Similarity')
ax.set_xlim(0, 0.9)
ax.set_title('FinBERT Sentiment: Cosine Similarity to Sentiment Anchors',
             fontsize=16, fontweight='bold', pad=12)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(loc='lower right', framealpha=0.9)
ax.grid(axis='x', alpha=0.3, zorder=0)

plt.tight_layout()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chart.pdf')
plt.savefig(out, bbox_inches='tight', pad_inches=0.1, facecolor='white')
plt.close()
print(f'Saved: {out}')
