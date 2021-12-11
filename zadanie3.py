class MyMath:

    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)

    def substraction(self):
        return self.a - self.b


    def addition(self):
        return self.a+self.b

    def multiplication(self):
        return self.a*self.b

    def division(self):
        if self.b == 0:
            raise ValueError()
        return self.a/self.b


