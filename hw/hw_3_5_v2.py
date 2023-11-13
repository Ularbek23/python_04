nums = [6, 2, 88, 23, 0, -5, 30, 9, 20, 10, 6, 56, -7]
spis_3 = []
spis_5 = []
for i in nums:
    a = i % 3
    b = i % 5
    if i == 0:
        continue
    if a == 0:
        spis_3.append(i)
    if b == 0:
        spis_5.append(i)
print(f"Кратные 3: {spis_3}")
print(f"Кратные 5: {spis_5}")


