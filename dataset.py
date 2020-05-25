import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

df = pd.read_csv("product_reviews_dirty.csv", index_col=0)

df.head()

print("There are {} observations and {} features in this dataset. \n".format(df.shape[0],df.shape[1]))

print("There are {} types of wine in this dataset such as {}... \n".format(len(df.category.unique()),", ".join(df.category.unique()[0:5])))

print("There are {} countries producing wine in this dataset such as {}... \n".format(len(df.text.unique()), ", ".join(df.text.unique()[0:5])))

df[["text", "product_name","rating"]].head()

# Groupby by country
country = df.groupby("product_name")

# Summary statistic of all countries
country.describe().head()

country.mean().sort_values(by="rating",ascending=False).head()

# Start with one review:
text = df.category[0]

# lower max_font_size, change the maximum number of word and lighten the background:
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
