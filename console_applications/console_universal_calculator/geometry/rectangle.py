import math


def rect_area(length, width):
    return length * width


def rect_diagonal(length, width):
    return math.sqrt((length ** 2) + (width ** 2))


def rect_length(area, width):
    return area / width


def rect_perimeter(length, width):
    return (length * 2) + (width * 2)


def rect_width(area, length):
    return area / length
