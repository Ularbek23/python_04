def jow(a, b):
    slovar = {}
    for i in a:
        res_pow = i ** b
        slovar[i] = res_pow
    return slovar
print(jow([5, 3, 2], 8))