# Implement a destructor of the objects which voids the object of the Class 
class MyClass:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Deleting object {self.name}")


obj1 = MyClass("Object 1")
obj2 = MyClass("Object 2")


del obj1
del obj2
