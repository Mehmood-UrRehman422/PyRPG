#    Character Stats    #

class Character:
    Stats = {
        "Strength" : 5,
        "Dexterity" : 5,
        "Intelligence" : 5,
        "Vitality" : 5
    }





class Fighter(Character):
    Stats = {
        "Strength" : 10, 
        "Dexterity" : 6,
        "Intelligence" : 4,
        "Vitality" : 8}

class Archer(Character):
    Stats = {
        "Strength" : 8, 
        "Dexterity" : 10,
        "Intelligence" : 4,
        "Vitality" : 6}

class Mage(Character):
    Stats = {
        "Strength" : 4, 
        "Dexterity" : 6,
        "Intelligence" : 10,
        "Vitality" : 8}


def InitializeCharacter():
    playerName = str(input("What is the name of your Character? \n"))
    return playerName

print(InitializeCharacter())