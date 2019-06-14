# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:06:55 2019

@author: Himanshu Rathore
"""
import requests
#input from user
city = input("Enter city name: ")

#url computing
base_url = "http://api.openweathermap.org/data/2.5/weather"
query = "?q="+city
api_key = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = base_url + query + api_key

#get json data in response
response = requests.get(url)
#convert json data into python datatype
data_dict = response.json()

#temperature calculation
print("Temperature:",round(data_dict['main']['temp'] - 273.15, 2),"degree celcius")

#coord calculation
print("Latitude: {} and Longitude: {}".format( data_dict['coord']['lat'], data_dict['coord']['lon'] ))

#weather condition
print("Weather Condition:",data_dict['weather'][0]['main'])

#wind speed
print("Wind Speed:",data_dict['wind']['speed'],"m/s")

#Sun set and rise
from datetime import datetime

SunRise_time = datetime.fromtimestamp(data_dict['sys']['sunrise'])
SunSet_time = datetime.fromtimestamp(data_dict['sys']['sunset'])

print("Sunrise time: {} and Sunset time: {}".format( SunRise_time,SunSet_time ))