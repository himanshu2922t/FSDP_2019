# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 08:22:57 2019

@author: Himanshu Rathore
"""

import pandas as pd
data = pd.read_csv('training_titanic.csv')

total_survived = pd.DataFrame(data['Survived'].value_counts())[1:].iloc[:,-1].tolist()[0]

total_died = data['PassengerId'].count() - total_survived

survival_rate = pd.DataFrame(data['Survived'].value_counts(normalize=True))*100

survival_data = data.groupby(['Sex','Survived'])
survival_data.size()
survival_list = survival_data.size().tolist()
survival_data = pd.DataFrame(list(zip(['female_Survived','female_Died','male_Survived','male_Died']\
                                      ,survival_list)), columns=['passenger','count'])

data['Age'] = data['Age'].fillna(data['Age'].mean())
child = list(map(lambda age: 1 if age<18 else 0, data['Age'].tolist()))
data['Child'] = child
survived_data = data[data['Survived']==1]
child_survival_rate = pd.DataFrame(survived_data['Child'].value_counts(normalize=True))*100