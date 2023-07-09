# Write a program that takes two inputs from user and perform division of a by input2. 
# (Exception handling)  
#         - Handle invalid integers 
#         - Handle divide by zero exception.  (Use Nested exception, else and finally)      
#         ========================================= 
#   Input: 
#    Enter Intput1: 10 
#   Enter Input2: 0 
#     Output: 
#    Divide by Zero exception...!!! 
#    Hi, I'm from finally...!!! 
#         ========================================== 
#         Input: 
#    Enter Input1: 10 
#   Enter Input2: abc 
#     Output: 
# 	Invalid inputs, expected integers...!!! 
#  Hi, I'm from finally...!!! 
def q3():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
    except ValueError:
        print("Invalid inputs, expected integers")
    else:
        try:
            result = a / b
            print(f"The result of {a} divided by {b} is: {result}")
        except ZeroDivisionError:
            print("Divide by Zero exception")
    finally:
        print("Hi, I'm from finally")
q3()
