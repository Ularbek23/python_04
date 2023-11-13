class Dog():
    size = 0.5
    tail = 1
    is_running = True
    def talk(self):
        print("ГАВ!")

class Video():
    views = 0
    likes = 100
    subscribers = []
    is_published = True
    def subscribe(self):
        print("Вы успешно подписаны")

class Student():
    name = "Ularbek"
    age = 23
    course = 1
    def info_1(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        print(f"name - {self.name}, age - {self.age}, course - {self.course}")
        
    def info_2(self, age):
        self.age = age
        print(f"{2023 - self.age} - год рождения")
    
Warik = Dog()
Pes = Dog()
Mark = Dog()
Youtube = Video()
Twitch = Video()
Tik_Tok = Video()
Ularbek = Student()
Tomas = Student()
Arthur = Student()
print(Warik.tail)
Pes.talk()
print(Mark.is_running)
Youtube.subscribe()
print(Twitch.views)
print(Tik_Tok.subscribers)
Tomas.age = 18
Tomas.info_2(24)
Arthur.name = "Arthur"
Arthur.info_1("Arthur", 18, 2)
print(Arthur.name)
Ularbek.info_1("Ularbek", 23, 4)