# import functions as func

# inventory = []

# current_room = "Kitchen"

rooms = {
    "Hall": {
        "north": "Kitchen",
        "east": "Dining Room",
        "item": "key"
    },
    "Kitchen": {
        "south": "Hall",
        "item": "chainsaw"
    },
    "Garden": {
        "north": "Dining Room",
        "west": "Hall",
        "item": "Chainsaw"
    },
    "Dining Room": {
        "west": "Hall",
        "item": "potion",
        "south": "Garden"
    }
}

# while True:
#     print(f"You are currently in the {current_room}.")
#     move = input(">")
#     move = move.split(" ",1)
#     if move[0] == "get":
#         if move[1] == rooms[current_room]["item"]:
#             print(f"You got the {move[1]}!")
#             inventory.append(move[1])
#             rooms[current_room]["item"] = ""
#         else:
#             print("There is not one here.")
            
#     if move[0] == "go":
#         if move[1] in rooms[current_room]:
#             current_room = rooms[current_room][move[1]]
#             print(f"You are now in the {current_room}.")
#         else:
#             print("You can't go that way.")
            

