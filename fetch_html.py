# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:11:27 2020

@author: kuldeep sharma
"""

import os
import time
import requests
import sys

def retrieve_aqi_html():
    for year in range(2013,2019):
        for month in range(1,13):
            if (month<10):
                url="http://en.tutiempo.net/climate/0{}-{}/ws-421820.html".format(month,year)
                
            else:
                url="http://en.tutiempo.net/climate/{}-{}/ws-421820.html".format(month,year)
                
            texts=requests.get(url)
            text_utf=texts.text.encode('utf=8')
        
            if not os.path.exists("Data/Html_Data/{}".format(year)):
                os.makedirs("Data/Html_Data/{}".format(year))
            with open("Data/Html_Data/{}/{}.html".format(year,month),"wb") as output:
                output.write(text_utf)
            
        sys.stdout.flush()
        
if __name__=="__main__":
    start_time=time.time()
    retrieve_aqi_html()
    stop_time=time.time()
    print("Time take  {}".format(stop_time-start_time))
    
 
        