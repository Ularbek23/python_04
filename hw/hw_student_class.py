class Student:
    name = "Gregor"
    groupNumber = "10a"
    age = 18

    def getName(self):
        print(self.name)
    
    def getAge(self):
        print(self.age)

    def getGroupNumber(self):
        print(self.groupNumber)

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber

st_1 = Student()
st_2 = Student()
st_3 = Student()
st_4 = Student()
st_5 = Student()
st_1.getName()
st_1.getAge()
st_1.getGroupNumber()
st_2.setNameAge("Ularbek", 23)
st_2.getName()
st_2.getAge()
st_2.getGroupNumber()
st_3.setNameAge("Tomas", 20)
st_3.getName()
st_3.getAge()
st_3.getGroupNumber()
st_4.setNameAge("Anna", 19)
st_4.getName()
st_4.getAge()
st_4.getGroupNumber()
st_5.setNameAge("Carl", 21)
st_5.setGroupNumber("10b")
st_5.getName()
st_5.getAge()
st_5.getGroupNumber()
