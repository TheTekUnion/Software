#Makes the program run continuously (RUNTIME)
while True:
    #user input
    number = input("Enter a number ")
    #Initially True
    prime = True
    #2 - sqrt of number
    for factor in range(2, int(number ** 0.5 + 1)):
        #Trial Division Algorithm
        if number % factor == 0:
            prime = False
            break
    #Output
    if prime is True:
        print("%d is a prime number" % number)
    else:
        print("%d is not a prime number" % number)
