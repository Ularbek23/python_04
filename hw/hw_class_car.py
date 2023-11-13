class Car():
    def __init__(self, brand, year, color, horsepower=85):
        self.brand = brand
        self.year = year
        self.color = color
        self.horsepower = horsepower
    def get_auto(self):
        print(f"{self.brand}, {self.year}, {self.color}")
    def get_year(self):
        print(f"{2023 - int(self.year)} - возраст автомобиля")
    def add_horsepower(self):
        spis = ["Mers", "Bmw", "Porshe"]
        if self.brand in spis:
            self.horsepower += 40
        else:
            self.horsepower += 20
    
Mark = Car("Toyota", "1999", "White")
Mark.get_auto()
Mark.get_year()
Mark.add_horsepower()
print(Mark.horsepower)
bmw = Car("Bmw", 1997, "Black")
print(bmw.brand)
print(bmw.year)
print(bmw.color)
bmw.get_auto()
bmw.get_year()
bmw.add_horsepower()
print(bmw.horsepower)
porshe = Car("Porshe", 2001, "Yellow")
tesla = Car("Tesla", 2021, "Blue")
porshe.get_auto()
tesla.get_auto()
