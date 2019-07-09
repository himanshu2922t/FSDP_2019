# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 17:10:30 2019

@author: Himanshu Rathore
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importing the dataset
dataset = pd.read_csv('iq_size.csv')

#Check if any NaN values in dataset
dataset.isnull().any(axis=0)

#prepare the data to train the model
features = dataset.iloc[:, 1:].values  
labels = dataset.iloc[:, 0].values

import statsmodels.api as sm
#adds a constant column to input data set
features = sm.add_constant(features)

features_opt = features[:,:]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
while (True):
    regressor_OLS = sm.OLS(endog = labels,exog =features_opt).fit()
    p_values = regressor_OLS.pvalues
    if p_values.max() > 0.05 :
        features_opt = np.delete(features_opt, p_values.argmax(),1)
    else:
        break
regressor_OLS.summary()
    
# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(features_opt, labels)

# Visualising the Linear Regression results
plt.scatter(features_opt, labels, color = 'red')
plt.plot(features_opt, lin_reg.predict(features_opt), color = 'blue')
plt.title('Linear Regression')
plt.xlabel('Brain Size')
plt.ylabel('IQ')
plt.show()

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 11)
features_poly = poly_object.fit_transform(features_opt)
quad_reg = LinearRegression()
quad_reg.fit(features_poly, labels)

# Visualising the Polynomial Regression results
plt.scatter(features_opt, labels, color = 'red')
plt.plot(features_opt, quad_reg.predict(poly_object.fit_transform(features_opt)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Brain Size')
plt.ylabel('IQ')
plt.show()

print ("Predicting result with Polynomial Regression")
print (quad_reg.predict(poly_object.transform(90)))