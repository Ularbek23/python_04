from openpyxl import load_workbook
file_name = "students.xlsx"
excel = load_workbook(file_name)
list_1 = excel["Лист1"]
list_1["A2"] = "Ularbek"
list_1["B2"] = 100
list_1["A3"] = "Eldiyar"
list_1["B3"] = 100
list_1["A4"] = "Sasha"
list_1["B4"] = 54
list_1["A5"] = "Tolik"
list_1["B5"] = 76
excel.save(file_name)