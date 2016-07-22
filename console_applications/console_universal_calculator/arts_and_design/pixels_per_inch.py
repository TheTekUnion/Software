import math


def ppi(pixel_width, pixel_height, diagonal):
    return ((pixel_height ** 2 + pixel_width ** 2) ** .5) / diagonal
