balance = int(input("Введите свой баланс:"))
if balance > 0:
    print(f"Ваш баланс составляет: {balance} сом")
elif balance == 0:
    print("У Вас 0 сом")
else:
    print(f"Ваш долг составляет: {balance} сом")