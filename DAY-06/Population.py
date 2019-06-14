# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:50:50 2019

@author: Himanshu Rathore
"""

import csv
output_dict = {}
with open("population.csv", mode='rt') as file:
    file_content = csv.DictReader(file, delimiter=',')
    
    for row in file_content:
        if "India, "+row['State or union territory'] in output_dict.keys():
            output_dict["India, "+ row['State or union territory'] ] += int(row['Population'].replace(",",""))
        else: 
            output_dict["India, "+ row['State or union territory'] ] = int(row['Population'].replace(",",""))
print(output_dict)