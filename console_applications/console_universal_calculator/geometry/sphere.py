import math


def sphere_volume(radius):
    return (4 / 3) * math.pi * (radius ** 3)


def sphere_radius(volume):
    return math.pow(3 * (volume / (4 * math.pi)), 1 / 3)


def sphere_diameter(radius):
    return 2 * radius


def sphere_surface_area(radius):
    return 4 * math.pi * (radius ** 2)