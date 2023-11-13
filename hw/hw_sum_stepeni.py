def sum_pow(a, b):
    summa = 0
    degree = a ** b
    g = (degree)
    spis = list(str(g))
    for i in spis:
        summa += int(i)
    return summa
print(sum_pow(2, 1000))