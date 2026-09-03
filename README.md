# Week 2 — Advanced Data Visualization & Storytelling

Data science internship task: turn a cleaned dataset into a visual narrative
a non-technical reader can follow, using 6 annotated visualizations.

**Dataset:** Titanic passenger records, cleaned in [Week 1](../week1-titanic-eda) (773 rows, 0 missing values).

**Full write-up:** [`report/Week2_Data_Storytelling_Report.docx`](report/Week2_Data_Storytelling_Report.docx)

---

## Project structure

```
week2-titanic-storytelling/
├── data/
│   └── titanic_clean.csv          # Cleaned dataset (from Week 1)
├── images/                        # 6 narrative visualizations (PNG)
├── scripts/
│   ├── 01_overview_donut.py
│   ├── 02_class_gender_bar.py
│   ├── 03_age_violin.py
│   ├── 04_fare_stripbox.py
│   ├── 05_family_size_bar.py
│   └── 06_class_gender_treemap.py
├── report/
│   └── Week2_Data_Storytelling_Report.docx
├── requirements.txt
└── README.md
```

## How to run

Run each script from the repo root (so the `data/` and `images/` relative paths resolve):

```bash
pip install -r requirements.txt
python scripts/01_overview_donut.py
python scripts/02_class_gender_bar.py
python scripts/03_age_violin.py
python scripts/04_fare_stripbox.py
python scripts/05_family_size_bar.py
python scripts/06_class_gender_treemap.py
```

Each script writes its chart to `images/`.

## The story, in six charts

| # | Chart | Question it answers |
|---|---|---|
| 1 | Donut / KPI | What's the headline number? (42% overall survival) |
| 2 | Grouped bar | How did gender and class compare, side by side? |
| 3 | Violin plot | Did age matter, and how — not just on average? |
| 4 | Strip + boxplot (log scale) | Did money/fare matter? |
| 5 | Annotated bar | Any non-obvious, non-linear patterns? (family size "Goldilocks" effect) |
| 6 | Treemap | What's the combined picture of all three factors at once? |

The sequence is deliberate: overall picture → two-factor comparison → distribution
shape → a skewed variable → a non-linear twist → a combined multi-factor view —
mirroring how you'd explain a complex result out loud, one layer at a time.

## Key insights

- Overall survival rate: **41.5%**
- Gender was the strongest factor: women **73.9%** vs. men **22.0%**
- Class mattered too: First **64.1%** vs. Third **26.0%**
- Children (0–12) survived at **57.4%**, well above average
- Survivors paid a median fare of **£26** vs. **£13** for non-survivors
- Family size showed a **"Goldilocks" effect**: groups of 2–4 fared best (55–71%); solo travelers and groups of 5+ fared worse

## Tools

Python 3, pandas, matplotlib, seaborn, squarify (treemap layout).

## Author

Shridhar Raj S — B.E. Computer Science Engineering, Priyadarshini Engineering College
