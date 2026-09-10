import math
from cmath import atan


class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im


    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)
        elif isinstance(other, (int, float)):
            return Complex(self.re + other, self.im)
        else:
            raise TypeError("no")

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)
        elif isinstance(other, (int, float)):
            return Complex(self.re + other, self.im)
        else:
            raise TypeError("no")

    def __mul__(self, other):
        return Complex(self.re * other.re -(self.im * other.im), self.re * other.im + self.im * other.re)

    def __truediv__(self, other):
        numerator = self * Complex(other.re, -other.im)
        denominator = other * Complex(other.re, -other.im)
        return Complex(numerator.re / denominator.re, numerator.im / denominator.re)

    def __repr__(self):
        return f"Complex(re={self.re!r}, im={self.im!r})"

    def __str__(self):
        return f"{self.re}+{self.im}i" if self.im >= 0 else f"{self.re}{self.im}i"

    def _find_r(self):
        return (self.re ** 2 + self.im ** 2) ** 0.5

    def _fi(self):
        a, b = self.re, self.im
        if a > 0:
            return atan(abs(b / a))
        elif b > 0:
            return math.pi + atan(b / a)
        elif b < 0:
            return -math.pi + atan(b / a)
        elif a == 0 and b > 0:
            return math.pi / 2
        elif a == 0 and b < 0:
            return -math.pi / 2
        return None


    def as_trig(self):
        return f"{self._find_r()}(cos({self._fi()})+isin({self._fi()}))"

a = Complex(1, 1)
b = Complex(2, 0)

print(a.as_trig())