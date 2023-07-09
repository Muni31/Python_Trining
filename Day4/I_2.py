# Inheritance Eg-2
class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Orange(Fruit):
    def __init__(self, name, color):
        super().__init__(name, color)

class Banana(Fruit):
    def __init__(self, name, color):
        super().__init__(name, color)

class WaterMelon(Fruit):
    def __init__(self, name, color):
        super().__init__(name, color)

orange = Orange("orange", "Orange")
banana = Banana("Banana", "Yellow")
waterMelon=WaterMelon("watermelon","Green")

print(f"orange: {orange.color}  ")
print(f"Banana: {banana.color}  ")
print(f"WaterMelon: {waterMelon.color}  ")
