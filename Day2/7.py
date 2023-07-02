# # 7) Write a Python program to input a list of non-empty tuples, sort it in increasing order by the
# last element in each tuple. 

# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 

# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] 
def my_sort(sorty):
    by=sorted(sorty,key=lambda x:x [-1])
    return by
my_list=[]
no_tuple=int(input("Enter the no. of tuples : "))
for i in range(no_tuple):
    my_tuple=input(f"Enter the tuple{i+1} : (seperate with ',') : ")
    my_tuple=tuple(my_tuple.split(","))
    my_list.append(my_tuple)
mysort=my_sort(my_list)
print(mysort)
    