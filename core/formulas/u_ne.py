import core.formulas.shepli
from  sympy import var

var('V1:4')
var('B1:4')
var('L1:4')
var('S t T x0 ')

class U_NE(object):
    def __init__(self, *args, **kwargs):
        '''
        first arg is i - position in vector
        second arg is instance of shepli class
        '''
        self.b = args[1].get_diff_symbolic()
        self.d = 0
        sum_v = V1 + V2 + V3
        if args[0] == 1:
            self.d = L1 / sum_v
        elif args[0] == 2:
            self.d = L2 / sum_v
        elif args[0] == 3:
            self.d = L3 / sum_v
    
    def get_symbolic(self):
        return self.b - self.d * (T - t)
        