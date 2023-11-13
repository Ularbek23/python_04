a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
i = 0
while i < len(a):
    if a[i] < 7:
        print(a[i])
    i = i + 1

b = len(a) - 1
print(a[0], a[b])
print(len(a))