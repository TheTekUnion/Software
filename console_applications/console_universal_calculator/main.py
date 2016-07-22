"""
The Tek Union 2015-2016
Console Universal Calculator
Programming by Nate Hill
"""
import ast
import math
import os

import sys

from algebra import equations_and_expressions, exponents, factorial, function, graphing, imaginary, line, logarithms, \
    matrices, primality_test, quadratic, radicals, rounding, trig_functions
from arts_and_design import color_codes, metronome, pixels_per_inch
from chemistry import temperature_conversions
from computer_science import base_conversion, sorting_algorithms
from geometry import angle_measure_conversion, circle, distance, midpoint, pythagorean_theorem, rectangle, \
    rectangular_prism, regular_polygon, rhombus, sphere, trapezoid, triangle, trig_definitions
import constants
import sort_list
import standard_calculator
import tree
import updater


#Calculation Group Section Decisions
#Algebra Decision
def algebra_decision():
    print("Sections: \n"
          "Equations and Expressions (EE)\n"
          "Exponents (EX)\n"
          "Factorial (F)\n"
          "Function (FUN)\n"
          "Graphing (G)\n"
          "Imaginary (I)\n"
          "Line (L)\n"
          "Logarithm (LOG)\n"
          "Matrices (M)\n"
          "Primality Test (PT)\n"
          "Quadratic (Q)\n"
          "Radicals (RD)\n"
          "Rounding (R)\n"
          "Trig Functions (TF)")

    section_choice = input("Choose Section: ")

    if section_choice.upper() == "EE":
        equations_and_expressions_decision()

    elif section_choice.upper() == "EX":
        exponents_decision()

    elif section_choice.upper() == "F":
        factorial_decision()

    elif section_choice.upper() == "FUN":
        function_decision()

    elif section_choice.upper() == "G":
        graphing_decision()

    elif section_choice.upper() == "I":
        imaginary_decision()

    elif section_choice.upper() == "L":
        line_decision()

    elif section_choice.upper() == "LOG":
        logarithms_decision()

    elif section_choice.upper() == "M":
        matrices_decision()

    elif section_choice.upper() == "PT":
        primality_test_decision()

    elif section_choice.upper() == "Q":
        quadratic_decision()

    elif section_choice.upper() == "RD":
        radicals_decision()

    elif section_choice.upper() == "R":
        rounding_decision()

    elif section_choice.upper() == "TF":
        trig_functions_decision()

    else:
        print(section_choice + " was not a valid option. ")


#Algebra Subsection Decisions
def equations_and_expressions_decision():
    print("Subsections: \n"
          "Evaluate Expression with Known Variables (EVAL)\n"
          "Solve Equation (SE)\n"
          "Solve a 2x2 System of Linear or Nonlinear Equations by Substitution (SSES)")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "EVAL":
        print("NOTE: Variable names are case sensitive. ")
        n_vars = int(eval(input("Enter the number of variables in your expression: ")))
        output = equations_and_expressions.evaluate_expression(n_vars)
        print(output[1] + " = " + str(output[0]))

    elif subsection_choice.upper() == "SE":
        print("NOTE: Variable names are case sensitive. ")
        equation = input("Enter your equation that contains your included variable(s) (Literal equations can also be solved.): ")
        solve_var = input("Enter the variable you want to solve for: ")

        print(equations_and_expressions.solve_equation(equation, solve_var))

    elif subsection_choice.upper() == "SSES":
        print("NOTE: Remember to use the syntax rules stated above and to use \"x\" and \"y\" as the variables.")
        print("NOTE: There must be at least one equation that has been solved for \"y\". (Use the Solve Equation subsection if needed)")
        print("NOTE: Only functions and vertical lines will work. ")
        print("NOTE: \"y\" must be in both equations. If \"y\" is absent in your equation, then multiply \"y\" by zero. (Ex. x = 5 + y * 0.) Equations without \"x\" are valid. (Ex. y = math.pi) ")
        print("NOTE: The above restrictions will be lifted in coming updates. ")
        print("How to write vertical lines: \n"
              "Multiply \"y\" by 0. (Ex. x = 2 + y * 0)")

        equation_1 = input("Enter your first equation: ")
        equation_2 = input("Enter your second equation: ")
        equation_1 = equation_1.lower()
        equation_2 = equation_2.lower()

        print("Solution(s): " + equations_and_expressions.system_of_equations_substitution(equation_1, equation_2))
    else:
        print(subsection_choice + " was not a valid option. ")


def exponents_decision():
    print("Subsections: \n"
          "Exponent (EX)\n"
          "Rational Exponent (RE)")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "RE":
        base = float(eval(input("Enter the base: ")))
        power = float(eval(input("Enter the exponent numerator (Power): ")))
        root = float(eval(input("Enter the exponent denominator (Root): ")))
        print("Result: " + str(exponents.rational_exponent_float(base, power, root)))

    elif subsection_choice.upper() == "EX":
        base = float(eval(input("Enter the base: ")))
        power = float(eval(input("Enter the exponent (Power): ")))
        print("Result: " + str(exponents.exponent_float(base, power)))

    else:
        print(subsection_choice + " was not a valid option. ")


def factorial_decision():
    print("NOTE: Integers only.")
    num = int(eval(input("Enter number: ")))
    print("Result: " + str(factorial.factorial(num)))


def function_decision():

    print("Remember to use the syntax rules stated above.")
    func_val = input("Enter the value of your function: f(x) = ")

    if "math.pi" in func_val:
        value = math.pi
        func_val = func_val.replace("math.pi", str(value))

    if "math.e" in func_val:
        value = math.e
        func_val = func_val.replace("math.e", str(value))

    func_loop = True
    while func_loop:
        try:

            print("Subsections: \n"
              "Function Call (FC)\n"
              "Find Roots (FR)\n"
              "Find y-intercept (FYI)\n"
              "Factor Function (FF)\n"
              "Expand Function (EF)\n")

            print("f(x) = " + func_val)

            subsection_choice = input("Choose Subsection: ")

            if subsection_choice.upper() == "FC":
                func_input = str(float(eval(input("x = "))))
                print("f(" + func_input + ") = " + str(function.func_call(func_input, func_val)))

            elif subsection_choice.upper() == "FR":
                print("Root(s): ")
                print(function.find_roots(func_val))

            elif subsection_choice.upper() == "FYI":
                print("f(0) = " + str(function.find_y_int(func_val)))

            elif subsection_choice.upper() == "FF":
                print("Factored form: " + str(function.factor_func(func_val)))

            elif subsection_choice.upper() == "EF":
                print("Expanded form: " + str(function.expand_func(func_val)))

            else:
                print(subsection_choice + " was not a valid option. ")

            func_loop_input = input("Type \"EXIT\" if you want to exit the function menu. (This clears the current function value.)\n"
                                    "Type anything else to continue using the function menu. (This keeps the current function value.): ")

            if func_loop_input.upper() == "EXIT":
                func_loop = False

        except ZeroDivisionError:
            print("UNDEFINED")

        except Exception as e:

            print("SYNTAX ERROR!")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            filename = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

            info = exc_type.__name__, filename, exc_tb.tb_lineno

            print("Error description: " + str(info))
            print("Error message: " + str(e))
            print("If you believe this is a bug, then please report it by sending a DM to @tekunion on Twitter. https://twitter.com/tekunion")


def graphing_decision():
    print("Additional info: \n")
    print("How to graph Functions: \n"
          "Constant: Use exponentiation of zero and multiplication (Ex. 2 * (x ** 0)) \n"
          "Linear: Use multiplication (Ex. 2 * x) \n"
          "Polynomial: Use exponentiation (Ex. x ** 0, x ** 1, x ** 2, 4 * ((x - 2) ** 4) + 2, x ** 3 + x ** 2 + x  etc.) \n"
          "Exponential: Use exponentiation (Ex. 2 ** x, math.e ** x) \n"
          "Radical: Use np.sqrt(radicand) for square roots or radicals.nth_root(radicand (variable x), index (float/int)) for any other root (Ex. np.sqrt(4 * x), radicals.nth_root(x, 3)) \n"
          "Rational: Use division (Ex. 1/x -Vertical asymptotes are shown) \n"
          "Rational Exponential/Rational Power: Use either exponentiation or exponents.rational_exponent(base (float/int/variable x), power (float/int/variable x), root (float/int/variable x)) \n"
          "Examples for above: x ** (1/2), exponents.rational_exponent(x, 3, 2), -2 * exponents.rational_exponent(2, x, 2), exponents.rational_exponent(2, 3, x) \n"
          "Logarithms: Use logarithms.logarithm(argument (variable x), base (float/int)) (Ex. -2 * logarithms.logarithm(x, math.e) + 1, logarithms.logarithm(x, 2) \n"
          "Absolute Value: Use abs(value) (Ex. abs(x), 2 * abs(x), -abs(x)) \n"
          "Sine Function: Use trig_functions.sin(argument (variable x)) \n"
          "Cosine Function: Use trig_functions.cos(argument (variable x)) \n"
          "Tangent Function: Use trig_functions.tan(argument (variable x)) \n"
          "Arcsine Function: Use trig_functions.asin(argument (variable x)) \n"
          "Arccosine Function: Use trig_functions.acos(argument (variable x)) \n"
          "Arctangent Function: Use trig_functions.atan(argument (variable x))")

    print("Subsections: \n"
        "Coordinate (C)\n"
        "Function (F)\n"
        "Multiple Functions (MF)")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "C":
        x = float(eval(input("Enter the x-coordinate: ")))
        y = float(eval(input("Enter the y-coordinate: ")))
        graphing.plot_coordinate(x, y)

    elif subsection_choice.upper() == "F":
        func_val = input("Enter the value of your function: f(x) = ")
        domain_values = graphing.get_domain()
        graphing.plot_function(func_val, domain_values[0], domain_values[1])

    elif subsection_choice.upper() == "MF":
        num_func = int(eval(input("Enter the amount of functions you want to graph: ")))
        func_values = graphing.get_func_values_ls(num_func)
        domain_values = graphing.get_domain()
        graphing.plot_multiple_functions(func_values, domain_values[0], domain_values[1])

    else:
        print(subsection_choice + " was not a valid option. ")


