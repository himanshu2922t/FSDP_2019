# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:12:30 2019

@author: Himanshu Rathore
"""
import matplotlib.pyplot as plt

girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.plot(girls_grades, grades_range, 'gs', color='red', label='Girls')
plt.scatter(boys_grades, grades_range, marker='o', color='green', label='Boys')
plt.legend()
plt.show()