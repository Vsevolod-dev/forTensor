class X: 
    def __init__(self, x): 
        self.x = x 

    def __add__(self, y): 
        return self.x - y.x 

    def __sub__(self, y):
        return self.x ** y.x

    def __mul__(self, y):
        return pow(self.x + y.x, 0.5)

    def __truediv__(self, y):
        return self.x % y.x

    def __lt__(self, y):
        return self.x > y.x


ob1 = X(15) 
ob2 = X(32)  
print(ob1 + ob2)
print(ob1 - ob2)
print(ob1 * ob2)
print(ob1 / ob2)
print(ob1 < ob2)