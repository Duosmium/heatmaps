import requests
import sys
import pandas
import seaborn as sns
import matplotlib.pyplot as plt

pandas.options.mode.chained_assignment = None

tournament: str = ""
try:
    tournament: str = sys.argv[1].split("/")[-1]
except IndexError:
    print("No tournament (e.g. 2019-06-01_nationals_c) provided!")
    exit(1)
r = requests.get(f"https://duosmium.org/results/{tournament}")
comp_yaml = requests.get(f"https://duosmium.org/data/{tournament}.yaml")
p = pandas.read_html(r.text)
table = p[0]
table = table[table.columns[4:-1]]
table.columns = [c.replace("  Td", "").replace("  T", "") for c in table.columns]
corr = table.corr()
plt.figure(figsize=(20, 20))
sns.heatmap(data=corr, annot=True, cmap="YlGnBu").get_figure().savefig(f"{tournament}_corr.png")
