#importing libraries
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

#Cleaning the file
def remove_unwanted_characters(review):
    uwc= '!#$%&\'\"()*+-=,:;<>{}[]^@~`.?/1234567890\_|'
    #Add Cuss words to remove
    uwc2= "List of Words"
    for i in range(0, len(uwc)):
        review=review.replace(uwc[i], "")
    review= review.replace(uwc2, "")
    review.lower()
    return review

#Remaoval of stop words
def stop_words(review):
    stop_words = set(stopwords.words('english')) 
    review = " ".join([word for word in review.split() if word not in stop_words]) #Joins word list w/o stop words with a space " "
    return review

#Lemmatization of the data
def lemmatization(review):
    lemmatizer= WordNetLemmatizer() 
    ps= PorterStemmer()          
    review = " ".join([lemmatizer.lemmatize(word, pos= 'v') for word in review.split()])#Joins lemmatized verbs list with a space " "
    review = " ".join([ps.stem(word) for word in review.split()]) #Joins lemmatized words list with a space " "
    return review

#Get sentiment of overall review
def get_sentiment(text):
    analysis = Tb(text) 
        # set sentiment 
    if analysis.sentiment.polarity > 0: 
        return 'positive'
    elif analysis.sentiment.polarity == 0: 
        return 'neutral'
    else: 
        return 'negative'

with open('Final_data.csv', 'r') as my_file:    
    reader = csv.reader(my_file)
    reviews = list(reader)
    
    for review in reviews:
        review[1]= remove_unwanted_characters(review[1])
    
    for review in reviews:
        review[1]=stop_words(review[1])
        
    for review in reviews:
        review[1]=lemmatization(review[1])
    
    with open('Cleaned_final_data.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile)
        filewriter.writerows(reviews)
    csvfile.close()
    
my_file.close()

#Business_Id from user in real time
Business_ID= ""
