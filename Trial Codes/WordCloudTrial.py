from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 

#Add relevant words/ parts of text
myFile= open('essayTrial.txt', 'r')
text= myFile.readline() 
comment_words= text
stopwords = set(STOPWORDS)
wordcloud = WordCloud(width = 800, height = 800, 
               background_color ='black', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words) 
  
# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 