import json
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline


data = json.dumps({}) 
data = json.loads(data)

years = [i['year'] for i in data["UNKN"]]
variables = [i['variable'] for i in data['UNKN']]

df = pd.DataFrame({'dates':years, 'values':variables})


df = df.sort_values(by='dates')
#plt.bar(dates, values)

from google.colab import files

df.to_csv('name.csv')
files.download('name.csv')
