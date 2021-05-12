import json
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline


data = json.dumps({}) # вставить json файл с частотностями частей речи по годам
data = json.loads(data)

years = [i['year'] for i in data["noun"]]
variables = [i['variable'] for i in data['noun']]

df = pd.DataFrame({'dates':years, 'values':variables})
df['dates']  = [pd.to_datetime(i) for i in df['dates']]

print(df.sort_values(by='dates'))
plt.bar(dates, values)
