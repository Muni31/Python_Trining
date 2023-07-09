# Create classes: Circle, Square, Rectangle, Triangle, Pentagon, Hexagon, Heptagon, Octagon 
# as child classes of Shape. These classes should have functions to calculate perimeter, 
# area, description about the shape and comparison with another shape based on area or perimeter.
# For eg: there is an object of Circle with x area and object of Heptagon with y area,
# a function should tell which object has a larger area. 

import math
class Shape:
    def compare_area(self, other_shape):
        if self.area() > other_shape.area():
            return f"This shape has a larger area than the {other_shape}"
        elif self.area() < other_shape.area():
            return f"The {other_shape} has a larger area than this shape"
        else:
            return "Both shapes have the same area."
    def compare_perimeter(self, other_shape):
        if self.perimeter() > other_shape.perimeter():
            return f"This shape has a larger perimeter than the {other_shape}."
        elif self.perimeter() < other_shape.perimeter():
            return f"The{other_shape} has a larger perimeter than this shape."
        else:
            return "Both shapes have the same perimeter."
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
    def description(self):
        return f"A circle with radius {self.radius}."
    
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    def area(self):
        return self.side_length ** 2
    def perimeter(self):
        return 4 * self.side_length   
    def description(self):
        return f"A square with side length {self.side_length}."

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width   
    def area(self):
        return self.length * self.width 
    def perimeter(self):
        return 2 * (self.length + self.width)  
    def description(self):
        return f"A rectangle with length {self.length} and width {self.width}."

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3  
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))  
    def perimeter(self):
        return self.side1 + self.side2 + self.side3    
    def description(self):
        return f"A triangle with side lengths {self.side1}, {self.side2}, and {self.side3}."

class Pentagon(Shape):
    def __init__(self, side_length):
        self.side_length = side_length    
    def area(self):
        return (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.side_length ** 2    
    def perimeter(self):
        return 5 * self.side_length   
    def description(self):
        return f"A pentagon with side length {self.side_length}."

class Hexagon(Shape):
    def __init__(self, side_length):
        self.side_length = side_length   
    def area(self):
        return (3 * math.sqrt(3) * self.side_length ** 2) / 2   
    def perimeter(self):
        return 6 * self.side_length   
    def description(self):
        return f"A hexagon with side length {self.side_length}."

def shape_input():
    shape_type = input("Enter the shape type (circle, square, rectangle, triangle, pentagon, hexagon): ")    
    if shape_type == "circle":
        radius = float(input("Enter the radius: "))
        return Circle(radius)    
    elif shape_type == "square":
        side_length = float(input("Enter side length: "))
        return Square(side_length)    
    elif shape_type == "rectangle":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        return Rectangle(length, width)    
    elif shape_type == "triangle":
        side1 = float(input("Enter the length of side 1: "))
        side2 = float(input("Enter the length of side 2: "))
        side3 = float(input("Enter the length of side 3: "))
        return Triangle(side1, side2, side3)    
    elif shape_type == "pentagon":
        side_length = float(input("Enter the side length: "))
        return Pentagon(side_length)    
    elif shape_type == "hexagon":
        side_length = float(input("Enter the side length: "))
        return Hexagon(side_length)    
    else:
        print("Invalid shape type.")
        return None

shape1 = shape_input()
shape2 = shape_input()   
if shape1 and shape2:
    print(f"Shape 1: {shape1.description()}")
    print(f"Shape 2: {shape2.description()}")        
    print(f"Area comparison: {shape1.compare_area(shape2)}")
    print(f"Perimeter comparison: {shape1.compare_perimeter(shape2)}")

