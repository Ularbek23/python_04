def game(num):
    q = 0
    c = int(k / 2)
    step = c / 2
    while True:
        print(c)
        if c < num:
            print("Меньше")
            c = round(c + step)
        elif c > num:
            print("Больше")
            c = round(c - step)
        else:
            print(c, f"Верно! Кол-во шагов {q}")
            break
        step /= 2
        q += 1
k = 100
n = int(input(f"Введите число от 1 до {k}: "))
game(n)