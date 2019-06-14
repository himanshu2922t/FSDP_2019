# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:45:44 2019

@author: Himanshu Rathore
"""
from bs4 import BeautifulSoup
import requests

#Get Source Code of page
url = "https://www.icc-cricket.com/rankings/mens/team-rankings/t20i"
source = requests.get(url).text

#Parsing of HTML data
soup = BeautifulSoup(source,"lxml")

#Get table from html data
ranking_table = soup.find('table', class_='table')

#Get columns' data into lists
rank = []
team = []
weighted_matches = []
points = []
rating = []

for row in ranking_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 5:
        rank.append(cells[0].text.strip())
        team.append(cells[1].text.strip())
        weighted_matches.append(cells[2].text.strip())
        points.append(cells[3].text.strip())
        rating.append(cells[4].text.strip())
    
col_name = ["Rank","Team","Weighted Matches","Points","Rating"]
col_data = dict(zip(col_name,[rank,team,weighted_matches,points,rating]))

#Creating Dataframe and storing data in csv
import pandas 
final_data = pandas.DataFrame(col_data) 
final_data.to_csv("icc_cricket.csv", index=False)