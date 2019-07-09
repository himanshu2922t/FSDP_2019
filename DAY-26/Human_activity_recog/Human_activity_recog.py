# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 10:51:11 2019

@author: Himanshu Rathore
"""

# importing Libraries
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score 

# Preparing the Dataset
dataset_train = pd.read_csv("train.csv") 
features_train = dataset_train.iloc[:,:-2]
labels_train = dataset_train.iloc[:,-1]

dataset_test = pd.read_csv("test.csv")
features_test = dataset_test.iloc[:,:-2]
labels_test = dataset_test.iloc[:,-1]


# Applying PCA for dimension reduction
from sklearn.decomposition import PCA
pca = PCA(n_components = 60)
features_train = pca.fit_transform(features_train)
features_test = pca.transform(features_test)


# TRAINNING AND MAKING PREDICTIONS


# 1 using decision tree approach
from sklearn.tree import DecisionTreeClassifier
  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)
labels_pred = classifier.predict(features_test)

#   Evaluate Score 
score_1 = accuracy_score(labels_test, labels_pred)


# 2 using random forest approach
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier.fit(features_train, labels_train)  
labels_pred = classifier.predict(features_test)

#   Evaluate Score 
score_2 = accuracy_score(labels_test, labels_pred)


# 3 Using logistic Regression
from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()
classifier.fit(features_train, labels_train)
labels_pred = classifier.predict(features_test)

#   Evaluate Score 
score_3 = accuracy_score(labels_test, labels_pred)


# 4 Using KNN Approach
from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) 
classifier.fit(features_train, labels_train)
labels_pred = classifier.predict(features_test)

#   Evaluate Score 
score_4 = accuracy_score(labels_test, labels_pred)


# Plotting Bar Graph of scores
labels = ('Decision Tree', 'Random Forest', 'Logistic Regression', 'k-NN')
x_index = [0,1,2,3]
performance = [score_1,score_2,score_3,score_4]
plt.bar(x_index, performance, width = 0.5, align='center', alpha=1.0)
plt.xticks(x_index, labels, rotation=45)
plt.ylabel('Accuracy Score')
plt.title('Human Activity Recognision') 
plt.show()
