# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 10:53:14 2019

@author: Himanshu Rathore
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('deliveryfleet.csv')
features = dataset.iloc[ :, 1: ].values

#Scatter all these data points
plt.scatter(features[:,0], features[:,1])
plt.show()

# Fitting K-Means to distinguish urban and rural drivers
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 0)
pred_cluster_1 = kmeans.fit_predict(features)

# Distinguishing Urban and Rural Drivers
urban_drivers = features[ pred_cluster_1 == 0 ]
rural_drivers = features[ pred_cluster_1 == 1 ]

# Again K-Means to further distinguish speeding drivers
kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

# Visualizing made clusters to accordingly labeling
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Urban_speed_follower')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Urban_speed_Unfollower')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Rural_speed_follower')
plt.scatter(features[pred_cluster == 3, 0], features[pred_cluster == 3, 1], c = 'yellow', label = 'Rural_speed_Unfollower')
plt.title('Clusters of datapoints')
plt.xlabel('Distance')
plt.ylabel('Speed')
plt.legend()
plt.show()

Urban_speed_follower = features[pred_cluster == 0]
Urban_speed_Unfollower = features[pred_cluster == 1]
Rural_speed_follower = features[pred_cluster == 2]
Rural_speed_Unfollower = features[pred_cluster == 3]

