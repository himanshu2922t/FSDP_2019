# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:11:29 2019

@author: Himanshu Rathore
"""

import csv

with open('passwd', mode='r') as source_file:
    source_content = csv.reader(source_file, delimiter=':')
    
    with open('passwd_with_tab', mode='w') as destination_file:
        desination_content = csv.writer(destination_file, delimiter="\t")
        for row in source_content:
            desination_content.writerow([row[0],row[2]])
