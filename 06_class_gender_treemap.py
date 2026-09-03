import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import squarify

df = pd.read_csv('data/titanic_clean.csv')
df['Outcome'] = df['survived'].map({0: 'Did not survive', 1: 'Survived'})
df['Sex'] = df['sex'].str.capitalize()

classes = ['First', 'Second', 'Third']
sexes = ['Female', 'Male']
color_map = {'Survived': '#2E86AB', 'Did not survive': '#C94C4C'}

fig, axes = plt.subplots(1, 3, figsize=(16, 6.2), facecolor='white')

for ax, cls in zip(axes, classes):
    sub = df[df['class'] == cls]
    labels, sizes, colors = [], [], []
    for sx in sexes:
        for outcome in ['Survived', 'Did not survive']:
            n = len(sub[(sub['Sex'] == sx) & (sub['Outcome'] == outcome)])
            if n > 0:
                pct = n / len(sub) * 100
                # shorter label for small slices so text doesn't overflow the box
                if pct < 8:
                    lbl = f"{sx[0]}\n{n}"
                else:
                    lbl = f"{sx}\n{outcome}\n{n} ({pct:.0f}%)"
                labels.append(lbl)
                sizes.append(n)
                colors.append(color_map[outcome])
    squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.92, ax=ax,
                   pad=True, text_kwargs={'fontsize': 10.5, 'fontweight': 'bold', 'color': 'white'})
    ax.set_title(f"{cls} Class\n(n={len(sub)})", fontsize=15, fontweight='bold', pad=8)
    ax.axis('off')

fig.suptitle('The Full Picture: Class, Gender, and Survival Combined',
             fontsize=19, fontweight='bold', y=1.02)
fig.text(0.5, 0.965, 'Box size = number of passengers in that group  ·  blue = survived, red = did not',
          ha='center', fontsize=12, color='#666666')

plt.tight_layout()
plt.savefig('images/viz6_treemap.png', dpi=170, bbox_inches='tight', facecolor='white')
print("saved viz6")
