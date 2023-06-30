# Write a Python function to remove the characters which have odd index values of a given string.
def remov(a):
    b=""
    count=0
    for i in a:
        if count%2==0:
            b+=i
        count+=1
    print(b)
a=input("Enter a string : ")
remov(a)