# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 16:31:29 2017

@author: daniel.roberts
"""

import jw_search as jw
import hm_search as hm
import sys, json

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    # Since our input would only be having one line, parse our JSON data from that
    return lines[0]

def main():
    #get our data as an array from read_in()
    lines = read_in()

    with open('test2.txt', 'w') as filelog:

        filelog.write(str(lines))

    '''

    # Sum  of all the items in the providen array
    total_sum_inArray = 0
    for item in lines:
        total_sum_inArray += item

    #return the sum to the output stream
    print (total_sum_inArray)

    '''
    query = str(lines)

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

    sys.stdout.write(json.dumps(data))
    print (json.dumps(data))

if __name__ == '__main__':
    main()
