# Write a program to convert a string value to integer and raise a custom exception. (Hint: Use raise) 
# =============  
# Input:  
# Enter value: “test” 
#  Output: 
# Entered value can’t be converted to integer!!

class ConversionError(Exception):
    pass
def fun(value):
    try:
        num = int(value)
        return num
    except ValueError:
        raise ConversionError("Entered value can't be converted to an integer ")
def fan():
    value = input("Enter value: ")
    try:
        a = fun(value)
        print(f"Successfully converted to integer: {a}")
    except ConversionError as e:
        print(e)

fan()
 