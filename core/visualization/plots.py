import matplotlib.pyplot as plot
import sympy
import numpy as np


def plot_sympy_func(func, args, x_key, xlabel, ylabel, savepath):
    '''
    func - sympy function
    args - list of lists of all func args. 
    x_key - str - name of arg that shoul be ploted as x axis
    '''
    n = len(args)
    x = np.empty(n)
    y = np.empty(n)
    for i in range(n):
        x[i] = args[i][x_key]
        y[y] = func.subs(args[i])
    plot.figure()
    plot.plot(x, y)
    plot.xlabel(xlabel)
    plot.ylabel(ylabel)
    plot.savefig(savepath)
    
