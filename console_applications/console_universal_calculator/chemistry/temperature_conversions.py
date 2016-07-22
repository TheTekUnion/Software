import math


#Temperature conversions
def celsius_to_fahrenheit(celsius_temp, rounding_place):
    new_temp = (celsius_temp * 1.8) + 32
    return round(new_temp, rounding_place)


def celsius_to_kelvin(celsius_temp, rounding_place):
    new_temp = celsius_temp + 273.15
    return round(new_temp, rounding_place)


def fahrenheit_to_celsius(fahrenheit_temp, rounding_place):
    new_temp = (fahrenheit_temp - 32) * (5 / 9)
    return round(new_temp, rounding_place)


def fahrenheit_to_kelvin(fahrenheit_temp, rounding_place):
    new_temp = (fahrenheit_temp + 459.67) * (5 / 9)
    return round(new_temp, rounding_place)


def kelvin_to_celsius(kelvin_temp, rounding_place):
    new_temp = kelvin_temp - 273.15
    return round(new_temp, rounding_place)


def kelvin_to_fahrenheit(kelvin_temp, rounding_place):
    new_temp = (kelvin_temp * 1.8) - 459.67
    return round(new_temp, rounding_place)
