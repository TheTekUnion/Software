"""
Playable Classes

Horse Archer
Steppe Lancer
Hunter
ChuKuNu
Steppe Spearmen
Uar Warrior
Khan's Guard
"""

import random
import characters

#The following notes should be added to the class definitions
#Explicit is better than implicit (Classes use a boolean literals instead of quality comparisons in conditionals)
#(Follows PEP Guidelines)
#function in the battle module


class HorseArcher(characters.Character):
    #Overrides super class variables
    #Utilizes inherited instance variables
    health = 100
    attack = 200
    defense = 50
    mounted = True
    class_name = "horse archer"

    #Target opponent variables for multiple methods used for skills in combat
    target = None
    target_name = ""
    target_health = 0
    target_defense = 0

    #Skill list created in order call a selected skill with a specific string
    skills = ["mounted quick shot", "mounted flaming shot", "mounted heart seeker"]

    def __init__(self, name, apprenticeship):
        self.name = name
        self.apprenticeship = apprenticeship

    #Quick shot skill method
    def mounted_quick_shot(self):
        base_damage = 70
        chance = .9
        beast_bonus = False
        #Generate random float
        r = random.random()

        #If the player class is mounted, then it receives an attack boost for that skill as well as an accuracy penalty.
        if self.mounted:
            base_damage *= 1.25
            chance *= .8

        #Applies a bonus against the target if the target is a beast AND if the skill has a beast bonus
        if beast_bonus and isinstance(self.target, characters.Beast):
            base_damage *= 2

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250

        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)
        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health
        else:
            return "You failed to induct " + self.skills[0] + "."

    #Flaming shot skill method
    def mounted_flaming_shot(self):
        base_damage = 90
        chance = .75
        beast_bonus = True

        #Generate random float
        r = random.random()

        #If the player class is mounted, then it receives an attack boost for that skill as well as an accuracy penalty.
        if self.mounted:
            base_damage *= 1.25
            chance *= .8

        #Applies a bonus against the target if the target is a beast AND if the skill has a beast bonus
        if beast_bonus and isinstance(self.target, characters.Beast):
            base_damage *= 2

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250
        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)

        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health

        else:
            return "You failed to induct " + self.skills[1] + "."

    #Mounted heart seeker skill method
    def mounted_heart_seeker(self):
        base_damage = 350
        chance = .2
        beast_bonus = False

        #Generate random float
        r = random.random()

        #If the player class is mounted, then it receives an attack boost for that skill as well as an accuracy penalty.
        if self.mounted:
            base_damage *= 1.25
            chance *= .8

        #Applies a bonus against the target if the target is a beast AND if the skill has a beast bonus
        if beast_bonus and isinstance(self.target, characters.Beast):
            base_damage *= 2

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250
        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)

        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health
        else:
            return "You failed to induct " + self.skills[2] + "."


class SteppeLancer(characters.Character):
    #Overrides super class variables
    #Utilizes inherited instance variables
    health = 100
    attack = 130
    defense = 120
    mounted = True
    class_name = "steppe lancer"

    #Target opponent variables for multiple methods used for skills in combat
    target = None
    target_name = ""
    target_health = 0
    target_defense = 0

    #Skill list created in order call a selected skill with a specific string
    skills = ["happy mounted javelin day", "mounted mace attack", "mounted lance attack"]

    def __init__(self, name, apprenticeship):
        self.name = name
        self.apprenticeship = apprenticeship

    #Quick shot skill method
    def happy_mounted_javelin_day(self):
        base_damage = 80
        chance = .9
        beast_bonus = False
        #Generate random float
        r = random.random()

        #If the player class is mounted, then it receives an attack boost for that skill as well as an accuracy penalty.
        if self.mounted:
            base_damage *= 1.25
            chance *= .8

        #Applies a bonus against the target if the target is a beast AND if the skill has a beast bonus
        if beast_bonus and isinstance(self.target, characters.Beast):
            base_damage *= 2

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250

        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)
        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health
        else:
            return "You failed to induct " + self.skills[0] + "."

    #Flaming shot skill method
    def mounted_mace_attack(self):
        base_damage = 100
        chance = .75
        beast_bonus = False

        #Generate random float
        r = random.random()

        #If the player class is mounted, then it receives an attack boost for that skill as well as an accuracy penalty.
        if self.mounted:
            base_damage *= 1.25
            chance *= .8

        #Applies a bonus against the target if the target is a beast AND if the skill has a beast bonus
        if beast_bonus and isinstance(self.target, characters.Beast):
            base_damage *= 2

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250
        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)

        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health

        else:
            return "You failed to induct " + self.skills[1] + "."

    #Mounted heart seeker skill method
    def mounted_lance_attack(self):
        base_damage = 350
        chance = .2
        beast_bonus = True

        #Generate random float
        r = random.random()

        #If the player class is mounted, then it receives an attack boost for that skill as well as an accuracy penalty.
        if self.mounted:
            base_damage *= 1.25
            chance *= .8

        #Applies a bonus against the target if the target is a beast AND if the skill has a beast bonus
        if beast_bonus and isinstance(self.target, characters.Beast):
            base_damage *= 2

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250
        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)

        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health
        else:
            return "You failed to induct " + self.skills[2] + "."


