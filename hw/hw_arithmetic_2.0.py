def arithmetic(num_1, num_2, znak):
    if znak == "+":
        res = num_1 + num_2
    elif znak == "-":
        res = num_1 - num_2
    elif znak == "*":
        res = num_1 * num_2
    elif znak == "/":
        if num_2 == 0:
            res = "Неизвестная операция"
        else:
            res = num_1 / num_2
    else:
        res = "Неизвестная операция"
    return res
q = arithmetic(6, 0, "/")
print(q)