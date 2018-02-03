# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 16:31:29 2017

@author: daniel.roberts
"""

import jw_search as jw
import hm_search as hm
import sys, json

def main():
    #get our data as an array from read_in()

    query = sys.argv[1]

    if query == "":

        data = [{'name': "Please enter a search term!"}]

    else:

        jw_result = jw.searcher(query)
        hm_result = hm.searcher(query)

        jw_count = jw_result.pop(-1)
        hm_count = hm_result.pop(-1)

        count = int(jw_count["searchcount"]) + int(hm_count["searchcount"])

        result = jw_result + hm_result

        print (count)

        result.append(str(count))

        if result == []:

            data = [{'name': "Sorry, no results!"}]

        else:

            data = result

    print (json.dumps(data))

if __name__ == '__main__':
    main()
