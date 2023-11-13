# from my_lib.operation_class import Operation
# from my_lib.operation_class import *
from my_lib import *
res = 0
while True:
    n_1 = int(input())
    if n_1 == 0:
        print(res)
        break
    op_1 = input()
    n_2 = int(input())
    
    op_object = Operation(n_1, op_1, n_2)
    res += op_object.value
    print(res)