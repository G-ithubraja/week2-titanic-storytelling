import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/titanic_clean.csv')
df['Outcome'] = df['survived'].map({0: 'Did not survive', 1: 'Survived'})

fig, ax = plt.subplots(figsize=(9, 6), facecolor='white')
palette = {'Did not survive': '#C94C4C', 'Survived': '#2E86AB'}
sns.violinplot(data=df, x='Outcome', y='age', hue='Outcome', palette=palette,
                inner='quartile', ax=ax, cut=0, legend=False)

mean_died = df.loc[df.survived == 0, 'age'].mean()
mean_surv = df.loc[df.survived == 1, 'age'].mean()
child_rate = df.loc[df.age <= 12, 'survived'].mean() * 100

ax.annotate(f"Mean age: {mean_died:.0f}", xy=(0, mean_died), xytext=(-0.44, mean_died + 16),
            fontsize=11, color='#333333', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#888888'))
ax.annotate(f"Mean age: {mean_surv:.0f}", xy=(1, mean_surv), xytext=(0.66, mean_surv + 20),
            fontsize=11, color='#333333', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#888888'))
ax.annotate(f"Children (0-12): {child_rate:.0f}% survived", xy=(1, 8), xytext=(0.55, -14),
            fontsize=11, color='#1a5276', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#2E86AB'))

ax.set_title('Survivors Skewed Slightly Younger — and Children Fared Best of All\nAge Distribution by Outcome',
             fontsize=16, fontweight='bold', pad=14)
ax.set_ylabel('Age (years)', fontsize=12)
ax.set_ylim(-22, 85)
ax.set_xlabel('')
ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout()
plt.savefig('images/viz3_age_violin.png', dpi=180, bbox_inches='tight', facecolor='white')
print("saved viz3")
