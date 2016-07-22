#Factorial algorithm using iteration
def factorial(n):

    if n == 0 or n == 1:
        return 1

    else:
        product = 1

        for i in range(1, n + 1):
            product *= i

        return product
