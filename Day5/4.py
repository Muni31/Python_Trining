# Write a program that takes integer age from the user if age is under 18, raise custom exception 
# UnderAgeError and if age is over 40, raise custom exception OverAgeError. (Exception handling) 
#         ========================== 
# Input:  
#  Enter age: 10 
# Output: 
# You are UnderAge by 8 years..!! 
#         ========================== 
# Input:  
# Enter age: 45 
#Output: 
#  You are OverAge by 5 years..!! 

class UnderAgeError(Exception):
    pass
class OverAgeError(Exception):
    pass
def q4():
    try:
        age = int(input("Enter your age : "))
        if age < 18:
            raise UnderAgeError(f"You are UnderAge by {18 - age} years")
        elif age > 40:
            raise OverAgeError(f"You are OverAge by {age - 40} years")
        else:
            print("You have a valid age")
    except ValueError:
        print("Invalid input, expected an integer age")
    except UnderAgeError as e:
        print(e)
    except OverAgeError as e:
        print(e)
q4()
