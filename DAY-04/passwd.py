# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:13:00 2019

@author: Himanshu Rathore
"""
import csv

try:
    file = open('passwd', mode='rt')
    file_content = csv.reader(file, delimiter=':')
    
    out_dict = {}
    
    for line in file_content:
        if line[0][0] == '#':
            raise Exception
            next(file_content)
        out_dict[ line[0] ] = line[2] 
    
    for user_name, ID in sorted(out_dict.items()):
        print(user_name,ID)
    
except Exception:
    print("This line is a comment")
    
finally:
    file.close()