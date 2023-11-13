spis = [5, 6, 10]
def arif():
    summa = 0
    for i in spis:
        summa += i
    res = summa / len(spis)
    return res
print(arif())