import math
from algebra import trig_functions


def find_opposite_given_hypotenuse(theta, hypotenuse, mode, rounding_place=2):
    return trig_functions.sin_float(theta, mode, rounding_place) * hypotenuse


def find_adjacent_given_hypotenuse(theta, hypotenuse, mode, rounding_place=2):
    return trig_functions.cos_float(theta, mode, rounding_place) * hypotenuse


def find_opposite_given_adjacent(theta, adjacent, mode, rounding_place=2):
    return trig_functions.tan_float(theta, mode, rounding_place) * adjacent


def find_hypotenuse_given_opposite(theta, opposite, mode, rounding_place=2):
    return (1 / trig_functions.sin_float(theta, mode, rounding_place)) * opposite


def find_hypotenuse_given_adjacent(theta, adjacent, mode, rounding_place=2):
    return (1 / trig_functions.cos_float(theta, mode, rounding_place)) * adjacent


def find_adjacent_given_opposite(theta, opposite, mode, rounding_place=2):
    return (1 / trig_functions.tan_float(theta, mode, rounding_place)) * opposite


def find_theta_given_hypotenuse_and_opposite(hypotenuse, opposite, mode, rounding_place=2):
    o_div_h = opposite / hypotenuse
    return trig_functions.asin_float(o_div_h, mode, rounding_place)


def find_theta_given_hypotenuse_and_adjacent(hypotenuse, adjacent, mode, rounding_place=2):
    a_div_h = adjacent / hypotenuse
    return trig_functions.acos_float(a_div_h, mode, rounding_place)


def find_theta_given_opposite_and_adjacent(opposite, adjacent, mode, rounding_place=2):
    o_div_a = opposite / adjacent
    return trig_functions.atan_float(o_div_a, mode, rounding_place)
