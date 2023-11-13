def mid(*args):
    summa = 0
    for i in args:
        summa += i
    res = summa / len(args)
    return res
print(mid(8, 7, 3, 2, 5))