from openpyxl import Workbook
new_excel_file = Workbook()
new_excel_file.title = "students.xlsx"
page = new_excel_file.active
page.title = "worksheet"
page["A1"] = "Имя"
page["B1"] = "Возраст"
page["A2"] = "Ularbek"
page["B2"] = 23
page["A3"] = "Tomas"
page["B3"] = 18
page["A4"] = "Pol"
page["B4"] = 20

new_excel_file.save("students.xlsx") 