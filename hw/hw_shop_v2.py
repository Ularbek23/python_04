class Shop:

    def __init__(self, name, slovar={}):
        self.name = name
        self.slovar = slovar

    def add_product(self, product_name, price, quantity=1):
        if product_name in self.slovar:
            self.slovar.update({product_name : (price, self.slovar[product_name][1] + quantity)})
        else:
            self.slovar.update({product_name : (price, quantity)})
        
        print(f"Товар {product_name} добавлен, его цена - {price}")

    def get_product_info(self, product_name):
        if product_name in self.slovar:
            print(f"Цена: {self.slovar[product_name][0]}, Количество: {self.slovar[product_name][1]} ")
        else:
            print(None)
            
    def buy_product(self, product_name, quantity):
        if product_name in self.slovar and quantity <= self.slovar[product_name][1]:
            res = 1
            self.res = res
            self.res = self.slovar[product_name][0] * self.slovar[product_name][1]
            self.slovar[product_name] = self.slovar[product_name][0], self.slovar[product_name][1] - quantity
            print("Покупка прошла успешно")
        elif not product_name in self.slovar:
            print("Такого товара нет")
        elif quantity > self.slovar[product_name][1]:
            print("Недостаточно товара")

# my_mag = Shop("Пятерочка")
# my_mag.add_product("Хлеб", 25, 5)
# my_mag.get_product_info("Хлеб")
# my_mag.buy_product("Хлеб", 4)
# my_mag.get_product_info("Хлеб")
# my_mag.buy_product("Хлеб", 1)
# my_mag.get_product_info("Хлеб")
# my_mag.buy_product("Хлеб", 4)
my_mag_2 = Shop("Globus")
my_mag_2.add_product("Пельмени", 67, 6)
my_mag_2.add_product("Молоко", 40, 8)
my_mag_2.get_product_info("Пельмени")
my_mag_2.get_product_info("Молоко")
my_mag_2.buy_product("Молоко", 9)
my_mag_2.get_product_info("Молоко")
my_mag_2.buy_product("Молоко", 7)
my_mag_2.get_product_info("Молоко")
my_mag_2.buy_product("Молоко", 2)
my_mag_2.get_product_info("Молоко")
my_mag_2.buy_product("Молоко", 1)
my_mag_2.get_product_info("Молоко")
my_mag_2.buy_product("Пельмени", 6)
my_mag_2.get_product_info("Пельмени")
my_mag_2.buy_product("Хлеб", 1)
my_mag_2.add_product("Молоко", 40, 4)
my_mag_2.get_product_info("Молоко")
my_mag_2.add_product("Молоко", 40, 6)
my_mag_2.get_product_info("Молоко")
# my_mag_3 = Shop("Frunze")
# my_mag_3.add_product("egg", 23, 3)

