# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:13:30 2019

@author: Himanshu Rathore
"""
import requests
url = "http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=ultra&apiKey=07ca862e0b339dd56245"
current_USD_in_INR = requests.get(url).json()['USD_INR']
print("Equivalent INR: ",round( float(input("Enter USD: "))*current_USD_in_INR, 2) )