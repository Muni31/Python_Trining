# Write a function to find larger of three numbers.  
# 	- Functions for each possible way we can find larger of three numbers. 
def larger(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        print(f"{num1} is larger than {num2,num3}")
    elif num2>=num1 and num2>=num3:
        print(f"{num2} is larger than {num1,num3}")
    else:
        print(f"{num3} is larger than {num2,num1}")

num1=int(input("Enter num1 : "))
num2=int(input("Enter num2 : "))
num3=int(input("Enter num3 : "))
larger(num1,num2,num3)