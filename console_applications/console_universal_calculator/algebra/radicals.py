import math
import numpy as np


#Returns nth_root as numpy array
#Param radicand is a numpy array and index is an integer
def nth_root(radicand, index):

    try:
        it = np.nditer([radicand, None])
        for element, result in it:
            if index % 2 == 0:
                if element > 0:
                    result[...] = np.power(element, 1 / index)
                elif element < 0:
                    raise ValueError("A radical with an even index and a negative radicand results in an imaginary solution.")
                else:
                    zero = np.array([0.0])
                    result[...] = zero
            else:
                    if element > 0:
                        result[...] = np.power(element, (1 / index))

                    elif element < 0:
                        result[...] = -np.power(abs(element), (1 / index))

                    else:
                        zero = np.array([0.0])
                        result[...] = zero
    except ValueError:
        print("INVALID DOMAIN!")

    return it.operands[1]


#Returns nth root as a float
def nth_root_float(radicand, index, rounding_place=3):
    if index % 2 == 0:

        if radicand > 0:
            return round(math.pow(radicand, 1 / index), rounding_place)

        elif radicand < 0:
            print("UNDEFINED")

        else:
            return round(0.0, rounding_place)

    else:

        if radicand > 0:
            return round(math.pow(radicand, (1 / index)), rounding_place)

        elif radicand < 0:
            return round(-math.pow(abs(radicand), (1 / index)), rounding_place)

        else:
            return round(0.0, rounding_place)
