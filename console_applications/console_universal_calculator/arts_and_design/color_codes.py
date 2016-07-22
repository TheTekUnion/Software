import pygame
import sys
import math


def hex_to_rgb(value):
    value = value.lstrip("#")
    len_val = len(value)
    #Convert hex to an integer then divide it up into three parts thus creating an rgb value
    return tuple(int(value[i:i + len_val // 3], 16) for i in range(0, len_val, len_val // 3))


def rgb_to_hex(rgb):
    #Convert rgb to hex by inserting three two digit hex values
    hex_val = "#%02x%02x%02x" % rgb
    hex_val = hex_val.upper()
    return hex_val


def show_color(rgb):
    try:
        pygame.init()
        width, height = 600, 400
        size = width, height
        screen = pygame.display.set_mode(size)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()

            screen.fill(rgb)
            pygame.display.update()

    #Ignore error to continue program
    except Exception:
        pass
