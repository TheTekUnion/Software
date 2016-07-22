import math


def reg_polygon_interior_angle_measure(sides):
    return (180 * (sides - 2)) / sides


def reg_polygon_interior_angle_sum(sides):
    return 180 * (sides - 2)


def reg_polygon_exterior_angle_measure(sides):
    return 360 / sides


def reg_polygon_exterior_angle_sum():
    return 360


def reg_polygon_area(apothem, perimeter):
    return (apothem * perimeter) / 2


def reg_polygon_perimeter(sides, side_length):
    return sides * side_length
