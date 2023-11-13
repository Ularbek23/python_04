#1
def create_squares_dict(n):
    res = {i: i ** 2 for i in range(1, n+1)}
    return res
print(create_squares_dict(5))

#2
def generate_even_numbers(n):
    res_2 = [j for j in range(1, n+1) if j % 2 == 0]
    return res_2
print(generate_even_numbers(23))