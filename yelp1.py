# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 19:12:22 2019

@author: Vedika Bansal
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
# open input file: 
ifile = open('yelp_dataset/business.json', encoding = 'utf-8') 
# read the first 70k entries
# set to -1 to process everything
stop = 70000
all_data = list()
stateList = []
businesses = []
categoryList = []
favBusiness = []

#to mine relevant business IDs by filtering through categories
fCategories = "Restaurants, Pizza, Cafes, Bars & Pubs, Bars, Burgers, Diners, Breakfast & Brunch, Chinese, Chicken Wings, Italian,  Desserts, Caterers, Bakeries, Waffles, American (Traditional), Soup, Comfort food, Sandwiches, Steak houses, Glutten free, French, Fast food, Salad, Bagels, Coffee and tea, Vegan, Lounges, Speciality food, Sea food, Food trucks, Mexican, Tapas, Asian Fusion"
favourableCategories = fCategories.split(", ")

for i, line in enumerate(ifile):
    if i%10000==0:
        print(i)
    if i==stop:
        break    
    # convert the json on this line to a dict
    data = json.loads(line)
    # extract what we want

    ID = data['business_id']
    name = data['name']
    state = data['state']
    categories = data['categories']

    if categories is not None:
        categ = categories.split(",")
        #categList.append(categ)
    else:
        categ = "xxx"
    print(categ)
    flag = 0 
    for item in categ :
        if item in favourableCategories:
            print(item)
            flag = flag + 1
            break
    if flag!=0:    
        favBusiness.append(ID)
        categoryList.append(categ)

  
    stateList.append(state)
    businesses.append(ID)
    # add to the data collected so far
    
    all_data.append([ID, name, state])

fav_data = []
    
# create the DataFrame
df = pd.DataFrame(all_data, columns=['ID' ,'name','state'])
print(df)

# df.to_hdf('revie20ws.h5','reviews')
ifile.close()

ifile = open('yelp_dataset/review.json', encoding = 'utf-8') 
stop = 70000
data_reviews = list()
reviews = []
for i, line in enumerate(ifile):
    
    if i%10000==0:
        print(i)
    if i==stop:
        break    
    # convert the json on this line to a dict
    data = json.loads(line)
    # extract what we want
    ID = data['business_id']
    text = data['text']
    reviews.append(text)
    # add to the data collected so far
    all_data.append([ID, text])
# create the DataFrame
df = pd.DataFrame(all_data, columns=['ID','text'])
print(df)

# df.to_hdf('revie20ws.h5','reviews')
ifile.close()    
