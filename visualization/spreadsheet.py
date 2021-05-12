import pandas as pd


df = pd.read_json(input('json file с сущ. и прил: '))
df.to_excel("nounsandadjectives.xlsx") # сохраняем таблицу xl с распределением употребления прилагательных с существительным по годам

