i = 1
a = 0
while i <= 100:
    if i % 3 == 0 or i % 5 == 0:
        a = a + i
    i += 1
print(a)