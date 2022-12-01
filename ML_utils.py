import numpy as np
import matplotlib.pyplot as plt

class LinearFunction():
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
        return LinearFunction(self.m, self.b)
        
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

def ableitung(funktion, x, h=0.001):
    output = []
    for i in range(len(x)):
        onehot = onehotvector(i,len(x))
        abl = (funktion(x+onehot*h)-funktion(x))/h
        output.append(abl)
    return np.array(output)

def onehotvector(i, laenge):
    one_hot = np.zeros(laenge)
    one_hot[i] = 1
    return one_hot

def get_data(n, m):
    means = 4*np.random.randn(m,2)
    data = np.zeros([1,2])
    label = []
    for i in range(m):
        d = np.random.randn(n, 2) + means[i]
        data = np.row_stack((data, d))
        label.extend(n*[i])
    return data[1:],np.array(label)

def plot_stuff(data, pred, plotline=None):
    plt.figure()
    plt.scatter(data[pred==0, 0], data[pred==0, 1], marker=".", c="b")
    plt.scatter(data[pred==1, 0], data[pred==1, 1], marker=".", c="r")
    if plotline:
        ax = plt.gca()
        f.plot_classline(ax)
    plt.show()
    
class LinClass():
    def __init__(self, params=np.array([-1,1,1])):
        self.params = params

    def __call__(self, x):
        x = np.column_stack((x, -np.ones(len(x))))
        return self.params@x.T

    def get_predictions(self, x):
        return (self.__call__(data)>0)

    def plot_classline(self,  ax):
        weights = self.params[:-1]
        threshold = self.params[-1]
        assert weights.any(), "Weights must not be the zero vector."
        x_min, x_max = ax.get_xbound()
        y_min, y_max = ax.get_ybound()
        if weights[1] == 0:
            x_min = threshold / weights[0]
            x_max = x_min
        else:
            y_min = (threshold - weights[0] * x_min) / weights[1]
            y_max = (threshold - weights[0] * x_max) / weights[1]
        plt.plot([x_min, x_max], [y_min, y_max], "g")
