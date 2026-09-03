import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PALETTE = {"survived": "#2E86AB", "died": "#C94C4C", "bg": "#F7F7F7", "text": "#2B2B2B"}

df = pd.read_csv('data/titanic_clean.csv')
rate = df['survived'].mean() * 100
n_total = len(df)
n_survived = df['survived'].sum()

fig, ax = plt.subplots(figsize=(7, 7), facecolor='white')
wedges, _ = ax.pie(
    [rate, 100 - rate],
    colors=[PALETTE['survived'], '#E8E8E8'],
    startangle=90,
    counterclock=False,
    wedgeprops=dict(width=0.38, edgecolor='white', linewidth=3),
)
ax.text(0, 0.08, f"{rate:.0f}%", ha='center', va='center', fontsize=58, fontweight='bold', color=PALETTE['text'])
ax.text(0, -0.18, "survived", ha='center', va='center', fontsize=20, color='#666666')
ax.set_title(f"Only 4 in 10 Passengers Survived\n", fontsize=20, fontweight='bold', color=PALETTE['text'], pad=10)
ax.text(0, -1.35, f"Based on {n_total:,} passenger records ({n_survived:,} survivors, {n_total-n_survived:,} did not)",
        ha='center', fontsize=12, color='#888888')
ax.set_aspect('equal')
plt.tight_layout()
plt.savefig('images/viz1_overview.png', dpi=180, bbox_inches='tight', facecolor='white')
print("saved viz1")
