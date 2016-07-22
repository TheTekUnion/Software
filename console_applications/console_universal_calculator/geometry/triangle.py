import math


def triangle_area(base, height):
    return (base * height) / 2


def triangle_base(height, area):
    return (area / height) * 2


def triangle_height(base, area):
    return (area / base) * 2


def triangle_perimeter(side_a, side_b, side_c):
    return side_a + side_b + side_c


def triangle_third_angle(angle_1, angle_2):
    return 180 - angle_1 - angle_2