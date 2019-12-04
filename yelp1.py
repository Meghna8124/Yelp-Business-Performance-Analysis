# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 19:12:22 2019

@author: Vedika Bansal
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import operator

# open input file: 
ifile = open('yelp_dataset/business.json', encoding = 'utf-8') 
# read the first 70k entries
# set to -1 to process everything
stop = 100000
all_data = list()
stateList = []
businesses = []
categoryList = []
favBusiness = []

our_business_id = 'SBNucLXc9dQP6VBj__XOmQ'
our_business_categories = []

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
        if state== 'AZ':
            favBusiness.append(ID)
            categoryList.append(categ)
            
    if ID== our_business_id:
        our_business_categories = categ
        
    stateList.append(state)
    businesses.append(ID)
    # add to the data collected so far
    
    all_data.append([ID, name, state])
    
fav_data = []
    
# create the DataFrame
df = pd.DataFrame(all_data, columns=['ID' ,'name','state'])
print(df)
ifile.close()
# df.to_hdf('revie20ws.h5','reviews')

# get the count of categories overlapping with our business
size = len(favBusiness)
similarity_count = []
similar_business_id = []
for i in range(size):
    id_category = []
    id_category = categoryList[i]
    count = 0
    for j in id_category:
        for k in our_business_categories:
            if k==j:
                count += 1
    similarity_count.append(count)
    similar_business_id.append(favBusiness[i])

# dictionary with business and their corresponding similar categories count
    
similarity_dict = dict(zip(similar_business_id, similarity_count))
    
sorted_similarity_dict = sorted(similarity_dict.items(), key=operator.itemgetter(1))

# collecting business ids with max similarity
threshold = 50
max_similar_businesses = []
max_counts = []
for x in list(reversed(list(sorted_similarity_dict)))[1:threshold+1]:
    max_similar_businesses.append(x[0])


all_data = []
ifile = open('yelp_dataset/review.json', encoding = 'utf-8') 
stop = 100000
data_reviews = list()
reviews = []
businessIdOfReview = []
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
    
    if ID in max_similar_businesses:
        print(ID)
        reviews.append(text)
        businessIdOfReview.append(ID)
        all_data.append([ID, text])
 
    
# create the DataFrame
df = pd.DataFrame(all_data, columns=['ID','text'])
#print(df)
        
res = dict(zip(reviews, businessIdOfReview))
Counter(res.values())


# df.to_hdf('revie20ws.h5','reviews')
ifile.close()  