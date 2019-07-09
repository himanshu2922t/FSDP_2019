# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 12:40:52 2019

@author: Himanshu Rathore
"""

# Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
from apyori import apriori

# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)


# Preparing Data
transactions = []

for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20) if str(dataset.values[i,j])!= 'nan'])


# Training Apriori on the dataset

results = list( apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4) )


for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
    
    
# Top 10 edibles

import itertools
edibles = list(itertools.chain(*transactions))

from collections import Counter
occurence_count = Counter(edibles)

top_10_edibles = dict(occurence_count.most_common(10))

# Ploting Bar Graph
index = [0,1,2,3,4,5,6,7,8,9]
label = top_10_edibles.keys()
counts = top_10_edibles.values()
plt.bar(index, counts)
plt.xlabel('Edible', fontsize=15)
plt.ylabel('No of selling', fontsize=15)
plt.xticks(index, label, fontsize=10, rotation=90)
plt.title('Market Basket Most Selled Edibles')
plt.show()
