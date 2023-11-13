n = 4000000
res = 2
num_1 = 1
num_2 = 2
f = num_1 + num_2 
while f < n:
    num_1 = num_2       
    num_2 = f           
    f = num_1 + num_2  
    if f > n:
        break
    if f % 2 == 0:
        res += f
print(res)