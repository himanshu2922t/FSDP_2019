# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:55:06 2019

@author: Himanshu Rathore
"""

import re
# input emails from user
email_list = list()
while True:
    email = input("Enter a email: ")
    if not email:
        break
    email_list.append(email)

# storing valid email list 
valid_email_list = []
for email in email_list:
    # matching the requirements for valid email
    if re.match(r'^[a-z0-9_-]+@[a-z0-9]+\.[a-z]{2,4}', email):
        valid_email_list.append(email)
    
print("Valid emails in alphabatical order:",sorted(valid_email_list))