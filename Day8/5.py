import requests
import threading
import logging
import json
import os
import time

# Step 3: Set up logging
logging.basicConfig(filename='5.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Step 4: Define the function to make API calls and parse data
def get_location_info(lat_lon, file_lock):
    lat, lon = lat_lon
    api_key='fLZuA48mCjjHapdUF142crBTsQeCwuNz'
    url = f'https://open.mapquestapi.com/geocoding/v1/reverse?key={api_key}={lat},{lon}'
    max_retries = 3

    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response_json = response.json()

            if response_json['info']['statuscode'] == 0:
                location_info = response_json['results'][0]['locations'][0]

                street = location_info.get('street', '')
                postalcode = location_info.get('postalCode', '')
                city = location_info.get('adminArea5', '')
                country = location_info.get('adminArea1', '')

                data = {
                    'street': street,
                    'postalcode': postalcode,
                    'city': city,
                    'country': country
                }

                output_file = f"{street.replace(' ', '_')}_{postalcode}.json"
                with file_lock:
                    with open(output_file, 'w') as f:
                        json.dump(data, f)

                logging.info(f"Successfully processed: {lat},{lon}")
                break
            else:
                logging.error(f"Error processing: {lat},{lon} - {response_json['info']['messages']}")
        except Exception as e:
            logging.error(f"Error processing: {lat},{lon} - {str(e)}")
            time.sleep(2 ** attempt)  # Exponential backoff for retries

# Step 5: Read latitude and longitude list from the provided URL
def get_lat_lon_list(url):
    response = requests.get(url)
    lines = response.text.strip().split('\n')
    lat_lon_list = [tuple(line.strip().split(',')) for line in lines if line.strip()]
    return lat_lon_list

if __name__ == "__main__":
    url = "https://dpaste.com/F9VQFPJED.txt"
    lat_lon_list = get_lat_lon_list(url)

    # Step 6: Create and start the threads
    file_lock = threading.Lock()  # A lock to be used for writing to the output.json file
    max_threads = 10  # Set the maximum number of concurrent threads

    threads = []
    for lat_lon in lat_lon_list:
        thread = threading.Thread(target=get_location_info, args=(lat_lon, file_lock))
        threads.append(thread)
        thread.start()

        # Limit the number of concurrent threads
        while threading.active_count() >= max_threads:
            time.sleep(1)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Step 7: Save the output data to output.json
    def combine_json_files():
        all_data = []
        for file_name in os.listdir('.'):
            if file_name.endswith('.json'):
                with open(file_name, 'r') as f:
                    data = json.load(f)
                    all_data.append(data)

        with open('output.json', 'w') as f:
            json.dump(all_data, f)

    combine_json_files()


	