import numpy as np 
import pandas as pd 

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

data = pd.read_csv('reviews.csv')
print len(data)

selectword = set(STOPWORDS)
sentimentimg = WordCloud(stopwords=selectword, background_color='white',).generate(" ".join([i for i in data['comments']]))
plt.imshow(sentimentimg)
plt.axis("off")
plt.title("Airbnb Reactions")
plt.show()


