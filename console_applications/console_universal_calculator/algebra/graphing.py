from algebra import exponents, factorial, radicals, logarithms, trig_functions
import numpy as np
import matplotlib.pyplot as plt
import string
import math
import random


def plot_coordinate(x, y):
    x_cord = [x]
    y_cord = [y]
    x_min = abs(x_cord[0]) * -2
    x_max = abs(x_cord[0]) * 2
    y_min = abs(y_cord[0]) * -2
    y_max = abs(y_cord[0]) * 2
    plt.plot(x_cord, y_cord, "ro")
    plt.axis([x_min, x_max, y_min, y_max])
    plt.hlines(y_cord, x_min, x_max)
    plt.xlabel("X-Axis")
    plt.vlines(x_cord, y_min, y_max)
    plt.ylabel("Y-Axis")
    plt.title("Cartesian Coordinate System")
    plt.grid()
    plt.show()


def plot_function(func_val, minimum_domain, maximum_domain):
    x = np.linspace(minimum_domain, maximum_domain, 1000)
    y = eval(func_val)
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("Cartesian Coordinate System")
    plt.plot(x, y)
    plt.grid()
    plt.show()


def plot_multiple_functions(func_ls, minimum_domain, maximum_domain):
    x = np.linspace(minimum_domain, maximum_domain, 1000)

    #Graph every function in func_ls
    for func in func_ls:
        y = eval(func)
        plt.plot(x, y)
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("Cartesian Coordinate System")
    plt.grid()
    plt.show()


def get_domain():
    min_x = float(eval(input("Enter the minimum domain value: ")))

    max_x = float(eval(input("Enter the maximum domain value: ")))

    return [min_x, max_x]


def get_func_values_ls(amount):
    #List Input
    cur_index = 0
    ls = []
    #Decremented size to use lists that start at 1 instead of 0
    amount -= 1
    #Character array of function names starting with "f"
    func_names = list(string.ascii_lowercase.replace("abcde", ""))
    while cur_index <= amount:
        item = input("Enter the value of your function: " + func_names[cur_index] + "(x) = ")
        ls.append(item)
        cur_index += 1
    return ls
