# Write a Python function to insert a string in the middle of a string. For odd length of 	string, 
# remove the middle character and replace with given string.
def insert_string_middle(original, insert):
    length = len(original)
    middle = length // 2

    if length % 2 == 0:
        # Even length, insert in the middle
        print( original[:middle] + insert[middle:])
    else:
        # Odd length, replace middle character
        print( original[:middle] + insert[middle + 1:])

# Example usage:
original = input("enter a string : ")
insert = input("enter a string : ")
result = insert_string_middle(original, insert)
print(result)
