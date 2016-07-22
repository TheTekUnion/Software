import sympy
import math
from sympy.parsing.sympy_parser import parse_expr


def evaluate_expression(n_vars):

    var_names = []
    var_values = []

    for i in range(1, n_vars + 1):
        name = input("Enter the name of variable " + str(i) + ": ")
        var_names.append(name)
        value = float(eval(input("Enter the value of " + name + ": ")))
        var_values.append(value)

    for i in range(0, n_vars):
        exec(str(var_names[i]) + " = " + str(var_values[i]))

    expression = input("Enter your expression that contains the variables you have defined: ")
    return [eval(expression), expression]


#Solve algebraic equations using SymPy
def solve_equation(equation, variable):
    if "math.pi" in equation:
        value = math.pi
        equation = equation.replace("math.pi", str(value))

    if "math.e" in equation:
        value = math.e
        equation = equation.replace("math.e", str(value))

    var = sympy.Symbol(variable)
    expressions = equation.split("=")
    left_expression = expressions[0]
    right_expression = expressions[1]

    solution_ls = sympy.solve(sympy.Eq(parse_expr(left_expression), parse_expr(right_expression)), var)
    solution_str = ""
    for sol_ind in range(0, len(solution_ls)):
        if (len(solution_ls) - 1) != sol_ind:
            assignment_str = variable + " = " + str(solution_ls[sol_ind]) + "\n"
            solution_str += assignment_str
        else:
            assignment_str = variable + " = " + str(solution_ls[sol_ind])
            solution_str += assignment_str

    return solution_str


