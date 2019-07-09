# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:12:45 2019

@author: Himanshu Rathore
"""

import pandas as pd

# Reading the dataset
dataset = pd.read_csv("breast_cancer.csv")

# Check if any NaN values in dataset
dataset.isnull().any(axis=0)

# Filling NaN values with most frequent values
from scipy import stats
dataset['G'] = dataset['G'].fillna(stats.mode(dataset['G'])[0][0])

# Making Features and Labels
features = dataset.iloc[:, 1:-1].values
labels = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 0)

# Fitting Kernel SVM to the Training set
# kernels: linear, poly and rbf
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# Model Score
score = classifier.score(features_test,labels_test)


prediction = classifier.predict([[6,2,5,3,9,4,7,2,2]])
if prediction == 4:
    print("Woman has Malignant tumor")
else:
    print("Woman has Benign tumor")
