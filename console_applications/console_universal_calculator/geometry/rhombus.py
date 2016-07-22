import math


def rhombus_area(diagonal_p, diagonal_q):
    return (diagonal_p * diagonal_q) / 2


def rhombus_perimeter(side_length):
    return 4 * side_length


def rhombus_side_length(perimeter):
    return perimeter / 4


def rhombus_diagonal_q(diagonal_p, area):
    return (area / diagonal_p) * 2


def rhombus_diagonal_p(diagonal_q, area):
    return (area / diagonal_q) * 2