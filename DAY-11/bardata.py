# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:57:25 2019

@author: Himanshu Rathore
"""
import csv
from collections import Counter
with open('bardata.csv', mode='rt') as survey_file:
    survey_content = csv.DictReader(survey_file, delimiter=',')
    language_counter = Counter()
    for row in survey_content:
        language_counter.update( row['LanguagesWorkedWith'].split(';') )

print('Most Popular Languages: ',language_counter.most_common(10))
languages=[]
popularity=[]
for item in language_counter.most_common(10):
    languages.append(item[0])
    popularity.append(item[1])
    
from matplotlib import pyplot as plt
plt.barh(languages, popularity)
plt.ylabel("Programming Language", fontsize=12)
plt.xlabel("Votes", fontsize=12)
plt.title("StackOverFlow Survey", fontsize=16)
plt.yticks(languages, fontsize=10)
plt.show()