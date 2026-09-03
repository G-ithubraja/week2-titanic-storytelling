import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/titanic_clean.csv')

grp = df.groupby(['class', 'sex'], observed=True)['survived'].mean().unstack() * 100
classes = ['First', 'Second', 'Third']
grp = grp.loc[classes]

x = np.arange(len(classes))
width = 0.36

fig, ax = plt.subplots(figsize=(9, 6), facecolor='white')
b1 = ax.bar(x - width/2, grp['female'], width, label='Women', color='#C94C4C')
b2 = ax.bar(x + width/2, grp['male'], width, label='Men', color='#2E86AB')

for bars in (b1, b2):
    for b in bars:
        h = b.get_height()
        ax.text(b.get_x() + b.get_width()/2, h + 1.5, f'{h:.0f}%', ha='center', fontsize=12, fontweight='bold', color='#333333')

# annotate the widest gap
gap = grp['female'] - grp['male']
widest_idx = gap.idxmax()
xi = classes.index(widest_idx)
ax.annotate(
    f"{gap[widest_idx]:.0f}-point gap",
    xy=(xi, (grp.loc[widest_idx,'female'] + grp.loc[widest_idx,'male'])/2),
    xytext=(xi + 0.65, 55),
    fontsize=12, color='#555555', fontweight='bold',
    arrowprops=dict(arrowstyle='->', color='#888888', lw=1.5),
)

ax.set_xticks(x)
ax.set_xticklabels([f'{c} Class' for c in classes], fontsize=13)
ax.set_ylabel('Survival Rate (%)', fontsize=12)
ax.set_ylim(0, 108)
ax.set_title('Survival Depended More on Gender Than on Class —\nBut Class Still Mattered Within Each Gender',
             fontsize=16, fontweight='bold', pad=16)
ax.legend(loc='upper right', frameon=False, fontsize=12)
ax.spines[['top', 'right']].set_visible(False)
ax.grid(axis='y', alpha=0.25)
plt.tight_layout()
plt.savefig('images/viz2_class_gender.png', dpi=180, bbox_inches='tight', facecolor='white')
print("saved viz2")
