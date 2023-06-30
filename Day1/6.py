# Write a python function which counts the frequency of given character in a given string. 
# Inputs - A String A Character whose frequency needs to be determined 
def freq(a,b):
    count=0
    for i in a:
        if i==b:
            count+=1
    print(f"the Character '{b}' is appears {count} from the string '{a}' ")
a=input("enter a string : ")
b=input ("enter a character : ")
freq(a,b)