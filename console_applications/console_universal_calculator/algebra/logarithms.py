import math
import numpy as np


def logarithm(argument, base):
    try:
        it = np.nditer([argument, None])
        for element, result in it:
            if element > 0:
                result[...] = logarithm_float(element, base)
            else:
                raise ValueError("INVALID DOMAIN")

    except ValueError:
        print("INVALID DOMAIN!")

    return it.operands[1]


def logarithm_float(argument, base):
    return math.log(argument, base)
