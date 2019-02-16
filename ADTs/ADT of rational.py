#ADT Rational:
#   Rational(self, int num, int den)
#   +(self, Rational(int num, int den))
#   -(self, Rational(int num, int den))
#   *(self, Rational(int num, int den))
#   //(self, Rational(int num, int den))
#   <(self, Rational(int num, int den))
#   >(self, Rational(int num, int den))
#   =(self, Rational(int num, int den))
#   str(self)
#   print(self)
#   get_num(self)
#   get_den(self)

class Rational():
    @staticmethod
    def __g(m, n):
        if n == 0:
            m, n = n, m
        while m != 0:
            m, n = n % m, m
        return n
    
    def __init__(self, num, den):
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError
        if den == 0:
            raise ZeroDivisionError

        sign = 1
        if num < 0:
            num, sign = -num, -sign
        if den < 0:
            den, sign = -den, -sign
        g = Rational.__g(num, den)
        self._num = sign * (num // g)
        self._den = den // g

    def __add__(self, another):
        num = self._num * another.get_den() + self._den * another.get_num()
        den = self._den * another.get_den()
        return Rational(num, den)

    def __num__(self, another):
        num = self._num * another.get_num()
        den = self._den * another.get_den()
        return Rational(num, den)

    def __sub__(self, another):
        num = self._num * another.get_den() - self._den * another.get_num()
        den = self._den * another.get_den()
        return Rational(num, den)

    def __floordiv__(self, another):
        num = self._num * another.get_den()
        den = self._den * another.get_num()
        return Rational(num, den)

    def __lt__(self, another):
        return (self._num * another.get_den() < self._den * another.get_num())

    def __gt__(self, another):
        return (self._num * another.get_den() > self._den * another.get_num())

    def __eq__(self, another):
        return (self._num * another.get_den() == self._den * another.get_num())

    def __str__(self):
        return (str(self._num) + '/' + str(self._den))

    def print(self):
        print(str(self._num) + '/' + str(self.den))
        
    def get_num(self):
        return self._num

    def get_den(self):
        return self.den
