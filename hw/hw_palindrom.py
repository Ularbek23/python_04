word = input("").lower()
print(word)
i = 0
b = ""
lst = list(word)
while i < len(lst):
    sym = lst[i]
    i += 1     
    if sym == " ":
        continue
    b = b + sym  
if b == b[::-1]:
    print("Палиндром")            
else:
    print("Не Палиндром") 
print(b) 

# a = input("")
# st = a.replace(" ", "").lower()
# if st == st[::-1]:
#     print("Палиндром")
# else:
#     print("Не Палиндром")