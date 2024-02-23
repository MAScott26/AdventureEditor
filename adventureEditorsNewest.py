# -*- coding: utf-8 -*-
"""
Michael Scott
Adventure editor



"""
def main():
    keepGoing = True
    while keepGoing:
        userChoice = getMenuChoice()
        if userChoice == "0":
            keepGoing = False
        elif userChoice == "1":
            getDefaultGame()
        elif userChoice == "2":
            loadGame()
        elif userChoice == "3":
            saveGame()
        elif userChoice == "4":
            editNode()
            editField()
        elif userChoice == "5":
            playGame()
        else:
            print("\n please select a valid number \n")
        
#"start": ["Play again or quit", "Play again", "start", "Quit Game", "quit"],       
    
    
    
def getMenuChoice():
    print("""please choose a number
          0) exit
          1) load default game
          2) load a game file
          3) save the current game
          4) edit or add a node
          5) play the current game""")
    menuChoice = input("what would you like to do? (0-5)\n")
    return menuChoice

def playGame():
    keepGoing = True
    currentNode = "start"
    game = getDefaultGame()
    while keepGoing:
        if currentNode == "quit":
            keepGoing = False
        else:
            currentNode = playNode(game, currentNode)
    
def playNode(game, currentNode):
    print("playNode function")
    
def getDefaultGame():
    game = {"start": ["Play again or quit", "Play again", "start", "Quit Game", "quit"],}
    print ("Default game loaded")
    return game

def editNode():
    print("edit node function")
    
def editField():
    print("edit field function")
    
def saveGame():
    print("save game function")
    
def loadGame():
    print("load game function")
    
    
main()

