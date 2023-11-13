# 1
spis = list(range(0, 60, 5))
print(spis)
for i, j in enumerate(spis):
    if j == 20:
        spis[i] = 200
    else:continue
print(spis)
print(sum(spis))

# 2
def absolut(list):
    for k, o in enumerate(list):
        if o < 0:
            list[k] = o * -1
    return list

def okr(list):
    for g, v in enumerate(list):
        if isinstance(v, float):
            list[g] = round(v)
    return list
def step_3(list):
    first = list[0] ** 3
    last = list[-1] ** 3
    return first, last
a = [1, 1, 2.3, 3, -5, 8, -13, -21, 34.5, 55, 89]
print(absolut(a))
print(okr(a))
print(step_3(a))