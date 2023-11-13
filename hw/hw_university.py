class University:
    def __init__(self, university_name, departments={}):
        self.university_name = university_name
        self.departments = departments

    def add_department(self, faq):
        self.departments.update({faq : []})

class Student(University):
    def __init__(self, first_name, last_name):
        self.name = f"{last_name} {first_name}"

    def add_student(self, faq, university_object):
        university_object.departments[faq].append(self.name)
        print(university_object.departments)

un_1 = University("Hogwarts")
un_1.add_department("Slizerin")
print(un_1.departments)
st_1 = Student("Harry", "Poter")

st_1.add_student("Slizerin", un_1)
print(un_1.departments)
st_2 = Student("Ron", "Uizly")
st_2.add_student("Slizerin", un_1)
print(un_1.departments)
un_1.add_department("Pufendui")
print(un_1.departments)
st_3 = Student("Gnom", "Gnomych")
st_3.add_student("Pufendui", un_1)
print(un_1.departments)