from sympy import var, Rational


var('V1:4')
var('B1:4')
var('L1:4')
var(' t t0 T x0 ')


class X(object):
    def get_symbolic(self, *args, **kwargs):
        sum_d = (L1 + L2 + L3) / (V1 + V2 + V3)
        sum_b = (B1 + B2 + B3)
        return x0 + (sum_b - 3*T*sum_d) * (t - t0) +\
            Rational(3, 2) * sum_d * (t*t - t0 * t0)


class XNE(object):
    def get_symbolic(self, *args, **kwargs):
        sum_d = (L1 + L2 + L3) / (V1 + V2 + V3)
        sum_b = (B1 + B2 + B3)
        return x0 + (sum_b - T*sum_d) * (t - t0) +\
            Rational(1, 2) * sum_d * (t*t - t0 * t0)


class U(object):
    def __init__(self, *args, **kwargs):
        self.i = args[0]

    def get_symbolic(self, *args, **kwargs):
        sum_d = (L1 + L2 + L3) / (V1 + V2 + V3)
        b = 0
        if self.i == 1:
            b = B1
        elif self.i == 2:
            b = B2
        elif self.i == 3:
            b = B3
        return b - sum_d * (T - t)


