def showInstructions():
    print(
        """
RPG Game
========
Commands:
go [direction]
get [item]
look
inventory
quit
"""
    )
    
def look(currentRoom, rooms):
    """
    Display room details including description, items, and available exits.
    
    Args:
        currentRoom: The name of the current room
        rooms: The rooms dictionary from rooms.py
    """
    room = rooms.rooms[currentRoom]
    
    # Print room name and description
    print(f"\n=== {currentRoom} ===")
    print(room.get("description", ""))
    
    # Print items in the room
    if room.get("item"):
        print(f"\nItems here: {room['item']}")
    
    # Print available exits (doors)
    print("\nExits:")
    directions = ["north", "south", "east", "west"]
    available_exits = []
    
    for direction in directions:
        if direction in room:
            destination = room[direction]
            available_exits.append(f"  {direction.capitalize()} → {destination}")
    
    if available_exits:
        print("\n".join(available_exits))
    else:
        print("  No exits available.")
    print()
