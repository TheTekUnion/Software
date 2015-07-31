
print "Welcome to Calculator! \n"
print "Instructions: "
print "Enter operation. Ex. 3 * 3 \n"

while True:
    try:
        userIn = float(input("Enter operation: "))
        print userIn
    except ZeroDivisionError:
        print "You cannot divide by zero."
    except:
        print "You cannot enter text."



