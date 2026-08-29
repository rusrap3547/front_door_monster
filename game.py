import dictionaries.functions as func
import dictionaries.rooms as rooms
import dictionaries.monsters as monster

from dictionaries.monsters import Vampire

func.showInstructions()

inventory = []
currentRoom = monster[Vampire]["startingRoom"]

while True:
    print(f"You are currently in the {currentRoom}.")
    move = input(">")
    move = move.split(" ",1)
    if move[0] == "get":
        if move[1] == rooms[currentRoom]["item"]:
            print(f"You got the {move[1]}!")
            inventory.append(move[1])
            rooms[currentRoom]["item"] = ""
        else:
            print("There is not one here.")
            
    if move[0] == "go":
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            print(f"You are now in the {currentRoom}.")
        else:
            print("You can't go that way.")
            
    if "key" in inventory and "potion" in inventory:
        print("You escaped the house, well done!")
    break