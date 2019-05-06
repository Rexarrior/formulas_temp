from formulas import *
from utils import *
import json
import sympy as sp
import core.plots as my_plt

shepli_args = [
    [[1, 2, 3], [2, 3], [1, 2], [2], [1, 3], [3], [1]],
    [[1, 2, 3], [1, 3], [1, 2], [1], [2, 3], [3], [2]],
    [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3]]
]


def read_fname(s):
    print(f"write {s} file name: ", end='')
    fname = input()
    return fname


def read_data(s):
    fname = read_fname(s)
    with open(fname, 'rt', encoding='utf8') as f:
        return json.loads(f.read())


def save_data(data, s):
    fname = read_fname(s)
    with open(fname, 'wt', encoding='utf8') as f:
        f.write(json.dumps(data))


def plot_all():
    funcs = {'x': X().get_symbolic(),
             'x_ne': XNE().get_symbolic(),
             }
    for i in range(1, 4):
        funcs['u' + str(i)] = U(i).get_symbolic()
    parameters = read_data("plot parameters")
    tmin = parameters['t_min']
    step = parameters['t_step']
    tmax = parameters['t_max']
    for t in range(tmin, tmax, step):
        parameters['t'] = t
        for key in funcs.keys():
            my_plt.plot_sympy_func(funcs[key], parameters, 't', 't', key, f'.\\plots\\'):


def show_dict(dct):
    for key in dct.keys():
        print(f'{key}: {dct[key]}\n')


def apply_params(formulas, params):
    u_res = {}
    for key in formulas.keys():
        #  x0, t,  l1, l2, l3
        u_res[key] = formulas[key]
        for param_key in params.keys():
            u_res[key] = u_res[key].subs(param_key, params[param_key])
        # u_res[key] = sp.simplify(u_res[key])
    return u_res


def compute_bi(params):
    for i in range(1, 4):
        params['B' + str(i)] = params['P' + str(i)] / params['V' + str(i)]
    return params


def init():
    params = read_data("input parameters")
    params = compute_bi(params)
    s = SClass(params['S'])
    u_classes = {'U_alpha': U_alpha(s),
         'U_delta': U_delta(s),
         'U_ksi': U_ksi(s),
         'U_eta': U_eta(s)
         }
    shepli_classes = {
         'Sh_alpha_1': Shepli(shepli_args[0], U_alpha),
         'Sh_alpha_2': Shepli(shepli_args[1], U_alpha),
         'Sh_alpha_3': Shepli(shepli_args[2], U_alpha),
         'Sh_delta_1': Shepli(shepli_args[0], U_delta),
         'Sh_delta_2': Shepli(shepli_args[1], U_delta),
         'Sh_delta_3': Shepli(shepli_args[2], U_delta),
         'Sh_ksi_1': Shepli(shepli_args[0], U_ksi),
         'Sh_ksi_2': Shepli(shepli_args[1], U_ksi),
         'Sh_ksi_3': Shepli(shepli_args[2], U_ksi),
         'Sh_eta_1': Shepli(shepli_args[0], U_eta),
         'Sh_eta_2': Shepli(shepli_args[1], U_eta),
         'Sh_eta_3': Shepli(shepli_args[2], U_eta)
    }
    u_formulas = {}
    for key in u_classes.keys():
        u_formulas[key] = u_classes[key].get_symbolic()
    shepli_formulas = {}
    for key in shepli_classes.keys():
        shepli_formulas[key] = shepli_classes[key].get_symbolic()
    params['S'] = s.compute_value()
    return u_formulas, shepli_formulas, params


def read_use_command():
    print("Commands:\n")
    print("1. Load parameters\n")
    print("2. Change parameter \n")
    print("3. Compute results\n")
    print("4. Save results\n")
    print("5. Show formulas\n")
    print("6. Show unknown parameters\n")
    print("7. Delete parameter\n")
    print("8. Back to main menu\n")
    print("write number of command: ", end='')
    return input()


def change_parameter(params):
    print("Write parameter name:")
    key = input()
    print("write parameter value (number)")
    value = input()
    try:
        value = int(value)
    except:
        print("bad value.")
        return params
    params[key] = value
    return params


def delete_parameter(params):
    print("Write parameter name:")
    key = input()
    if (key in params):
        params[key] = value
    else:
        print(" can't delete. unknown parameter")
    return params


def use_loop(formulas, params):
    res = formulas
    while True:
        command = read_use_command()
        if (command == '1'):
            params.update(read_data("unknown parameters"))
        elif (command == '2'):
            params = change_parameter(params)
        elif (command == '3'):
            res = apply_params(formulas, params)
            show_dict(res)
        elif (command == '4'):
            save_data({key: str(res[key]) for key in res}, "results")
        elif (command == '5'):
            show_dict(formulas)
        elif (command == '6'):
            show_dict(params)
        elif (command == '7'):
            params = delete_parameter(params)
        elif (command == '8'):
            return


def read_main_command():
    print("Commands:\n")
    print("1. Load input parameters\n")
    print("2. Use current u functions:\n")
    print("3. Use current shepli functions:\n")
    print("4. Exit\n")
    print("write number of command: ", end='')
    return input()


def main_loop():
    init_symbolic()
    u_formulas, shepli_formulas, params = init()
    while True:
        command = read_main_command()
        if (command == '1'):
            u_formulas, shepli_formulas, params = init()
        elif (command == '2'):
            use_loop(u_formulas, params)
        elif (command == '3'):
            use_loop(shepli_formulas, params)
        elif (command == '4'):
            return None

if __name__ == "__main__":
    main_loop()
