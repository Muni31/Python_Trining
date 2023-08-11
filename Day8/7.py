# 	Add following features in above example. 

# a.      Create different processes for API call and File writing. 

# b.      Manage communication between processes. 

# 	(Hint: Use queue for inter-process communication) 


# Note: Add flow-diagram of final application in repo


import requests
import json
import logging
import concurrent.futures
import multiprocessing
import queue

# Global lists and queue
lat_lon_list = []
output_list = []
lat_lon_queue = queue.Queue()

# Global lock for file access
file_lock = multiprocessing.Lock()

def get_geocoding_info(lat, lon):
    url = f"https://open.mapquestapi.com/geocoding/v1/reverse?key=YOUR_API_KEY&location={lat},{lon}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        logging.error(f"Failed to retrieve geocoding information for Lat:{lat}, Lon:{lon}")
        return None

def parse_and_store_info(data):
    if not data or "results" not in data or len(data["results"]) == 0:
        return

    location_info = data["results"][0]["locations"][0]
    street = location_info.get("street", "")
    postal_code = location_info.get("postalCode", "")
    country = location_info.get("adminArea1", "")
    city = location_info.get("adminArea5", "")

    info = {
        "street": street,
        "postalCode": postal_code,
        "country": country,
        "city": city
    }
    output_list.append(info)

def process_lat_lon():
    while True:
        try:
            lat, lon = lat_lon_queue.get(timeout=1)
        except queue.Empty:
            break

        data = get_geocoding_info(lat, lon)
        if data:
            parse_and_store_info(data)

def write_to_file(output_list, output_file):
    # Acquire the lock and write output to the file
    with file_lock:
        with open(output_file, "w") as file:
            for info in output_list:
                json.dump(info, file)
                file.write("\n")

def fetch_lat_lon_list(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.splitlines()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to retrieve the latitude and longitude list. Error: {e}")
        return None

if __name__ == "__main__":
    logging.basicConfig(filename="7.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    # Read the latitude and longitude list from the provided URL
    url = "https://dpaste.com/F9VQFPJED.txt"
    lat_lon_list = fetch_lat_lon_list(url)
    if lat_lon_list is None:
        exit("Failed to fetch the latitude and longitude list.")

    # Get user input for max no. of threads for API call and writing to the file
    max_threads_api = int(input("Enter the max number of threads for API call: "))
    max_threads_write = int(input("Enter the max number of threads for writing to the file: "))

    # Enqueue latitude and longitude entries to the queue
    for lat_lon_entry in lat_lon_list:
        lat, lon = lat_lon_entry.split(",")
        lat_lon_queue.put((lat.strip(), lon.strip()))

    # Create separate processes for API calls and writing to the file
    api_process = multiprocessing.Process(target=process_lat_lon)
    write_process = multiprocessing.Process(target=write_to_file, args=(output_list, "output.json"))

    # Start the processes
    api_process.start()
    write_process.start()

    # Wait for both processes to finish
    api_process.join()
    write_process.join()
