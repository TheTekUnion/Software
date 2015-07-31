""" 
***PSUEDOCODE***

Give Instructions
Ask for the users minimum number.
Ask for the users maximum number.
Create a random number from the range.
Print the number.

""" 

#import modules
import random

#instructions
print "Welcome to Random Number."
print "Enter your minimum and maximum numbers. "
print "Numbers with decimals will be rounded. \n"

#Make the program run continuously.
while True:
	try:
		userMin = int(input("Enter your minimum number: "))
		userMax = int(input("Enter your maximum number: "))
		print random.randint(userMin, userMax)
	except:
		print "You cannot enter text."