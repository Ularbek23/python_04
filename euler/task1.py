i = 1
my_sum = 0
while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
        # print(i)
        my_sum = my_sum + i
    i += 1
print(my_sum)