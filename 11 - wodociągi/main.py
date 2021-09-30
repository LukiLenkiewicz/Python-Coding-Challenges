import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("wodociagi.txt", sep=';')

districts = []

for id_ in data["KodKlienta"]:
    districts.append(id_[-3:])

data["Dzielnica"] = districts

df = pd.DataFrame(data.loc[:, "I":"Dzielnica"])
iterate_through = list(df.columns)
iterate_through = iterate_through[:-1]

values = []

for i in iterate_through:
    table = df.groupby('Dzielnica')[i].sum().reset_index()
    table = table.to_numpy()
    table = [row[1] for row in table]
    values.append(table)
