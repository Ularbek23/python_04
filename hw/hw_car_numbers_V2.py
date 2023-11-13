spis = []
while True:
    name = input("Введите Ваше имя: ")
    if not name.isalpha():
        continue
    while True:
        surname = input("Введите Вашу фамилию: ")
        if not surname.isalpha():
            continue
        else:
            break
    while True:    
        numbers = input("Введите номерной знак машины: ")
        if len(numbers) < 6 or len(numbers) > 7:
            continue
        else:
            if len(numbers) == 7 and numbers[:1].isalpha() and numbers[1:5].isdigit() and numbers[5:6].isalpha() and numbers[6:].isalpha():
                break
            elif len(numbers) == 6 and numbers[:1].isalpha() and numbers[1:5].isdigit() and numbers[5:].isalpha():
                break
            elif len(numbers) == 6 and numbers[:3].isdigit() and numbers[3:6].isalpha():
                break
            else:
                continue
    for i in numbers:
        if i.isdigit():
            spis.append(i)
    if len(spis) == 3:
        print(f"{name.capitalize()} {surname.capitalize()}, номерной знак: {numbers}, у Вас новый образец.")
        break
    else:
        print(f"{name.capitalize()} {surname.capitalize()}, номерной знак: {numbers}, у Вас старый образец.")
        break
