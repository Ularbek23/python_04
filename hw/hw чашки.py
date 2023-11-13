num = int(input())
a = num % 10
if num == 11 or num == 12 or num == 13 or num == 14:
    print(f"{num} чашек")
elif a == 1:
    print(f"{num} чашка")
elif a == 2 or a == 3 or a == 4:
    print(f"{num} чашки")
else:
    print(f"{num} чашек")

