num = int(input("Введите оценку за экзамен:"))
dz = int(input("Введите количество выполненных домашних заданий:"))
if num >= 90 and dz >= 10:
    print("Отлично")
elif num >= 70 or dz >= 5:
    print("Хорошо")
else:
    print("Удовлетворительно")