class Hunter(characters.Character):
    #Overrides super class variables
    #Utilizes inherited instance variables
    health = 100
    attack = 190
    defense = 60
    mounted = False
    class_name = "hunter"

    #Target opponent variables for multiple methods used for skills in combat
    target = None
    target_name = ""
    target_health = 0
    target_defense = 0

    #Skill list created in order call a selected skill with a specific string
    skills = ["quick shot", "flaming shot", "heart seeker"]

    def __init__(self, name, apprenticeship):
        self.name = name
        self.apprenticeship = apprenticeship

    #Quick shot skill method
    def quick_shot(self):
        base_damage = 70
        chance = .9
        beast_bonus = False
        #Generate random float
        r = random.random()

        #If the player class is mounted, then it receives an attack boost for that skill as well as an accuracy penalty.
        if self.mounted:
            base_damage *= 1.25
            chance *= .8

        #Applies a bonus against the target if the target is a beast AND if the skill has a beast bonus
        if beast_bonus and isinstance(self.target, characters.Beast):
            base_damage *= 2

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250

        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)
        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health
        else:
            return "You failed to induct " + self.skills[0] + "."

    #Flaming shot skill method
    def flaming_shot(self):
        base_damage = 90
        chance = .75
        beast_bonus = True

        #Generate random float
        r = random.random()

        #If the player class is mounted, then it receives an attack boost for that skill as well as an accuracy penalty.
        if self.mounted:
            base_damage *= 1.25
            chance *= .8

        #Applies a bonus against the target if the target is a beast AND if the skill has a beast bonus
        if beast_bonus and isinstance(self.target, characters.Beast):
            base_damage *= 2

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250
        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)

        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health

        else:
            return "You failed to induct " + self.skills[1] + "."

    #Mounted heart seeker skill method
    def heart_seeker(self):
        base_damage = 350
        chance = .2
        beast_bonus = False

        #Generate random float
        r = random.random()

        #If the player class is mounted, then it receives an attack boost for that skill as well as an accuracy penalty.
        if self.mounted:
            base_damage *= 1.25
            chance *= .8

        #Applies a bonus against the target if the target is a beast AND if the skill has a beast bonus
        if beast_bonus and isinstance(self.target, characters.Beast):
            base_damage *= 2

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250
        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)

        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health
        else:
            return "You failed to induct " + self.skills[2] + "."


