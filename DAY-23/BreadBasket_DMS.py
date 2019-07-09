# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 10:46:17 2019

@author: Himanshu Rathore
"""

# Importing the libraries
import pandas as pd
from apyori import apriori
from matplotlib import pyplot as plt

# Dataset Loading
dataset = pd.read_csv('BreadBasket_DMS.csv')


# Ploting Pie Chart of top 15 selling items
most_selled_15 = dataset["Item"].value_counts().head(15)

labels = list(most_selled_15.index)
slices = list(most_selled_15)
plt.pie(slices,labels=labels, wedgeprops={'edgecolor':'black'})
plt.axis('equal')
plt.show()



# Preparing data

#transactions = []
#for i in set(dataset['Transaction']):
#    transactions.append( list(dataset['Item'][dataset['Transaction']==i]) )
# 
#counter = 0
#for i in transactions:
#    transactions[ counter ]  = list(set(transactions[counter]).discard("None"))
#    counter +=1
#

dataset = dataset[dataset["Item"]!= "NONE"]

def cart(values):
    return list(set(values))

transactions = list(dataset.groupby("Transaction")["Item"].apply(cart))


# Training Apriori on the dataset
results = list( apriori(transactions, min_support = 0.0025, min_confidence = 0.2, min_lift = 3) )

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


