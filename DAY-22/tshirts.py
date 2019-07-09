# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:24:54 2019

@author: Himanshu Rathore
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('tshirts.csv')
features = dataset.iloc[ :, 1: ].values

#Scatter all these data points
plt.scatter(features[:,0], features[:,1])
plt.show()

# Fitting K-Means 
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

# Distinguishing  Clusters for T-Shirt Size
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green')
plt.title('Clusters of datapoints')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.show()

# Standardizing Sizes
standard_small = kmeans.cluster_centers_[2]
standard_medium = kmeans.cluster_centers_[0]
standard_large = kmeans.cluster_centers_[1]
