class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        for i in range(self.b):
            if i==0 or i==self.b-1:
                for j in range(self.a):
                    print('*',end='')
            else:
                print('*',end='')
                for j in range(1,self.a-1):
                    print(' ',end='')
                print('*',end='')
            print()

figure_1 = Rectangle(7, 4)
figure_1.show()