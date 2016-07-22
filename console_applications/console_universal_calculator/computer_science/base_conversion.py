import string
import math


#Binary Conversions
def binary_to_octal(binary_value):
    decimal_value = int(binary_value, 2)
    return oct(decimal_value)


def binary_to_decimal(binary_value):
    return int(binary_value, 2)


def binary_to_hexadecimal(binary_value):
    decimal_value = int(binary_value, 2)
    return hex(decimal_value)


#Octal Conversions
def octal_to_binary(octal_value):
    decimal_value = int(octal_value, 8)
    return bin(decimal_value)


def octal_to_decimal(octal_value):
    return int(octal_value, 8)


def octal_to_hexadecimal(octal_value):
    decimal_value = int(octal_value, 8)
    return hex(decimal_value)


#Decimal Conversions
def decimal_to_binary(decimal_value):
    return bin(decimal_value)


def decimal_to_octal(decimal_value):
    return oct(decimal_value)


def decimal_to_hexadecimal(decimal_value):
    return hex(decimal_value)


#Hexadecimal Conversions
def hexadecimal_to_binary(hexadecimal_value):
    decimal_value = int(hexadecimal_value, 16)
    return bin(decimal_value)


def hexadecimal_to_octal(hexadecimal_value):
    decimal_value = int(hexadecimal_value, 16)
    return oct(decimal_value)


def hexadecimal_to_decimal(hexadecimal_value):
    return int(hexadecimal_value, 16)


#Custom Conversion
def base_n_to_decimal(base_n_value, base_n):
    if base_n < 2 or base_n > 36:
        return "Base must be >= 2 and <= 36. "
    else:
        return int(base_n_value, base_n)


def decimal_to_base_n(decimal_value, base_n):
    if decimal_value == 0:
        return 0

    elif base_n < 2 or base_n > 36:
        return "Base must be >= 2 and <= 36. "

    else:
        alpha_num = string.digits + string.ascii_lowercase
        alpha_num_ls = list(alpha_num)
        unit_ls = []
        while decimal_value > 0:
            unit = decimal_value % base_n
            unit_char_index = alpha_num_ls[unit]
            unit_ls.append(unit_char_index)
            decimal_value //= base_n

        #Put the tuple in order (Elements were added in reverse)
        unit_ls.reverse()

        unit_str = "".join(unit_ls)

        return unit_str


def base_n_to_base_m(base_n, base_n_value, base_m):
    decimal_value = int(base_n_value, base_n)
    if decimal_value == 0:
        return 0

    elif base_n < 2 or base_n > 36:
        return "Base must be >= 2 and <= 36. "

    else:
        return decimal_to_base_n(decimal_value, base_m)
