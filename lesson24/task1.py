class Counting:
    balance = 0
    def plus(self, num):
        self.balance += num

    def minus(self, num):
        self.balance -= num

qwe = Counting()
print(qwe.balance)
qwe.plus(230)
print(qwe.balance)
qwe.minus(120)
print(qwe.balance)