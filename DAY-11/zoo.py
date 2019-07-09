# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:30:41 2019

@author: Himanshu Rathore
"""

import csv
zoo_data = {}
with open('zoo.csv','rt') as zoo_file:
    zoo_reader = csv.DictReader(zoo_file,delimiter = ',')
    for row in zoo_reader:
        if row['animal'] in zoo_data:
            zoo_data[ row['animal'] ] += int( row['water_need'] )
        else:
            zoo_data[ row['animal'] ] = int( row['water_need'] )
print(zoo_data)

animals = list(map(lambda x: x ,zoo_data.keys()))
total_water_need = list(map(lambda x: x ,zoo_data.values()))

from matplotlib import pyplot as plt
plt.bar(animals, total_water_need, width=0.8, align='center')
plt.xlabel("Animal", fontsize=12)
plt.ylabel("Total Water Need", fontsize=12)
plt.title("Zoo Survey", fontsize=16)
plt.xticks(animals, fontsize=10, rotation=45)
plt.show()