def imaginary_decision():
    print("Remember to use the engineering standard, j, as the imaginary unit.")
    print("For more information read here: https://en.wikipedia.org/wiki/Imaginary_unit")

    print("Subsections: \n"
          "Raise j to the nth Power (JN)\n"
          "Evaluate an Imaginary Expression (EIE)")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "JN":
        power = float(eval(input("Enter the exponent (Power): ")))
        print("j ** " + str(power) + " = " + str(imaginary.j_to_the_n(power)))

    elif subsection_choice.upper() == "EIE":
        print("NOTE: Implicit multiplication is required here. (Write 2j instead of 2*j)")
        expression = input("Enter the expression using j: ")

        if "math.pi" in expression:
            value = math.pi
            expression = expression.replace("math.pi", str(value))

        if "math.e" in expression:
            value = math.e
            expression = expression.replace("math.e", str(value))

        print(str(expression) + " = " + str(imaginary.eval_imaginary(expression)))

    else:
        print(subsection_choice + " was not a valid option. ")


def line_decision():
    print("Subsections: \n"
          "Slope (S)\n"
          "Find Equation of Line in Slope-intercept Form (SIF)")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "S":
        print("Points (x1, y1) and (x2, y2)")
        x1 = float(eval(input("Enter x1: ")))
        y1 = float(eval(input("Enter y1: ")))
        x2 = float(eval(input("Enter x2: ")))
        y2 = float(eval(input("Enter y2: ")))
        print("Slope: " + str(line.slope(x1, y1, x2, y2)))

    elif subsection_choice.upper() == "SIF":
        print("Points (x1, y1) and (x2, y2)")
        x1 = float(eval(input("Enter x1: ")))
        y1 = float(eval(input("Enter y1: ")))
        x2 = float(eval(input("Enter x2: ")))
        y2 = float(eval(input("Enter y2: ")))
        print("Slope-intercept form: " + str(line.equation_of_line_slope_int(x1, y1, x2, y2)))

    else:
        print(subsection_choice + " was not a valid option. ")


def logarithms_decision():
    base = float(eval(input("Enter the base of the logarithm: ")))
    argument = float(eval(input("Enter the argument of the logarithm: ")))
    print("log (base: " + str(base) + ") of (" + str(argument) + ") = " + str(logarithms.logarithm_float(argument, base)))


def matrices_decision():
    # Store Matrices here
    mat_names = []
    mat_rows = []
    mat_columns = []

    mats = []
    index = []

    mat_dict = {}

    mat_loop = True
    while mat_loop:
        try:
            print("Subsections: \n"
              "Add Matrices (AM)\n"
              "Create Matrices (CM)\n"
              "Display Matrices (DM)\n"
              "Multiply by a Scalar (MS)\n"
              "Multiply Matrices (MM)\n"
              "Find Determinant (FD)\n"
              "Inverse (INV)\n"
              "Transpose (TP)")

            subsection_choice = input("Choose Subsection: ")

            if subsection_choice.upper() == "AM":
                mat1_name = input("Enter the name of the first matrix: ")
                mat2_name = input("Enter the name of the second matrix: ")
                mat1 = mats[mat_dict[mat1_name]]
                mat2 = mats[mat_dict[mat2_name]]
                print(mat1_name + " + " + mat2_name + " = " + str(mat1.add(mat2)))

            elif subsection_choice.upper() == "CM":

                num_matrices = int(input("Enter the amount of matrices that you want to create: "))

                for i in range(0, num_matrices):
                    name = input("Enter the name of matrix " + str(i + 1) + ": ")
                    mat_names.append(name)
                    rows = int(input("Enter the number of rows in " + name + ": "))
                    mat_rows.append(rows)
                    columns = int(input("Enter the number of columns in " + name + ": "))
                    mat_columns.append(columns)

                for i in range(0, num_matrices):
                    new = matrices.Matrix(mat_rows[i], mat_columns[i], mat_names[i])
                    new.fill_matrix()
                    mats.append(new)
                    index.append(i)

                mat_dict = dict(zip(mat_names, index))

            elif subsection_choice.upper() == "DM":
                swap_dict = dict(zip(mat_dict.values(), mat_dict.keys()))

                for i in range(0, len(mat_dict)):
                    mat = mats[i].multiply_scalar(1.0)
                    print(swap_dict[i] + " = " + str(mat))

            elif subsection_choice.upper() == "MS":
                mat_name = input("Enter the name of the matrix: ")
                scalar = float(input("Enter the scalar: "))
                mat = mats[mat_dict[mat_name]]
                print(str(scalar) + " * " + mat_name + " = " + str(mat.multiply_scalar(scalar)))

            elif subsection_choice.upper() == "MM":
                mat1_name = input("Enter the name of the first matrix: ")
                mat2_name = input("Enter the name of the second matrix: ")
                mat1 = mats[mat_dict[mat1_name]]
                mat2 = mats[mat_dict[mat2_name]]
                print(mat1_name + " * " + mat2_name + " = " + str(mat1.multiply(mat2)))

            elif subsection_choice.upper() == "FD":
                mat_name = input("Enter the name of the matrix: ")
                mat = mats[mat_dict[mat_name]]
                print("Determinant of " + mat_name + " = " + str(mat.determinant()))

            elif subsection_choice.upper() == "INV":
                mat_name = input("Enter the name of the matrix: ")
                mat = mats[mat_dict[mat_name]]
                print("Inverse of " + mat_name + " = " + str(mat.inverse()))

            elif subsection_choice.upper() == "TP":
                mat_name = input("Enter the name of the matrix: ")
                mat = mats[mat_dict[mat_name]]
                print("Transpose of " + mat_name + " = " + str(mat.transpose()))

            else:
                print(subsection_choice + " was not a valid option. ")

            mat_loop_input = input("Type \"EXIT\" if you want to exit the matrix menu. (This clears all matrices.)\n"
                                   "Type anything else to continue using the matrix menu. (This keeps all matrices.): ")

            if mat_loop_input.upper() == "EXIT":
                mat_loop = False

        except ZeroDivisionError:
            print("UNDEFINED")

        except Exception as e:
            print("SYNTAX ERROR!")
            print("Error description: " + str(e))
            print("If you believe this is a bug, then please report it by sending a DM to @tekunion on Twitter. https://twitter.com/tekunion")


def primality_test_decision():
    print("NOTE: Integers only.")
    candidate = int(eval(input("Enter Number for Primality Test: ")))
    if primality_test.is_prime(candidate):
        print(str(candidate) + " is a prime number. ")
    else:
        print(str(candidate) + " is a not prime number. ")


