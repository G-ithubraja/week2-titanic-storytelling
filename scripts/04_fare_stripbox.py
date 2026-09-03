import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('data/titanic_clean.csv')
df['Outcome'] = df['survived'].map({0: 'Did not survive', 1: 'Survived'})
df['fare_plot'] = df['fare'].replace(0, 0.5)  # avoid log(0) for the few free-fare rows

fig, ax = plt.subplots(figsize=(9.5, 6), facecolor='white')
palette = {'Did not survive': '#C94C4C', 'Survived': '#2E86AB'}
sns.stripplot(data=df, x='Outcome', y='fare_plot', hue='Outcome', palette=palette,
              alpha=0.45, jitter=0.28, size=4, ax=ax, legend=False)
sns.boxplot(data=df, x='Outcome', y='fare_plot', showcaps=True,
            boxprops={'facecolor': 'none', 'edgecolor': '#333333', 'linewidth': 1.6},
            whiskerprops={'color': '#333333'}, medianprops={'color': '#333333', 'linewidth': 2},
            showfliers=False, width=0.35, ax=ax)

ax.set_yscale('log')
ax.set_ylabel('Fare paid (£, log scale)', fontsize=12)
ax.set_xlabel('')
med_died = df.loc[df.survived == 0, 'fare'].median()
med_surv = df.loc[df.survived == 1, 'fare'].median()
ax.set_title(f'Survivors Paid More Than 2x the Fare of Those Who Perished\nMedian fare: £{med_died:.0f} (did not survive) vs £{med_surv:.0f} (survived)',
             fontsize=15, fontweight='bold', pad=14)
ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout()
plt.savefig('images/viz4_fare.png', dpi=180, bbox_inches='tight', facecolor='white')
print("saved viz4")
print(med_died, med_surv)
