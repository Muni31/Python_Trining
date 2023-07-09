# Inheritance Eg-1
# Parent class
class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.brand} is driving.")

class Car(Vehicle):
    def __init__(self, brand, color, model):
        super().__init__(brand, color)
        self.model = model

    def honk(self):
        print(f"The {self.color} {self.brand} {self.model} is honking.")

class Motorcycle(Vehicle):
    def __init__(self, brand, color):
        super().__init__(brand, color)

    def wheelie(self):
        print(f"The {self.color} {self.brand} motorcycle is doing a wheelie.")

my_car = Car("Toyota", "Red", "Corolla")
my_motorcycle = Motorcycle("Harley-Davidson", "Black")

my_car.drive()
my_car.honk()

my_motorcycle.drive()
my_motorcycle.wheelie()
