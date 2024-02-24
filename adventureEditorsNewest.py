"""
Michael Scott
Adventure editor
"""

import json

def main():
    
    game = ""
    keepGoing = True
    while keepGoing:
        userChoice = getMenuChoice()
        if userChoice == "0":
            keepGoing = False
        elif userChoice == "1":
            game = getDefaultGame()
        elif userChoice == "2":
            loadGame()
        elif userChoice == "3":
            saveGame(game)
        elif userChoice == "4":
            editNode(game)
        elif userChoice == "5":
            playGame(game)
        else:
            print("\n please select a valid number \n")
        
#"start": ["Description", "MenuA", "NodeA", "MenuA", "NodeB"],       
    
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

def playGame(game):
    keepGoing = True
    currentNode = "start"
    while keepGoing:
        if currentNode == "quit":
            keepGoing = False
        else:
            currentNode = playNode(game, currentNode)
    
def playNode(game, currentNode):
    print (game[currentNode][0])
    choice = input (f"1) {game[currentNode][1]}\n2) {game[currentNode][3]}\n")
    if choice == "1":
        currentNode = game[currentNode][2]
    elif choice == "2":
        currentNode = game[currentNode][4]
    else:
        print ("Invalid choice. Please type 1 or 2.")
    return currentNode
    
def getDefaultGame():
    defaultGame = {"start": ["Play again or quit", "Play again", "start", "Quit Game", "quit"],}
    print("Default game loaded")
    return defaultGame
    
def editNode(game):
    nodes = game.keys()
    print(nodes)
    editChoice = input("what node do you want to edit? if an existing node is not selected, a new one will be created.\n")
    if editChoice in nodes:
        newNode = game[editChoice]
    else:
        newNode = ["","","","",""]
    (desc, menuA, nodeA, menuB, nodeB) = newNode
    desc = editField(desc)
    menuA = editField(menuA)
    nodeA = editField(nodeA)
    menuB = editField(menuB)
    nodeB = editField(nodeB)
    newNode = (desc, menuA, nodeA, menuB, nodeB)
    game[editChoice] = newNode
    return game

def editField(node):
    edited = input(f"please insert new data for ({node})")
    return edited
    print("one f string, one return statement")
    
def saveGame(dictionaryGame):
    outFile = open("newAdventure.json", "w")
    json.dump(dictionaryGame, outFile, indent=2)
    print("saved game to newAdventure.json")
    outFile.close()
    
def loadGame():
    inFile = open("newAdventure.json", "r")
    loaded = json.load(inFile)
    inFile.close
    return loaded
    print("loaded Game")
    
main()

