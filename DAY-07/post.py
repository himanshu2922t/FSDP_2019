# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:30:05 2019

@author: Himanshu Rathore
"""

import json
import requests

Host = "https://enjp693gkcxhl.x.pipedream.net/post"

data = {"user_name":"Himanshu","city":"Jaipur","mobile":"7073001938","Department":"CS","Year":2}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )
