# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:50:49 2019

@author: Himanshu Rathore
"""

# Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv('bluegills.csv')
features = dataset.iloc[:, 0:1].values
labels = dataset.iloc[:, -1].values

# visualizing the dataset
plt.scatter(features, labels)

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(features, labels)

# Visualising the Linear Regression results
plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg.predict(features), color = 'blue')
plt.title('Linear Regression')
plt.xlabel('Age')
plt.ylabel('Length')
plt.show()

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 2)
features_poly = poly_object.fit_transform(features)
quad_reg = LinearRegression()
quad_reg.fit(features_poly, labels)

# Visualising the Polynomial Regression results
plt.scatter(features, labels, color = 'red')
plt.plot(features, quad_reg.predict(poly_object.fit_transform(features)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Age')
plt.ylabel('Length')
plt.show()

print ("Predicting result with Polynomial Regression")
print (quad_reg.predict(poly_object.transform(5)))

print ("Predicting result with Linear Regression")
print (lin_reg.predict(5))