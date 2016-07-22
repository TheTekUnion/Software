import math
import sympy
from sympy.parsing.sympy_parser import parse_expr


def func_call(inpt, func_val):
    plug_in = "(" + inpt + ")"
    func_val = func_val.replace("x", plug_in)
    return eval(func_val)


def find_roots(func_val):
    x = sympy.Symbol("x")
    solution_ls = sympy.solve(sympy.Eq(parse_expr(func_val), parse_expr("0")), x)
    solution_str = ""
    for sol_ind in range(0, len(solution_ls)):
        if (len(solution_ls) - 1) != sol_ind:
            solution_str += "x = " + str(solution_ls[sol_ind]) + "\n"
        else:
            solution_str += "x = " + str(solution_ls[sol_ind])

    return solution_str


def find_y_int(func_val):
    func_val = func_val.replace("x", "0")
    return eval(func_val)


def factor_func(func_val):
    return sympy.factor(func_val)


def expand_func(func_val):
    return sympy.expand(func_val)

