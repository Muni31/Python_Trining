# Write a program to take two integers  as input. Print those two integers as output and 	then call a function to swap those two integers. 
# 	- Write function for each possible way to swap two integers 

def swap(a,b):
    c=a
    a=b
    b=c
    print(f"swapped numbers are a={a},b={b}")
    
a=int(input("Enter the number a  : "))
b=int(input("Enter the number b  : "))
print (f"the values of a={a} and b={b} ")
swap(a,b)