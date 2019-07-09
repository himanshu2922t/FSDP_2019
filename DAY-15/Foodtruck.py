# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:02:04 2019

@author: Himanshu Rathore
"""

import pandas as pd
import matplotlib.pyplot as plt

#imports the CSV dataset using pandas
dataset = pd.read_csv('Foodtruck.csv')

#explore the dataset
print (dataset.shape)
print (dataset.ndim)
print (dataset.head())
print (dataset.describe())

#check data types for each column
print (dataset.dtypes)

#Check if any NaN values in dataset
dataset.isnull().any(axis=0)

# Check for outlier values
plt.boxplot(dataset.values) # Here outliers but size of data smaller -> No Action

# Finding relationship manually
dataset.plot(x='Population', y='Profit', style='o')
plt.title('Population Vs Profit')
plt.xlabel('Population of City')
plt.ylabel('Profit Earned')
plt.show()

#prepare the data to train the model
features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, 1].values 

# Train-Test split
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)

# train the algo
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train)

# Prediction for Jaipur
print(regressor.predict(3.073))

# Performance Measure
# making predictions
labels_pred = regressor.predict(features_test) 
# comparing actual values with predicated values
df = pd.DataFrame({'Actual': labels_test, 'Predicted': labels_pred})  
print (df) 
