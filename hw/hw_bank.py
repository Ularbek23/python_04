def bank(a, years):
    summa = a
    for year in range(years):
        proc = summa / 10
        summa += proc
    return summa
res = bank(1000, 10)
print(round(res, 2))