num = int(input("Введите число (для завершения введите 0):"))
a = 0
while num != 0:
    a = a + num
    num = int(input("Введите число (для завершения введите 0):"))
    if num == 0:
        print(a)
