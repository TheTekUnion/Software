import math


def rect_prism_height(volume, length, width):
    return volume / (length * width)


def rect_prism_length(volume, height, width):
    return volume / (height * width)


def rect_prism_space_diagonal(length, width, height):
    return math.sqrt((length ** 2) + (width ** 2) + (height ** 2))


def rect_prism_surface_area(length, width, height):
    return 2 * ((width * length) + (height * length) + (height * width))


def rect_prism_volume(length, width, height):
    return length * width * height


def rect_prism_width(volume, height, length):
    return volume / (height * length)