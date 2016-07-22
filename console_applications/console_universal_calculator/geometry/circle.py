import math


def circle_area(radius):
    return math.pi * radius ** 2


def circle_sector_area(radius, central_angle):
    return (circle_area(radius)) * (central_angle / 360)


def circle_circumference(radius):
    return radius * 2 * math.pi


def circle_diameter(radius):
    return radius * 2


def circle_radius(diameter):
    return diameter / 2