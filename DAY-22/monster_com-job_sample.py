# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:48:55 2019

@author: Himanshu Rathore
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('monster_com-job_sample.csv')

# Check if any NaN values in dataset
dataset.isnull().any(axis=0)

# Filling NaN values in organization column
dataset['organization'] = dataset['organization'].fillna("Missing")

# Searching location in Organization
import re
row_no = 0
for i in dataset.iloc[:,[8,9]].values:
    organization = i[1]
    if re.search(r'\,\s*\w{2}\s*\d*',str(organization)):
        dataset.iloc[ row_no, 9 ] = dataset.iloc[ row_no, 8 ]
        dataset.iloc[ row_no, 8 ] = organization
    row_no += 1

# Searching only pin in loc
for i in dataset.iloc[:,[8]].values:
    if re.findall(r'\d',str(i)):
        
# 
        
