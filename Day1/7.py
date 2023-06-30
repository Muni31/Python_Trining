# Write a Python program to get a string made of the first 2 and the last 2 chars from a 	given a string.  
# 	If the string length is less than 2, return "Empty String"
def empy(a):
    if len(a)<2:
        print("Empty String")
    else:
        first_two=a[:2]
        last_two=a[-2:]
        print(first_two+last_two)
ino=input("Enter the string  : ")
empy(ino)
