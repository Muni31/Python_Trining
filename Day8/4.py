import requests
import json
import logging
from concurrent.futures import ThreadPoolExecutor

# Function to make API call and get information from Mapquest API
def get_location_info(lat, lon):
    api_key='fLZuA48mCjjHapdUF142crBTsQeCwuNz'
    url = f'https://open.mapquestapi.com/geocoding/v1/reverse?key={api_key}={lat},{lon}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['results'][0]['locations'][0]
    else:
        logging.error(f'Error while fetching information for {lat}, {lon}. Status Code: {response.status_code}')
        return None

# Function to store parsed information in a separate file
def store_parsed_info(info, filename):
    with open(filename, 'w') as file:
        json.dump(info, file)

def main():
    # Read latitude and longitude list from the provided URL
    lat_lon_url = 'https://dpaste.com/F9VQFPJED.txt'
    response = requests.get(lat_lon_url)
    if response.status_code != 200:
        print(f'Error while fetching latitude and longitude list. Status Code: {response.status_code}')
        return

    # Extract latitudes and longitudes from the response
    lat_lon_list = [line.strip().split(',') for line in response.text.split('\n') if line.strip()]

    # Configure logging
    logging.basicConfig(filename='4.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

    with ThreadPoolExecutor(max_workers=5) as executor:
        # Fetch information for each latitude and longitude concurrently
        for i, (lat, lon) in enumerate(lat_lon_list):
            info = get_location_info(lat, lon)
            if info:
                filename = f'{info["street"]}_{info["postalCode"]}.json'
                store_parsed_info(info, filename)
                print(f'Record {i + 1}: Information stored in {filename}')

if __name__ == '__main__':
    main()
