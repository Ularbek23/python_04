def extract_digits(a):
    summa = 0
    spis = []
    for i in a:
        if i.isdigit():
            spis.append(i)
    for j in spis:
        summa += int(j)  
    print(summa)
    print(spis)
    return
extract_digits("tggr77r8g7 et78et 7e8t7 8te7 b6t6t5eh 678")
