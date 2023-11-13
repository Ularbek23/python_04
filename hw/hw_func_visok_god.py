year = int(input(""))
def a(year):
    if year % 4 == 0 and year % 100 != 0 or (year % 400 == 0):
        res = "Високосный год"
    else:
        res = "Не Високосный год"
    return res
itog = a(year)
print(itog)
