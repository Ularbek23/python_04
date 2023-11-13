from openpyxl import load_workbook
file_name = "students.xlsx"
excel = load_workbook(file_name)
page = excel["Лист1"]
commands = {
    "1": "Показать студентов",
    "2": "Показать оценки",
    "3": "Средняя оценка"
}
print("Выберите команду: ")
for key, value in commands.items():
    print(key, value)
input_value = input()

if input_value == "1":
    for cell in page["A"]:
        if cell.row == 1:
            continue
        print(cell.value)

elif input_value == "2":
    for cell in page["B"]:
        if cell.row == 1:
            continue
        print(cell.value)

elif input_value == "3":
    spis = []
    for cell in page["B"]:
        if cell.row == 1:
            continue
        spis.append(cell.value)
    res = sum(spis) / len(spis)
    print(res)
    
    