# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 11:17:01 2019

@author: Himanshu Rathore
"""

# Importing the libraries
import pandas as pd
import numpy as np

# What male and female look for in his/her partner
# Reading Dataset
req_dataset = pd.read_csv('Dating_Data.csv', engine='python', 
                      usecols=['gender', 'attr1_1', 'sinc1_1', 'intel1_1', 
                               'fun1_1', 'amb1_1', 'shar1_1'])
# Checking NaN values
req_dataset.isnull().any(axis=0)

# Handling NaN values
req_dataset = req_dataset.dropna()

# Results
male_look_for =  np.argmax( req_dataset.iloc[:,1:][ req_dataset['gender'] == 1 ].mean() )
female_look_for =  np.argmax( req_dataset.iloc[:,1:][ req_dataset['gender'] == 0 ].mean() )


# How often they go out
# Reading Dataset
req_data_2 = pd.read_csv('Dating_Data.csv', engine='python', usecols=['go_out'])
# Checking NaN values
req_data_2.isnull().any(axis=0)

# Handling NaN values
req_data_2 = req_data_2.dropna()

# Results
mean_counts = req_data_2.iloc[:,0].value_counts()
how_often = np.argmax( mean_counts )


# In which activity they are intereseted 
# Reading Dataset
req_data_3 = pd.read_csv('Dating_Data.csv', engine='python', usecols=range(50,67))
# Checking NaN values
req_data_3.isnull().any(axis=0)

# Handling NaN values
req_data_3 = req_data_3.dropna()

# Results
mean_counts_2 = req_data_3.iloc[:,:].mean()
most_interseted = np.argmax( mean_counts_2 )

