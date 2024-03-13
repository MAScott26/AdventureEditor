# AdventureEditor
made by Michael Scott
for CS120 Andy Harris.

import Json


define main
  game gets empty data
  while loop
  userchoice gets getMenuChoice
if/elif for # 1-5
else user is told to select a vailid number.

define getMenuChoice
  creates a menu
  please choose a number
          0) exit
          1) load default game
          2) load a game file
          3) save the current game
          4) edit or add a node
          5) play the current game
menuChoice gets  input 0-5
return menuChoice

define playGame(game)
keepGoing gets True
sets current node to start
while loop
if current node is quit, leave loop
currentnode gets result of playNode

define playNode(game,currentNode)
print current node and options,
if choice is 1, go to node 2
if choice is 2, go to node 4
else tell user to choose a  valid number


define getDefaultGame
defaultGame = "start": ["Play again or quit", "Play again", "start", "Quit Game", "quit"],
tell user default game is loaded

define editNode(game)
nodes get game.keys()
print nodes
ask user what node they want to edit
if its an existing node, edits their choice
else
newNode is filled with blank data
each section of the node gets data from user.
return game

define editField(node)
variable gets data thats being changed
return variable

define saveGame(dictionaryGame)
opens newAdventure for writing
dump file
writes edited data to newAdventure file
tell user the game is saved
close file

define loadGame
inFile opens newAdventure.json
loaded gets load newAdventure.json
close file
tell user game is loaded
returnloaded

main()
