#  Print all the files as INFO level log which are present in the folder. 
# Print all the files as CRITICAL level log which are not present in the folders in log files.

import os
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='info_logs.log',
                    filemode='w')

def info_files(folder_path):
    for filename in os.listdir(folder_path):
        logging.info(f"INFO: File found: {filename}")

def critical_files(folder_path, log_folder_path):
    log_files = os.listdir(log_folder_path)
    for filename in os.listdir(folder_path):
        if filename not in log_files:
            logging.critical(f"CRITICAL: File not found: {filename}")

folder_path = 'D:\Python-Training\Day7'
log_folder_path = 'D:\Python-Training\info_logs.log'

info_files(folder_path)
critical_files(folder_path, log_folder_path)
