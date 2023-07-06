# Polymorphism Eg-2
class Chocolate:
    def __init__(self, brand):
        self.brand = brand
    def get_price(self):
        pass

class munch(Chocolate):
    def get_price(self):
        return 10

class five_star(Chocolate):
    def get_price(self):
        return 5

class perk(Chocolate):
    def get_price(self):
        return 25

# Taking input from the user
brand = input("Enter the chocolate brand(munch,five_star,perk): ")

# Creating an instance based on user input
if brand.lower() == "munch":
    chocolate = munch("munch")
elif brand.lower() == "five_star":
    chocolate = five_star("five_star")
elif brand.lower() == "perk":
    chocolate = perk("perk")
else:
    chocolate = Chocolate(brand)

price = chocolate.get_price()
print(f"The price of {chocolate.brand} chocolate is ${price:.2f}")

