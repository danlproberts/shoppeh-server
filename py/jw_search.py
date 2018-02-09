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

    ipt = str(ipt).replace(" ", "+")
    return ipt

def presentable(txt):

    result = txt.lower().title().strip()

    return result


def searcher(search_term):

    result_list = []

    if search_term == "":

        return "Sorry!"

    else:

        count = 0

        i = 0

        while i <= int(count):

            website = 'http://www.jackwills.com'

            search_web = website + '/search?q='

            url = search_web + query(search_term) + '&sz=48&start=' + str(i) + '&pmin=0&pmax=1000'

            data = requests.get(url)

            soup = BeautifulSoup(data.content, 'html.parser')

            with open('test.txt', 'w') as filelog:

                filelog.write(str(type(search_term)))
                filelog.write(query(search_term))
                filelog.write(url)

                for j in query(search_term):

                    filelog.write('\n' + str(ord(j)))

                filelog.close()

            html_count = soup.find('div', class_="search-results-count").get_text()

            #html_count = soup.find('div', class_="search-results-count").h1.get_text()

            count = html_count[html_count.find("(") + 1:html_count.find(")")].replace(",", "")


            html_list = soup.find_all('li', class_="grid-tile")

            for item in html_list:

                item_dict = {}

                html_product = item.find('a', class_="name-link").text

                html_product_href = item.find('a', class_="name-link").get('href')

                html_product_img = item.find('img').get('src')

                try:
                    html_product_des = item.find('div', class_="visually-hidden gifthits-description").p.get_text()

                    item_dict["des"] = html_product_des

                except AttributeError:

                    pass

                item_dict["name"] = presentable(html_product)
                item_dict["link"] = website + str(html_product_href)
                item_dict["img"] = html_product_img
                item_dict["retailer"] = "JW"


                result_list.append(item_dict)

            i += 48

        result_list.append({"searchcount": count})

        #print ("JW - " + count)





   # for products in html_list:



    #print ("Update! " + str(datetime.fromtimestamp(time.mktime(time.gmtime()))))

    return result_list
