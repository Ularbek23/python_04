from random import randrange
random_number = randrange(10)
n = 1
while True:
    num = input("Введите число: ")
    if num.isdigit():
        if num == str(random_number):
                print(f"Поздравляем! Вы угадали число {random_number} с {n} попытки.")
                break
        elif int(num) < 0 or int(num) > 10:
            print("Введите число в диапазоне от 0 до 9.")
        elif 0 <= int(num) < 10:
            print("Попробуйте ещё раз.")
    else:
        print("Введите целое число от 0 до 9.")
    n+=1
