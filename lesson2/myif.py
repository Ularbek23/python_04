a = int(input())
sym = input()
b = int(input())
if sym == "+":
    c = a + b
elif sym == "*":
    c = a * b
elif sym == "/":
    c = a / b
elif sym == "**":
    c = a ** b
elif sym == "-":
    c = a - b
else:
    c = "ERROR"
print(c)