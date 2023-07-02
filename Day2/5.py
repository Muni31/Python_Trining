# 5) Iterate on the dictionary made in Program #3 and find the percentage of each student,
# store it and print it in the console. 
# Use iterables objects to store the values. 
def totalmark(marks):
    return sum(marks)
def per(marks):
    per=(marks/300)*100
    return per

no_of_students=int(input("Enter the no. of students : "))
students={}
for i in range(no_of_students):
    student=input("Enter the student name : ")
    marks=[]
    for j in range (3):
        mark=int(input("Enter the mark of the subject : "))
        marks.append(mark)
        
    total=totalmark(marks) 
    percentage=per(total)    
    students[student]={"Total Marks" :total,"Percentage":percentage}
    print("*******************************")
    
    
for student, marks in students.items():
    print("---------------------------------")
    
    print(f"{student} -->total_marks={marks['Total Marks']} -->Percentage {marks['Percentage']} ")
 