def quadratic_decision():
    print("Remember to use the syntax rules stated above.")
    quad_val = input("Enter the value of your quadratic function: f(x) = ")

    if "math.pi" in quad_val:
        value = math.pi
        quad_val = quad_val.replace("math.pi", str(value))

    if "math.e" in quad_val:
        value = math.e
        quad_val = quad_val.replace("math.e", str(value))

    coefficients = quadratic.find_a_b_c(quad_val)
    a = coefficients[0]
    b = coefficients[1]
    c = coefficients[2]

    quad_loop = True
    while quad_loop:
        try:
            print("Subsections: \n"
              "Quadratic Function Call (QFC)\n"
              "Find Discriminant (FD)\n"
              "Find Roots (FR)\n"
              "Find y-intercept (FYI)\n"
              "Find vertex (FV)\n"
              "Factor Quadratic (FQ)\n"
              "Expand Quadratic (EQ)\n")

            print("f(x) = " + quad_val)

            subsection_choice = input("Choose Subsection: ")

            if subsection_choice.upper() == "QFC":
                quad_input = str(float(eval(input("x = "))))
                print("f(" + quad_input + ") = " + str(quadratic.quadratic_function_call(quad_input, quad_val)))

            elif subsection_choice.upper() == "FD":
                print("Discriminant = " + str(quadratic.quadratic_find_discriminant(a, b, c)))

            elif subsection_choice.upper() == "FR":
                print("Root(s): ")
                print(quadratic.quadratic_find_roots(quad_val))

            elif subsection_choice.upper() == "FYI":
                print("f(0) = " + str(quadratic.quadratic_find_y_int(quad_val)))

            elif subsection_choice.upper() == "FV":
                print("Vertex: " + "(" + str(quadratic.quadratic_find_vertex(a, b, quad_val)[0]) + ", " + str(quadratic.quadratic_find_vertex(a, b, quad_val)[1]) + ")")

            elif subsection_choice.upper() == "FQ":
                print("Factored form: " + str(quadratic.quadratic_factor(quad_val)))

            elif subsection_choice.upper() == "EQ":
                print("Expanded form: " + str(quadratic.quadratic_expand(quad_val)))

            else:
                print(subsection_choice + " was not a valid option. ")

            quad_loop_input = input("Type \"EXIT\" if you want to exit the quadratic menu. (This clears the current quadratic function value.)\n"
                                    "Type anything else to continue using the quadratic menu. (This keeps the current quadratic function value.): ")

            if quad_loop_input.upper() == "EXIT":
                quad_loop = False

        except ZeroDivisionError:
            print("UNDEFINED")

        except Exception as e:
            print("SYNTAX ERROR!")
            print("Error description: " + str(e))
            print("If you believe this is a bug, then please report it by sending a DM to @tekunion on Twitter. https://twitter.com/tekunion")


def radicals_decision():
    print("Subsections: \n"
          "Find nth Root (FNR)")

    subsection_choice = input("Choose Subsection: ")
    if subsection_choice.upper() == "FNR":
        radicand = float(eval(input("Enter the radicand: ")))
        index = float(eval(input("Enter the index: ")))
        rounding_place = int(eval(input("Enter the number of decimal places to round to: ")))
        print("Result = " + str(radicals.nth_root_float(radicand, index, rounding_place)))

    else:
        print(subsection_choice + " was not a valid option. ")


def rounding_decision():
    print("Subsections: \n"
          "Regular Rounding (RR)\n"
          "Round to Ceiling (RC)\n"
          "Round to Floor (RF)")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "RR":
        number = float(eval(input("Enter your number that needs rounding: ")))
        dec_places = int(eval(input("Enter the number of decimal places: ")))
        print("Rounded Number: " + str(rounding.round_reg(number, dec_places)))

    elif subsection_choice.upper() == "RC":
        number = float(eval(input("Enter your number that needs rounding: ")))
        print("Rounded Number: " + str(rounding.round_ceil(number)))

    elif subsection_choice.upper() == "RF":
        number = float(eval(input("Enter your number that needs rounding: ")))
        print("Rounded Number: " + str(rounding.round_floor(number)))

    else:
        print(subsection_choice + " was not a valid option. ")


def trig_functions_decision():
    print("Subsections: \n"
          "Sine (SIN)\n"
          "Cosine (COS)\n"
          "Tangent (TAN)\n"
          "Arcsine (ASIN)\n"
          "Arccosine (ACOS)\n"
          "Arctangent (ATAN)")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "SIN":
        mode = input("Mode: Degrees or Radians (D/R)? ")
        mode = mode.upper()
        theta = float(eval(input("Theta = ")))
        dec_places = int(eval(input("Enter the number of decimal places to round to: ")))
        print("sin(" + str(theta) + mode + ")" + " = " + str(trig_functions.sin_float(theta, mode, dec_places)))

    elif subsection_choice.upper() == "COS":
        mode = input("Mode: Degrees or Radians (D/R)? ")
        mode = mode.upper()
        theta = float(eval(input("Theta = ")))
        dec_places = int(eval(input("Enter the number of decimal places to round to: ")))
        print("cos(" + str(theta) + mode + ")" + " = " + str(trig_functions.cos_float(theta, mode, dec_places)))

    elif subsection_choice.upper() == "TAN":
        mode = input("Mode: Degrees or Radians (D/R)? ")
        mode = mode.upper()
        theta = float(eval(input("Theta = ")))
        dec_places = int(eval(input("Enter the number of decimal places to round to: ")))
        print("tan(" + str(theta) + mode + ")" + " = " + str(trig_functions.tan_float(theta, mode, dec_places)))

    elif subsection_choice.upper() == "ASIN":
        mode = input("Mode: Degrees or Radians (D/R)? ")
        mode = mode.upper()
        theta = float(eval(input("Theta = ")))
        dec_places = int(eval(input("Enter the number of decimal places to round to: ")))
        print("asin(" + str(theta) + mode + ")" + " = " + str(trig_functions.asin_float(theta, mode, dec_places)))

    elif subsection_choice.upper() == "ACOS":
        mode = input("Mode: Degrees or Radians (D/R)? ")
        mode = mode.upper()
        theta = float(eval(input("Theta = ")))
        dec_places = int(eval(input("Enter the number of decimal places to round to: ")))
        print("acos(" + str(theta) + mode + ")" + " = " + str(trig_functions.acos_float(theta, mode, dec_places)))

    elif subsection_choice.upper() == "ATAN":
        mode = input("Mode: Degrees or Radians (D/R)? ")
        mode = mode.upper()
        theta = float(eval(input("Theta = ")))
        dec_places = int(eval(input("Enter the number of decimal places to round to: ")))
        print("atan(" + str(theta) + mode + ")" + " = " + str(trig_functions.atan_float(theta, mode, dec_places)))

    else:
        print(subsection_choice + " was not a valid option. ")


#Arts and Design Decision
def arts_and_design_decision():
    print("Sections: \n"
          "Color Codes (CC)\n"
          "Metronome (M)\n"
          "Pixels Per Inch Calculator (PPI)")

    section_choice = input("Choose Section: ")

    if section_choice.upper() == "CC":
        color_codes_decision()

    elif section_choice.upper() == "M":
        metronome_decision()

    elif section_choice.upper() == "PPI":
        pixels_per_inch_decision()

    else:
        print(section_choice + " was not a valid option. ")


#Arts and Design Subsection Decisions
def color_codes_decision():
    print("Subsections: \n"
        "Convert Hexadecimal to RGB (HR)\n"
        "Convert RGB to Hexadecimal (RH)\n"
        "Show Color by RGB Value (SC)")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "HR":
        print("NOTE: Expressions not allowed here. ")
        hex_value = input("Enter the Hexadecimal Code: ")
        print("RGB Value: " + str(color_codes.hex_to_rgb(hex_value)))

    elif subsection_choice.upper() == "RH":
        print("NOTE: Expressions not allowed here. ")
        print("Input format: (value, value, value) Ex: (255, 255, 255)")
        rgb_value = ast.literal_eval((input("Enter the RGB Code (In parenthesis): ")))
        print("Hex Value: " + str(color_codes.rgb_to_hex(rgb_value)))

    elif subsection_choice.upper() == "SC":
        print("NOTE: Expressions not allowed here. ")
        print("Input format: (value, value, value) Ex: (255, 255, 255)")
        rgb_value = ast.literal_eval(input("Enter the RGB Code (In parenthesis): "))
        print("Close the window to continue.")
        color_codes.show_color(rgb_value)

    else:
        print(subsection_choice + " was not a valid option. ")


def metronome_decision():
    bpm = float(eval(input("Enter the number of beats per minute: ")))
    duration = float(eval(input("Enter the duration in seconds: ")))
    metronome.metronome(bpm, duration)


def pixels_per_inch_decision():
        pix_width = int(eval(input("Enter the Width in Pixels (horizontal x-axis): ")))
        pix_height = int(eval(input("Enter the Height in Pixels (vertical y-axis): ")))
        diagonal = float(eval(input("Enter the Length of the Diagonal in Inches: ")))
        print("Pixels Per Inch: " + str(pixels_per_inch.ppi(pix_width, pix_height, diagonal)))


#Chemistry Decision
def chemistry_decision():
    print("Sections: \n"
          "Temperature Conversion (TC)")

    section_choice = input("Choose Section: ")

    if section_choice.upper() == "TC":
        temperature_conversion_decision()
    else:
        print(section_choice + " was not a valid option. ")


