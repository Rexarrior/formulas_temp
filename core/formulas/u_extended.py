from core.formulas.base_formulas import *


class U_alpha(U_base):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def get_symbolic(self):
        part1, sum_b, sum_b_sqr, ds,\
            dn, dsn, s, tdiff = U_base.get_symbolic(self)
        part2 = Rational(1, 6) * s * ds * ds * tdiff**3
        return part1 + part2


class U_delta(U_base):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def get_symbolic(self):
        part1, sum_b, sum_b_sqr, ds,\
            dn, dsn, s, tdiff = U_base.get_symbolic(self)
        part2 = Rational(1, 6) * (2 * dsn * ds + s * ds * ds) * tdiff**3
        return part1 + part2


class U_ksi(U_base):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def get_symbolic(self):
        part1, sum_b, sum_b_sqr, ds,\
            dn, dsn, s, tdiff = U_base.get_symbolic(self)
        part2 = Rational(-1, 6) * s * dn * (dn - 2 * ds) * tdiff**3
        return part1 + part2


class U_eta(U_base):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def get_symbolic(self):
        part1, sum_b, sum_b_sqr, ds,\
            dn, dsn, s, tdiff = U_base.get_symbolic(self)
        part2 = Rational(1, 6) * ((-1 * s * dn * dn) +
                                  (2 * s * dn * ds) + (2 * dn * ds) -
                                  (2 * ds * ds)) * tdiff**3
        return part1 + part2
