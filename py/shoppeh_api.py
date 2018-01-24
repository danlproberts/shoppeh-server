# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 16:31:29 2017

@author: daniel.roberts
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import jw_search as jw
import hm_search as hm
import importlib

app = Flask(__name__)
CORS(app)

@app.route('/search_api')
def api_root():
    
    query = request.args.get('query')

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

    return jsonify(data)

@app.route('/reload')
def reload():
    
    importlib.reload(jw)
    importlib.reload(hm)
    
    return "<h3>Modules reloaded!</h3>"

if __name__ == '__main__':
    app.run(port="5000")
    #app.run(host="192.168.1.239", port="8080")