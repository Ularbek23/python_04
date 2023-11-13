class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak():
        pass

class Dog(Animal):
    def speak(self):
        return "Гав"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Cow(Animal):
    def speak(self):
        return "Myyy"

class Zoo():
    def add_animal(self, animal_object, spis=[]):
        self.spis = spis
        self.spis.append({
            "Животное" : animal_object.name,
            "Возраст" : animal_object.age,
            "Звук" : animal_object.speak()
        }),
    
    def list_animals(self):
        print(self.spis)

dog = Dog("Sharik", 5)
print(dog.speak())
print(dog.name, dog.age)
zoo = Zoo()
zoo.add_animal(dog)
zoo.list_animals()
cat = Cat("Murzik", 4)
zoo.add_animal(cat)
zoo.list_animals()
cow = Cow("Burenka", 9)
zoo.add_animal(cow)
zoo.list_animals()
