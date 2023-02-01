import sys

import matplotlib.pyplot as plt
import pandas
import seaborn as sns

pandas.options.mode.chained_assignment = None

tournament: str = ""
try:
    tournament = sys.argv[1].split("/")[-1]
except IndexError:
    print("No tournament (e.g. 2019-06-01_nationals_c) provided!")
    exit(1)

table = pandas.read_csv(f"https://duosmium.org/results/csv/{tournament}/")
table = table[table.columns[8:]]
corr = table.corr(numeric_only=True)
plt.figure(figsize=(20, 20))
sns.heatmap(data=corr, annot=True, cmap="YlGnBu").get_figure().savefig(f"corr.png")
