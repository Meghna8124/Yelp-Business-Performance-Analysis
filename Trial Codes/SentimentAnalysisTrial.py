import re
from textblob import TextBlob as Tb

def get_sentiment(text):
    analysis = Tb(text) 
        # set sentiment 
    #analysis.sentiment_assessments(text)
    if analysis.sentiment.polarity > 0: 
        return 'positive'
    elif analysis.sentiment.polarity == 0: 
        return 'neutral'
    else: 
        return 'negative'
#To get subjectivity    
def get_sub(text):
    analysis= Tb(text)
    
    return analysis.sentiment.subjectivity
#add clean text to function    
myFile= open('essayTrial.txt', 'r')
text= myFile.readline() 
Sentence= text
Sentiment= get_sentiment(Sentence)

# =============================================================================
# #Trial
# text='Pizza was amazing but burgers was horrible.'
# Subjectivity= get_sub('Today is Monday.')
# analysis = Tb(text) 
# analysis.sentiment_assessments
# 
# from nltk.corpus import wordnet
# #for np in analysis.noun_phrases:
#  #   print (np)
# words= text.split()
# for w in words:
#     syns = wordnet.synsets(w)
#     print(w, syns[0].lexname().split('.')[0]) if syns else (w, None)
#     
# print(analysis.tags) 
# =============================================================================
