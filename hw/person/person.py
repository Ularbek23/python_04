class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Меня зовут {self.name} и мне {self.age} лет")
