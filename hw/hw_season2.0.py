season = {
    1: "Зима",
    2: "Зима",
    3: "Весна",
    4: "Весна",
    5: "Весна",
    6: "Лето",
    7: "Лето",
    8: "Лето",
    9: "Осень",
    10: "Осень",
    11: "Осень",
    12: "Зима",
}
num = int(input("Введите номер месяца: "))
while True:
    if num in season:
            print(season[num])
            break
    else:
        num = int(input("Не корректный ввод, введите от 1 - 12: "))