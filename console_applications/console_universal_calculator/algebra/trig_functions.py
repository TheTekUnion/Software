import math

import numpy as np


def sin(theta):
    it = np.nditer([theta, None])
    for element, result in it:
        result[...] = sin_float(element, "R")

    return it.operands[1]


def cos(theta):
    it = np.nditer([theta, None])
    for element, result in it:
        result[...] = cos_float(element, "R")

    return it.operands[1]


def tan(theta):
    it = np.nditer([theta, None])
    for element, result in it:
        result[...] = tan_float(element, "R")

    return it.operands[1]


def asin(theta):
    it = np.nditer([theta, None])
    for element, result in it:
        result[...] = asin_float(element, "R")

    return it.operands[1]


def acos(theta):
    it = np.nditer([theta, None])
    for element, result in it:
        result[...] = acos_float(element, "R")

    return it.operands[1]


def atan(theta):
    it = np.nditer([theta, None])
    for element, result in it:
        result[...] = atan_float(element, "R")

    return it.operands[1]


def sin_float(theta, unit, rounding_place=3):
    if unit == "R":
        return round(math.sin(theta), rounding_place)
    elif unit == "D":
        return round(math.sin(math.radians(theta)), rounding_place)
    else:
        return "Invalid input."


def cos_float(theta, unit, rounding_place=3):
    if unit == "R":
        return round(math.cos(theta), rounding_place)
    elif unit == "D":
        return round(math.cos(math.radians(theta)), rounding_place)
    else:
        return "Invalid input."


def tan_float(theta, unit, rounding_place=3):
    try:
        if unit == "R":
            return round(math.tan(theta), rounding_place)
        elif unit == "D":
            return round(math.tan(math.radians(theta)), rounding_place)
        else:
            return "Invalid input."
    except ValueError:
        print("INVALID DOMAIN!")


def asin_float(theta, unit, rounding_place=3):
    try:
        if unit == "R":
            return round(math.asin(theta), rounding_place)
        elif unit == "D":
            return round(math.degrees(math.asin(theta)), rounding_place)
        else:
            return "Invalid input."

    except ValueError:
        print("INVALID DOMAIN!")


def acos_float(theta, unit, rounding_place=3):
    try:
        if unit == "R":
            return round(math.acos(theta), rounding_place)
        elif unit == "D":
            return round(math.degrees(math.acos(theta)), rounding_place)
        else:
            return "Invalid input."

    except ValueError:
        print("INVALID DOMAIN!")


def atan_float(theta, unit, rounding_place=3):
    if unit == "R":
        return round(math.atan(theta), rounding_place)
    elif unit == "D":
        return round(math.degrees(math.atan(theta)), rounding_place)
    else:
        return "Invalid input."
