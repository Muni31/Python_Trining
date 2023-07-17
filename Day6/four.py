import logging
import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import RequestException
from requests.packages.urllib3.util.retry import Retry

class MapQuest:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'http://www.mapquestapi.com/geocoding/v1'
        self.session = self._create_session()

    def _create_session(self):
        session = requests.Session()
        retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
        session.mount('http://', HTTPAdapter(max_retries=retries))
        return session

    def _make_request(self, method, endpoint, **params):
        try:
            params['key'] = self.api_key
            response = self.session.request(method, f'{self.base_url}/{endpoint}', params=params)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            logging.error(f'Request failed: {str(e)}')
            return None

    def get_address(self, address):
        endpoint = 'address'
        params = {'location': address}
        return self._make_request('GET', endpoint, **params)

    def post_address(self, data):
        endpoint = 'address'
        return self._make_request('POST', endpoint, json=data)

    def get_reverse(self, lat, lng):
        endpoint = 'reverse'
        params = {'location': f'{lat},{lng}'}
        return self._make_request('GET', endpoint, **params)


import four

def demo():
    api_key = 'fLZuA48mCjjHapdUF142crBTsQeCwuNz'
    client = four.MapQuest(api_key)


    address = '1600 Amphitheatre Parkway, Mountain View, CA'
    response = client.get_address(address)
    print(response)


    data = {
        'locations': [
            {'street': '123 Main St', 'city': 'Seattle', 'state': 'WA'},
            {'street': '456 Broadway', 'city': 'New York', 'state': 'NY'}
        ]
    }
    response = client.post_address(data)
    print(response)


    lat, lng = 37.7749, -122.4194
    response = client.get_reverse(lat, lng)
    print(response)

if __name__ == '__main__':
    demo()