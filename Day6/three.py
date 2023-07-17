# Create a simple API Web Server (using flask) similar to PhishTank API service.  
# PhishTank is a free online service, which stores information about Phishing URLs. 
# It should have one POST endpoint named "checkurl" which accepts the following Request Body Parameters  

# and returns the response with following Response Fields.  
#Implement a demo function which will utilize the functionality 

# Request Body Parameter: 
# - url: encoded url 
# - format: “json” | “xml” 

# Response Fields: 
# - url: URL passed in input 
# - is_valid: yes | no | unknown 

# Server will have one static hard-coded csv file with two columns "url" and "is_valid".  
# For each request, check if csv file contains entry for that url,  
# if yes then return is_valid field accordingly else return is_valid as unknown. 

# Sample CSV File: 
# url, is_valid 
# https://google.com, yes 
# https://dummy.com, no 

# PhishTank API: https://www.phishtank.com/api_info.php 

import os
import csv
from flask import Flask, request, jsonify

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(script_dir, 'urls.csv')



app = Flask(__name__)

csv_file = 'D:/Python-Training/Day6/urls.csv'
urls = {}
with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        urls[row['url']] = row['is_valid']

@app.route('/checkurl', methods=['POST'])
def check_url():
    url = request.form.get('url')
    form = request.form.get('format')

    if url:
        is_valid = urls.get(url, 'unknown')
        response = {
            'url': url,
            'is_valid': is_valid
        }

        if form == 'xml':
            xml_response = '<response>'
            xml_response += f'<url>{url}</url>'
            xml_response += f'<is_valid>{is_valid}</is_valid>'
            xml_response += '</response>'
            return xml_response, 400, {'Content-Type': 'application/xml'}
        else:
            return jsonify(response)
    else:
        return 'URL parameter is missing.', 400

def demo():
    app.run(port=8000)

demo()

