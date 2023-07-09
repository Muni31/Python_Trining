# Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.(Regex) 
import re

def xyz(date):
    date_pattern = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
    match = re.match(date_pattern, date)
    if match:
        year = match.group(1)
        month = match.group(2)
        day = match.group(3)
        converted_date = f"{day}-{month}-{year}"
        return converted_date
    else:
        return None

def abc():
    date = input("Enter the date (yyyy-mm-dd): ")
    converted_date = xyz(date)
    if converted_date:
        print(f"Converted date: {converted_date}")
    else:
        print("Invalid date format.")

abc()