#Chemistry Subsection Decisions
def temperature_conversion_decision():
    print("Subsections: \n"
          "Celsius to Fahrenheit (CF)\n"
          "Celsius to Kelvin (CK)\n"
          "Fahrenheit to Celsius (FC)\n"
          "Fahrenheit to Kelvin (FK)\n"
          "Kelvin to Celsius (KC)\n"
          "Kelvin to Fahrenheit (KF)")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "CF":
        c = float(eval(input("Enter the Celsius Temperature: ")))
        dec_places = int(eval(input("Enter the number of decimal places: ")))

        result = temperature_conversions.celsius_to_fahrenheit(c, dec_places)
        output = "Fahrenheit Temperature: " + str(result)

        print(output)

    elif subsection_choice.upper() == "CK":
        c = float(eval(input("Enter the Celsius Temperature: ")))
        dec_places = int(eval(input("Enter the number of decimal places: ")))

        result = temperature_conversions.celsius_to_kelvin(c, dec_places)
        output = "Kelvin Temperature: " + str(result)

        print(output)

    elif subsection_choice.upper() == "FC":
        f = float(eval(input("Enter the Fahrenheit Temperature: ")))
        dec_places = int(eval(input("Enter the number of decimal places: ")))

        result = temperature_conversions.fahrenheit_to_celsius(f, dec_places)
        output = "Celsius Temperature: " + str(result)

        print(output)

    elif subsection_choice.upper() == "FK":
        f = float(eval(input("Enter the Fahrenheit Temperature: ")))
        dec_places = int(eval(input("Enter the number of decimal places: ")))

        result = temperature_conversions.fahrenheit_to_kelvin(f, dec_places)
        output = "Kelvin Temperature: " + str(result)

        print(output)

    elif subsection_choice.upper() == "KC":
        k = float(eval(input("Enter the Kelvin Temperature: ")))
        dec_places = int(eval(input("Enter the number of decimal places: ")))

        result = temperature_conversions.kelvin_to_celsius(k, dec_places)
        output = "Celsius Temperature: " + str(result)

        print(output)

    elif subsection_choice.upper() == "KF":
        k = float(eval(input("Enter the Kelvin Temperature: ")))
        dec_places = int(eval(input("Enter the number of decimal places: ")))

        result = temperature_conversions.kelvin_to_fahrenheit(k, dec_places)
        output = "Fahrenheit Temperature: " + str(result)

        print(output)

    else:
        print(subsection_choice + " was not a valid option. ")


#Computer Science Decision
def computer_science_decision():
    print("Sections: \n"
          "Base Conversion (BC)\n"
          "Sorting Algorithms (SRTA)")

    section_choice = input("Choose Section: ")

    if section_choice.upper() == "BC":
        base_conversion_decision()

    elif section_choice.upper() == "SRTA":
        sorting_algorithms_decision()

    else:
        print(section_choice + " was not a valid option. ")


#Computer Science Subsection Decisions
def base_conversion_decision():
    print("Subsections: \n"
          "Binary to Octal (BO)\n"
          "Binary to Decimal (BD)\n"
          "Binary to Hexadecimal (BH)\n"
          "Octal to Binary (OB)\n"
          "Octal to Decimal (OD)\n"
          "Octal to Hexadecimal (OH)\n"
          "Decimal to Binary (DB)\n"
          "Decimal to Octal (DO)\n"
          "Decimal to Hexadecimal (DH)\n"
          "Hexadecimal to Binary (HB)\n"
          "Hexadecimal to Octal (HO)\n"
          "Hexadecimal to Decimal (HD)\n"
          "Base N to Decimal (ND)\n"
          "Decimal to Base N (DN)\n"
          "Base N to Base M (NM)\n"
          "NOTE: Expressions not allowed here.\n"
          "NOTE: Only integers (in whatever base) are allowed for input. Fractional base conversion will be implemented soon. \n"
          "NOTE: The binary, octal, and hexadecimal specific conversions are formatted with the following prefixes: 0b, 0o, and, 0x, respectively. \n"
          "If you would like your answer to be formatted without a prefix, then please use the custom conversions. ")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "BO":
        bin_val = input("Enter Binary Value:")
        print("Octal Value: " + str(base_conversion.binary_to_octal(bin_val)))

    elif subsection_choice.upper() == "BD":
        bin_val = input("Enter Binary Value:")
        print("Decimal Value: " + str(base_conversion.binary_to_decimal(bin_val)))

    elif subsection_choice.upper() == "BH":
        bin_val = input("Enter Binary Value:")
        print("Hexadecimal Value: " + str(base_conversion.binary_to_hexadecimal(bin_val)))

    elif subsection_choice.upper() == "OB":
        oct_val = input("Enter Octal Value:")
        print("Binary Value: " + str(base_conversion.octal_to_binary(oct_val)))

    elif subsection_choice.upper() == "OD":
        oct_val = input("Enter Octal Value:")
        print("Decimal Value: " + str(base_conversion.octal_to_decimal(oct_val)))

    elif subsection_choice.upper() == "OH":
        oct_val = input("Enter Octal Value:")
        print("Hexadecimal Value: " + str(base_conversion.octal_to_hexadecimal(oct_val)))

    elif subsection_choice.upper() == "DB":
        dec_val = int(input("Enter Decimal Value:"))
        print("Binary Value: " + str(base_conversion.decimal_to_binary(dec_val)))

    elif subsection_choice.upper() == "DO":
        dec_val = int(input("Enter Decimal Value:"))
        print("Octal Value: " + str(base_conversion.decimal_to_octal(dec_val)))

    elif subsection_choice.upper() == "DH":
        dec_val = int(input("Enter Decimal Value:"))
        print("Hexadecimal Value: " + str(base_conversion.decimal_to_hexadecimal(dec_val)))

    elif subsection_choice.upper() == "HB":
        hex_val = input("Enter Hexadecimal Value:")
        print("Binary Value: " + str(base_conversion.hexadecimal_to_binary(hex_val)))

    elif subsection_choice.upper() == "HO":
        hex_val = input("Enter Hexadecimal Value:")
        print("Octal Value: " + str(base_conversion.hexadecimal_to_octal(hex_val)))

    elif subsection_choice.upper() == "HD":
        hex_val = input("Enter Hexadecimal Value:")
        print("Decimal Value: " + str(base_conversion.hexadecimal_to_decimal(hex_val)))

    elif subsection_choice.upper() == "ND":
        base_n = int(input("Enter Base N: "))
        base_n_val = input("Enter Base " + str(base_n) + " Value: ")
        print("Decimal Value: " + str(base_conversion.base_n_to_decimal(base_n_val, base_n)))

    elif subsection_choice.upper() == "DN":
        base_n = int(input("Enter Base N: "))
        dec_val = int(input("Enter Decimal Value: "))
        print("Base " + str(base_n) + " Value: " + str(base_conversion.decimal_to_base_n(dec_val, base_n)))

    elif subsection_choice.upper() == "NM":
        base_n = int(input("Enter Base N: "))
        base_n_val = input("Enter Base " + str(base_n) + " Value: ")
        base_m = int(input("Enter Base M: "))
        print("Base " + str(base_m) + " Value: " + str(base_conversion.base_n_to_base_m(base_n, base_n_val, base_m)))

    else:
        print(subsection_choice + " was not a valid option. ")


