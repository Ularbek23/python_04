class Fruit:
    sweet = True
    mass = 150
    def eat(self):
        self.mass = 0

class Apple(Fruit):
    color_options = ["red", "green"]
    def __init__(self, color):
        if color in self.color_options:
            self.color = color

class Orange(Fruit):
    color = "orange"
    def make_juice(self):
        self.juice = self.mass / 2

fruit = Fruit()
fruit.eat()
print(fruit.mass)
apple = Apple("green")
print(apple.color)
orange = Orange()
orange.make_juice()
print(orange.mass)
print(orange.juice)