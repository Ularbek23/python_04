i = 0
while True:
    a = input("Введите число ( для завершения нажмите ввод): ")
    if a.isalpha():
        print("Введите корректные данные: ")
        continue
    if a == "":
        break
    b = float(a)
    i += b
    print(i)




        
    


    

    

