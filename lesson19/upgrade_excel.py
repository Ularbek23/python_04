from openpyxl import load_workbook

excel_file = load_workbook("users_table.xlsx")
page = excel_file["Sheet"]
# добавление
# page["A11"] = "Ularbek"
# excel_file.save("users_table.xlsx")
print(page["A7"].value)
excel_file.save("users_table.xlsx")