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


def plot_funcs(funcs, path):
    parameters = read_data("plot parameters")
    tmin = parameters['t_min']
    step = parameters['t_step']
    tmax = parameters['t_max']
    for t in range(tmin, tmax, step):
        parameters['t'] = t
        for key in funcs.keys():
            my_plt.plot_sympy_func(funcs[key], parameters, 't', 't', key, path)


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


def classes_to_formulas(classes):
    formulas = {}
    for key in classes.keys():
        formulas[key] = classes[key].get_symbolic()
    return formulas


def init_u(params):
    s = SClass(params['S'])
    u_classes = {'U_alpha': U_alpha(s),
         'U_delta': U_delta(s),
         'U_ksi': U_ksi(s),
         'U_eta': U_eta(s)
         }
    return classes_to_formulas(u_classes)
    

def init_shepli():
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
    return classes_to_formulas(shepli_classes)


def get_derivatives(formulas):
    ders = {}
    for key in formulas.keys():
        ders[key + '_derivative'] = sp.diff(formulas[key], 't')
    return ders


def init_simple_plot_funcs():
    classes = {
        "X":X(),
        "XNE":XNE(),
        "U1":U(1),
        "U2":U(2),
        "U3":U(3)
    }
    return classes_to_formulas(classes)


def init():
    params = read_data("input parameters")
    params = compute_bi(params)
    formulas = {}
    u_formulas = init_u(params)
    shepli_formulas = init_shepli()
    shepli_ders = get_derivatives(shepli_formulas)
    formulas['u'] = u_formulas
    formulas['shelpli'] = shepli_formulas
    formulas['shepli_ders'] = shepli_ders
    formulas['simple_plot_funcs'] = init_simple_plot_funcs()
    
    params['S'] = s.compute_value()
    return formulas, params


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
        del params[key]
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
    print("4. Plot x,xne,un functions\n")
    print("5. Plot u functions\n")
    print("6. Plot shepli functions\n")
    print("7. Plot derivatives of shepli functions\n")
    print("8. Plot all\n")
    print("9. Exit\n")
    print("write number of command: ", end='')
    return input()


def main_loop():
    formulas, params = init()
    all_formulas = {}
    for key in formulas.keys():
        all_formulas.update(formulas[key])
    while True:
        command = read_main_command()
        if (command == '1'):
            formulas, params = init()
        elif (command == '2'):
            use_loop(formulas['u'], params)
        elif (command == '3'):
            use_loop(formulas['shepli'], params)
        elif (command == '4'):
            plot_funcs(formulas['simple_plot_funcs'], '.\\plots\\simple')
        elif (command == '5'):
            plot_funcs(formulas['u'], '.\\plots\\u_functions\\')
        elif (command == '6'):
            plot_funcs(formulas['shepli'], '.\\plots\\shepli\\')
        elif (command == '7'):
            plot_funcs(formulas['shepli_der'], '.\\plots\\shepli_der\\')
        elif (command == '8'):
            plot_funcs(all_formulas, '.\\plots\\all\\')
        elif (command == '9'):
            return None
f'.\\plots\\'
if __name__ == "__main__":
    main_loop()
