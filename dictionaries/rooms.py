inventory = []

current_room = "Kitchen"

rooms = {
    "Hall": {
        "north": "Kitchen"
    },
    "Kitchen": {
        "south": "Hall",
        "item": "chainsaw"
    }
}

while True:
    move = input(">")
    move = move.split(" ",1)
    if move[0] == "get":
        if move[1] == rooms[current_room]["item"]:
            print(f"You got the {move[1]}!")
            inventory.append(move[1])
            rooms[current_room]["item"] = ""
        else:
            print("There is not one here.")
            

