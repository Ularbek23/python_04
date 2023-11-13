mess = input()
i = 0 
count = 1
while i < len(mess):
    sym = mess[i]
    if sym == " ":
        count += 1
    i += 1
print(count)
