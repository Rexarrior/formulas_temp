from utils import *
from sympy import var, Rational


def init_symbolic():
    var('V1:4')
    var('B1:4')
    var('L1:4')
    var('S t T x0 ')


class SClass(object):
    def __init__(self, *args, **kwargs):
        self.List = []
        if (len(args) > 0):
            self.List = args[0]
        if ('List' in kwargs):
            self.List = kwargs['List']

    def get_value_lambda(self, params):
        return lambda x0, t,  l1, l2, l3: len(self.List)

    def get_str(self, params):
        return str(len(self.List))
        # return "{" + ", ".join(self.List) + "}"

    def get_symbolic(self):
        return S

    def compute_value(self):
        return len(self.List)


class Ds(object):
    def __init__(self, *args, **kwargs):
        if ('s' in kwargs):
            self.S = kwargs['s']
        else:
            self.S = args[0]

    def get_symbolic(self):
        sum_v = V1 + V2 + V3
        ret = 0
        if (1 in self.S.List):
            ret += L1
        if (2 in self.S.List):
            ret += L2
        if (3 in self.S.List):
            ret += L3
        ret = ret / sum_v
        return ret


class Dsn(object):
    def __init__(self, *args, **kwargs):
        if ('s' in kwargs):
            self.S = kwargs['s']
        else:
            self.S = args[0]

    def get_symbolic(self):
        sum_v = V1 + V2 + V3
        ret = 0
        if not(1 in self.S.List):
            ret += L1
        if not(2 in self.S.List):
            ret += L2
        if not(3 in self.S.List):
            ret += L3
        ret = ret / sum_v
        return ret


class Dn(object):
    def __init__(self, *args, **kwargs):
        if ('s' in kwargs):
            self.S = kwargs['s']
        else:
            self.S = args[0]

    def get_value_lambda(self, params):
        sum_v = sum([params['V'+str(i+1)] for i in range(3)])
        return lambda x0, t,  l1, l2, l3: (l1 + l2 + l3) / sum_v

    def get_str(self, params):
        sum_v = str(sum([params['V'+str(i+1)] for i in range(3)]))
        return "(l1 + l2 + l3) / " + sum_v

    def get_symbolic(self):
        sum_v = V1 + V2 + V3
        return (L1 + L2 + L3) / sum_v


class U_base(object):
    def __init__(self, *args, **kwargs):
        if ('s' in kwargs):
            self.S = kwargs['s']
        else:
            self.S = args[0]
        self.Ds = Ds(self.S)
        self.Dn = Dn(self.S)
        self.Dsn = Dsn(self.S)

    def get_symbolic(self):
        sum_b = B1 + B2 + B3
        sum_b_sqr = 0
        if (1 in self.S.List):
            sum_b_sqr += B1 * B1
        if (2 in self.S.List):
            sum_b_sqr += B2 * B2
        if (3 in self.S.List):
            sum_b_sqr += B3 * B3
        tdiff = T - t
        ds = self.Ds.get_symbolic()
        dn = self.Dn.get_symbolic()
        dsn = self.Dsn.get_symbolic()
        s = self.S.get_symbolic()
        part1 = - ds * tdiff * x0
        part2 = Rational(1, 2) * sum_b_sqr * tdiff
        part3 = Rational(-1, 2) * sum_b * ds * tdiff**2
        return part1 + part2 + part3, sum_b, sum_b_sqr, ds, dn, dsn, s, tdiff