def sorting_algorithms_decision():
    print("Subsections: \n"
          "Bubble Sort (BS)\n"
          "Insertion Sort (IS)\n"
          "Selection Sort (SS)\n"
          "Quicksort (QS)\n"
          "NOTE: These sorts are for integers only. If you want to sort other data types without algorithm info, \n"
          "then you have to use the Sort List by Data Type (SLDT) section. ")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "BS":
        list_type = input("Would you like to generate a random list (GRL) or generate a custom list (GCL)? ")
        if list_type.upper() == "GRL":
            size = int(eval(input("Enter the size of your list (number of elements): ")))
            min_val = int(eval(input("Enter the minimum value for a number in your list: ")))
            max_val = int(eval(input("Enter the maximum value for a number in your list: ")))
            ls = sorting_algorithms.generate_random_ls(size, min_val, max_val)
            print("Sorted list: " + str(sorting_algorithms.bubble_sort(ls)[0]))
            print("Runtime: " + str(sorting_algorithms.bubble_sort(ls)[1]) + " seconds")
            print("Big O: " + str(sorting_algorithms.bubble_sort(ls)[2]))

        elif list_type.upper() == "GCL":
            size = int(eval(input("Enter the size of your list (number of elements): ")))
            ls = sorting_algorithms.generate_custom_ls(size)
            print("Sorted list: " + str(sorting_algorithms.bubble_sort(ls)[0]))
            print("Runtime: " + str(sorting_algorithms.bubble_sort(ls)[1]) + " seconds")
            print("Big O Notation: " + str(sorting_algorithms.bubble_sort(ls)[2]))

        else:
            print(list_type + " was not a valid option. ")

    elif subsection_choice.upper() == "IS":
        list_type = input("Would you like to generate a random list (GRL) or generate a custom list (GCL)? ")
        if list_type.upper() == "GRL":
            size = int(eval(input("Enter the size of your list (number of elements): ")))
            min_val = int(eval(input("Enter the minimum value for a number in your list: ")))
            max_val = int(eval(input("Enter the maximum value for a number in your list: ")))
            ls = sorting_algorithms.generate_random_ls(size, min_val, max_val)
            print("Sorted list: " + str(sorting_algorithms.insertion_sort(ls)[0]))
            print("Runtime: " + str(sorting_algorithms.insertion_sort(ls)[1]) + " seconds")
            print("Big O: " + str(sorting_algorithms.insertion_sort(ls)[2]))

        elif list_type.upper() == "GCL":
            size = int(eval(input("Enter the size of your list (number of elements): ")))
            ls = sorting_algorithms.generate_custom_ls(size)
            print("Sorted list: " + str(sorting_algorithms.insertion_sort(ls)[0]))
            print("Runtime: " + str(sorting_algorithms.insertion_sort(ls)[1]) + " seconds")
            print("Big O Notation: " + str(sorting_algorithms.insertion_sort(ls)[2]))

        else:
            print(list_type + " was not a valid option. ")

    elif subsection_choice.upper() == "SS":
        list_type = input("Would you like to generate a random list (GRL) or generate a custom list (GCL)? ")
        if list_type.upper() == "GRL":
            size = int(eval(input("Enter the size of your list (number of elements): ")))
            min_val = int(eval(input("Enter the minimum value for a number in your list: ")))
            max_val = int(eval(input("Enter the maximum value for a number in your list: ")))
            ls = sorting_algorithms.generate_random_ls(size, min_val, max_val)
            print("Sorted list: " + str(sorting_algorithms.selection_sort(ls)[0]))
            print("Runtime: " + str(sorting_algorithms.selection_sort(ls)[1]) + " seconds")
            print("Big O: " + str(sorting_algorithms.selection_sort(ls)[2]))

        elif list_type.upper() == "GCL":
            size = int(eval(input("Enter the size of your list (number of elements): ")))
            ls = sorting_algorithms.generate_custom_ls(size)
            print("Sorted list: " + str(sorting_algorithms.selection_sort(ls)[0]))
            print("Runtime: " + str(sorting_algorithms.selection_sort(ls)[1]) + " seconds")
            print("Big O Notation: " + str(sorting_algorithms.selection_sort(ls)[2]))

        else:
            print(list_type + " was not a valid option. ")

    elif subsection_choice.upper() == "QS":
        list_type = input("Would you like to generate a random list (GRL) or generate a custom list (GCL)? ")
        if list_type.upper() == "GRL":
            size = int(eval(input("Enter the size of your list (number of elements): ")))
            min_val = int(eval(input("Enter the minimum value for a number in your list: ")))
            max_val = int(eval(input("Enter the maximum value for a number in your list: ")))
            ls = sorting_algorithms.generate_random_ls(size, min_val, max_val)
            print("Sorted list: " + str(sorting_algorithms.quick_sort(ls)[0]))
            print("Runtime: " + str(sorting_algorithms.quick_sort(ls)[1]) + " seconds")
            print("Big O: " + str(sorting_algorithms.quick_sort(ls)[2]))

        elif list_type.upper() == "GCL":
            size = int(eval(input("Enter the size of your list (number of elements): ")))
            ls = sorting_algorithms.generate_custom_ls(size)
            print("Sorted list: " + str(sorting_algorithms.quick_sort(ls)[0]))
            print("Runtime: " + str(sorting_algorithms.quick_sort(ls)[1]) + " seconds")
            print("Big O Notation: " + str(sorting_algorithms.quick_sort(ls)[2]))

        else:
            print(list_type + " was not a valid option. ")

    else:
        print(subsection_choice + " was not a valid option. ")


#Constants Decision
def constants_decision():
    print("Constants: \n"
          "Value of Pi (PI)\n"
          "Value of Euler\'s Number (E)")

    constant_choice = input("Choose Constant: ")

    if constant_choice.upper() == "PI":
        print("Value of Pi: " + str(constants.get_pi()))

    elif constant_choice.upper() == "E":
        print("Value of Euler\'s Number: " + str(constants.get_e()))


#Geometry Decision
def geometry_decision():
    print("Sections: "
          "Angle Measure Conversion (AMC)\n"
          "Circle (C)\n"
          "Distance (D)\n"
          "Midpoint (M)\n"
          "Pythagorean Theorem (PT)\n"
          "Rectangle (R)\n"
          "Rectangular Prism (RP)\n"
          "Regular Polygon (POLY)\n"
          "Rhombus (RH)\n"
          "Sphere (SPH)\n"
          "Trapezoid (TRAP)\n"
          "Triangle (T)\n"
          "Trig Definitions (TD)")

    section_choice = input("Choose Section: ")

    if section_choice.upper() == "AMC":
        angle_measure_conversion_decision()

    elif section_choice.upper() == "C":
        circle_decision()

    elif section_choice.upper() == "D":
        distance_decision()

    elif section_choice.upper() == "M":
        midpoint_decision()

    elif section_choice.upper() == "PT":
        pythagorean_theorem_decision()

    elif section_choice.upper() == "R":
        rectangle_decision()

    elif section_choice.upper() == "RP":
        rectangular_prism_decision()

    elif section_choice.upper() == "POLY":
        regular_polygon_decision()

    elif section_choice.upper() == "RH":
        rhombus_decision()

    elif section_choice.upper() == "SPH":
        sphere_decision()

    elif section_choice.upper() == "TRAP":
        trapezoid_decision()

    elif section_choice.upper() == "T":
        triangle_decision()

    elif section_choice.upper() == "TD":
        trig_definitions_decision()

    else:
        print(section_choice + " was not a valid option. ")


#Geometry Subsection Decisions
def angle_measure_conversion_decision():
    print("Subsections: \n"
          "Radians to Degrees (RD)\n"
          "Degrees to Radians (DR)")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "RD":
        rads = float(eval(input("Enter the angle measure in radians: ")))
        print(str(rads) + " Radians = " + str(angle_measure_conversion.to_degrees(rads)) + " Degrees")

    elif subsection_choice.upper() == "DR":
        degrees = float(eval(input("Enter the angle measure in degrees: ")))
        print(str(degrees) + " Degrees = " + str(angle_measure_conversion.to_radians(degrees)) + " Radians")

    else:
        print(subsection_choice + " was not a valid option. ")


def circle_decision():
    print("Subsections: \n"
          "Find Area (A)\n"
          "Find the Area of a Sector (AS)\n"
          "Find Circumference (C)\n"
          "Find Diameter (D)\n"
          "Find Radius (R)")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "A":
        r = float(eval(input("Enter Radius: ")))
        print("Area: " + str(circle.circle_area(r)))

    elif subsection_choice.upper() == "AS":
        r = float(eval(input("Enter Radius: ")))
        ca = float(eval(input("Enter Central Angle: ")))
        print("Area of Sector: " + str(circle.circle_sector_area(r, ca)))

    elif subsection_choice.upper() == "C":
        r = float(eval(input("Enter Radius: ")))
        print("Circumference: " + str(circle.circle_circumference(r)))

    elif subsection_choice.upper() == "D":
        r = float(eval(input("Enter Radius: ")))
        print("Diameter: " + str(circle.circle_diameter(r)))

    elif subsection_choice.upper() == "R":
        d = float(eval(input("Enter Diameter: ")))
        print("Radius: " + str(circle.circle_radius(d)))

    else:
        print(subsection_choice + " was not a valid option. ")


def distance_decision():
    print("Subsections: \n"
          "Two-Dimensional Distance (2D)\n"
          "Three-Dimensional Distance (3D)")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "2D":
        print("Points (x1, y1) and (x2, y2)")
        x1 = float(eval(input("Enter x1: ")))
        x2 = float(eval(input("Enter x2: ")))
        y1 = float(eval(input("Enter y1: ")))
        y2 = float(eval(input("Enter y2: ")))
        print("Distance: " + str(distance.distance_2d(x1, x2, y1, y2)))

    elif subsection_choice.upper() == "3D":
        print("Points (x1, y1, z1) and (x2, y2, z2)")
        x1 = float(eval(input("Enter x1: ")))
        x2 = float(eval(input("Enter x2: ")))
        y1 = float(eval(input("Enter y1: ")))
        y2 = float(eval(input("Enter y2: ")))
        z1 = float(eval(input("Enter z1: ")))
        z2 = float(eval(input("Enter z2: ")))
        print("Distance: " + str(distance.distance_3d(x1, x2, y1, y2, z1, z2)))

    else:
        print(subsection_choice + " was not a valid option. ")


def midpoint_decision():
    print("Subsections: \n"
          "One-Dimensional Midpoint (1D)\n"
          "Two-Dimensional Midpoint (2D)\n"
          "Three-Dimensional Midpoint (3D)\n"
          "N-Dimensional Midpoint (ND)\n"
          "N-Dimensional Midpoint with M Points (NDMP)")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "1D":
        print("Points (x1) and (x2)")
        x1 = float(eval(input("Enter x1: ")))
        x2 = float(eval(input("Enter x2: ")))
        print("Midpoint: " + str(midpoint.midpoint_1d(x1, x2)))

    elif subsection_choice.upper() == "2D":
        print("Points (x1, y1) and (x2, y2)")
        x1 = float(eval(input("Enter x1: ")))
        x2 = float(eval(input("Enter x2: ")))
        y1 = float(eval(input("Enter y1: ")))
        y2 = float(eval(input("Enter y2: ")))
        print("Midpoint: " + str(midpoint.midpoint_2d(x1, x2, y1, y2)))

    elif subsection_choice.upper() == "3D":
        print("Points (x1, y1, z1) and (x2, y2, z2)")
        x1 = float(eval(input("Enter x1: ")))
        x2 = float(eval(input("Enter x2: ")))
        y1 = float(eval(input("Enter y1: ")))
        y2 = float(eval(input("Enter y2: ")))
        z1 = float(eval(input("Enter z1: ")))
        z2 = float(eval(input("Enter z2: ")))
        print("Midpoint: " + str(midpoint.midpoint_3d(x1, x2, y1, y2, z1, z2)))

    elif subsection_choice.upper() == "ND":
        dimensions = int(eval(input("Enter the number of dimensions: ")))
        print("Midpoint: " + str(midpoint.midpoint_nd(dimensions)))

    elif subsection_choice.upper() == "NDMP":
        dimensions = int(eval(input("Enter the number of dimensions: ")))
        points = int(eval(input("Enter the number of points in each dimension: ")))
        print("Midpoint: " + str(midpoint.midpoint_ndmp(dimensions, points)))

    else:
        print(subsection_choice + " was not a valid option. ")


