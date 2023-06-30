# Write a program to take two numbers as input parameter and then ask for the arithmetic parameter to be performed.  
# 	>>> “Enter Two numbers” 
# 	10 45  
# 	>>>“Operations to perform “  
# 	+  
# 	>>> 55 
num1=int(input("Enter the number : "))
num2=int(input("Enter the number : "))
oper=input("""Choose Operations to perform 
           '+' , '-' , '*' , '/' """)
if oper=='+':
    print(num1+num2)
elif oper=='-':
    print(num1-num2)
elif oper=='*':
    print(num1*num2)
elif oper=='/':
    print(num1/num2)
else:
    print ("Invalid operator choose fromm the given operators ")