class ChuKuNu(characters.Character):
    #Overrides super class variables
    #Utilizes inherited instance variables
    health = 100
    attack = 180
    defense = 70
    mounted = False
    class_name = "chukunu"

    #Target opponent variables for multiple methods used for skills in combat
    target = None
    target_name = ""
    target_health = 0
    target_defense = 0

    #Skill list created in order call a selected skill with a specific string
    skills = ["dagger stab", "crossbow shot", "crossbow headshot"]

    def __init__(self, name, apprenticeship):
        self.name = name
        self.apprenticeship = apprenticeship

    #Quick shot skill method
    def dagger_stab(self):
        base_damage = 60
        chance = .9
        beast_bonus = False
        #Generate random float
        r = random.random()

        #If the player class is mounted, then it receives an attack boost for that skill as well as an accuracy penalty.
        if self.mounted:
            base_damage *= 1.25
            chance *= .8

        #Applies a bonus against the target if the target is a beast AND if the skill has a beast bonus
        if beast_bonus and isinstance(self.target, characters.Beast):
            base_damage *= 2

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250

        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)
        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health
        else:
            return "You failed to induct " + self.skills[0] + "."

    #Flaming shot skill method
    def crossbow_shot(self):
        base_damage = 125
        chance = .75
        beast_bonus = True

        #Generate random float
        r = random.random()

        #If the player class is mounted, then it receives an attack boost for that skill as well as an accuracy penalty.
        if self.mounted:
            base_damage *= 1.25
            chance *= .8

        #Applies a bonus against the target if the target is a beast AND if the skill has a beast bonus
        if beast_bonus and isinstance(self.target, characters.Beast):
            base_damage *= 2

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250
        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)

        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health

        else:
            return "You failed to induct " + self.skills[1] + "."

    #Mounted heart seeker skill method
    def crossbow_headshot(self):
        base_damage = 350
        chance = .2
        beast_bonus = True

        #Generate random float
        r = random.random()

        #If the player class is mounted, then it receives an attack boost for that skill as well as an accuracy penalty.
        if self.mounted:
            base_damage *= 1.25
            chance *= .8

        #Applies a bonus against the target if the target is a beast AND if the skill has a beast bonus
        if beast_bonus and isinstance(self.target, characters.Beast):
            base_damage *= 2

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250
        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)

        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health
        else:
            return "You failed to induct " + self.skills[2] + "."


class SteppeSpearmen(characters.Character):
    #Overrides super class variables
    #Utilizes inherited instance variables
    health = 100
    attack = 180
    defense = 20
    mounted = False
    class_name = "steppe spearmen"

    #Target opponent variables for multiple methods used for skills in combat
    target = None
    target_name = ""
    target_health = 0
    target_defense = 0

    #Skill list created in order call a selected skill with a specific string
    skills = ["happy javelin day", "spear stab", "spear head stab"]

    def __init__(self, name, apprenticeship):
        self.name = name
        self.apprenticeship = apprenticeship

    #Quick shot skill method
    def happy_javelin_day(self):
        base_damage = 70
        chance = .9
        beast_bonus = False
        #Generate random float
        r = random.random()

        #If the player class is mounted, then it receives an attack boost for that skill as well as an accuracy penalty.
        if self.mounted:
            base_damage *= 1.25
            chance *= .8

        #Applies a bonus against the target if the target is a beast AND if the skill has a beast bonus
        if beast_bonus and isinstance(self.target, characters.Beast):
            base_damage *= 2

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250

        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)
        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health
        else:
            return "You failed to induct " + self.skills[0] + "."

    #Flaming shot skill method
    def spear_stab(self):
        base_damage = 90
        chance = .75
        beast_bonus = True

        #Generate random float
        r = random.random()

        #If the player class is mounted, then it receives an attack boost for that skill as well as an accuracy penalty.
        if self.mounted:
            base_damage *= 1.25
            chance *= .8

        #Applies a bonus against the target if the target is a beast AND if the skill has a beast bonus
        if beast_bonus and isinstance(self.target, characters.Beast):
            base_damage *= 2

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250
        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)

        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health

        else:
            return "You failed to induct " + self.skills[1] + "."

    #Mounted heart seeker skill method
    def spear_head_stab(self):
        base_damage = 350
        chance = .2
        beast_bonus = False

        #Generate random float
        r = random.random()

        #If the player class is mounted, then it receives an attack boost for that skill as well as an accuracy penalty.
        if self.mounted:
            base_damage *= 1.25
            chance *= .8

        #Applies a bonus against the target if the target is a beast AND if the skill has a beast bonus
        if beast_bonus and isinstance(self.target, characters.Beast):
            base_damage *= 2

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250
        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)

        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health
        else:
            return "You failed to induct " + SteppeSpearmen.skills[2] + "."


