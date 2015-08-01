#Classes made to be used as templates for battlefield and village instances
#Villages have a class variable called quest_completed to check if the player has completed that quest yet,
#an instance variable called village_name, and a method that completes the quest
#Villages also take a dialogue string as an instance variable


class Village():
    quest_completed = False

    def __init__(self, village_name, dialogue):
        self.village_name = village_name
        self.dialogue = dialogue

    def complete(self):
        self.quest_completed = True

#Dialogue for quest information
dialogue_n = """
You tell the Chief of the Naiman tribe that you wish to unite the tribes under your banner.
The Chief agrees, under one condition... you alliance with the Naimans to defeat the Tatars.
He offers you time to decide.
"""
dialogue_m = """
You tell the Chief of the Merkit tribe that you wish to unite the tribes under your banner.
The Chief agrees, but only if you pass the god, Tengri\'s, test. You are brought to the shaman,
Yesui, and he says that when you are ready, you can endure the god, Tengri\'s, test.
He offers you time to prepare.
"""
dialogue_t = """
You tell the Chief of the Tatar tribe that you wish to unite the tribes under your banner.
The Chief agrees, under one condition... you alliance with the Tatars to defeat the Naimans.
He offers you time to decide.
"""
dialogue_k = """
You tell the Chief of the Khereid tribe that you wish to unite the tribes under your banner.
The Chief agrees, under one condition... you defeat Ornlu the Wolf, a vile beast that has
defiled our sheep for weeks now. He tells you the location of Ornlu. He offers you time to prepare.
"""
dialogue_kg = """
You tell the Chief of the Khamag tribe that you wish to unite the tribes under you banner.
The Chief agrees, under one condition... he tells you that due to a harsh winter, the food
supply is low. He says that if you can bring them enough food to get through the rest of
the winter (15 sheep), they will gladly unite under your banner. He offers you time to think.
"""
#Functions to return quest information dialogues


def get_dialogue_n():
    return dialogue_n


def get_dialogue_m():
    return dialogue_m


def get_dialogue_t():
    return dialogue_t


def get_dialogue_k():
    return dialogue_k


def get_dialogue_kg():
    return dialogue_kg
