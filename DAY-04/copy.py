# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:49:38 2019

@author: Himanshu Rathore
"""
import csv
with open('words.txt', mode='rt') as file, open('words_copy.txt', mode='wt') as file_copy:
    r = csv.reader(file, delimiter=':')
    w = csv.writer(file_copy, delimiter='\t')    
    for record in r:
        if len(record) > 1:
            w.writerow((record[0], record[2]))