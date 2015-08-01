"""
The Tek Union 2015
The Unification of Mongolia
Programming by Nate Hill
Game Design by Nate Hill and Chaise Glenn
"""

import apprenticeships
import battle
import classes
import characters
import sys
import time
import quests


#Exception Class Created to break out of multiple loops
class ExitAllLoops(Exception):
    pass


#WARNING!!!!!!!!
#COMMENTING HAS NOT BEEN COMPLETED AND IN SOME SECTIONS IT IS OUTDATED
#UPDATED COMMENTS WILL COME IN A LATER PATCH
#This program uses modules in order to store external user information (class, village, etc.)
#Several loops are used in decision making
#Receive user's initial information
#RUNTIME LOGIC
try:
    while True:
        start = input("Are you ready to begin your epic adventure through Mongolia? (Y/N)?").upper()
        if start == "N":
            #Exit the program after 3 Seconds
            for i in range(1):
                print("Goodbye!")
                time.sleep(3)
                if i == 0:
                    sys.exit()

        elif start == "Y":
            name = input("Young adventurer, what is your name? ")
            print("Welcome, " + name)

            #Decision making
            while True:
                gender = input("Are you a male or female? (M/F)").upper()
                if gender == "M":
                    print("You are a man. ")
                    break
                elif gender == "F":
                    print("You are a woman. ")
                    break
                else:
                    print(gender + " is not a valid gender. ")
                    continue

            village = input("What village are you from? ")
            #Ternary conditionals are used frequently throughout the passage (marked by parenthesis)
            #String literals are also used in the form of new line and single quote
            print(
                "There once was a " + ("man" if gender == "M" else "woman") + " named \n"
                + name + " who lived in a village on the steppes of Mongolia. \n" +
                ("He" if gender == "M" else "She") + " lived in a village called " + village + ", and " + ("he" if gender == "M" else "she") + "\n"
                + " lived a solitary life. This " + ("man" if gender == "M" else "woman") + " is you. \n"
                "You\'ve worked for your father, Yesugei, your entire life. \n"
                "You don\'t ask for much, just for a peaceful life with your father. \n"
                "When you were young, your mother passed away from a disease. \n"
                "It has been hard for your father, but he has done everything to provide for you. \n"
                "Everything had been going smoothly since... until that day.")

            print(
                "It\'s late into the night, and you are awaken from you sleep to the sound of screaming. \n"
                "You hear fire and the sound of swords being clashed together. \n"
                "As soon as you jump out of bed, an arrow flies through your window and right past your head. \n"
                "You yell for your father, who is only a room away, but by the time you get there, the room is ablaze. \n"
                "You realize that you must leave the house as fast as possible, and you dash out the door. \n"
                " You see your village in flames and men with swords everywhere. \n"
                "You can only deduce that you are under attack by the Kara-Khitai. \n"
                "You look around, wondering what to do, but you aren\'t very trained in combat, and you still don\'t know where \n"
                "your dad is. Suddenly, you hear your name being called... it\'s your dad. You see him on the ground, and you go \n"
                " to his side to make sure he is okay. You try not to believe it, but you see the stab wound in his right \n"
                " shoulder. He is bleeding fast, and you don\'t know what to do. Just then, you look up and see moonlit metal \n"
                "cover the horizon. It\'s the army from Ulaanbaatar, being led by The Great Khan! You feel a faint light of hope,\n"
                " but as you look down at your father, you realize that he isn\'t moving. You call out his name, shake him, slap \n"
                "him, but he does not respond.You cry out in agony, but you are smart enough to know that now is not the time to\n"
                " mourn over the dead... you need to get out of there. You give your dad one last kiss on the head, \n"
                "and you flee into a field and begin heading towards Naiman. You may still be sixteen, but you know how to fend \n"
                "for yourself... your dad has taught you much. \n")

            #Decision Making
            while True:
                print("Apprenticeship options: \n"
                      "Note: Apprenticeships have the three following bonuses: Health, Attack, Defense (H/A/D) \n"
                      "Apothecary (60/0/0) \n"
                      "Blacksmith (0/0/60) \n"
                      "Farmer (40/0/20) \n"
                      "Laborer (20/20/20) \n"
                      "Steppe Bandit (0/60/0) \n"
                      "Woodsman (20/40/0) \n")
                apprenticeship = input("You begin your apprenticeship as a ").lower()
                if apprenticeship == "apothecary":
                    break
                elif apprenticeship == "blacksmith":
                    break
                elif apprenticeship == "farmer":
                    break
                elif apprenticeship == "laborer":
                    break
                elif apprenticeship == "steppe bandit":
                    break
                elif apprenticeship == "woodsman":
                    break
                else:
                    continue

            print("Four Years Later... ")

            print(
                "It\'s been years since your father died, and so far you\'ve been able to hold your own, but you are \n"
                "beginning to feel bored with the way you are currently living. Everyday \n"
                "just seems to be the same day, and you wish to make a name for yourself. You still \n"
                "remain an apprentice as a " + apprenticeship + " , but you want to be recognized for something more. ")

            #Nested If/Elif/Else statements are used in the following code to manipulate the user's choice
            #Decision making
            while True:
                choice1 = input("Do you want to pursue your dream of becoming something greater? (Y/N)").upper()
                if choice1 == "N":
                    print(
                        "You eventually master your skill and become a very successful " + apprenticeship + ", \n"
                        "but after many years, you die alone. ")
                    continue

                elif choice1 == "Y":
                    print(
                        "You decide to pursue your dreams of fame, so the next day you journey to Ulaanbaatar in hopes of finding a \n"
                        "better life. You arrive in the thriving capital city the next day, and you immediately head towards the \n"
                        "chieftain\'s yurt in hopes of applying for the military. You arrive at the yurt, and you see that it is \n"
                        " heavily guarded. You are confronted by two guards who ask you what your business there is. ")

                    #Decision making
                    while True:
                        choice2 = input(
                            """
                            Tell the guards that you have an urgent message for The Great Khan so that you can get by them. (1)\n
                            Tell them that you want to apply for the military. (2)
                            """
                        ).upper()

                        if choice2 == "1":
                            print(
                                "You enter the yurt and see The Great Khan there sitting with his chiefs. \n"
                                "As soon as you explain your real purpose to him and he realizes that you lied,\n"
                                " he throws you out of his tent and orders you to be disembodied and then burnt at the stake. "
                            )
                            continue

                        elif choice2 == "2":
                            print(
                                "You enter the tent and approach The Great Khan. He isn\'t as intimidating as you remember him to be,\n"
                                " and it looks as if he is fallen under a sickness. He speaks very softly, but he asks what you want.\n"
                                "You tell him that you wish to apply for the military. He says that you have guts to come all the way\n"
                                "to him to only ask for a position in the military. He quickly takes you for a fool. He jokingly says\n"
                                "that if you can lift his sickness from him, then he will let you become anything you wanted to be.\n"
                                " You can hear the sarcasm in his voice, but you aren\'t going to give up so easily. You leave the city,\n"
                                " and begin your search for a cure. You think that if you can cure him, he must keep his word, but you \n"
                                "don\'t know where to begin. You could either go back toward Naiman, \n"
                                "or you could head to a bigger village in search of a cure. \n")
                            #Decision making
                            while True:
                                choice3 = input(
                                    """
                                    Head back to Naiman and look around. (1) \n
                                    Head on to Merkit, a bigger village.  (2)

                                    """
                                ).upper()

                                if int(choice3) == 1:
                                    print("You look around at your village, but you find nothing. A day wasted..."
                                          " Later in the afternoon you hear word of Khan\'s death. ")
                                    continue

                                elif int(choice3) == 2:
                                    print(
                                        "You head towards Merkit, and you see that they have a much better shaman than in Naiman. \n"
                                        "You head into the yurt and you are greeted by the shaman. You explain your situation, \n"
                                        "but instead of mentioning Khan, you simply say that it is for a sibling. The shaman, \n"
                                        " Yesui, recommends a rare herb that has been known to cure diseases like the one you described. \n"
                                        " You tell Yesui that you will take the herb, but as you reach for your money, you find that \n"
                                        "it is missing. If you do not get this herb, Khan will surely die! ")

                                    #Decision making
                                    while True:
                                        choice4 = input(
                                            """
                                            Snatch the herb and make a run for it. (1) \n
                                            Walk out of the door empty handed. (2)
                                            """
                                        ).upper()
                                        if int(choice4) == 1:
                                            print(
                                                "You grab the herb out of Yesui\'s hand and make a mad dash for the door. \n"
                                                "You make it out of the shop, but the commotion attracts the attention of \n"
                                                "some village officials, and they quickly catch you and declare you a thief.\n"
                                                " You are thrown in jail, never to see the light of day again. ")
                                            continue

                                        elif int(choice4) == 2:
                                            print(
                                                "With a sorrowful expression, you apologize to Yesui, saying that you do not\n"
                                                " have enough money. Seeing the distress on your face, Yesui offers the herb for \n"
                                                "free and says to consider it as a gift. Grateful for his generosity, you embrace \n"
                                                "him and rejoice over his kindness. You quickly make the journey back to Ulaanbaatar\n"
                                                " and rush to present Khan with your gift. Khan is hesitant at first, but he allows\n"
                                                " the herb to be administered to him. The herb allowed him to live for a few more \n"
                                                "days, but it was not enough to save him. His dying wish is for you to become his\n"
                                                " heir and fulfill his dream of uniting the Mongol tribes. \n"
                                                "He suggests that you unite the neighboring tribes under your banner\n"
                                                " and then you should defeat his arch nemesis, Kuchlag. ")

                                            #Decision making
                                            while True:
                                                print("Class Options: \n"
                                                      "Note: Skills have three attributes: Damage, Chance, Beast Bonus (D/C/BB)\n"
                                                      "Note: Mounted classes cause more damage but have a lower chance of success for skills \n"
                                                      "Horse Archer: \n"
                                                      "\tMounted: Yes\n"
                                                      "\tHealth: 100\n"
                                                      "\tAttack: 200\n"
                                                      "\tDefense: 50\n"
                                                      "\tSkill 1: Mounted Quick Shot (70, .9, N)\n"
                                                      "\tSkill 2: Mounted Flaming Shot (90, .75, Y)\n"
                                                      "\tSkill 3: Mounted Heart Seeker (350, .2, N)\n"
                                                      "\n"
                                                      "Steppe Lancer: \n"
                                                      "\tMounted: Yes\n"
                                                      "\tHealth: 100\n"
                                                      "\tAttack: 130\n"
                                                      "\tDefense: 120\n"
                                                      "\tSkill 1: Happy Mounted Javelin Day (80, .9, N)\n"
                                                      "\tSkill 2: Mounted Mace Attack (100, .75, N)\n"
                                                      "\tSkill 3: Mounted Lance Attack (350, .2, Y)\n"
                                                      "\n"
                                                      "Hunter: \n"
                                                      "\tMounted: No\n"
                                                      "\tHealth: 100\n"
                                                      "\tAttack: 190\n"
                                                      "\tDefense: 60\n"
                                                      "\tSkill 1: Quick Shot (70, .9, N)\n"
                                                      "\tSkill 2: Flaming Shot (90, .75, Y)\n"
                                                      "\tSkill 3: Heart Seeker (350, .2, N)\n"
                                                      "\n"
                                                      "ChuKuNu: \n"
                                                      "\tMounted: No\n"
                                                      "\tHealth: 100\n"
                                                      "\tAttack: 180\n"
                                                      "\tDefense: 70\n"
                                                      "\tSkill 1: Dagger Stab (60, .9, N)\n"
                                                      "\tSkill 2: Crossbow Shot (125, .75, N)\n"
                                                      "\tSkill 3: Crossbow Headshot (350, .2, Y)\n"
                                                      "\n"
                                                      "Steppe Spearmen: \n"
                                                      "\tMounted: No\n"
                                                      "\tHealth: 100\n"
                                                      "\tAttack: 125\n"
                                                      "\tDefense: 125\n"
                                                      "\tSkill 1: Happy Javelin Day (70, .9, N)\n"
                                                      "\tSkill 2: Spear Stab (90, .75, Y)\n"
                                                      "\tSkill 3: Spear Head Stab (350, .2, N)\n"
                                                      "\n"
                                                      "Uar Warrior: \n"
                                                      "\tMounted: No\n"
                                                      "\tHealth: 100\n"
                                                      "\tAttack: 250\n"
                                                      "\tDefense: 0\n"
                                                      "\tSkill 1: Happy Javelin Day (70, .9, N)\n"
                                                      "\tSkill 2: Sword Slash (120, .75, N)\n"
                                                      "\tSkill 3: Decapitation (350, .2, Y)\n"
                                                      "\n"
                                                      "Khan\'s Guard: \n"
                                                      "\tMounted: No\n"
                                                      "\tHealth: 100\n"
                                                      "\tAttack: 100\n"
                                                      "\tDefense: 150\n"
                                                      "\tSkill 1: Happy Javelin Day (70, .9, N)\n"
                                                      "\tSkill 2: Shield Bash (120, .75, Y)\n"
                                                      "\tSkill 3: Loyalty of the Tenth (350, .2, N)\n"
                                                      "\n"
                                                      "Statistics for NPCs: \n"
                                                      "Ornlu: \n"
                                                      "\tMounted: No\n"
                                                      "\tHealth: 300\n"
                                                      "\tAttack: 150\n"
                                                      "\tDefense: 100\n"
                                                      "\tSkill 1: Attack Skill (50, .8, N)\n"
                                                      "\n"
                                                      "Kuchlag: \n"
                                                      "\tMounted: No\n"
                                                      "\tHealth: 1000\n"
                                                      "\tAttack: 50\n"
                                                      "\tDefense: 200\n"
                                                      "\tSkill 1: Attack Skill (50, .8, N)\n"
                                                      )
                                                player_class = input("What class you like to be on your adventure?").lower()
                                                if player_class == classes.HorseArcher.class_name:
                                                    p = classes.HorseArcher(name, apprenticeship)
                                                    #Apply the apprenticeship bonus
                                                    apprenticeships.apprenticeships(p, apprenticeship)
                                                    print("You are now a, " + player_class + ".")
                                                    break
                                                elif player_class == classes.SteppeLancer.class_name:
                                                    p = classes.SteppeLancer(name, apprenticeship)
                                                    #Apply the apprenticeship bonus
                                                    apprenticeships.apprenticeships(p, apprenticeship)
                                                    print("You are now a, " + player_class + ".")
                                                    break
                                                elif player_class == classes.Hunter.class_name:
                                                    p = classes.Hunter(name, apprenticeship)
                                                    #Apply the apprenticeship bonus
                                                    apprenticeships.apprenticeships(p, apprenticeship)
                                                    print("You are now a, " + player_class + ".")
                                                    break
                                                elif player_class == classes.ChuKuNu.class_name:
                                                    p = classes.ChuKuNu(name, apprenticeship)
                                                    #Apply the apprenticeship bonus
                                                    apprenticeships.apprenticeships(p, apprenticeship)
                                                    print("You are now a, " + player_class + ".")
                                                    break
                                                elif player_class == classes.SteppeSpearmen.class_name:
                                                    p = classes.SteppeSpearmen(name, apprenticeship)
                                                    #Apply the apprenticeship bonus
                                                    apprenticeships.apprenticeships(p, apprenticeship)
                                                    print("You are now a, " + player_class + ".")
                                                    break
                                                elif player_class == classes.UarWarrior.class_name:
                                                    p = classes.UarWarrior(name, apprenticeship)
                                                    #Apply the apprenticeship bonus
                                                    apprenticeships.apprenticeships(p, apprenticeship)
                                                    print("You are now a, " + player_class + ".")
                                                    break
                                                elif player_class == classes.KhansGuard.class_name:
                                                    p = classes.KhansGuard(name, apprenticeship)
                                                    #Apply the apprenticeship bonus
                                                    apprenticeships.apprenticeships(p, apprenticeship)
                                                    print("You are now a, " + player_class + ".")
                                                    break
                                                else:
                                                    print(player_class + " is not a valid option. ")
                                                    continue

                                            #Village quests handled in the quests module
                                            quests.quests(p, player_class)

                                            #Village quests have completed
                                            print("Now that you have united the tribes, you are ready to confront the Kara-Khitai and \n"
                                            "behead their leader Kuchlag! You will need the combined strength of all the tribes to take on \n"
                                            "this mighty foe, so lead your men! You start the battle on the opposite side of the river as \n"
                                            "the Kara-Khitai, and there stands Kuchlag. The anticipation builds, and although Kuchlag has \n"
                                            "strength in numbers, you know how you can win this battle with strategy alone. You send your \n"
                                            "horse archers across the river to get the enemy scrambled, and you use this distraction as \n"
                                            "bait to draw their front lines straight into your infantry trap. You sit towards the front, \n"
                                            "knee-deep in the blood of your enemies, but after a brief moment of calm, you find your way \n"
                                            "through the battlefield to where Kuchlag sits. In this moment, the chaos around seems to die \n"
                                            "away, and your sole focus is to take the head of this beast. After much anticipation, you face \n"
                                            "Kuchlag in battle.")
                                            #Instantiate kuchlag as an instance of Kuchlag
                                            kuchlag = characters.Kuchlag()
                                            #Action setup for several playable troop types
                                            #Action for Horse Archer
                                            if player_class == classes.HorseArcher.class_name:
                                                #Add buffs from defeating ornlu
                                                p.health += 100
                                                p.attack += 100
                                                p.defense += 100
                                                #Initialize target variables with statistics of Kuchlag
                                                p.target = kuchlag
                                                p.target_name = kuchlag.name
                                                p.target_health = kuchlag.health
                                                p.target_defense = kuchlag.defense
                                                #Initializes AI target variables for Kuchlag with statistics of the player
                                                kuchlag.target = p
                                                kuchlag.target_name = p.name
                                                kuchlag.target_health = p.health
                                                kuchlag.target_defense = p.defense
                                                #Repeat the battle instance function with the player instance and kuchlag instance until the player wins
                                                while True:
                                                    battle.battle_instance(p, kuchlag)
                                                    if kuchlag.is_alive is False:
                                                        break
                                            #Action for Steppe Lancer
                                            elif player_class == classes.SteppeLancer.class_name:
                                                #Add buffs from defeating ornlu
                                                p.health += 100
                                                p.attack += 100
                                                p.defense += 100
                                                #Initialize target variables with statistics of Kuchlag
                                                p.target = kuchlag
                                                p.target_name = kuchlag.name
                                                p.target_health = kuchlag.health
                                                p.target_defense = kuchlag.defense
                                                #Initializes AI target variables for Kuchlag with statistics of the player
                                                kuchlag.target = p
                                                kuchlag.target_name = p.name
                                                kuchlag.target_health = p.health
                                                kuchlag.target_defense = p.defense
                                                #Repeat the battle instance function with the player instance and kuchlag instance until the player wins
                                                while True:
                                                    battle.battle_instance(p, kuchlag)
                                                    if kuchlag.is_alive is False:
                                                        break
                                            #Action for Hunter
                                            elif player_class == classes.Hunter.class_name:
                                                #Add buffs from defeating ornlu
                                                p.health += 100
                                                p.attack += 100
                                                p.defense += 100
                                                #Initialize target variables with statistics of Kuchlag
                                                p.target = kuchlag
                                                p.target_name = kuchlag.name
                                                p.target_health = kuchlag.health
                                                p.target_defense = kuchlag.defense
                                                #Initializes AI target variables for Kuchlag with statistics of the player
                                                kuchlag.target = p
                                                kuchlag.target_name = p.name
                                                kuchlag.target_health = p.health
                                                kuchlag.target_defense = p.defense
                                                #Repeat the battle instance function with the player instance and kuchlag instance until the player wins
                                                while True:
                                                    battle.battle_instance(p, kuchlag)
                                                    if kuchlag.is_alive is False:
                                                        break
                                            #Action for ChuKuNu
                                            elif player_class == classes.ChuKuNu.class_name:
                                                #Add buffs from defeating ornlu
                                                p.health += 100
                                                p.attack += 100
                                                p.defense += 100
                                                #Initialize target variables with statistics of Kuchlag
                                                p.target = kuchlag
                                                p.target_name = kuchlag.name
                                                p.target_health = kuchlag.health
                                                p.target_defense = kuchlag.defense
                                                #Initializes AI target variables for Kuchlag with statistics of the player
                                                kuchlag.target = p
                                                kuchlag.target_name = p.name
                                                kuchlag.target_health = p.health
                                                kuchlag.target_defense = p.defense
                                                #Repeat the battle instance function with the player instance and kuchlag instance until the player wins
                                                while True:
                                                    battle.battle_instance(p, kuchlag)
                                                    if kuchlag.is_alive is False:
                                                        break
                                            #Action for Steppe Spearmen
                                            elif player_class == classes.SteppeSpearmen.class_name:
                                                #Add buffs from defeating ornlu
                                                p.health += 100
                                                p.attack += 100
                                                p.defense += 100
                                                #Initialize target variables with statistics of Kuchlag
                                                p.target = kuchlag
                                                p.target_name = kuchlag.name
                                                p.target_health = kuchlag.health
                                                p.target_defense = kuchlag.defense
                                                #Initializes AI target variables for Kuchlag with statistics of the player
                                                kuchlag.target = p
                                                kuchlag.target_name = p.name
                                                kuchlag.target_health = p.health
                                                kuchlag.target_defense = p.defense
                                                #Repeat the battle instance function with the player instance and kuchlag instance until the player wins
                                                while True:
                                                    battle.battle_instance(p, kuchlag)
                                                    if kuchlag.is_alive is False:
                                                        break
                                            #Action for UarWarrior
                                            elif player_class == classes.UarWarrior.class_name:
                                                #Add buffs from defeating ornlu
                                                p.health += 100
                                                p.attack += 100
                                                p.defense += 100
                                                #Initialize target variables with statistics of Kuchlag
                                                p.target = kuchlag
                                                p.target_name = kuchlag.name
                                                p.target_health = kuchlag.health
                                                p.target_defense = kuchlag.defense
                                                #Initializes AI target variables for Kuchlag with statistics of the player
                                                kuchlag.target = p
                                                kuchlag.target_name = p.name
                                                kuchlag.target_health = p.health
                                                kuchlag.target_defense = p.defense
                                                #Repeat the battle instance function with the player instance and kuchlag instance until the player wins
                                                while True:
                                                    battle.battle_instance(p, kuchlag)
                                                    if kuchlag.is_alive is False:
                                                        break
                                            #Action for Khan's Guard
                                            elif player_class == classes.KhansGuard.class_name:
                                                #Add buffs from defeating ornlu
                                                p.health += 100
                                                p.attack += 100
                                                p.defense += 100
                                                #Initialize target variables with statistics of Kuchlag
                                                p.target = kuchlag
                                                p.target_name = kuchlag.name
                                                p.target_health = kuchlag.health
                                                p.target_defense = kuchlag.defense
                                                #Initializes AI target variables for Kuchlag with statistics of the player
                                                kuchlag.target = p
                                                kuchlag.target_name = p.name
                                                kuchlag.target_health = p.health
                                                kuchlag.target_defense = p.defense
                                                #Repeat the battle instance function with the player instance and kuchlag instance until the player wins
                                                while True:
                                                    battle.battle_instance(p, kuchlag)
                                                    if kuchlag.is_alive is False:
                                                        break
                                            print("""
                                            Now that you have defeated Kuchlag, his forces waver and
                                            start fleeing the field. As you hold his head high up into the air, your battle cry can be
                                            heard across the battlefield. Your troops begin to rally... soon enough, they have chased
                                            down and slaughtered every last enemy. Mongolia is now united under the same banner, and
                                            it is a victorious day!""")
                                            print("Thank you for playing The Unification of Mongolia! Please check out our other games and software on thetekunion.com")
                                            #Output credits.
                                            print(
                                                """
                                                The Tek Union 2015
                                                The Unification of Mongolia
                                                Programming by Nate Hill
                                                Game Design by Nate Hill and Chaise Glenn
                                                """)
                                            #Throw the exception to exit all of the loops
                                            raise ExitAllLoops

                                        #Tell the user their input was invalid
                                        else:
                                            print(choice4 + " was not a valid option. ")
                                            continue

                                #Tell the user their input was invalid
                                else:
                                    print(choice3 + " was not a valid option. ")
                                    continue

                        #Tell the user their input was invalid
                        else:
                            print(choice2 + " was not a valid option. ")
                            continue

                #Tell the user their input was invalid
                else:
                    print(choice1 + " was not a valid option. ")
                    continue
        else:
            print(start + " was not a valid option. ")

except ExitAllLoops:
    pass