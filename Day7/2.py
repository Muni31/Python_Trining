# Create a json file in following format.    { 
# ""folder_name_1"": [filename_1, filename_2, ....], 
# ""folder_name_2"": [filename_1, filename_2, .... 
#         . 
#         . 
#         . 
#     } 

# Fetch folder names from the json file and if that folder is present in a predefined location using
# pythonic way then check if all the files mentioned in the list is present or not. 

import os
import json

def check_folders_and_files(json_path, predef_loc):
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)

    for folder_name, file_list in data.items():
        folder_path = os.path.join(predef_loc, folder_name)

        if os.path.exists(folder_path):
            print(f"Folder '{folder_name}' exists at location: {folder_path}")
            for filename in file_list:
                file_path = os.path.join(folder_path, filename)
                if os.path.exists(file_path):
                    print(f"  File '{filename}' exists at location: {file_path}")
                else:
                    print(f"  File '{filename}' does not exist at location: {file_path}")
        else:
            print(f"Folder '{folder_name}' does not exist at location: {folder_path}")

if __name__ == "__main__":
    json_path = "folders_and_files.json"
    predef_loc = "D:\Python-Training\Day7" 
    check_folders_and_files(json_path, predef_loc)
