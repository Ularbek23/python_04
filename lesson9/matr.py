m = [
    [3, 7, 8, 6],
    [4, 2, 9, 3],
    [5, 2, 7, 0]
    ]
# for r in m:
#     for num in r:
#         print(num)
nums = []
for i in range(len(m)):
    for j in range(len(m[i])):
        nums.append(m[i][j])
        print(nums)
print(nums)