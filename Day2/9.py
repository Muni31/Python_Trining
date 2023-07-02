# 9) Write a program to input 2 strings, and merge the reversed strings separated with $. 

# Sample strings : abcd wxyz 

# Output string: dcba$zyxw 
s1=input("enter the string 1 : ")
s2=input("Enter the string 2 : ")
a=s1[::-1]
b=s2[::-1]
print(a+"$"+b)