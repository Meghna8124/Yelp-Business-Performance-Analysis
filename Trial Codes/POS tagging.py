# from textblob lib import TextBlob method 
from textblob import TextBlob 
myFile= open('essayTrial.txt', 'r')
text= myFile.readline() 
  
# create a textblob object 
blob_object = TextBlob(text) 
  
# Part-of-speech tags can be accessed  
# through the tags property of blob object.' 
  
# print word with pos tag. 
print(blob_object.tags) 