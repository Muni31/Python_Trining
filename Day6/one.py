# Write a python program using "requests" (3rdparty) and "urllib3" (in-built) module to integrate 
# "PhishTank" service.  
# PhishTank is a free online service, which stores information about Phishing URLs. 
# The Input to the program should be a URL. The output should tell us whether the input url is Phishing URL
# or not. 

# Implement a demo function which will utilize the functionality. 
 
# Input: http://www.travelswitchfly.com/ 	 
# Output: "http://www.travelswitchfly.com/" is a phishing URL.  
# PhishTank API - https://www.phishtank.com/api_info.php 

# POST Endpoint - https://checkurl.phishtank.com/checkurl/index.php 

import requests
import urllib3

def check_url(url):
    endpoint = 'https://checkurl.phishtank.com/checkurl/index.php'
    params = {
        'format': 'json',
        'url': url
    }

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    try:
        response = requests.post(endpoint, params=params, verify=False)
        result = response.json()

        if result['valid']:
            if result['phish_detail_page']:
                return f"{url} is a phishing URL"
            else:
                return f"{url} is not a phishing URL"
        else:
            return "Invalid response from PhishTank service"

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def home():
    url = input("Enter the URL to check: ")
    result = check_url(url)
    print(result)

home()
