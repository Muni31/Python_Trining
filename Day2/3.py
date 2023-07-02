# 3) Write a program that takes Student's name and their marks in 3 subjects as input.
# Print each student's total marks as output. 
def totalmark(marks):
    return sum(marks)

no_of_students=int(input("Enter the no. of students : "))
students={}
for i in range(no_of_students):
    student=input("Enter the student name : ")
    marks=[]
    for j in range (3):
        mark=int(input("Enter the mark of the subject : "))
        marks.append(mark)
    students[student]=marks
    print("*******************************")
for student, marks in students.items():
    print("---------------------------------")
    total=totalmark(marks)
    print(f"{student} total_marks={total} ")