def sum_pow(n):
    lst = [i for i in range(1, n) if i % 3 == 0 or i % 5 == 0]
    return sum(lst)
print(sum_pow(1000))
