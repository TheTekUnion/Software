
while True:
    try:
        y2 = float(input("Enter y2: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        x1 = float(input("Enter x1: "))

        def slope(y1, y2, x1, x2):
            return (y2 - y1) / (x2 - x1)


        print("Slope: " + str(slope(y1, y2, x1, x2)))
    except ZeroDivisionError:
        print("Slope: Undefined")
    except:
        print("You cannot enter text.")
