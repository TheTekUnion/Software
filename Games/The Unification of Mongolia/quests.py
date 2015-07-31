import battle
import characters
import game_map
import classes
import random


def quests(p, player_class):

    #Create the village instances from the Map module
    naiman = game_map.Village("Naiman", game_map.get_dialogue_n())
    merkit = game_map.Village("Merkit", game_map.get_dialogue_m())
    tatar = game_map.Village("Tatar", game_map.get_dialogue_t())
    khereid = game_map.Village("Khereid", game_map.get_dialogue_k())
    khamag = game_map.Village("Khamag", game_map.get_dialogue_kg())

    while True:
        naiman_choice_complete = naiman.quest_completed and merkit.quest_completed and khereid.quest_completed and khamag.quest_completed
        tatar_choice_complete = merkit.quest_completed and tatar.quest_completed and khereid.quest_completed and khamag.quest_completed

        if naiman_choice_complete is True or tatar_choice_complete is True:
            break
        print("What tribe would you like to visit? ")
        village_option = input(
            """
            Naiman (N)\n
            Merkit (M)\n
            Tatar (T)\n
            Khereid (K)\n
            Khamag (KG)
            """).upper()

        def village_order(vil_in):
            if vil_in == "N":
                return naiman

            elif vil_in == "M":
                return merkit

            elif vil_in == "T":
                return tatar

            elif vil_in == "K":
                return khereid

            elif vil_in == "KG":
                return khamag

            #Tell the user their input was invalid
            else:
                return village_option + " was not a valid option. "

        #Create a variable to avoid several function calls (Simple is better than Complex!)
        vil = village_order(village_option)

        #Checks to see if a village object is returned
        village_order(village_option)
        if isinstance(vil, game_map.Village):
            #Conditionals used to set up quests
            #Quest for Naiman
            if vil == naiman:
                if tatar.quest_completed is not True:
                    #Output dialogue and ask the user if they want to enter the quest
                    print(vil.dialogue)
                    naiman_quest_accept = input("Do you want to take this quest? (Y/N) ").upper()
                    if naiman_quest_accept == "Y":
                        print("You travel to the Tatar village and raze it to the ground. ")
                        naiman.complete()
                        continue
                    elif naiman_quest_accept == "N":
                        print("You decide to come back later. ")
                    else:
                        print(naiman_quest_accept + " is not a valid option. ")
                else:
                    print("You have already razed this village. ")

            #Quest for Merkit
            elif vil == merkit:
                if merkit.quest_completed is not True:
                    #Output dialogue and ask the user if they want to enter the quest
                    print(vil.dialogue)
                    merkit_quest_accept = input("Do you want to take this quest? (Y/N) ").upper()
                    if merkit_quest_accept == "Y":
                        print("Yesui says that if you are worthy, then you will have Tengri on your side. ")
                        print("He hands you a dice and he tells you that you must roll a 6.")
                        dice_roll = random.randrange(1, 7)
                        if dice_roll == 6:
                            print("You rolled a " + str(dice_roll))
                            print("You have passed Tengri\'s test!")
                            merkit.complete()
                            continue
                        else:
                            print("You rolled a " + str(dice_roll))
                            print("You have failed Tengri\'s test!")
                    elif merkit_quest_accept == "N":
                        print("You decide to come back later. ")
                    else:
                        print(merkit_quest_accept + " is not a valid option. ")
                else:
                    print("You have already completed this quest. ")

            #Quest for Tatar
            elif vil == tatar:
                if naiman.quest_completed is not True:
                    #Output dialogue and ask the user if they want to enter the quest
                    print(vil.dialogue)
                    tatar_quest_accept = input("Do you want to take this quest? (Y/N) ").upper()
                    if tatar_quest_accept == "Y":
                        print("You travel to the Naiman village and raze it to the ground. ")
                        tatar.complete()
                        continue
                    elif tatar_quest_accept == "N":
                        print("You decide to come back later. ")
                    else:
                        print(tatar_quest_accept + " is not a valid option. ")
                else:
                    print("You have already razed this village. ")

            #Quest for Khereid
            elif vil == khereid:
                if khereid.quest_completed is not True:
                    #Output dialogue and ask the user if they want to enter the quest
                    print(vil.dialogue)
                    khereid_quest_accept = input("Do you want to take this quest? (Y/N) ").upper()
                    if khereid_quest_accept == "Y":
                        #Wolf's lair fight scene dialogue
                        print("You attack ornlu. ")
                        #Instantiate ornlu as an instance of Ornlu
                        ornlu = characters.Ornlu()
                        #Action setup for several playable troop types
                        #Action for Horse Archer
                        if player_class == classes.HorseArcher.class_name:
                            #Initialize target variables with statistics of Ornlu
                            p.target = ornlu
                            p.target_name = ornlu.name
                            p.target_health = ornlu.health
                            p.target_defense = ornlu.defense
                            #Initializes AI target variables for Ornlu with statistics of the player
                            ornlu.target = p
                            ornlu.target_name = p.name
                            ornlu.target_health = p.health
                            ornlu.target_defense = p.defense
                            #Run the battle instance function with the player instance and ornlu instance with stats
                            battle.battle_instance(p, ornlu)
                        #Action for Steppe Lancer
                        elif player_class == classes.SteppeLancer.class_name:
                            #Initialize target variables with statistics of Ornlu
                            p.target = ornlu
                            p.target_name = ornlu.name
                            p.target_health = ornlu.health
                            p.target_defense = ornlu.defense
                            #Initializes AI target variables for Ornlu with statistics of the player
                            ornlu.target = p
                            ornlu.target_name = p.name
                            ornlu.target_health = p.health
                            ornlu.target_defense = p.defense
                            #Run the battle instance function with the player instance and ornlu instance with stats
                            battle.battle_instance(p, ornlu)
                        #Action for Hunter
                        elif player_class == classes.Hunter.class_name:
                            #Initialize target variables with statistics of Ornlu
                            p.target = ornlu
                            p.target_name = ornlu.name
                            p.target_health = ornlu.health
                            p.target_defense = ornlu.defense
                            #Initializes AI target variables for Ornlu with statistics of the player
                            ornlu.target = p
                            ornlu.target_name = p.name
                            ornlu.target_health = p.health
                            ornlu.target_defense = p.defense
                            #Run the battle instance function with the player instance and ornlu instance with stats
                            battle.battle_instance(p, ornlu)
                        #Action for ChuKuNu
                        elif player_class == classes.ChuKuNu.class_name:
                            #Initialize target variables with statistics of Ornlu
                            p.target = ornlu
                            p.target_name = ornlu.name
                            p.target_health = ornlu.health
                            p.target_defense = ornlu.defense
                            #Initializes AI target variables for Ornlu with statistics of the player
                            ornlu.target = p
                            ornlu.target_name = p.name
                            ornlu.target_health = p.health
                            ornlu.target_defense = p.defense
                            #Run the battle instance function with the player instance and ornlu instance with stats
                            battle.battle_instance(p, ornlu)
                        #Action for SteppeSpearmen
                        elif player_class == classes.SteppeSpearmen.class_name:
                            #Initialize target variables with statistics of Ornlu
                            p.target = ornlu
                            p.target_name = ornlu.name
                            p.target_health = ornlu.health
                            p.target_defense = ornlu.defense
                            #Initializes AI target variables for Ornlu with statistics of the player
                            ornlu.target = p
                            ornlu.target_name = p.name
                            ornlu.target_health = p.health
                            ornlu.target_defense = p.defense
                            #Run the battle instance function with the player instance and ornlu instance with stats
                            battle.battle_instance(p, ornlu)
                        #Action for UarWarrior
                        elif player_class == classes.UarWarrior.class_name:
                            #Initialize target variables with statistics of Ornlu
                            p.target = ornlu
                            p.target_name = ornlu.name
                            p.target_health = ornlu.health
                            p.target_defense = ornlu.defense
                            #Initializes AI target variables for Ornlu with statistics of the player
                            ornlu.target = p
                            ornlu.target_name = p.name
                            ornlu.target_health = p.health
                            ornlu.target_defense = p.defense
                            #Run the battle instance function with the player instance and ornlu instance with stats
                            battle.battle_instance(p, ornlu)
                        #Action for UarWarrior
                        elif player_class == classes.KhansGuard.class_name:
                            #Initialize target variables with statistics of Ornlu
                            p.target = ornlu
                            p.target_name = ornlu.name
                            p.target_health = ornlu.health
                            p.target_defense = ornlu.defense
                            #Initializes AI target variables for Ornlu with statistics of the player
                            ornlu.target = p
                            ornlu.target_name = p.name
                            ornlu.target_health = p.health
                            ornlu.target_defense = p.defense
                            #Run the battle instance function with the player instance and ornlu instance with stats
                            battle.battle_instance(p, ornlu)
                        #Quest completion
                        if ornlu.is_alive is False:
                            print("You have gained experience from your fight. (+100 to Attack, Defense, and Health)")
                            khereid.complete()
                            continue

                    elif khereid_quest_accept == "N":
                        print("You decide to come back later. ")
                    else:
                        print(khereid_quest_accept + " is not a valid option. ")
                else:
                    print("You have already completed this quest. ")

            #Quest for Khamag
            elif vil == khamag:
                if khamag.quest_completed is not True:
                    #Output dialogue and ask the user if they want to enter the quest
                    print(vil.dialogue)
                    khamag_quest_accept = input("Do you want to take this quest? (Y/N) ").upper()
                    if khamag_quest_accept == "Y":
                        r = random.randrange(0, 21)
                        print("You find " + str(r) + " sheep. ")
                        if r >= 15:
                            print("You find " + str(r) + " sheep and deliver them to the khamag village center. ")
                            khamag.complete()
                            continue
                        else:
                            print("You failed to gather enough sheep and the khamags refuse to join you. ")

                    elif khamag_quest_accept == "N":
                        print("You decide to come back later. ")
                    else:
                        print(khamag_quest_accept + " is not a valid option. ")
                else:
                    print("You have already completed this quest. ")

        #Tell the user their input was invalid
        else:
            print(village_order(village_option) + " was not a valid option.")
