a = int(input("Введите трехзначное число: "))
while a < 100 or a > 999:
    a = int(input("Введите трехзначное число: "))
one = a // 100
two = a // 10 % 10    
three = a % 10
summa = one + two + three
pro = one * two * three
print(f"Сумма цифр числа: {summa}")
print(f"Произведение цифр числа: {pro}")
