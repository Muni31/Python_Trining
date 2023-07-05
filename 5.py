# In task 2, implement function to compare two shape's perimeter and area based on length/breadth 
# of the shape.Add validations on the input taken from user. 
def compare_shapes(len1, brth1, len2, brth2):
    
    if not (isinstance(len1, (int, float)) and isinstance(brth1, (int, float)) and
            isinstance(len2, (int, float)) and isinstance(brth2, (int, float))):
        raise ValueError("Length and breadth must be numeric values.")
    if len1 <= 0 or brth1 <= 0 or len2 <= 0 or brth2 <= 0:
        raise ValueError("Length and breadth values must be greater than zero.")
    perimeter1 = 2 * (len1 + brth1)
    area1 = len1 * brth1
    perimeter2 = 2 * (len2 + brth2)
    area2 = len2 * brth2
    if perimeter1 > perimeter2:
        perimeter = "Shape 1 has a greater perimeter."
    elif perimeter1 < perimeter2:
        perimeter = "Shape 2 has a greater perimeter."
    else:
        perimeter = "Both shapes have the same perimeter."

    if area1 > area2:
        area = "Shape 1 has a greater area."
    elif area1 < area2:
        area = "Shape 2 has a greater area."
    else:
        area = "Both shapes have the same area."

    return perimeter, area

length1 = float(input("Enter the length of shape 1: "))
breadth1 = float(input("Enter the breadth of shape 1: "))
length2 = float(input("Enter the length of shape 2: "))
breadth2 = float(input("Enter the breadth of shape 2: "))

perimeter, area = compare_shapes(length1, breadth1, length2, breadth2)

print(perimeter)
print(area)