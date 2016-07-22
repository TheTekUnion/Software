import math
import sympy
from sympy.parsing.sympy_parser import parse_expr


def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


def equation_of_line_slope_int(x1, y1, x2, y2):
    m = slope(x1, y1, x2, y2)
    b = sympy.Symbol("b")
    equation = "y = " + str(m) + " * x + b"
    equation = equation.replace("y", str(y1))
    equation = equation.replace("x", str(x1))
    equation = equation.split("=")
    b = sympy.solve(sympy.Eq(parse_expr(equation[0]), parse_expr(equation[1])), b)
    if b[0] != 0 and m != 0:
        return "y = " + str(m) + " * x + " + str(float(b[0]))
    elif b[0] == 0 and m != 0:
        return "y = " + str(m) + " * x"
    elif b[0] != 0 and m == 0:
        return "y = " + str(float(b[0]))
