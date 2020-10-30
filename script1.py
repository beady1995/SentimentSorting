import pandas as pd
import os
top = os.getcwd()
RootOutput = top
df=pd.DataFrame(columns=['Name','Purpose'])
for root,dirs,files in os.walk(top):
    for file in files:
        if file.endswith(".csv"):
            print(file)
            df1=pd.read_csv(file).iloc[:,-2:]
            df1.columns=['Name','Purpose']
            df=df.append(df1)


df.to_csv('Merged.csv')

