"""
Characters used In Combat

Player
Kuchlag
Ornlu
"""


import random


class Character():
    #Health ranges from 0 - 600
    health = 0
    #Attack ranges from 0 - 250
    attack = 0
    #Defense ranges from 0 - 249
    defense = 0
    is_alive = True
    mounted = False
    beast = False
    name = ""

    #Defeat method
    def defeat(self):
        self.is_alive = False


class Kuchlag(Character):
    health = 1000
    attack = 50
    defense = 200
    name = "Kuchlag"

    #Target opponent variables for multiple methods used for skills in combat
    target = None
    target_name = ""
    target_health = 0
    target_defense = 0

    def attack_skill(self):
        base_damage = 50
        chance = .8
        beast_bonus = False
        #Generate random float
        r = random.random()

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250
        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)
        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health
        else:
            return "You dodged Kuchlag\'s attack. "


class Beast(Character):
    beast = True


class Ornlu(Beast):
    health = 300
    attack = 150
    defense = 100
    name = "Ornlu"

    #Target opponent variables for multiple methods used for skills in combat
    target = None
    target_name = ""
    target_health = 0
    target_defense = 0

    def attack_skill(self):
        base_damage = 50
        chance = .8
        beast_bonus = False
        #Generate random float
        r = random.random()

        #Total damage calculated by multiplying the base by the attack rating of the class then
        #multiplying the defence rating subtracted from 250
        total_damage = (base_damage * (self.attack / 100)) * ((250 - self.target_defense) / 100)
        #Checks to see if attack is successful
        if r < chance:
            #take total damage away from target's health
            self.target_health -= total_damage
            return self.target_health
        else:
            return "You dodged Ornlu\'s attack. "