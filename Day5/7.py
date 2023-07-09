#  Write a python program to find Urls from a given string.(Regex) 
import re


def xyz(text):
    url_pattern = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    urls = re.findall(url_pattern, text)
    return urls

def abc():
    text = input("Enter the text : ")
    urls = xyz(text)
    if urls:
        print("Found URLs:")
        for url in urls:
            print(url)
    else:
        print("No URLs found in given text")

abc()