def pythagorean_theorem_decision():
    print("Subsections: \n"
          "Find the Hypotenuse (HYPO)\n"
          "Find Leg A (LA)\n"
          "Find Leg B (LB)")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "HYPO":
        leg_a = float(eval(input("Enter Leg A: ")))
        leg_b = float(eval(input("Enter Leg B: ")))
        print("Hypotenuse: " + str(pythagorean_theorem.find_hypotenuse(leg_a, leg_b)))

    elif subsection_choice.upper() == "LA":
        leg_b = float(eval(input("Enter Leg B: ")))
        hypo = float(eval(input("Enter Hypotenuse: ")))
        print("Hypotenuse: " + str(pythagorean_theorem.find_leg_a(leg_b, hypo)))

    elif subsection_choice.upper() == "LB":
        leg_a = float(eval(input("Enter Leg A: ")))
        hypo = float(eval(input("Enter Hypotenuse: ")))
        print("Leg B: " + str(pythagorean_theorem.find_leg_b(leg_a, hypo)))

    else:
        print(subsection_choice + " was not a valid option. ")


def rectangle_decision():
    print("Subsections: \n"
          "Find Area (A)\n"
          "Find Diagonal (D)\n"
          "Find Length (L)\n"
          "Find Perimeter (P)\n"
          "Find Width (W)")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "A":
        l = float(eval(input("Enter Length: ")))
        w = float(eval(input("Enter Width: ")))
        print("Area: " + str(rectangle.rect_area(l, w)))

    elif subsection_choice.upper() == "D":
        l = float(eval(input("Enter Length: ")))
        w = float(eval(input("Enter Width: ")))
        print("Diagonal: " + str(rectangle.rect_diagonal(l, w)))

    elif subsection_choice.upper() == "L":
        a = float(eval(input("Enter Area: ")))
        w = float(eval(input("Enter Width: ")))
        print("Length: " + str(rectangle.rect_length(a, w)))

    elif subsection_choice.upper() == "P":
        l = float(eval(input("Enter Length: ")))
        w = float(eval(input("Enter Width: ")))
        print("Perimeter: " + str(rectangle.rect_perimeter(l, w)))

    elif subsection_choice.upper() == "W":
        a = float(eval(input("Enter Area: ")))
        l = float(eval(input("Enter Length: ")))
        print("Width: " + str(rectangle.rect_width(a, l)))

    else:
        print(subsection_choice + " was not a valid option. ")


def rectangular_prism_decision():
    print("Subsections: \n"
          "Find Height (H)\n"
          "Find Length (L)\n"
          "Find Space Diagonal (SD)\n"
          "Find Surface Area (SA)\n"
          "Find Volume (V)\n"
          "Find Width (W)")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "H":
        v = float(eval(input("Enter Volume: ")))
        l = float(eval(input("Enter Length: ")))
        w = float(eval(input("Enter Width: ")))
        print("Height: " + str(rectangular_prism.rect_prism_height(v, l, w)))

    elif subsection_choice.upper() == "L":
        v = float(eval(input("Enter Volume: ")))
        h = float(eval(input("Enter Height: ")))
        w = float(eval(input("Enter Width: ")))
        print("Length: " + str(rectangular_prism.rect_prism_length(v, h, w)))

    elif subsection_choice.upper() == "SD":
        l = float(eval(input("Enter Length: ")))
        w = float(eval(input("Enter Width: ")))
        h = float(eval(input("Enter Height: ")))
        print("Space Diagonal: " + str(rectangular_prism.rect_prism_space_diagonal(l, w, h)))

    elif subsection_choice.upper() == "SA":
        l = float(eval(input("Enter Length: ")))
        w = float(eval(input("Enter Width: ")))
        h = float(eval(input("Enter Height: ")))
        print("Surface Area: " + str(rectangular_prism.rect_prism_surface_area(l, w, h)))

    elif subsection_choice.upper() == "V":
        l = float(eval(input("Enter Length: ")))
        w = float(eval(input("Enter Width: ")))
        h = float(eval(input("Enter Height: ")))
        print("Volume: " + str(rectangular_prism.rect_prism_volume(l, w, h)))

    elif subsection_choice.upper() == "W":
        v = float(eval(input("Enter Volume: ")))
        h = float(eval(input("Enter Height: ")))
        l = float(eval(input("Enter Length: ")))
        print("Width: " + str(rectangular_prism.rect_prism_width(v, h, l)))

    else:
        print(subsection_choice + " was not a valid option. ")


def regular_polygon_decision():
    print("Subsections: \n"
          "Find Interior Angle Measure (IAM)\n"
          "Find Interior Angle Sum (IAS)\n"
          "Find Exterior Angle Measure (EAM)\n"
          "Find Exterior Angle Sum (EAS)\n"
          "Find Area (A)\n"
          "Find Perimeter (P)")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "IAM":
        sides = int(eval(input("Enter Number of Sides: ")))
        print("Interior Angle Measure: " + str(regular_polygon.reg_polygon_interior_angle_measure(sides)))

    elif subsection_choice.upper() == "IAS":
        sides = int(eval(input("Enter Number of Sides: ")))
        print("Interior Angle Sum: " + str(regular_polygon.reg_polygon_interior_angle_sum(sides)))

    elif subsection_choice.upper() == "EAM":
        sides = int(eval(input("Enter Number of Sides: ")))
        print("Exterior Angle Measure: " + str(regular_polygon.reg_polygon_exterior_angle_measure(sides)))

    elif subsection_choice.upper() == "EAS":
        print("Exterior Angle Sum: " + str(regular_polygon.reg_polygon_exterior_angle_sum()))

    elif subsection_choice.upper() == "A":
        apothem = float(eval(input("Enter Apothem: ")))
        perimeter = float(eval(input("Enter Perimeter: ")))
        print("Area: " + str(regular_polygon.reg_polygon_area(apothem, perimeter)))

    elif subsection_choice.upper() == "P":
        sides = int(eval(input("Enter Number of Sides: ")))
        side_length = float(eval(input("Enter The Length of Each Side: ")))
        print("Perimeter: " + str(regular_polygon.reg_polygon_perimeter(sides, side_length)))

    else:
        print(subsection_choice + " was not a valid option. ")


def rhombus_decision():
    print("Subsections: \n"
          "Find Area (A)\n"
          "Find Perimeter (P)\n"
          "Find Side Length (SL)\n"
          "Find Diagonal Q (DQ)\n"
          "Find Diagonal P (DP)")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "A":
        dp = float(eval(input("Enter Diagonal P: ")))
        dq = float(eval(input("Enter Diagonal Q: ")))
        print("Area: " + str(rhombus.rhombus_area(dp, dq)))

    elif subsection_choice.upper() == "P":
        side_length = float(eval(input("Enter the Length of Each Side: ")))
        print("Perimeter: " + str(rhombus.rhombus_perimeter(side_length)))

    elif subsection_choice.upper() == "SL":
        perimeter = float(eval(input("Perimeter: ")))
        print("Side Length: " + str(rhombus.rhombus_side_length(perimeter)))

    elif subsection_choice.upper() == "DQ":
        dp = float(eval(input("Enter Diagonal P: ")))
        area = float(eval(input("Enter Area: ")))
        print("Diagonal Q: " + str(rhombus.rhombus_diagonal_q(dp, area)))

    elif subsection_choice.upper() == "DP":
        dq = float(eval(input("Enter Diagonal Q: ")))
        area = float(eval(input("Enter Area: ")))
        print("Diagonal P: " + str(rhombus.rhombus_diagonal_p(dq, area)))

    else:
        print(subsection_choice + " was not a valid option. ")


def sphere_decision():
    print("Subsections: \n"
          "Find Volume (V)\n"
          "Find Radius (R)\n"
          "Find Diameter (D)\n"
          "Find Surface Area (SA)")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "V":
        r = float(eval(input("Enter Radius: ")))
        print("Volume: " + str(sphere.sphere_volume(r)))

    elif subsection_choice.upper() == "R":
        v = float(eval(input("Enter Volume: ")))
        print("Radius: " + str(sphere.sphere_radius(v)))

    elif subsection_choice.upper() == "D":
        r = float(eval(input("Enter Radius: ")))
        print("Diameter: " + str(sphere.sphere_diameter(r)))

    elif subsection_choice.upper() == "SA":
        r = float(eval(input("Enter Radius: ")))
        print("Surface Area: " + str(sphere.sphere_surface_area(r)))

    else:
        print(subsection_choice + " was not a valid option. ")


