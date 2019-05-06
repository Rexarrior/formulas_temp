from sympy import var, Rational


def init_symbolic():
    var('D1:4')
    var('B1:4')
    var('L1:4')
    var(' t t0 T x0 ')


class X(object):
    def get_symbolic(self, *args, **kwargs):
        sum_d = (D1 + D2 + D3)
        sum_b = (B1 + B2 + B3)
        return x0 + (sum_b - 3*T*sum_d) * (t - t0) +\
            Rational(3, 2) * sum_d * (t*t - t0 * t0)


class XNE(object):
    def get_symbolic(self, *args, **kwargs):
        sum_d = (D1 + D2 + D3)
        sum_b = (B1 + B2 + B3)
        return x0 + (sum_b - T*sum_d) * (t - t0) +\
            Rational(1, 2) * sum_d * (t*t - t0 * t0)


class U(object):
    def __init__(self, *args, **kwargs):
        self.i = args[0]
        return super().__init__(*args, **kwargs)

    def get_symbolic(self, *args, **kwargs):
        sum_d = (D1 + D2 + D3)
        b = 0
        if self.i == 1:
            b = b1
        elif self.i == 2:
            b = b2
        elif self.i == 3:
            b = b3
        return b - sum_d * (T - t)


