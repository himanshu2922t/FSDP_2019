# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:39:05 2019

@author: Himanshu Rathore
"""

import json
import requests

Host = "http://13.127.155.43/api_v0.1/post"

data = {"Phone_Number":"7073001938","Name":"Himanshu","College_Name":"PIET","Branch":"CS"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )


def get_method():
    response = requests.get("http://13.127.155.43/api_v0.1/get?Phone_Number=7073001938")
    return response

print (get_method().text)