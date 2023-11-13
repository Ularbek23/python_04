from openpyxl import load_workbook
from openpyxl import Workbook
excel_file = Workbook()
excel_file.title = "students_with_semester_grades.xlsx"
page = excel_file["Sheet"]
page["A1"] = "Имя"
page["B1"] = "Возраст"
page["C1"] = "Факультет"
page["D1"] = "Специальность"
page["E1"] = "Оценки"
page["F1"] = "Средняя оценка за семестр"
dic = [
    {
    "name": "Ularbek",
    "old": 23,
    "faq": "Естественно-технический",
    "spec": "Техника и технологии",
    "estimates": [4, 5, 5, 4, 3]
},
    {
    "name": "Tomas",
    "old": 20,
    "faq": "Естественно-технический",
    "spec": "Техника и технологии",
    "estimates": [3, 3, 5, 4, 4]
    },
    {
    "name": "Oleg",
    "old": 18,
    "faq": "Естественно-технический",
    "spec": "Техника и технологии",
    "estimates": [5, 5, 5, 5, 5]
    },
    {
    "name": "Anya",
    "old": 22,
    "faq": "Естественно-технический",
    "spec": "Техника и технологии",
    "estimates": [4, 5, 5, 4, 5]
    },
    {
    "name": "Safari",
    "old": 21,
    "faq": "Естественно-технический",
    "spec": "Техника и технологии",
    "estimates": [4, 3, 3, 4, 3]
    }
]
a = 2
b = 2
c = 2
d = 2
e = 2
f = 2
for slov in dic:
    for key in slov:
        if key == "name":
            page[f"A{a}"] = slov[key]
            a+=1
        elif key == "old":
            page[f"B{b}"] = slov[key]
            b+=1
        elif key == "faq":
            page[f"C{c}"] = slov[key]
            c+=1
        elif key == "spec":
            page[f"D{d}"] = slov[key]
            d+=1
        elif key == "estimates":
            res = sum(slov[key]) / len(slov[key])
            page[f"F{f}"] = res
            page[f"E{e}"] = ', '.join(map(str, slov[key]))
            e+=1
            f+=1
            
        


excel_file.save("students_with_semester_grades.xlsx")