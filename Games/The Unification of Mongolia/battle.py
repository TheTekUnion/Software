import classes
import time
import sys

#Battle function that takes the player and another opponent as well as their statistics as parameters
#This function is used for resolving battles by using the players selected skills as well as the AI's selected skills


def battle_instance(player, enemy):
    #Action for Horse Archer Class
    if isinstance(player, classes.HorseArcher):
        while True:
            #Decision Making
            while True:
                #Player Attack Phase
                #Attack Phase
                skill = input("Enter attack ").lower()
                #Skills list index 0 == mounted quick shot
                if skill == player.skills[0]:
                    #If user types mounted quick shot, then that method is executed.
                    print(player.target_name + "\'s health: ")
                    print(player.mounted_quick_shot())
                    break
                #Skills list index 1 == mounted flaming shot
                elif skill == player.skills[1]:
                    #If user types mounted flaming shot, then that method is executed.
                    print(player.target_name + "\'s health: ")
                    print(player.mounted_flaming_shot())
                    break
                #Skills list index 2 == mounted heart seeker
                elif skill == player.skills[2]:
                    #If user types mounted mounted heart seeker, then that method is executed.
                    print(player.target_name + "\'s health: ")
                    print(player.mounted_heart_seeker())
                    break
                else:
                    print(skill + " was not a valid option. ")
                    continue
            #Exit if Ornlu is defeated
            if player.target_health <= 0:
                break
            #AI Attack Phase
            print("Your health after " + enemy.name + "\'s attack: ")
            print(enemy.attack_skill())
            #Exit if the player is defeated
            if enemy.target_health <= 0:
                break
        #Defeat the player's target
        if player.target_health <= 0:
            player.target.defeat()
            print("Congratulations, you have defeated " + enemy.name + ". ")
        else:
            for i in range(1):
                print("Game over!")
                time.sleep(3)
                if i == 0:
                    sys.exit()
            
    #Action for Steppe Lancer Class
    if isinstance(player, classes.SteppeLancer):
        while True:
            #Decision Making
            while True:
                #Player Attack Phase
                #Attack Phase
                skill = input("Enter attack ").lower()
                #Skills list index 0 == happy mounted javelin day
                if skill == player.skills[0]:
                    #If user types mounted quick shot, then that method is executed.
                    print(player.target_name + "\'s health: ")
                    print(player.happy_mounted_javelin_day())
                    break
                #Skills list index 1 == mounted mace attack
                elif skill == player.skills[1]:
                    #If user types mounted flaming shot, then that method is executed.
                    print(player.target_name + "\'s health: ")
                    print(player.mounted_mace_attack())
                    break
                #Skills list index 2 == mounted lance attack
                elif skill == player.skills[2]:
                    #If user types mounted flaming shot, then that method is executed.
                    print(player.target_name + "\'s health: ")
                    print(player.mounted_lance_attack())
                    break
                else:
                    print(skill + " was not a valid option. ")
                    continue
            #Exit if Ornlu is defeated
            if player.target_health <= 0:
                break
            #AI Attack Phase
            print("Your health after " + enemy.name + "\'s attack: ")
            print(enemy.attack_skill())
            #Exit if the player is defeated
            if enemy.target_health <= 0:
                break
        #Defeat the player's target
        if player.target_health <= 0:
            player.target.defeat()
            print("Congratulations, you have defeated " + enemy.name + ". ")
        else:
            for i in range(1):
                print("Game over!")
                time.sleep(3)
                if i == 0:
                    sys.exit()

    #Action for Hunter Class
    if isinstance(player, classes.Hunter):
        while True:
            #Decision Making
            while True:
                #Player Attack Phase
                #Attack Phase
                skill = input("Enter attack ").lower()
                #Skills list index 0 == quick shot
                if skill == player.skills[0]:
                    #If user types quick shot, then that method is executed.
                    print(player.target_name + "\'s health: ")
                    print(player.quick_shot())
                    break
                #Skills list index 1 == flaming shot
                elif skill == player.skills[1]:
                    #If user types flaming shot, then that method is executed.
                    print(player.target_name + "\'s health: ")
                    print(player.flaming_shot())
                    break
                #Skills list index 2 == mounted flaming shot
                elif skill == player.skills[2]:
                    #If user types mounted flaming shot, then that method is executed.
                    print(player.target_name + "\'s health: ")
                    print(player.heart_seeker())
                    break
                else:
                    print(skill + " was not a valid option. ")
                    continue
            #Exit if Ornlu is defeated
            if player.target_health <= 0:
                break
            #AI Attack Phase
            print("Your health after " + enemy.name + "\'s attack: ")
            print(enemy.attack_skill())
            #Exit if the player is defeated
            if enemy.target_health <= 0:
                break
        #Defeat the player's target
        if player.target_health <= 0:
            player.target.defeat()
            print("Congratulations, you have defeated " + enemy.name + ". ")
        else:
            for i in range(1):
                print("Game over!")
                time.sleep(3)
                if i == 0:
                    sys.exit()

    #Action for ChuKuNu Class
    if isinstance(player, classes.ChuKuNu):
        while True:
            #Decision Making
            while True:
                #Player Attack Phase
                #Attack Phase
                skill = input("Enter attack ").lower()
                #Skills list index 0 == mounted quick shot
                if skill == player.skills[0]:
                    #If user types mounted quick shot, then that method is executed.
                    print(player.target_name + "\'s health: ")
                    print(player.dagger_stab())
                    break
                #Skills list index 1 == mounted flaming shot
                elif skill == player.skills[1]:
                    #If user types mounted flaming shot, then that method is executed.
                    print(player.target_name + "\'s health: ")
                    print(player.crossbow_shot())
                    break
                #Skills list index 2 == mounted flaming shot
                elif skill == player.skills[2]:
                    #If user types mounted flaming shot, then that method is executed.
                    print(player.target_name + "\'s health: ")
                    print(player.crossbow_headshot())
                    break
                else:
                    print(skill + " was not a valid option. ")
                    continue
            #Exit if Ornlu is defeated
            if player.target_health <= 0:
                break
            #AI Attack Phase
            print("Your health after " + enemy.name + "\'s attack: ")
            print(enemy.attack_skill())
            #Exit if the player is defeated
            if enemy.target_health <= 0:
                break
        #Defeat the player's target
        if player.target_health <= 0:
            player.target.defeat()
            print("Congratulations, you have defeated " + enemy.name + ". ")
        else:
            for i in range(1):
                print("Game over!")
                time.sleep(3)
                if i == 0:
                    sys.exit()

    #Action for Steppe Spearmen Class
    if isinstance(player, classes.SteppeSpearmen):
        while True:
            #Decision Making
            while True:
                #Player Attack Phase
                #Attack Phase
                skill = input("Enter attack ").lower()
                #Skills list index 0 == mounted quick shot
                if skill == player.skills[0]:
                    #If user types mounted quick shot, then that method is executed.
                    print(player.target_name + "\'s health: ")
                    print(player.happy_javelin_day())
                    break
                #Skills list index 1 == mounted flaming shot
                elif skill == player.skills[1]:
                    #If user types mounted flaming shot, then that method is executed.
                    print(player.target_name + "\'s health: ")
                    print(player.spear_stab())
                    break
                #Skills list index 2 == mounted flaming shot
                elif skill == player.skills[2]:
                    #If user types mounted flaming shot, then that method is executed.
                    print(player.target_name + "\'s health: ")
                    print(player.spear_head_stab())
                    break
                else:
                    print(skill + " was not a valid option. ")
                    continue
            #Exit if Ornlu is defeated
            if player.target_health <= 0:
                break
            #AI Attack Phase
            print("Your health after " + enemy.name + "\'s attack: ")
            print(enemy.attack_skill())
            #Exit if the player is defeated
            if enemy.target_health <= 0:
                break
        #Defeat the player's target
        if player.target_health <= 0:
            player.target.defeat()
            print("Congratulations, you have defeated " + enemy.name + ". ")
        else:
            for i in range(1):
                print("Game over!")
                time.sleep(3)
                if i == 0:
                    sys.exit()

    #Action for Uar Warrior Class
    if isinstance(player, classes.UarWarrior):
        while True:
            #Decision Making
            while True:
                #Player Attack Phase
                #Attack Phase
                skill = input("Enter attack ").lower()
                #Skills list index 0 == mounted quick shot
                if skill == player.skills[0]:
                    #If user types mounted quick shot, then that method is executed.
                    print(player.target_name + "\'s health: ")
                    print(player.happy_javelin_day())
                    break
                #Skills list index 1 == mounted flaming shot
                elif skill == player.skills[1]:
                    #If user types mounted flaming shot, then that method is executed.
                    print(player.target_name + "\'s health: ")
                    print(player.sword_slash())
                    break
                #Skills list index 2 == mounted flaming shot
                elif skill == player.skills[2]:
                    #If user types mounted flaming shot, then that method is executed.
                    print(player.target_name + "\'s health: ")
                    print(player.decapitation())
                    break
                else:
                    print(skill + " was not a valid option. ")
                    continue
            #Exit if Ornlu is defeated
            if player.target_health <= 0:
                break
            #AI Attack Phase
            print("Your health after " + enemy.name + "\'s attack: ")
            print(enemy.attack_skill())
            #Exit if the player is defeated
            if enemy.target_health <= 0:
                break
        #Defeat the player's target
        if player.target_health <= 0:
            player.target.defeat()
            print("Congratulations, you have defeated " + enemy.name + ". ")
        else:
            for i in range(1):
                print("Game over!")
                time.sleep(3)
                if i == 0:
                    sys.exit()

    #Action for Khan's Guard Class
    if isinstance(player, classes.KhansGuard):
        while True:
            #Decision Making
            while True:
                #Player Attack Phase
                #Attack Phase
                skill = input("Enter attack ").lower()
                #Skills list index 0 == mounted quick shot
                if skill == player.skills[0]:
                    #If user types mounted quick shot, then that method is executed.
                    print(player.target_name + "\'s health: ")
                    print(player.happy_javelin_day())
                    break
                #Skills list index 1 == mounted flaming shot
                elif skill == player.skills[1]:
                    #If user types mounted flaming shot, then that method is executed.
                    print(player.target_name + "\'s health: ")
                    print(player.shield_bash())
                    break
                #Skills list index 2 == mounted flaming shot
                elif skill == player.skills[2]:
                    #If user types mounted flaming shot, then that method is executed.
                    print(player.target_name + "\'s health: ")
                    print(player.loyalty_of_the_tenth())
                    break
                else:
                    print(skill + " was not a valid option. ")
                    continue
            #Exit if Ornlu is defeated
            if player.target_health <= 0:
                break
            #AI Attack Phase
            print("Your health after " + enemy.name + "\'s attack: ")
            print(enemy.attack_skill())
            #Exit if the player is defeated
            if enemy.target_health <= 0:
                break
        #Defeat the player's target
        if player.target_health <= 0:
            player.target.defeat()
            print("Congratulations, you have defeated " + enemy.name + ". ")
        else:
            for i in range(1):
                print("Game over!")
                time.sleep(3)
                if i == 0:
                    sys.exit()