# Write a Python program to add 'ing' at the end of a given string (length should be at 	least 3).  
# 	If the given string already ends with 'ing' then add 'ly' instead. 
# If the string length of 	the given string is less than 3, leave it unchanged. 
stri=input("Enter a String : ")
if len(stri)<3:
    print(stri)
elif stri[-3:]=="ing":
    print(stri+"ly")
else:
    print(stri+"ing")