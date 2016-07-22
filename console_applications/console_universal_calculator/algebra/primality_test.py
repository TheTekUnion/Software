import math


def is_prime(candidate):
    prime = True
    #Trial division algorithm
    for factor in range(2, int(math.sqrt(candidate))):
        if candidate % factor == 0:
            prime = False
    return prime
