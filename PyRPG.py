#    Import Libraries    #
import time # For delays
import csv # For Data Tables
import json # For saving/Loading
import tkinter as tk # For Grapical User Interfaces


#    Character Stats    #

class Character:
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



#    Function to initialize the game    #
#    Includes Class selection and Name selection    #
def InitializeGame():

    #    Read and Save data table elements for later    #
    with open('CharacterClasses.csv', mode = 'r') as file: # With handles automatic opening and closing of files, 'R' is for Read Mode
        global CharacterClasses # Make Character Classes accessible throughout the script
        CharacterClasses = list(csv.reader(file)) # Save all the Character Classes from the CSV file into a list
    
    def PickCharacterClass():   #IMPORTANT: Could potentially move this either entirely into the Character Class or into a CSV File and read from a table
        global characterClass # Make characterClass accessible by whole script
        characterClass = str(input("\nWhat Character Class do you want your character to be? [Fighter, Archer, Mage]\n"))


        #########################if characterClass.Lower() != 
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
                    "Dexterity" : 8,
                    "Intelligence" : 10,
                    "Vitality" : 6}
                return Stats
            case _: # This happens if it is none of the cases above (similar to Else statement)
                print("This is not a valid Character Class, Please pick again")
                return PickCharacterClass()

    playerName = str(input("What is your character's name?\n------------------------------\n")) # Make the character pick a name for their player

    classStats = PickCharacterClass() # Make the player choose a Character Class

    global Player # Make the Player accessible by the whole script
    Player = Character(name=playerName, health=100, inventory=[], chosenClass=characterClass, baseStats=classStats) # Create a Player Object, that derives from the Character class

    time.sleep(1) # Gives the user a moment to process what is on screen

    print("Good Luck, " + Player.name + "!" + "\n\n")

    global isPlaying # Make an isPlaying Variable that is accessible by the whole script
    isPlaying=True # Set the isPlaying Boolean to True



InitializeGame() # Call the initializer function to gain appropriate data for the game
Player.showStats() # Show the player stats on screen


#    Game Loop    #
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
