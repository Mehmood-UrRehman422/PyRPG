#    Character Stats    #
class Character:
    #    Initialize Character Class    #
    def __init__(self, name, inventory, chosenClass, baseStats):
        #    Name is the Character Name    #
        self.name = name

        #    Inventory is an array of items that the player has    #
        self.inventory = inventory

        #    Chosen Class is the character class that the player has chosen    #
        self.chosenClass = chosenClass

        #    Max Health is the maximum amount of Hit Points (HP) possible for the character to have    #
        #    Current Health is the how many Hit Points (HP) the player currently has    #
        self.maxHealth = baseStats.get("Vitality") * 2
        self.health = self.maxHealth

        #    The Player has four stats that affect the overall efficiency/effect of the equipment and levelling    #
        self.strength = baseStats.get("Strength")
        self.dexterity = baseStats.get("Dexterity")
        self.intelligence = baseStats.get("Intelligence")
        self.vitality = baseStats.get("Vitality")

    #    Show Player stats    #
    def showStats(self):
        print("Name: " + self.name + "\n" + "Health: " + str(self.health))
        print("Maximum Health: " + str(self.maxHealth) + "\n")

        print("Strength:",str(self.strength))
        print("Dexterity:",str(self.dexterity))
        print("Intelligence:",str(self.intelligence))
        print("Vitality:",str(self.vitality))