class Shape():
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        super().area()
        s = self.width * self.height
        print(s)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        super().area()
        s = 3.14 * (self.radius ** 2)
        print(s)
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        super().area()
        s = (self.base * self.height) / 2
        print(s)

prim = Shape()
gru = Rectangle(5, 2)
frw = Circle(6)
erg = Triangle(5, 4)
prim.area()
gru.area()
frw.area()
erg.area()