# 1 

# first = int(input("Введите первое число: "))
# second = int(input("Введите второе число: "))
# summa = first + second
# if summa % 2 == 0:
#     print("Сумма является четным числом")
# else:
#     print("Сумма является нечетным числом")

# 2

# while True:
#     num = int(input("Введите радиус окружности: "))
#     if num <= 0:
#         print("Радиус должен быть положительным числом")
#         continue
#     else:
#         s = 3.14 * (num ** 2)
#         break
# print(f"Площадь окружности {s}")

# 3

# chislo = int(input("Введите число: "))
# spisok = []
# a = 1
# spisok.append(a)
# while True:
#     if a >= chislo:
#         break
#     a += 3
#     if a > chislo:
#         continue
#     spisok.append(a)
# print(spisok)
# for k in range(1, chislo+1, 4):
#     print(k, end=' ')

# 4

# slovar = {}
# i = 0
# g = int(input("Введите количество студентов: "))
# while i < g:
#     name = input("Введите имя студена: ")
#     old = int(input("Введите возраст студента: "))
#     slovar[name] = old
#     i += 1
# print("Ввод информации о студентах: ")
# for key in slovar:
#     print(f"Имя: {key}")
#     print(f"Возраст: {slovar[key]}")

# print(f"Словарь студентов: {slovar}")

# 5

# num_1 = 1
# num_2 = 2
# f = num_1 + num_2 
# i = 0
# while i < 997:
#     num_1 = num_2       
#     num_2 = f           
#     f = num_1 + num_2
#     i += 1
# print(f)

