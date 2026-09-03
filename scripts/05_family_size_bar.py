import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/titanic_clean.csv')
df['family_size'] = df['sibsp'] + df['parch'] + 1

grp = df.groupby('family_size')['survived'].agg(['mean', 'count'])
grp = grp[grp['count'] >= 6]  # drop sparse bins for a cleaner, more honest story
grp['pct'] = grp['mean'] * 100

colors = ['#2E86AB' if v >= 50 else '#C94C4C' for v in grp['pct']]

fig, ax = plt.subplots(figsize=(9.5, 6), facecolor='white')
bars = ax.bar(grp.index.astype(str), grp['pct'], color=colors, width=0.6)

for b, cnt in zip(bars, grp['count']):
    ax.text(b.get_x() + b.get_width()/2, b.get_height() + 2, f"{b.get_height():.0f}%",
            ha='center', fontsize=12, fontweight='bold', color='#333333')
    ax.text(b.get_x() + b.get_width()/2, -6, f"n={cnt}", ha='center', fontsize=9, color='#999999')

ax.axhline(df['survived'].mean()*100, color='#888888', linestyle='--', linewidth=1)
ax.text(len(grp)-0.4, df['survived'].mean()*100 + 2, 'overall average (42%)', fontsize=10, color='#888888', ha='right')

ax.set_ylim(-10, 85)
ax.set_xlabel('Family members aboard (including self)', fontsize=12)
ax.set_ylabel('Survival Rate (%)', fontsize=12)
ax.set_title('The "Goldilocks" Effect: Small Families Fared Best\nTraveling alone or in a large group both lowered survival odds',
             fontsize=15, fontweight='bold', pad=14)
ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout()
plt.savefig('images/viz5_family.png', dpi=180, bbox_inches='tight', facecolor='white')
print("saved viz5")
