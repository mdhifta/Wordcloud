from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Youtube04-Eminemdata.csv", encoding ="latin1")

words_data = " "
stopwords = set(STOPWORDS)

for i in df.CONTENT:
    i = str(i)

    tokens = i.split()

    for j in range(len(tokens)):
            tokens[j] = tokens[j].lower()

    for text in tokens:
            words_data = words_data + text + " "

wrc = WordCloud(width = 900, height = 950, background_color = 'red',
            stopwords = stopwords, min_font_size = 10).generate(words_data)

plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wrc)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()
