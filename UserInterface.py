import tkinter as tk
import PyRPG

isFullscreen = False
FullscreenToggleable = True

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
    setFullscreenToggleable(True)
    EmptyMainMenu()

    rootFrame = tk.Frame(rootWin, width=400, height=320)
    rootFrame.pack(padx=20, pady=20)
    rootFrame.pack_propagate(False)

    Btn_Back = tk.Button(rootFrame, text="Back", command=GameLoadMenu)
    Btn_Back.pack(side=tk.TOP, anchor=tk.NW)

    Ent_PlayerName = tk.Entry()
    Ent_PlayerName.pack()

    #rootWin.state("zoomed")
    #FullscreenToggle()

#    Opens Load Save File Menu    #
def LoadGame():
    setFullscreenToggleable(True)
    print("Loading save slots...")
    EmptyMainMenu()
    rootWin.resizable(True, True)
    rootWin.state("zoomed")
    #FullscreenToggle()



OpenMainWindow()