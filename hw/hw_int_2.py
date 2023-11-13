# while True:
#     num = input("put num: ")
#     if num.isdigit() and not num.isalpha():
#         print(num, type(num))
#         break
#     else:
#         continue


while True:
    num = input("put num(float): ")
    if "." in num:
        spis = []
        nums = True
        for i in num:
            if i == ".":
                continue
            elif i.isalpha():
                nums = False
                spis.append(nums)
        if not False in spis:
            a = float(num)
            print(a, type(a))
            break
        else:
            continue
    else:
        continue
