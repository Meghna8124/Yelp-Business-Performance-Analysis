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

def cleaner(filename):    
    with open(filename, 'r') as my_file:    
        reader = csv.reader(my_file)
        reviews = list(reader)
    
        for review in reviews:
            review[1]= remove_unwanted_characters(review[1])
            
        for review in reviews:
            review[1]=stop_words(review[1])
        file_new= 'Cleaned_'+filename
        with open(file_new, 'w', newline='') as csvfile:
            filewriter = csv.writer(csvfile)
            filewriter.writerows(reviews)
        csvfile.close()
    
    my_file.close()

#Sentiment Analysis of entire review
def analyzer(filename):
    sentiments=[]
    with open(filename, 'r') as my_file:    
        reader = csv.reader(my_file)
        reviews = list(reader)
    
        for review in reviews:
            Sentiment= get_sentiment(review[2])
            sentiments.append(Sentiment)
        file_new= 'Review Sentiments_'+filename
        with open(file_new, 'w', newline='') as csvfile:
            filewriter = csv.writer(csvfile)
            for i in range(0, len(sentiments)):
                filewriter.writerow([reviews[i][1], reviews[i][2], sentiments[i]])
        csvfile.close()
    my_file.close()
#Getting scores
#Self
def calculator_self(filename):
    score=0
    total=0
    with open(filename, 'r') as my_file:
        reader= csv.reader(my_file)
        reviews= list(reader)
        for i in range(0, len(reviews)):
            s= reviews[i][2]
            if s=='positive': 
                score=score+1
                total=total+1
            elif s=='negative':         
                score=score-1
                total=total+1        
            else:      
                total=total+1
    my_file.close()
    return (score/total)*5
#Competetors    
def calculator_comp(filename):
    rating1=0
    rating2= 0
    rating3= 0
    list1= []
    comp1=[]
    comp2=[]
    comp3=[]
    #Getting sentiment score of individual business
    with open(filename, 'r') as my_file:
        reader = csv.reader(my_file)
        reviews = list(reader)
        for i in range(0, len(reviews)):
            list1.append([reviews[i][0], reviews[i][2]])
        for i in range(1, 35):
            comp1.append([list1[i][0], list1[i][1]])
        for i in range(35, 59):
            comp2.append([list1[i][0], list1[i][1]])
        for i in range(59, 116):
            comp3.append([list1[i][0], list1[i][1]])
    my_file.close()
    
    score=0
    total=0
    for i in range(0, len(comp1)):
        s= comp1[i][1]
        if s=='positive': 
            score=score+1
            total=total+1
        elif s=='negative':         
            score=score-1
            total=total+1        
        else:      
            total=total+1
        
    rating1= (score/total)*5
    
    score=0
    total=0
    for i in range(0, len(comp2)):
        s= comp2[i][1]
        if s=='positive': 
            score=score+1
            total=total+1
        elif s=='negative':         
            score=score-1
            total=total+1        
        else:      
            total=total+1
        
    rating2= (score/total)*5
    
    score=0
    total=0
    for i in range(0, len(comp3)):
        s= comp3[i][1]
        if s=='positive': 
            score=score+1
            total=total+1
        elif s=='negative':         
            score=score-1
            total=total+1        
        else:      
            total=total+1
        
    rating3= (score/total)*5

    list1.clear()
    list1.append([comp1[1][0], rating1])
    list1.append([comp2[1][0], rating2])
    list1.append([comp3[1][0], rating3])
    return list1
    
#Calling all functions
cleaner('Our data.csv')
cleaner('Final Data.csv')
analyzer('Our data.csv')
analyzer('Final Data.csv')
rating_self= calculator_self('Review Sentiments_Our data.csv')
rating_comp_list= calculator_comp('Review Sentiments_Final Data.csv')


