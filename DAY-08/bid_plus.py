# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 16:42:26 2019

@author: Himanshu Rathore
"""

from  selenium import webdriver
from time import sleep

url = "https://bidplus.gem.gov.in/bidlists"

browser = webdriver.Chrome("C:\\Users\\Himanshu Rathore\\..Himanshu\\Softwares\\chromedriver_win32\\chromedriver.exe")
browser.get(url)

sleep(3)

bid_num_list = []
items_list = []
quantity_req_list = []
dept_details_list = []
start_date_list = []
start_time_list = []
end_date_list = []
end_time_list = []
pdf_name_list = []

for i in range(1,11):
    
    bid_num = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text.replace("\n"," ")
    bid_num_list.append(bid_num)
    
    items = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text.replace("\n"," ")
    items_list.append(items)
    
    quantity_req = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span').text.replace("\n"," ")
    quantity_req_list.append(quantity_req)
    
    dept_details = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text.replace("\n"," ")
    dept_details_list.append(dept_details)
    
    start_date = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text[:10]
    start_date_list.append(start_date)
    
    start_time = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text[11:]
    start_time_list.append(start_time)
    
    end_date = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text[:10]
    end_date_list.append(end_date)
    
    end_time = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text[11:]
    end_time_list.append(end_time)
    
    pdf_button = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a')
    pdf_button.click()
    
    import os 
    downloaded_items_list = os.listdir("C:\\Users\\Himanshu Rathore\\Downloads\\")
    for i in downloaded_items_list:
        if i.endswith('.pdf') and i.startswith('GeM'):
            pdf_name_list.append(i)
            os.remove('C:\\Users\\Himanshu Rathore\\Downloads\\'+i)
            break
    
from collections import OrderedDict
col_name = ["Bid Number","Items","Quantity Required","Department Name and Address","Start Date","Start Time","End Date","End Time","Pdf Name"]
col_data = OrderedDict(zip(col_name,[bid_num_list,items_list,quantity_req_list,dept_details_list,start_date_list,start_time_list,end_date_list,end_time_list,pdf_name_list]))

import pandas as pd
final_data = pd.DataFrame(col_data) 
final_data.to_csv("bid_plus.csv", index=False)

browser.quit()