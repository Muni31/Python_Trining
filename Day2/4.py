# 4) Write a program that takes the input from the user (i.e., N). Create the generator function that
# takes this input as an argument and returns numbers from 1 to N.
# Output: 

# - Using the generator function, print the numbers from 1 to N. 

def my_gen(n):
    a=1
    for i in range(1,n):
        yield a
        a+=1
    

N=int(input("Enter the 'N' number : "))
for i in my_gen(N):
    print(i)