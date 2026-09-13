class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError
        self.num = numerator
        self.den = denominator
        Fraction.simplify(self)

    @staticmethod
    def _valid(other):
        if isinstance(other, (int, Fraction)):
            if isinstance(other, int):
                return Fraction(other, 1)
            return other
        raise TypeError

    def simplify(self):
        if self.num < 0 and self.den < 0:
            self.num, self.den = -self.num, -self.den
        nod = Fraction.nod(self.num, self.den)
        self.num //= nod
        self.den //= nod

    def int_part(self):
        return self.num // self.den

    def __add__(self, other):
        other = Fraction._valid(other)
        nok = Fraction.nok(self.den, other.den)
        return Fraction(nok // self.den * self.num + nok // other.den * other.num, nok)

    def __sub__(self, other):
        other = Fraction._valid(other)
        nok = Fraction.nok(self.den, other.den)
        return Fraction(nok // self.den * self.num - nok // other.den * other.num, nok)

    def __mul__(self, other):
        other = Fraction._valid(other)
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        other = Fraction._valid(other)
        other.num, other.den = other.den, other.num
        return Fraction(self.num * other.num, self.den * other.den)

    def __pow__(self, power):
        return Fraction(self.num ** power, self.den ** power)

    @staticmethod
    def factor(n):
        res = dict()
        while n > 1:
            for div in range(2, int(n ** 0.5) + 1):
                if n % div == 0:
                    res[div] = res.get(div, 0) + 1
                    n //= div
                    break
            else:
                res[n] = res.get(n, 0) + 1
                return res
        return res

    @staticmethod
    def nod(a, b):
        fa = Fraction.factor(a)
        fb = Fraction.factor(b)
        res = 1
        commons = set(fa.keys()) & set(fb.keys())
        for f in commons:
            res *= f ** min(fa[f], fb[f])
        return res

    @staticmethod
    def nok(a, b):
        fa = Fraction.factor(a)
        fb = Fraction.factor(b)
        res = 1
        every = set(fa.keys()) | set(fb.keys())
        for f in every:
            res *= f ** max(fa.get(f, 0), fb.get(f, 0))
        return res

    @staticmethod
    def float_to_fraction(x):
        n = len(str(x).split('.')[1])
        return Fraction(int(x * 10 ** n), 10 ** n)

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraction(numerator={self.num}, denominator={self.den})"

a = Fraction(-2, -4)
b = Fraction(2, 3)