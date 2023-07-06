# Encapsulation Eg-1
class Car:
    def __init__(self, company, model, year):
        self.__company = company
        self.__model = model
        self.__year = year

    def get_company(self):
        return self.__company

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def set_company(self, company):
        self.__company = company

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year


company = input("Enter the car's company: ")
model = input("Enter the car's model: ")
year = input("Enter the car's year: ")

my_car = Car(company, model, year)
print("Car details:")
print("company:", my_car.get_company())
print("Model:", my_car.get_model())
print("Year:", my_car.get_year())

new_company = input("Enter the new company: ")
my_car.set_company(new_company)
print("Updated company:", my_car.get_company())