#Solve system of equations algebraically using substitution and SymPy
def system_of_equations_substitution(equation1, equation2):
    if "math.pi" in equation1:
        value = math.pi
        equation1 = equation1.replace("math.pi", str(value))

    if "math.e" in equation1:
        value = math.e
        equation1 = equation1.replace("math.e", str(value))

    if "math.pi" in equation2:
        value = math.pi
        equation2 = equation2.replace("math.pi", str(value))

    if "math.e" in equation2:
        value = math.e
        equation2 = equation2.replace("math.e", str(value))

    x = sympy.Symbol("x")
    y = sympy.Symbol("y")

    #Equation 1
    expressions1 = equation1.split("=")

    #Equation 2
    expressions2 = equation2.split("=")

    if "y" in expressions1[0].lower():

        if "y" in expressions2[0].lower():
            expressions2[0] = expressions2[0].replace("y", expressions1[1])

        elif "y" in expressions2[1].lower():
            expressions2[1] = expressions2[1].replace("y", expressions1[1])

        else:
            return "Invalid format. Please solve for y in at least one equation. "

        x_sol_ls = sympy.solve(sympy.Eq(parse_expr(expressions2[0]), parse_expr(expressions2[1])), x)

        y_sol_ls = []

        for solution in x_sol_ls:
            temp = expressions1[1]
            plug_in = "(" + str(solution) + ")"

            expressions1[1] = expressions1[1].replace("x", plug_in)

            y_sol = sympy.solve(sympy.Eq(parse_expr(expressions1[0]), parse_expr(expressions1[1])), y)

            y_sol_ls.append(y_sol[0])

            expressions1[1] = temp

        #If the length of the solution list is equal to zero, then print out no solution
        if len(x_sol_ls) == 0:
            return "This systems of equations has no solution. "

        #Otherwise, output as an ordered pair or ordered pairs.
        if len(x_sol_ls) == 1:
            return str((x_sol_ls[0], y_sol_ls[0]))

        else:
            solution_str = ""
            for num_sol in range(0, len(x_sol_ls)):
                if (len(x_sol_ls) - 1) != num_sol:
                    solution_str += str((x_sol_ls[num_sol], y_sol_ls[num_sol])) + ", "
                else:
                    solution_str += str((x_sol_ls[num_sol], y_sol_ls[num_sol]))

            return solution_str

    elif "y" in expressions1[1].lower():

        if "y" in expressions2[0].lower():
            expressions2[0] = expressions2[0].replace("y", expressions1[0])

        elif "y" in expressions2[1].lower():
            expressions2[1] = expressions2[1].replace("y", expressions1[0])

        else:
            return "Invalid format. Please solve for y in at least one equation. "

        x_sol_ls = sympy.solve(sympy.Eq(parse_expr(expressions2[0]), parse_expr(expressions2[1])), x)

        y_sol_ls = []

        for solution in x_sol_ls:
            temp = expressions1[1]
            plug_in = "(" + str(solution) + ")"

            expressions1[1] = expressions1[1].replace("x", plug_in)

            y_sol = sympy.solve(sympy.Eq(parse_expr(expressions1[0]), parse_expr(expressions1[1])), y)

            y_sol_ls.append(y_sol[0])

            expressions1[1] = temp

        #If the length of the solution list is equal to zero, then print out no solution
        if len(x_sol_ls) == 0:
            return "This systems of equations has no solution. "

        #Otherwise, output as an ordered pair or ordered pairs.
        if len(x_sol_ls) == 1:
            return str((x_sol_ls[0], y_sol_ls[0]))

        else:
            solution_str = ""
            for num_sol in range(0, len(x_sol_ls)):
                if (len(x_sol_ls) - 1) != num_sol:
                    solution_str += str((x_sol_ls[num_sol], y_sol_ls[num_sol])) + ", "
                else:
                    solution_str += str((x_sol_ls[num_sol], y_sol_ls[num_sol]))

            return solution_str

    elif "y" in expressions2[0].lower():

        if "y" in expressions1[0].lower():
            expressions1[0] = expressions1[0].replace("y", expressions2[1])

        elif "y" in expressions1[1].lower():
            expressions1[1] = expressions1[1].replace("y", expressions2[1])

        else:
            return "This system of equations has no solution. "

        x_sol_ls = sympy.solve(sympy.Eq(parse_expr(expressions2[0]), parse_expr(expressions2[1])), x)

        y_sol_ls = []

        for solution in x_sol_ls:
            temp = expressions1[1]
            plug_in = "(" + str(solution) + ")"

            expressions1[1] = expressions1[1].replace("x", plug_in)

            y_sol = sympy.solve(sympy.Eq(parse_expr(expressions1[0]), parse_expr(expressions1[1])), y)

            y_sol_ls.append(y_sol[0])

            expressions1[1] = temp

        #If the length of the solution list is equal to zero, then print out no solution
        if len(x_sol_ls) == 0:
            return "This systems of equations has no solution. "

        #Otherwise, output as an ordered pair or ordered pairs.
        if len(x_sol_ls) == 1:
            return str((x_sol_ls[0], y_sol_ls[0]))

        else:
            solution_str = ""
            for num_sol in range(0, len(x_sol_ls)):
                if (len(x_sol_ls) - 1) != num_sol:
                    solution_str += str((x_sol_ls[num_sol], y_sol_ls[num_sol])) + ", "
                else:
                    solution_str += str((x_sol_ls[num_sol], y_sol_ls[num_sol]))

            return solution_str

    elif "y" in expressions2[1].lower():

        if "y" in expressions1[0].lower():
            expressions1[0] = expressions1[0].replace("y", expressions2[0])

        elif "y" in expressions1[1].lower():
            expressions1[1] = expressions1[1].replace("y", expressions2[0])

        else:
            return "This system of equations has no solution. "

        x_sol_ls = sympy.solve(sympy.Eq(parse_expr(expressions2[0]), parse_expr(expressions2[1])), x)

        y_sol_ls = []

        for solution in x_sol_ls:
            temp = expressions1[1]
            plug_in = "(" + str(solution) + ")"

            expressions1[1] = expressions1[1].replace("x", plug_in)

            y_sol = sympy.solve(sympy.Eq(parse_expr(expressions1[0]), parse_expr(expressions1[1])), y)

            y_sol_ls.append(y_sol[0])

            expressions1[1] = temp

        #If the length of the solution list is equal to zero, then print out no solution
        if len(x_sol_ls) == 0:
            return "This systems of equations has no solution. "

        #Otherwise, output as an ordered pair or ordered pairs.
        if len(x_sol_ls) == 1:
            return str((x_sol_ls[0], y_sol_ls[0]))

        else:
            solution_str = ""
            for num_sol in range(0, len(x_sol_ls)):
                if (len(x_sol_ls) - 1) != num_sol:
                    solution_str += str((x_sol_ls[num_sol], y_sol_ls[num_sol])) + ", "
                else:
                    solution_str += str((x_sol_ls[num_sol], y_sol_ls[num_sol]))

            return solution_str
