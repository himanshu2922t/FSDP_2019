# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 16:54:41 2019

@author: Himanshu Rathore
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('data.csv')

# Identifying countries from where artwork comes
dataset = dataset.dropna(subset = ['Country', 'Artist Role'])
countries =  dataset['Country'][ dataset['Artist Role'] == "Artist" ]
countries = list(set(list(countries)))