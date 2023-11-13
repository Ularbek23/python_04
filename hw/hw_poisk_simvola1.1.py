word = input("Введите текст: ")
sym = input("Введите символ: ")
i = 0
pos = -1
while i < len(word):
    if sym == word[i]:
        pos = i 
        
        break
    i += 1
if pos != -1:
    print(f"Позиция в строке №{pos + 1}")

    
else:
    print("Символ не найден")
