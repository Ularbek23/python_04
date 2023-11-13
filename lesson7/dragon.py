nums = [1, 4, 6, 45, 646, 3, 345, 555, 233]
a = nums[0]
for n in nums:
    if n > a:
        a = n
print(a)