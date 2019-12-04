import re
import pandas as pd 
import numpy as np
import csv
import matplotlib.pyplot as plt 
import os
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
from nltk.stem import PorterStemmer

from textblob import TextBlob as Tb
from wordcloud import WordCloud, STOPWORDS 

#defining global values


#Cleaning the file
def remove_unwanted_characters(review):
    uwc= '#$%&\'\"()*+-=:<>{}[]^@~`?/\_|'
    #Add Cuss words to remove
    #uwc2= "List of Words"
    for i in range(0, len(uwc)):
        review=review.replace(uwc[i], "")
    #review= review.replace(uwc2, "")
    review.lower()
    return review

#Remaoval of stop words
def stop_words(review):
    stop_words = set(stopwords.words('english')) 
    review = " ".join([word for word in review.split() if word not in stop_words]) #Joins word list w/o stop words with a space " "
    return review

#Get sentiment of overall review
def get_sentiment(text):
    analysis = Tb(text) 
    if analysis.sentiment.polarity > 0: 
        return 'positive'
    elif analysis.sentiment.polarity == 0:         
        return 'neutral'
    else:         
        return 'negative'
#Getting review score
def rev_score(text):
    score=0
    total=0
    analysis = Tb(text) 
    if analysis.sentiment.polarity > 0: 
        score=score+0.75
        total=total+1
    elif analysis.sentiment.polarity == 0:         
        total=total+1
    else:         
        score=score-0.5
        total=total+1
      
    return (score/total)*5
    
with open('Final Data.csv', 'r') as my_file:    
    reader = csv.reader(my_file)
    reviews = list(reader)
    
    for review in reviews:
        review[2]= remove_unwanted_characters(review[2])
    
    for review in reviews:
        review[2]=stop_words(review[2])
        
    with open('Cleaned_final_data.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile)
        filewriter.writerows(reviews)
    csvfile.close()
    
my_file.close()

#Sentiment Analysis of entire review
sentiments=[]
with open('Final Data.csv', 'r') as my_file:    
    reader = csv.reader(my_file)
    reviews = list(reader)
    
    for review in reviews:
        Sentiment= get_sentiment(review[2])
        sentiments.append(Sentiment)
        
    with open('Review_sentiments.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile)
        for i in range(0, len(sentiments)):
            filewriter.writerow([reviews[i][1], reviews[i][2], sentiments[i]])
    csvfile.close()
my_file.close()
rating=0
#Getting sentiment score of individual business
with open('Review_sentiments.csv', 'r') as my_file:
    reader = csv.reader(my_file)
    reviews = list(reader)
    
    for review in reviews:
        rating=rev_score(review[2])

my_file.close()

print(rating)    
