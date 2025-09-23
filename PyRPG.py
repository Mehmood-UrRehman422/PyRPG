#    Import Libraries    #
from enum import Enum

#    Character Classes    #
class CharacterClass(enum):
    Fighter = ("Fighter", {
        "Strength" : 10, 
        "Dexterity" : 5, 
        "Intelligence" : 0, 
        "Vitality" : 5
    })
    Archer = ("Archer", {
        "Strength" : 5,
        "Dexterity" : 10,
        "Intelligence" : 5,
        "Vitality" : 0
    })

#    Character Stats    #


class character:
    Stats = {
        "Strength" : 5,
        "Dexterity" : 5,
        "Intelligence" : 5,
        "Vitality" : 5
    }







def InitializeCharacter():
    Classes = list(CharacterClass)
    playerName = str(input("What is the name of your Character? \n"))
    playerClass = str(input("What class is your character [".join(Classes),"]"))