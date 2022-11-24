import numpy as np
import matplotlib.pyplot as plt

class lineareFunktion():
    def __init__(self, m=1, b=-1):
        self.m = m
        self.b = b

    def __call__(self, x):
        return self.m*x+self.b

    def __str__(self):
        if self.m==0:
            return str(self.b)
        op = "+" if self.b>=0 else "-"
        b = self.b
        if b==0:
            return f"{self.m}*x"
        return f"{self.m}*x{op}{np.abs(b)}"

    def copy(self):
        return lineareFunktion(self.m, self.b)
        
class QuadraticFunction():
    def __init__(self, a=1, b=1, c=1):
        self.a = a
        self.b = b
        self.c = c
        
    def __call__(self, x):
        return self.a*x**2+self.b*x+self.c

    def __str__(self):
        op1 = "+" if self.b>=0 else "-"
        op2 = "+" if self.c>=0 else "-"
        return f"{self.a}*x^2{op1}{np.abs(self.b)}*x{op2}{np.abs(self.c)}"
        
    def copy(self):
        return QuadraticFunction(self.a, self.b, self.c)
