import pandas as pd
from collections import Counter

df=pd.read_csv('Merged.csv').iloc[:,-2:]
df

text=''
for i in range(df.shape[0]):
    text+=' '+df.iloc[i,1]

Counter =Counter(text.split())

most_occur = Counter.most_common(10)

print('The 10 most comment words is :')
print(most_occur)

