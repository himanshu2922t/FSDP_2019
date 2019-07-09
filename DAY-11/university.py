# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 14:35:13 2019

@author: Himanshu Rathore
"""

import csv
university_data = {}
with open('University_data.csv','rt') as university_file:
    university_reader = csv.DictReader(university_file,delimiter = ',')
    for row in university_reader:
        if row['University Name'] in university_data:
            university_data[ row['University Name'] ] += int( row['GRE Score'] )
        else:
            university_data[ row['University Name'] ] = int( row['GRE Score'] )

from matplotlib import pyplot as plt
university = list(map(lambda x: x ,university_data.keys()))
GRE_score = list(map(lambda x: x ,university_data.values()))
explode = tuple(map(lambda x: 0.1 if x==min(GRE_score) else 0.0, GRE_score))

plt.pie(GRE_score, explode=explode, labels=university, autopct='%.0f%%', startangle=0)
plt.axis('equal')
plt.show()