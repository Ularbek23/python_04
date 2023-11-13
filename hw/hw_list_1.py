def spisok(a):
    spis_1 = []
    spis_2 = []
    spis_3 = []
    for i in a:
        if isinstance(i, str):
            spis_1.append(i.capitalize())
        elif isinstance(i, int):
            spis_2.append(i)
        elif isinstance(i, float):
            spis_3.append(i)
    print(sorted(spis_1))
    print(sorted(spis_2, reverse=True))
    print(sum(spis_3))
    return

list_1 = [5.97, 6, "tom", 3.14, "bob", "alice", 5, -35, "nursultan", 42, "ulukbek", "edil", 91, "nurlan", 1.5, 27.9]
spisok(list_1)