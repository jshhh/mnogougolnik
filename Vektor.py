from math import *

class Vektor:
    def __init__(self, x=None, y=None, l=None, a=None):
        if x is not None and y is not None:
            self.x = x
            self.y = y
        elif l is not None and a is not None:
            self.x = l
            self.y = 0
            if a != 0:
                v1 = self.rotate(a)
                self.x = v1.x
                self.y = v1.y

    def rotate(self, a):
        a = a / 180 * pi
        x = self.x * cos(a) - self.y * sin(a)
        y = self.x * sin(a) + self.y * cos(a)
        return Vektor(x, y)