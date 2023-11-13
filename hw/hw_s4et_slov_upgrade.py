num = {}
word = input("")
b = list(word)
c = 0
h = []
n = []
while c < len(b):
    if not b[c].isalnum():
        n.append(b[c])
    if b[c].isalnum() or b[c] == " ":
        h.append(b[c])
    c += 1
m = ""
for d in h:
    m += d
t = m.split(" ") 
for i in t:
    if i == "":
        continue
    if i in num:
        num[i] += 1
    else:
        num[i] = 1
for key in num:
    print(key, num[key])    

print(num)
