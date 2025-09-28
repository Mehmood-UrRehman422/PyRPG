import tkinter as tk
import PyRPG

isFullscreen = False
FullscreenToggleable = True

PyRPG.InitDataTables()

#    Sets fullscreen to toggleable or not    #
def setFullscreenToggleable(state):
    global FullscreenToggleable
    FullscreenToggleable = state

#    Toggles Fullscreen On and Off (depending on FullscreenToggable Boolean)    #
def FullscreenToggle(event=None):
    global FullscreenToggleable
    global isFullscreen
    if FullscreenToggleable:
        print("Is Fullscreen Toggled")
        isFullscreen = not isFullscreen
        rootWin.attributes("-fullscreen", isFullscreen)

#    Opens main window that every widget will be attached to    #
def OpenMainWindow():
    global rootWin
    rootWin = tk.Tk()
    rootWin.title("PyRPG")
    rootWin.config(bg="dark slate grey")
    rootWin.resizable(True, True)
    rootWin.bind("<F11>", FullscreenToggle)
    GameLoadMenu()

#    Empties out Main Window for other widgets    #
def EmptyMainMenu():
    for each in rootWin.winfo_children():
        each.destroy()

#    Opens New Game/Load Game choice menu    #
def GameLoadMenu():
    EmptyMainMenu()
    rootWin.resizable(False, False)
    rootFrame = tk.Frame(rootWin, width=400, height=80)
    rootFrame.pack(padx=20, pady=20)
    rootFrame.pack_propagate(False)

    Btn_NewGame = tk.Button(rootFrame, text="New Game", command=NewGame)
    Btn_NewGame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    Btn_LoadGame = tk.Button(rootFrame, text="Load Game", command=LoadGame)
    Btn_LoadGame.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

    setFullscreenToggleable(False)

    rootWin.mainloop()


#    Opens New Character Chooser Menu    #
def NewGame():
    
    def NameChooser():
        EmptyMainMenu() # Clear the existing menu for new information to be displayed

        #    When player presses the "Next" button, this gets the string held inside Str_Name, which is saved in the Entry Box    #
        def SubmitName():
            print("Character name is", Str_Name.get()) # Debug Character Name
            classChooser(Name=Str_Name.get()) # Save CharacterName to what is held in Str_Name
        

        rootFrame = tk.Frame(rootWin, width=400, height=160) # Creates a frame
        rootFrame.pack(padx=20, pady=20) # Pack the frame
        rootFrame.pack_propagate(False) # Dont let the frame change size from Children

        Btn_Back = tk.Button(rootFrame, text="Back", command=GameLoadMenu) # Create a back button that takes the player back to the game load menu
        Btn_Back.pack(side=tk.TOP, anchor=tk.NW) # Attach it to the top and anchor it to the top left

        tk.Label(rootFrame, text="Enter Character Name:").pack()

        Str_Name = tk.StringVar()
        
        Ent_PlayerName = tk.Entry(rootFrame, textvariable=Str_Name)
        Ent_PlayerName.pack()

        Btn_Submit = tk.Button(rootFrame, text="Next", command=SubmitName)
        Btn_Submit.pack(side=tk.BOTTOM, padx=20, pady=20)

    def classChooser(Name):

        def SubmitClass():
            pass

        EmptyMainMenu()

        rootFrame = tk.Frame(rootWin, width=400, height=320)
        rootFrame.pack(padx=20, pady=20)
        rootFrame.pack_propagate(False)

        Btn_Back = tk.Button(rootFrame, text="Back", command=NameChooser)
        Btn_Back.pack(side=tk.TOP, anchor=tk.NW)

        tk.Label(rootFrame, text="Name: "+Name).pack(side=tk.TOP)

        PyRPG.CharacterClasses
        availableClasses = []
        for row in PyRPG.CharacterClasses[1:]:
            availableClasses.append(row[0])

        tk.OptionMenu(rootFrame, tk.StringVar(value=availableClasses[0]), *availableClasses).pack()


    #rootWin.state("zoomed")
    #FullscreenToggle()


    setFullscreenToggleable(False) # Set FullscreenToggleable to True, Lets user toggle Fullscreen
    NameChooser()

#    Opens Load Save File Menu    #
def LoadGame():
    setFullscreenToggleable(True)
    print("Loading save slots...")
    EmptyMainMenu()
    rootWin.resizable(True, True)
    rootWin.state("zoomed")
    #FullscreenToggle()



OpenMainWindow()