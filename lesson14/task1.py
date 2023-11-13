lst = [15, 18, 20, 25, 30, 40]
def prizyv(a):
    spis = [i for i in lst if 18 <= i <= 27]
    return spis
print(prizyv(lst))