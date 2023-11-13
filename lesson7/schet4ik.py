a = input("")
b = list(a)
c = 0
g = 2
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
    print(d)

print(h)
print(m)