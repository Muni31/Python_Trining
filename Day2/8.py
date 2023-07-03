# 8) Write a program to make a new string from a given string in which the xth character should be
# replaced with yth character, where x,y and string should be taken as input from user.
# (x,y should be less than length of string) 

# Input String: Helper 

# x= 2 

# y= 4 

# Output: Hpleer 
a=input("Enter a string : ")
x=int(input("Enter the value of 'x' : "))
y=int(input("Enter the value of 'y' : "))
if x>=len(a) or y>=len(a):
    print("Invalid input 'x' or 'y'")
else:
    b=list(a)
    b[x-1]=a[y-1]
    b[y-1]=a[x-1]
    just=''.join(b) 
print(just)