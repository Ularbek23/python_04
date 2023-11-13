num = int(input("put num: "))
if num > 0:
    print("Положительное число")
elif num < 0:
    print("Отрицательное число")
else:
    print("0")
if num % 2 == 0:
    print("Четное число")
else:
    print("Не четное число")