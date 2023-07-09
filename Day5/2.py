# # .Write a program that takes a number from user. If negative number is provided then raises an exception.
# (Exception handling) 
# ======================================= 
# Input: 
#Enter a positive integer: -5 
# output : 
#That is a negative number!  
def q2():
    try:
        number = int(input("Enter a +ve integer: "))
        if number < 0:
            raise ValueError("That is -ve number!")
        else:
            print("The number is valid.")
    except ValueError as e:
        print(e)


q2()
