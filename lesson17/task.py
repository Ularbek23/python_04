class Tech:
    qty = 3

class Computer(Tech):
    has_keyboard = True
    has_mouse = True
    def __init__(self, screen_size, ram, model, price):
        self.screen_size = screen_size
        self.ram = ram
        self.model = model
        self.price = price

class Laptop(Computer):
    has_mouse = False

class Printer(Tech):
    is_color = False
    printer_type = "laser"
    def __init__(self, model, price):
        self.model = model
        self.price = price

class DayBudget:
    money = 150
    def sell(self, tech_object):
        if tech_object.qty > 0:
            self.money += tech_object.price
            tech_object.qty -= 1
        else:
            print("Такого товара не осталось")

hp = Laptop(15, 8, "HP Espire 1505", 700)
lenovo = Laptop(16, 32, "Lenovo white 777", 1100)
budget_18 = DayBudget()
print(budget_18.money)
budget_18.sell(hp)
print(budget_18.money)
hp_2 = Printer("HP 1808", 600)
budget_18.sell(hp_2)
print(budget_18.money)
comp = Computer(26, 64, "Computer 123", 2000)
budget_18.sell(comp)
print(budget_18.money)
budget_18.sell(comp)
print(budget_18.money)
budget_18.sell(comp)
print(budget_18.money)
budget_18.sell(comp)
print(budget_18.money)
budget_18.sell(comp)
print(budget_18.money)