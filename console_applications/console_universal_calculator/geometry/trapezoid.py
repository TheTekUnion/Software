import math


def trapezoid_area(base_a, base_b, height):
    return ((base_a + base_b) / 2) * height


def trapezoid_height(base_a, base_b, area):
    return 2 * (area / (base_a + base_b))


def trapezoid_base_a(base_b, height, area):
    return (2 * (area / height)) - base_b


def trapezoid_base_b(base_a, height, area):
    return (2 * (area / height)) - base_a


def trapezoid_perimeter(side_a, side_b, side_c, side_d):
    return side_a + side_b + side_c + side_d


def trapezoid_side_c(perimeter, side_a, side_b, side_d):
    return perimeter - side_a - side_b - side_d


def trapezoid_side_d(perimeter, side_a, side_b, side_c):
    return perimeter - side_a - side_b - side_c