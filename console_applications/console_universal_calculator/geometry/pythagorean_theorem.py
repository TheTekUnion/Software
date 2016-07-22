import math


def find_hypotenuse(leg_a, leg_b):
    #a^2 + b^2 = c^2
    return math.sqrt(leg_a ** 2 + leg_b ** 2)


def find_leg_a(leg_b, hypotenuse):
    #c^2-b^2=a^2
    return math.sqrt(hypotenuse ** 2 - leg_b ** 2)


def find_leg_b(leg_a, hypotenuse):
    #c^2 - a^2 = b^2
    return math.sqrt(hypotenuse ** 2 - leg_a ** 2)