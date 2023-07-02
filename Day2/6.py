# 6) Create a program to take student information as input. Student will have First Name, Last Name,
# Roll No. Write a function to sort the list based on given input parameter.  
# Input Parameters can be: ‘By First Name’ or ‘Last Name’ or ‘Roll No’.

def By_sort(student,sort):
    if sort=="First_Name":
        student.sort(key=lambda x:x['First Name'])
    elif sort=="Last_Name":
        student.sort(key=lambda x:x['Last Name'])
    elif sort=="Roll_No":
        student.sort(key=lambda x:x['Roll No'])
    else:
        print("Invalid input, It is by default ")
        student.sort(key=lambda x:x['First Name'])
    return student
         
        
no_of_stud=int(input("Enter no. of students : "))
student_info=[]
for i in range(no_of_stud):
    first_name=input("Enter your First Name : ")
    last_name=input("Enter your Last Name : ")
    roll_no=int(input("Enter the roll number : "))
    student_info.append({"First Name":first_name,"Last Name":last_name,"Roll No":roll_no})
sort=input("Enter the sorting parameter (First_Name/Last_Name/Roll_No) : ")
By=By_sort(student_info,sort)
    
for i in By:
    print(f"First_Name: {i['First Name']} Last_Name: {i['Last Name']} -->Roll_No : {i['Roll No']}")



