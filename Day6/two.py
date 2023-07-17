# implement the retry mechanism in the task 1 (PhishTank) with backoff time for the fault tolerance 
# of request. 
# Use built-in “requests.packages.urllib3.util.retry.Retry” 

import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

def check_url(url):
    endpoint = 'https://checkurl.phishtank.com/checkurl/index.php'
    params = {
        'format': 'json',
        'url': url
    }

    retry_strategy = Retry(
        total=3,
        backoff_factor=0.5,
        status_forcelist=[500, 502, 503, 504],
        method_whitelist=["POST"]
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    http = requests.Session()
    http.mount("https://", adapter)

    try:
        response = http.post(endpoint, params=params, verify=False)
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
