
def lmd_sum(*args):
    if (len(args) == 0):
        return lmd_const(0)
    return lambda x0, t,  l1, l2, l3: args[0](x0, t,  l1, l2, l3) + \
                                      lmd_sum(*args[1:])(x0, t,  l1, l2, l3)


def lmd_minus(*args):
    if (len(args) == 0):
        return lmd_const(0)
    return lambda x0, t,  l1, l2, l3: args[0](x0, t,  l1, l2, l3) - \
                                      lmd_minus(*args[1:])(x0, t,  l1, l2, l3)


def lmd_product(*args):
    if (len(args) == 0):
        return lmd_const(1)
    return lambda x0, t,  l1, l2, l3: args[0](x0, t,  l1, l2, l3) * \
                                      lmd_product(*args[1:])(x0, t,  l1, l2, l3)


def lmd_devide(*args):
    if (len(args) == 0):
        return lmd_const(1)
    return lambda x0, t,  l1, l2, l3: args[0](x0, t,  l1, l2, l3) /\
                                      lmd_devide(*args[1:])(x0, t,  l1, l2, l3)


def lmd_pow(*args):
    return lambda x0, t,  l1, l2, l3: args[0](x0, t,  l1, l2, l3)**args[1]


def lmd_const(c):
    return lambda x0, t, l1, l2, l3: c


def str_sum(*args):
    return " + ".join(args)


def str_minus(*args):
    return " - ".join(args)


def str_product(*args):
    return " * ".join(args)


def str_devide(*args):
    return " / ".join(args)


def str_pow(*args):
    return f'{args[0]}^{args[1]}'


def str_const(c):
    return f"{c}"
