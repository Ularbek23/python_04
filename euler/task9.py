a, b, c = 1, 1, 1
while a < 1000:
    b = 1
    while b < 1000:
        c = (a ** 2 + b ** 2) ** 0.5
        # print(a, b, c)
        if a < b < c:
            if a + b + c == 1000:
                print(a * b * c)            
        b += 1
    a += 1