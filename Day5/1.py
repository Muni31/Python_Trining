# # Write a program check_inputs.py that gets two inputs and checks that the first represents a valid int 
# number and that the second represents a valid float number. (Exception handling) 
# # ===================================== 
# Input: 
#Enter Input1: 10 
# Enter Input2: Hello!! 
# Output: 
#"Hello!" is not a valid second input, expected a float value  
def check_inputs():
    try:
        a = int(input("Enter a number 1: "))
    except ValueError:
        print("Invalid first input, expected an integer value")
        return

    try:
        b = float(input("Enter a number 2: "))
    except ValueError:
        print(f'"{b}" is not a valid second input, expected a float value')
        return

    print("Both inputs are valid.")
   
check_inputs()
