# # 2.	Write python script to take one integer argument and then print as follows: 
#     	- If Value >0 and Value < 10 — Small 
#     	- If Value > 10 and Value <100 — Medium 
#     	- If Value <1000 — Large 
#     	- If Value > 1000 — Invalid 
a=int(input("enter a digit : "))
if a>0 and a<10:
    print(f"{a} is Small ")
elif a>10 and a<100:
     print(f"{a} is Medium ")
elif a<1000:
     print(f"{a} is Large ")
else:
     print(f"{a} is Invalid ")
    