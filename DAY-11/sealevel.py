# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:22:43 2019

@author: Himanshu Rathore
"""
# Reading csv file 
import csv
with open ('sealevel.csv', mode='rt') as file:
    file_content = csv.DictReader(file, delimiter=',')
    years = []
    sealevel_increases = []
    for row in file_content:
        years.append( int(row['Year']) )
        sealevel_increases.append( float(row['inches']) )

# Ploting Line Graph
from matplotlib import pyplot as plt
plt.plot( years, sealevel_increases, label='Sea_Level')
plt.axis(min(years), max(years), min(sealevel_increases), max(sealevel_increases))
plt.title('Sea Level Rise')
plt.xlabel('Sea Level increment')
plt.ylabel('Year')
plt.legend()
plt.show()