class UarWarrior(characters.Character):
    #Overrides super class variables
    #Utilizes inherited instance variables
    health = 100
    attack = 250
    defense = 0
    mounted = False
    class_name = "uar warrior"

    #Target opponent variables for multiple methods used for skills in combat
    target = None
    target_name = ""
    target_health = 0
    target_defense = 0

    #Skill list created in order call a selected skill with a specific string
    skills = ["happy javelin day", "sword slash", "decapitation"]

    def __init__(self, name, apprenticeship):
        self.name = name
        self.apprenticeship = apprenticeship

    #Quick shot skill method
    def happy_javelin_day(self):
        base_damage = 70
        chance = .9
        beast_bonus = False
        #Generate random float
        r = random.random()

        #If the player class is mounted, then it receives an attack boost for that skill as well as an accuracy penalty.
        if self.mounted:
            base_damage *= 1.25
            chance *= .8

        #Applies a bonus against the target if the target is a beast AND if the skill has a beast bonus
        if beast_bonus and isinstance(self.target, characters.Beast):
            base_damage *= 2

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250

        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)
        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health
        else:
            return "You failed to induct " + self.skills[0] + "."

    #Flaming shot skill method
    def sword_slash(self):
        base_damage = 120
        chance = .75
        beast_bonus = False

        #Generate random float
        r = random.random()

        #If the player class is mounted, then it receives an attack boost for that skill as well as an accuracy penalty.
        if self.mounted:
            base_damage *= 1.25
            chance *= .8

        #Applies a bonus against the target if the target is a beast AND if the skill has a beast bonus
        if beast_bonus and isinstance(self.target, characters.Beast):
            base_damage *= 2

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250
        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)

        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health

        else:
            return "You failed to induct " + self.skills[1] + "."

    #Mounted heart seeker skill method
    def decapitation(self):
        base_damage = 350
        chance = .2
        beast_bonus = True

        #Generate random float
        r = random.random()

        #If the player class is mounted, then it receives an attack boost for that skill as well as an accuracy penalty.
        if self.mounted:
            base_damage *= 1.25
            chance *= .8

        #Applies a bonus against the target if the target is a beast AND if the skill has a beast bonus
        if beast_bonus and isinstance(self.target, characters.Beast):
            base_damage *= 2

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250
        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)

        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health
        else:
            return "You failed to induct " + self.skills[2] + "."


class KhansGuard(characters.Character):
    #Overrides super class variables
    #Utilizes inherited instance variables
    health = 100
    attack = 180
    defense = 20
    mounted = False
    class_name = "khan\'s guard"

    #Target opponent variables for multiple methods used for skills in combat
    target = None
    target_name = ""
    target_health = 0
    target_defense = 0

    #Skill list created in order call a selected skill with a specific string
    skills = ["happy javelin day", "shield bash", "loyalty of the tenth"]

    def __init__(self, name, apprenticeship):
        self.name = name
        self.apprenticeship = apprenticeship

    #Quick shot skill method
    def happy_javelin_day(self):
        base_damage = 70
        chance = .9
        beast_bonus = False
        #Generate random float
        r = random.random()

        #If the player class is mounted, then it receives an attack boost for that skill as well as an accuracy penalty.
        if self.mounted:
            base_damage *= 1.25
            chance *= .8

        #Applies a bonus against the target if the target is a beast AND if the skill has a beast bonus
        if beast_bonus and isinstance(self.target, characters.Beast):
            base_damage *= 2

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250

        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)
        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health
        else:
            return "You failed to induct " + self.skills[0] + "."

    #Shield Bash skill method
    def shield_bash(self):
        base_damage = 120
        chance = .75
        beast_bonus = True

        #Generate random float
        r = random.random()

        #If the player class is mounted, then it receives an attack boost for that skill as well as an accuracy penalty.
        if self.mounted:
            base_damage *= 1.25
            chance *= .8

        #Applies a bonus against the target if the target is a beast AND if the skill has a beast bonus
        if beast_bonus and isinstance(self.target, characters.Beast):
            base_damage *= 2

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250
        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)

        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health

        else:
            return "You failed to induct " + self.skills[1] + "."

    #Loyalty of the Tenth skill method
    def loyalty_of_the_tenth(self):
        base_damage = 350
        chance = .2
        beast_bonus = False

        #Generate random float
        r = random.random()

        #If the player class is mounted, then it receives an attack boost for that skill as well as an accuracy penalty.
        if self.mounted:
            base_damage *= 1.25
            chance *= .8

        #Applies a bonus against the target if the target is a beast AND if the skill has a beast bonus
        if beast_bonus and isinstance(self.target, characters.Beast):
            base_damage *= 2

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250
        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)

        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health
        else:
            return "You failed to induct " + self.skills[2] + "."