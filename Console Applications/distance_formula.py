import math

while True:
    try:
        x2 = float(input("Enter x2: "))
        x1 = float(input("Enter x1: "))
        y2 = float(input("Enter y2: "))
        y1 = float(input("Enter y1: "))

        def distance(y1, y2, x1, x2):
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print "Distance: " + str(distance(y1, y2, x1, x2))
    except:
        print "You cannot enter text."
