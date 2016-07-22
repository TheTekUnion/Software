import math
import numpy as np

from algebra import radicals


def rational_exponent(base, power, root):
    try:
        if type(base) == np.ndarray:
            it = np.nditer([base, None])
            for element, result in it:
                result[...] = rational_exponent_float(element, power, root)
            return it.operands[1]

        elif type(power) == np.ndarray:
            it = np.nditer([power, None])
            for element, result in it:
                result[...] = rational_exponent_float(base, element, root)
            return it.operands[1]

        elif type(root) == np.ndarray:
            it = np.nditer([root, None])
            for element, result in it:
                result[...] = rational_exponent_float(base, power, element)
            return it.operands[1]
    except RuntimeWarning:
        print("INVALID DOMAIN!")


def rational_exponent_float(base, power, root):
        return math.pow(radicals.nth_root_float(base, root), power)


def exponent_float(base, power):
    return math.pow(base, power)