def trapezoid_decision():
    print("Subsections: \n"
          "Find Area (A)\n"
          "Find Height (H)\n"
          "Find Base A (BA)\n"
          "Find Base B (BB)\n"
          "Find Perimeter (P)\n"
          "Find Side C (SC)\n"
          "Find Side D (SD)")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "A":
        base_a = float(eval(input("Enter Base A: ")))
        base_b = float(eval(input("Enter Base B: ")))
        height = float(eval(input("Enter Height: ")))
        print("Area: " + str(trapezoid.trapezoid_area(base_a, base_b, height)))

    elif subsection_choice.upper() == "H":
        base_a = float(eval(input("Enter Base A: ")))
        base_b = float(eval(input("Enter Base B: ")))
        area = float(eval(input("Enter Area: ")))
        print("Height: " + str(trapezoid.trapezoid_height(base_a, base_b, area)))

    elif subsection_choice.upper() == "BA":
        base_b = float(eval(input("Enter Base B: ")))
        height = float(eval(input("Height: ")))
        area = float(eval(input("Enter Area: ")))
        print("Base A: " + str(trapezoid.trapezoid_base_a(base_b, height, area)))

    elif subsection_choice.upper() == "BB":
        base_a = float(eval(input("Enter Base A: ")))
        height = float(eval(input("Height: ")))
        area = float(eval(input("Enter Area: ")))
        print("Base B: " + str(trapezoid.trapezoid_base_b(base_a, height, area)))

    elif subsection_choice.upper() == "P":
        side_a = float(eval(input("Enter Side A: ")))
        side_b = float(eval(input("Enter Side B: ")))
        side_c = float(eval(input("Enter Side C: ")))
        side_d = float(eval(input("Enter Side D: ")))
        print("Perimeter: " + str(trapezoid.trapezoid_perimeter(side_a, side_b, side_c, side_d)))

    elif subsection_choice.upper() == "SC":
        perimeter = float(eval(input("Enter Perimeter: ")))
        side_a = float(eval(input("Enter Side A: ")))
        side_b = float(eval(input("Enter Side B: ")))
        side_d = float(eval(input("Enter Side D: ")))
        print("Side C: " + str(trapezoid.trapezoid_side_c(perimeter, side_a, side_b, side_d)))

    elif subsection_choice.upper() == "SD":
        perimeter = float(eval(input("Enter Perimeter: ")))
        side_a = float(eval(input("Enter Side A: ")))
        side_b = float(eval(input("Enter Side B: ")))
        side_c = float(eval(input("Enter Side C: ")))
        print("Side D: " + str(trapezoid.trapezoid_side_c(perimeter, side_a, side_b, side_c)))

    else:
        print(subsection_choice + " was not a valid option. ")


def triangle_decision():
    print("Subsections: \n"
          "Find Area (A)\n"
          "Find Base (B)\n"
          "Find Height (H)\n"
          "Find Perimeter (P)\n"
          "Find Third Angle Measure(TAM)")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "A":
        b = float(eval(input("Enter Base: ")))
        h = float(eval(input("Enter Height: ")))
        print("Area: " + str(triangle.triangle_area(b, h)))

    elif subsection_choice.upper() == "B":
        h = float(eval(input("Enter Height: ")))
        area = float(eval(input("Enter Area: ")))
        print("Base: " + str(triangle.triangle_base(h, area)))

    elif subsection_choice.upper() == "H":
        b = float(eval(input("Enter Base: ")))
        area = float(eval(input("Enter Area: ")))
        print("Height: " + str(triangle.triangle_height(b, area)))

    elif subsection_choice.upper() == "P":
        side_a = float(eval(input("Enter Side A: ")))
        side_b = float(eval(input("Enter Side B: ")))
        side_c = float(eval(input("Enter Side C: ")))
        print("Perimeter: " + str(triangle.triangle_perimeter(side_a, side_b, side_c)))

    elif subsection_choice.upper() == "TAM":
        ang_1 = float(eval(input("Enter the First Angle: ")))
        ang_2 = float(eval(input("Enter the Second Angle: ")))
        print("Third Angle Measure: " + str(triangle.triangle_third_angle(ang_1, ang_2)))

    else:
        print(subsection_choice + " was not a valid option. ")


def trig_definitions_decision():
    print("Subsections: \n"
          "Find Opposite Given Hypotenuse (OH)\n"
          "Find Adjacent Given Hypotenuse (AH)\n"
          "Find Opposite Given Adjacent (OA)\n"
          "Find Hypotenuse Given Opposite (HO)\n"
          "Find Hypotenuse Given Adjacent (HA)\n"
          "Find Adjacent Given Opposite (AO)\n"
          "Find Theta Given Hypotenuse and Opposite (THO)\n"
          "Find Theta Given Hypotenuse and Adjacent (THA)\n"
          "Find Theta Given Opposite and Adjacent (TOA)")

    subsection_choice = input("Choose Subsection: ")

    if subsection_choice.upper() == "OH":
        mode = input("Mode: Degrees or Radians (D/R)? ")
        mode = mode.upper()
        theta = float(eval(input("Enter Theta: ")))
        h = float(eval(input("Enter Hypotenuse: ")))
        dec_places = int(eval(input("Enter the number of decimal places to round to: ")))
        print("Opposite = " + str(trig_definitions.find_opposite_given_hypotenuse(theta, h, mode, dec_places)) + mode)

    elif subsection_choice.upper() == "AH":
        mode = input("Mode: Degrees or Radians (D/R)? ")
        mode = mode.upper()
        theta = float(eval(input("Enter Theta: ")))
        h = float(eval(input("Enter Hypotenuse: ")))
        dec_places = int(eval(input("Enter the number of decimal places to round to: ")))
        print("Adjacent = " + str(trig_definitions.find_adjacent_given_hypotenuse(theta, h, mode, dec_places)) + mode)

    elif subsection_choice.upper() == "OA":
        mode = input("Mode: Degrees or Radians (D/R)? ")
        mode = mode.upper()
        theta = float(eval(input("Enter Theta: ")))
        a = float(eval(input("Enter Adjacent: ")))
        dec_places = int(eval(input("Enter the number of decimal places to round to: ")))
        print("Opposite = " + str(trig_definitions.find_opposite_given_adjacent(theta, a, mode, dec_places)) + mode)

    elif subsection_choice.upper() == "HO":
        mode = input("Mode: Degrees or Radians (D/R)? ")
        mode = mode.upper()
        theta = float(eval(input("Enter Theta: ")))
        o = float(eval(input("Enter Opposite: ")))
        dec_places = int(eval(input("Enter the number of decimal places to round to: ")))
        print("Hypotenuse = " + str(trig_definitions.find_hypotenuse_given_opposite(theta, o, mode, dec_places)) + mode)

    elif subsection_choice.upper() == "HA":
        mode = input("Mode: Degrees or Radians (D/R)? ")
        mode = mode.upper()
        theta = float(eval(input("Enter Theta: ")))
        a = float(eval(input("Enter Adjacent: ")))
        dec_places = int(eval(input("Enter the number of decimal places to round to: ")))
        print("Hypotenuse = " + str(trig_definitions.find_hypotenuse_given_adjacent(theta, a, mode, dec_places)) + mode)

    elif subsection_choice.upper() == "AO":
        mode = input("Mode: Degrees or Radians (D/R)? ")
        mode = mode.upper()
        theta = float(eval(input("Enter Theta: ")))
        o = float(eval(input("Enter Opposite: ")))
        dec_places = int(eval(input("Enter the number of decimal places to round to: ")))
        print("Adjacent = " + str(trig_definitions.find_adjacent_given_opposite(theta, o, mode, dec_places)) + mode)

    elif subsection_choice.upper() == "THO":
        mode = input("Mode: Degrees or Radians (D/R)? ")
        mode = mode.upper()
        h = float(eval(input("Enter Hypotenuse: ")))
        o = float(eval(input("Enter Opposite: ")))
        dec_places = int(eval(input("Enter the number of decimal places to round to: ")))
        print("Theta = " + str(trig_definitions.find_theta_given_hypotenuse_and_opposite(h, o, mode, dec_places)) + mode)

    elif subsection_choice.upper() == "THA":
        mode = input("Mode: Degrees or Radians (D/R)? ")
        mode = mode.upper()
        h = float(eval(input("Enter Hypotenuse: ")))
        a = float(eval(input("Enter Adjacent: ")))
        dec_places = int(eval(input("Enter the number of decimal places to round to: ")))
        print("Theta = " + str(trig_definitions.find_theta_given_hypotenuse_and_adjacent(h, a, mode, dec_places)) + mode)

    elif subsection_choice.upper() == "TOA":
        mode = input("Mode: Degrees or Radians (D/R)? ")
        mode = mode.upper()
        o = float(eval(input("Enter Opposite: ")))
        a = float(eval(input("Enter Adjacent: ")))
        dec_places = int(eval(input("Enter the number of decimal places to round to: ")))
        print("Theta = " + str(trig_definitions.find_theta_given_hypotenuse_and_adjacent(o, a, mode, dec_places)) + mode)

    else:
        print(subsection_choice + " was not a valid option. ")


