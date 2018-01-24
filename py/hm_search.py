# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 20:33:39 2017

@author: Daniel
"""

from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime

def query(ipt):
    
    ipt.replace(" ", "+")
    
    return str(ipt)

def presentable(txt):
    
    result = txt.lower().title().strip()
    
    return result


def searcher(search_term):
    
    result_list = []
    
    if search_term == "":
        
        return "Sorry!"
    
    else:        
        
        count = 41
        
        i = 40
        
        while i <= int(count):
        
            website = 'https://www2.hm.com'
            
            search_web = website + '/en_gb/search-results.html?q=' 
            
            url = search_web + query(search_term) + '&sort=stock&offset=0&page-size=' + str(i)
            
            data = requests.get(url)
            
            soup = BeautifulSoup(data.content, 'html.parser')
            
            count = soup.find('span', class_="total-count").get_text()
            
            #html_count = soup.find('div', class_="search-results-count").h1.get_text()
            
            #count = html_count[html_count.find("(") + 1:html_count.find(")")].replace(",", "")
            
            
            html_list = soup.find_all('div', class_="grid col-3")
            
            
            for item in html_list:
                
                item_dict = {}
                
                html_product = item.find('a', class_="product-item-link").get('title')
                
                html_product_href = item.find('a', class_="product-item-link").get('href')
                
                html_product_img = item.find('img', class_="product-item-image").get('src')
                
                    
                item_dict["name"] = presentable(html_product)
                item_dict["link"] = website + str(html_product_href)
                item_dict["img"] = "http:" + html_product_img
                item_dict["retailer"] = "HM"
                
                
                result_list.append(item_dict)
                
            i += 40
            
        result_list.append({"searchcount": count})
        
        print ("HM - " + count)
            
        
        
        
    
   # for products in html_list:
        
        
    
    #print ("Update! " + str(datetime.fromtimestamp(time.mktime(time.gmtime()))))
    
    return result_list