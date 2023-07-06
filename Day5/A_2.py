# Abstraction Eg-2
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def wheels(self):
        pass

    @abstractmethod
    def average_cost(self):
        pass

class Car(Vehicle):
    def wheels(self):
        return 4

    def average_cost(self):
        return 800000

class Motorcycle(Vehicle):
    def wheels(self):
        return 2

    def average_cost(self):
        return 60000
    
class Auto(Vehicle):
    def wheels(self):
        return 3

    def average_cost(self):
        return 100000

car = Car()
motorcycle = Motorcycle()
auto=Auto()

print(f"Car : has {car.wheels()} Wheels and the average cost of the Car is {car.average_cost()} Rupees" )  
print(f"MotoCycle : has {motorcycle.wheels()} Wheels and the average cost of the MotorCycle is {motorcycle.average_cost()}  Rupees" )  
print(f"Auto : has {auto.wheels()} Wheels and the average cost of the Auto is {auto.average_cost()} Rupees" )  
