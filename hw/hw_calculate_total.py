def calculate_total_cost(*args):
    summa = 0
    for i in args:
        summa += i
    return summa
print(calculate_total_cost(43, 53, 2, 5, 45))