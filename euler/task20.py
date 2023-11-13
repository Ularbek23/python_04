class Factorial:
    def __init__(self, n):
        res = 1
        for i in range(1, n + 1):
            res *= i
        self.value = res
    
    def find_sum_num(self):
        str_value = str(self.value) 
        sm = 0
        for k in str_value:
            sm += int(k) 
        return sm

f_10 = Factorial(10)
print(f_10.value)
print(f_10.find_sum_num())

f_100 = Factorial(100)
print(f_100.value)
print(f_100.find_sum_num())