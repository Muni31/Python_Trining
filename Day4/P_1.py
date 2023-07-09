# Polymorphism Eg-1

class Country:
    def __init__(self, name, popula):
        self.name = name
        self.popula = popula
    def place(self):
        pass

class City:
    def __init__(self, name, popula):
        self.name = name
        self.popula = popula

class USA(Country):
    def __init__(self, name, popula, capital):
        super().__init__(name, popula)
        self.capital = capital

    def place(self):
        return f"The United States is a country with a population of {self.popula} and its capital is {self.capital}."

class India(Country):
    def __init__(self, name, popula, capital):
        super().__init__(name, popula)
        self.capital = capital

    def place(self):
        return f"India is a country with a population of {self.popula} and its capital is {self.capital}."

class NewYork(City):
    def __init__(self, name, popula):
        super().__init__(name, popula)

    def place(self):
        return f"New York City is a city in the United States with a population of {self.popula}."

class NewDelhi(City):
    def __init__(self, name, popula):
        super().__init__(name, popula)

    def place(self):
        return f"New_Delhi is a city in India with a populattion of {self.popula}."


usa = USA("United States", 331_000_000, "Washington D.C.")
india = India("India", 140_760_000_000, "New_Delhi")
new_york = NewYork("New York City", 8_400_000)
New_Delhi = NewDelhi("New_Delhi", 32_941_000)

names = [india,New_Delhi,usa,new_york]
for name in names:
    print(name.place())
