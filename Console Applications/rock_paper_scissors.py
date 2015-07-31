"""
***LOGIC TABLE***

Rock = Rock
Scissors = Scissors
Paper = Paper

Rock > Scissors
Scissors > Paper
Paper > Rock

Rock < Scissors
Scissors < Paper
Paper < Rock
"""

import random
def compare(choice1, choice2):
    if choice1 == choice2:
        return "You tied."

    elif choice1 == "rock":
        if choice2 == "scissors":
            return "Rock wins!"
        else:
            return "Paper wins!"

    elif choice1 == "scissors":
        if choice2 == "paper":
            return "Scissors wins!"
        else:
            return "Rock wins!"

    elif choice1 == "paper":
        if choice2 == "rock":
            return "Paper wins!"
        else:
            return "Scissors wins!"
    else:
        return "You can only choose rock, paper, or scissors."


while True:
    userChoice = input("Do you choose rock, paper, or scissors? ")
    aiChoice = random.random()

    if aiChoice < .34:
        aiChoice = "rock"
    elif (aiChoice >= .34) and (aiChoice < .67):
        aiChoice = "paper"
    else:
        aiChoice = "scissors"

    print("AI choice: " + aiChoice)
    print(compare(userChoice, aiChoice))