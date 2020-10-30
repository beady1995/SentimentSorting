# # Sentiment Analysis

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd


analyzer=SentimentIntensityAnalyzer()


df=pd.read_csv('Merged.csv').iloc[:,-2:]
sentiment=[]
for i in range(df.shape[0]):
    text=df.iloc[i,1]
    sentiment.append(analyzer.polarity_scores(text))
df=df.join(pd.DataFrame(sentiment),how='outer')



df.head()





print('The worst company idea is :')
print(df.iloc[df['neg'].idxmax()])



print('The best company idea is :')
print(df.iloc[df['pos'].idxmax()])

