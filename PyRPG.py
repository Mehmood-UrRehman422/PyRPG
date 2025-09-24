#    Import Libraries    #
import time

#    Character Stats    #

class Character:
    #    Name is the Character Name    #
    #    Health is the current Health Points of the Character    #
    #    Inventory is an Array of items    #
    def __init__(self, name, health, inventory, chosenClass, baseStats):
        self.name = name
        self.inventory = inventory
        self.chosenClass = chosenClass
        self.maxHealth = baseStats.get("Vitality") * 2
        self.health = self.maxHealth
        self.strength = baseStats.get("Strength")
        self.dexterity = baseStats.get("Dexterity")
        self.intelligence = baseStats.get("Intelligence")
        self.vitality = baseStats.get("Vitality")

    def showStats(self):
        print("Name: " + self.name + "\n" + "Health: " + str(self.health))
        print("Maximum Health: " + str(self.maxHealth) + "\n")

        print("Strength:",str(self.strength))
        print("Dexterity:",str(self.dexterity))
        print("Intelligence:",str(self.intelligence))
        print("Vitality:",str(self.vitality))




def InitializeGame():
    def PickCharacterClass():
        global characterClass
        characterClass = str(input("\nWhat Character Class do you want your character to be? [Fighter, Archer, Mage]\n"))
        match characterClass.Lower():
            case "fighter":
                Stats = {
                    "Strength" : 10, 
                    "Dexterity" : 6,
                    "Intelligence" : 4,
                    "Vitality" : 8}
                return Stats
            case "archer":
                Stats = {
                    "Strength" : 8, 
                    "Dexterity" : 10,
                    "Intelligence" : 4,
                    "Vitality" : 6}
                return Stats
            case "mage":
                Stats = {
                    "Strength" : 4, 
                    "Dexterity" : 6,
                    "Intelligence" : 10,
                    "Vitality" : 8}
                return Stats
            case _:
                print("This is not a valid Character Class, Please pick again")
                return PickCharacterClass()

    playerName = str(input("What is your character's name?\n------------------------------\n"))
    classStats = PickCharacterClass()
    global Player
    Player = Character(name=playerName, health=100, inventory=[], chosenClass=characterClass, baseStats=classStats)
    time.sleep(1)
    print("Good Luck, " + Player.name + "!" + "\n\n")
    global isPlaying
    isPlaying=True

InitializeGame()
Player.showStats()

while(isPlaying):
    action = str(input("\nSelect Action: Show Stats, Use Item, Exit\n"))
    print("Player Action: " + action)
    action = action.lower()
    match action:
        case "show stats" | "stats" | "stat":
            Player.showStats()
        case "use item":
            pass
        case "exit":
            isPlaying = False
        case _:
            print("This is not a valid action!")


'''

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

'''

