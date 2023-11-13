# def swim(a, b):
#     c = a + b
    
# aw = swim(3, 4)
# print(aw)
for i in range(4):
        if i==0 or i==3:
            for j in range(7):
                print('#',end='')
        else:
            print('#',end='')
            for j in range(1,6):
                print(' ',end='')
            print('#',end='')
        print()