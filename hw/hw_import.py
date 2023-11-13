import math
from datetime import datetime
from random import randint, choice
result1 = math.cos(math.pi)
result2 = math.sqrt(math.e)
result3 = math.factorial(5)
print(f'''cos(π) = {result1}
√e = {result2}
5! = {result3}
''')

print(datetime.now().time())
li = []
while len(li) < 5:
    rnd = randint(1, 20)
    li.append(rnd)
chc = choice(li)
print(li, chc)
print()
