"""RAG Pipeline Flow -- 5-box horizontal flowchart for L06d Modern Embeddings."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150
})

# ML color palette
COLORS = ['#3333B2', '#0066CC', '#FF7F0E', '#2CA02C', '#D62728']

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Box definitions: (x_center, label, subtitle, color)
boxes = [
    (1.0, 'Documents',       'Split text into\nparagraphs',      COLORS[0]),
    (3.0, 'Chunk +\nEmbed',  'sentence-\ntransformers',          COLORS[1]),
    (5.0, 'Vector DB',       'FAISS /\nChromaDB',                COLORS[2]),
    (7.0, 'Retrieve',        'Top-K\nnearest',                   COLORS[3]),
    (9.0, 'LLM\nAnswer',     'GPT generates\nanswer',            COLORS[4]),
]

box_w, box_h = 1.5, 1.6
y_center = 3.3

for x, label, subtitle, color in boxes:
    # Rounded box
    rect = mpatches.FancyBboxPatch(
        (x - box_w / 2, y_center - box_h / 2), box_w, box_h,
        boxstyle='round,pad=0.15', facecolor=color, edgecolor='white',
        linewidth=2, alpha=0.92
    )
    ax.add_patch(rect)
    # Main label
    ax.text(x, y_center + 0.15, label, ha='center', va='center',
            fontsize=14, fontweight='bold', color='white')
    # Subtitle below box
    ax.text(x, y_center - box_h / 2 - 0.35, subtitle, ha='center', va='top',
            fontsize=10, color='#444444', style='italic')

# Arrows between boxes
arrow_props = dict(arrowstyle='->', lw=2.5, color='#555555')
for i in range(len(boxes) - 1):
    x_start = boxes[i][0] + box_w / 2 + 0.05
    x_end = boxes[i + 1][0] - box_w / 2 - 0.05
    ax.annotate('', xy=(x_end, y_center), xytext=(x_start, y_center),
                arrowprops=arrow_props)

# Title
ax.text(5.0, 5.6, 'RAG Pipeline: From Documents to Answers',
        ha='center', va='center', fontsize=16, fontweight='bold', color='#333333')

# Step numbers
for i, (x, _, _, _) in enumerate(boxes):
    ax.text(x, y_center + box_h / 2 + 0.2, f'Step {i + 1}',
            ha='center', va='bottom', fontsize=9, color='#888888', fontweight='bold')

plt.tight_layout()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chart.pdf')
plt.savefig(out, bbox_inches='tight', pad_inches=0.1)
plt.close()
print(f'Saved: {out}')
