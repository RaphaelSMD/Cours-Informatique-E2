class Fraction :
    def __init__(self, num:int, den:int):
        if den == 0:
            raise ValueError("Denominator cannot be zero.")
        self.num = num
        self.den = den
    def __str__(self):
        if self.den == 1:
            return str(self.num)
        return f"{self.num}/{self.den}"
    def __add__(self, f):
        return Fraction(self.num * f.den + f.num * self.den, self.den * f.den)

    def __sub__(self, f):
        return Fraction(self.num * f.den - f.num * self.den, self.den * f.den)

    def __mul__(self, f):
        return Fraction(self.num * f.num, self.den * f.den)

    def __truediv__(self, f):
        return Fraction(self.num * f.den, self.den * f.num)

    def __eq__(self, f):
        return self.num * f.den == f.num * self.den

    def __ne__(self, f):
        return not self == f

    def __lt__(self, f):
        return self.num * f.den < f.num * self.den

    def __gt__(self, f):
        return self.num * f.den > f.num * self.den

    def __le__(self, f):
        return self.num * f.den <= f.num * self.den

    def __ge__(self, f):
        return self.num * f.den >= f.num * self.den

if __name__ == "__main__":
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 4)

    print(f"f1 = {f1}")
    print(f"f2 = {f2}")
    print(f"f1 + f2 = {f1 + f2}")
    print(f"f1 - f2 = {f1 - f2}")
    print(f"f1 * f2 = {f1 * f2}")
    print(f"f1 / f2 = {f1 / f2}")
    print(f"f1 > f2 : {f1 > f2}")
    print(f"f1 == f2 : {f1 == f2}")