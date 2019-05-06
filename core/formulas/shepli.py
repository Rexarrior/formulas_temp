from core.formulas.base_formulas import *


class Shepli(object):
    def __init__(self, *args, **kwargs):
        s_set_list = args[0]
        s_list = []
        for s_set in s_set_list:
            s_list.append(SClass(s_set))
        uclass = args[1]
        self.u_list = []
        for s in s_list:
            self.u_list.append(uclass(s).get_symbolic())

    def get_symbolic(self):
        part1 = Rational(-1, 3)*(self.u_list[0] - self.u_list[1])
        part2 = Rational(1, 6)*(self.u_list[2] - self.u_list[3])
        part3 = self.u_list[4] - self.u_list[5]
        part4 = Rational(1, 3) * self.u_list[6]
        return part1 + part2 + part3 + part4
