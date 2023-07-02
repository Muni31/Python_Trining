# Write a program to take size of the list as input. 
# Then read the integer values and store these details into list.  

# Output: 

# - The list entered by the user

a=int(input("Enter the list size : "))
b=[]
for i in range(0,a):
    b.append(int(input("Enter the item you need to add in your list : ")))
print(b)