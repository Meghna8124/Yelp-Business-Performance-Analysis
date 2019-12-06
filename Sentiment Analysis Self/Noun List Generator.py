#importing libraries
import re
import pandas as pd 
import numpy as np
import csv
import os
from textblob import TextBlob as Tb
import nltk

def sent_splitter(review):
    review= review.replace('\n', '')
    Temp= review.split('.')
    Sentences=[]
    for i in range(0, len(Temp)):
        if Temp[i]=='' or Temp[i]==' ':
            pass
        else:
            analysis = Tb(Temp[i]) 
            Sentences.append([Temp[i], analysis.sentiment.polarity])
    return Sentences

def pos_tag(text):
    
    is_noun = lambda pos: pos[:2] == 'NN'
    tokenized = nltk.word_tokenize(text)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
    
    return nouns

def list_creator(filename):        
    file= 'Review Sentiments_'+filename
    data=[]
    Sent_List=[]
    Noun_List=[]
    Final_List=[]
    with open(file, 'r') as my_file:
        reader= csv.reader(my_file)
        data= list(reader)
    my_file.close()
    
    
    for i in range(0, len(data)):
        Sent_List.append([data[i][0], sent_splitter(data[i][1])])
    print(Sent_List)
    
    for i in range(0, len(data)):
        Noun_List.append([data[i][0], pos_tag(data[i][1])])
    print(Noun_List)
    
    #Create final list    
    for i in range(0, len(Sent_List)):
        Final_List.append([Sent_List[i][0], Sent_List[i][1], Noun_List[i][1]])

    return Final_List
# =============================================================================
#     file1= 'Review_Sentences_'+filename
#     with open(file1, 'w', newline='') as csvfile:
#         filewriter = csv.writer(csvfile)
#         for i in range(0, len(Final_List)):
#             filewriter.writerows([Final_List[i][0], Final_List[i][1], Final_List[i][2]])
#     csvfile.close()
# 
# =============================================================================
    
#Creating files
with open('Review_Sentences_Our data.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile)
        filewriter.writerow(['Business Id', 'Sentences', 'Nouns'])
csvfile.close()
with open('Review_Sentences_Final Data.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile)
        filewriter.writerow(['Business Id', 'Sentences', 'Nouns'])
csvfile.close()

#calling functions
F1= list_creator('Our data.csv')
F2= list_creator('Final Data.csv')