#Sort List Decision
def sort_list_decision():
    print("Data Types: \n"
          "Integers (I) \n"
          "Floats/Decimals (F)\n"
          "Strings/Text (S)")
    data_type = input("Enter the type of data that is used in your list: ")

    if data_type.upper() == "I":
        list_type = input("Would you like to generate a random list (GRL) or generate a custom list (GCL)? ")
        if list_type.upper() == "GRL":
            size = int(eval(input("Enter the size of your list (number of elements): ")))
            min_val = int(eval(input("Enter the minimum value for an integer in your list: ")))
            max_val = int(eval(input("Enter the maximum value for an integer in your list: ")))
            ls = sort_list.generate_random_ls_integer(size, min_val, max_val)
            sorted_ls = sort_list.sort_list(ls)
            print("Sorted list: " + str(sorted_ls))

        elif list_type.upper() == "GCL":
            size = int(eval(input("Enter the size of your list (number of elements): ")))
            ls = sort_list.generate_custom_ls_int(size)
            int_list = list(map(int, sort_list.sort_list(ls)))
            sorted_ls = sort_list.sort_list(int_list)
            print("Sorted list: " + str(sorted_ls))

        else:
            print(list_type + " was not a valid option. ")

    elif data_type.upper() == "F":
        list_type = input("Would you like to generate a random list (GRL) or generate a custom list (GCL)? ")
        if list_type.upper() == "GRL":
            size = int(eval(input("Enter the size of your list (number of elements): ")))
            min_val = float(eval(input("Enter the minimum value for a float in your list: ")))
            max_val = float(eval(input("Enter the maximum value for a float in your list: ")))
            ls = sort_list.generate_random_ls_float(size, min_val, max_val)
            sorted_ls = sort_list.sort_list(ls)
            print("Sorted list: " + str(sorted_ls))

        elif list_type.upper() == "GCL":
            size = int(eval(input("Enter the size of your list (number of elements): ")))
            ls = sort_list.generate_custom_ls_float(size)
            float_ls = list(map(float, sort_list.sort_list(ls)))
            sorted_ls = sort_list.sort_list(float_ls)
            print("Sorted list: " + str(sorted_ls))

        else:
            print(list_type + " was not a valid option. ")

    elif data_type.upper() == "S":
        list_type = input("Would you like to generate a random list (GRL) or generate a custom list (GCL)? ")
        if list_type.upper() == "GRL":
            size = int(eval(input("Enter the size of your list (number of elements): ")))
            min_len = int(eval(input("Enter the minimum length for a string (Starting at 1) in your list: ")))
            max_len = int(eval(input("Enter the maximum length for a string in your list: ")))

            print("Character Generation Options: \n"
                  "Letters Only (LO)\n"
                  "Digits, Whitespace, Punctuation, and Letters (DWPL)\n"
                  "Digits, Punctuation, and Letters (DPL)\n"
                  "Letters and Whitespace (LW)")

            char_choice = input("Character Generation Choice: ")

            if char_choice.upper() == "LO":
                ls = sort_list.generate_random_ls_string(size, min_len, max_len, False, False)
                sorted_ls = sort_list.sort_list(ls)
                print("Sorted list: " + str(sorted_ls))

            elif char_choice.upper() == "DWPL":
                ls = sort_list.generate_random_ls_string(size, min_len, max_len, True, True)
                sorted_ls = sort_list.sort_list(ls)
                print("Sorted list: " + str(sorted_ls))

            elif char_choice.upper() == "DPL":
                ls = sort_list.generate_random_ls_string(size, min_len, max_len, True, False)
                sorted_ls = sort_list.sort_list(ls)
                print("Sorted list: " + str(sorted_ls))

            elif char_choice.upper() == "LW":
                ls = sort_list.generate_random_ls_string(size, min_len, max_len, False, True)
                sorted_ls = sort_list.sort_list(ls)
                print("Sorted list: " + str(sorted_ls))

        elif list_type.upper() == "GCL":
            size = int(eval(input("Enter the size of your list (number of elements): ")))
            ls = sort_list.generate_custom_ls_string(size)
            sorted_ls = sort_list.sort_list(ls)
            print("Sorted list: " + str(sorted_ls))

        else:
            print(list_type + " was not a valid option. ")


#Standard Calculator Decision
def standard_calculator_decision():
    expression = input("Enter your expression: ")
    print("Solution: " + str(standard_calculator.calculation(expression)))


#Calculation Group Main Decision
def calculation_group_decision():

    #Try/Except statements for the entire program
    try:
        print("Calculation Groups: \n"
              "Algebra (ALG)\n"
              "Arts & Design (AD)\n"
              "Chemistry (CHEM)\n"
              "Computer Science (CS)\n"
              "Constants (CON)\n"
              "Geometry (GEOM)\n"
              "Sort List by Data Type (SLDT)\n"
              "Standard Calculator (SC)\n"
              "Tree (TREE)\n"
              "Update Check (UC)")

        group_choice = input("Choose Calculation Group: ")

        if group_choice.upper() == "ALG":
            algebra_decision()

        elif group_choice.upper() == "AD":
            arts_and_design_decision()

        elif group_choice.upper() == "CHEM":
            chemistry_decision()

        elif group_choice.upper() == "CS":
            computer_science_decision()

        elif group_choice.upper() == "CON":
            constants_decision()

        elif group_choice.upper() == "GEOM":
            geometry_decision()

        elif group_choice.upper() == "SLDT":
            sort_list_decision()

        elif group_choice.upper() == "SC":
            standard_calculator_decision()

        elif group_choice.upper() == "TREE":
            print(tree.tree)

        elif group_choice.upper() == "UC":
            updater.update_check()

        else:
            print(group_choice + " was not a valid option. ")

    except ZeroDivisionError:
        print("UNDEFINED")

    except ValueError:
        pass

    except Exception as e:
        print("SYNTAX ERROR!")
        exc_type, exc_obj, exc_tb = sys.exc_info()
        filename = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

        info = exc_type.__name__, filename, exc_tb.tb_lineno

        print("Error description: " + str(info))
        print("Error message: " + str(e))
        print("If you believe this is a bug, then please report it by sending a DM to @tekunion on Twitter. https://twitter.com/tekunion")


#Main runtime function
def main():

    print("The Tek Union 2015-2016")
    print("Console Universal Calculator Version " + updater.current_version)
    print("Programming by Nate Hill\n"
          "Testing by Chaise Glenn\n"
          "***Prototype of the Web App version that is in development.***\n"
          "\n"
          "Syntax Rules:\n"
          "+ = addition\n"
          "- = subtraction\n"
          "* = multiplication\n"
          "/ = division\n"
          "// = integer division\n"
          "% = modulus\n"
          "** = exponents (ex. 5 ** 2 = 25)\n"
          "math.pi = pi\n"
          "math.e = e (Euler\'s Number)\n"
          "math.sqrt(n) = square root of n "
          "You can type expressions for input in most fields as long as the result is the required data type. (Inputs that require text or inputs that explicitly state that expressions are not allowed prohibit this.)\n"
          "Example for above: \"Enter the amount of items: 2**5\""
          "\n"
          "NOTE: You can use a negative to round to the left of the decimal; 0 rounds to the ones place while -1 rounds to the tens place. \n"
          "NOTE: This calculator uses bankers\' rounding. (round half to nearest even integer) \n"
          "NOTE: The behavior of rounding for floats can be surprising: for example, rounding 2.675 to two decimal places gives 2.67 instead of the expected 2.68. \n"
          "This is not a bug: it\'s a result of the fact that most decimal fractions can\'t be represented exactly as a float. See https://docs.python.org/3/tutorial/floatingpoint.html#tut-fp-issues for more information.\n"
          "NOTE: All commands are case-insensitive, but they are shown in all caps. \n"
          "NOTE: YOU CANNOT USE IMPLICIT MULTIPLICATION, YOU HAVE TO USE THE ASTERISK. EX. (3*x instead of 3x) \n"
          "However, implicit multiplication is required for evaluating complex expressions. (Write 2j instead of 2*j)\n")

    print("Update info: ")
    updater.update_check()

    print()

    print("Type \"TREE\" for a list of all commands. ")

    continue_main_process = True

    while continue_main_process:

        calculation_group_decision()

        continue_input = input("Type \"EXIT\" if you want to exit the Console Universal Calculator. \nType anything else to continue using it:")

        if continue_input.upper() == "EXIT":
            continue_main_process = False

        else:
            continue_main_process = True

main()
