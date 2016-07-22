import sympy
import math

from sympy.parsing.sympy_parser import parse_expr


def quadratic_function_call(inpt, quad_val):
    plug_in = "(" + inpt + ")"
    quad_val = quad_val.replace("x", plug_in)
    return eval(quad_val)


def quadratic_find_discriminant(a, b, c):
    return float((b ** 2) - (4 * a * c))


def quadratic_find_roots(quad_val):
    x = sympy.Symbol("x")
    solution_ls = sympy.solve(sympy.Eq(parse_expr(quad_val), parse_expr("0")), x)
    solution_str = ""
    for sol_ind in range(0, len(solution_ls)):
        if (len(solution_ls) - 1) != sol_ind:
            solution_str += "x = " + str(solution_ls[sol_ind]) + "\n"
        else:
            solution_str += "x = " + str(solution_ls[sol_ind])

    return solution_str


def quadratic_find_y_int(quad_val):
    quad_val = quad_val.replace("x", "0")
    return eval(quad_val)


def quadratic_find_vertex(a, b, quad_val):
    x = float((-b) / (2 * a))
    y = float(quadratic_function_call(str(x), quad_val))
    return [x, y]


def quadratic_factor(quad_val):
    return sympy.factor(quad_val)


def quadratic_expand(quad_val):
    return sympy.expand(quad_val)


def find_a_b_c(quad_val):
    x = sympy.Symbol("x")
    a_b_c = sympy.Poly(quad_val, x)
    return a_b_c.all_coeffs()
