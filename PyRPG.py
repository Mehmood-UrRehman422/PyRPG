#    Import Libraries    #
import time # For delays
import csv # For Data Tables
import json # For saving/Loading
import tkinter as tk # For Grapical User Interfaces
from character import Character
#from tkinter import *

rootWin = tk.Tk()
rootWin.title("PyRPG")
rootWin.config(bg="dark slate grey")
rootWin.resizable(False, False)

rootFrame = tk.Frame(rootWin, width=400, height=80)
rootFrame.pack(padx=20, pady=20)
rootFrame.pack_propagate(False)

Btn_NewGame = tk.Button(rootFrame, text="New Game")
Btn_NewGame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

Btn_LoadGame = tk.Button(rootFrame, text="Load Game")
Btn_LoadGame.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)


rootWin.mainloop()



#    Function to initialize the game    #
def InitializeGame():

    #    Read and Save data table elements for later    #
    with open('CharacterClasses.csv', mode = 'r') as file: # With handles automatic opening and closing of files, 'R' is for Read Mode
        global CharacterClasses # Make Character Classes accessible throughout the script
        CharacterClasses = list(csv.reader(file)) # Save all the Character Classes from the CSV file into a list
    
    playerName = str(input("What is your character's name?\n------------------------------\n")).capitalize() # Make the character pick a name for their player
    
    def PickCharacterClass():   #IMPORTANT: Could potentially move this either entirely into the Character Class or into a CSV File and read from a table
        
        availableClasses = []
        for row in CharacterClasses[1:]:
            availableClasses.append(row[0])
        
        global characterClass # Make characterClass accessible by whole script
        characterClass = str(input("\nWhat Character Class do you want your character to be? [" + ", ".join(availableClasses) + "]\n")) # Join up the classes into a string and ask the player what they want to be
        if characterClass.capitalize() in availableClasses: # convert both to lowercase and find if user chosen class exists in availableClasses
            print("Class found")
            classStats = availableClasses.index(characterClass.capitalize())
            classStats = CharacterClasses[classStats+1]
            print(classStats)
            classStats = {"Strength":int(classStats[1]), "Dexterity":int(classStats[2]), "Intelligence":int(classStats[3]), "Vitality":int(classStats[4])}
            global Player # Make the Player accessible by the whole script
            Player = Character(name=playerName, inventory=[], chosenClass=characterClass, baseStats=classStats) # Create a Player Object, that derives from the Character class
        else:
            print("Class not found")
    
    PickCharacterClass()
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
