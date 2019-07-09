# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:32:51 2019

@author: Himanshu Rathore
"""
import pandas as pd

#imports the CSV dataset using pandas
dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')

#Check if any NaN values in dataset
dataset.isnull().any(axis=0)

#prepare the data to train the model
features = dataset.iloc[:, 0].values  
labels = dataset.iloc[:, 1:].values # using two labels

# train the algo
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression() 
features = features.reshape(-1,1)
regressor.fit(features, labels) 

# prediction for Day 10
regressor.predict(10)