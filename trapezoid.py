import math
class Trapezoid:
    def __init__(self, a, b, c, d): #a, b - основания; c, d - стороны
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def get_area(self):
        return ((self.a + self.b) / 2) * (math.sqrt((self.c ** 2 - ((((self.b - self.a) ** 2) + self.c ** 2 - self.d ** 2 )) / (2 * ( self.b - self.a)))) ** 2)
