import random
import dictionaries.monsters as monster

def show_instructions():
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
    
def look(current_room, rooms):
    """
    Display room details including description, items, and available exits.
    
    Args:
        current_room: The name of the current room
        rooms: The rooms dictionary from rooms.py
    """
    room = rooms.rooms[current_room]
    
    # Print room name and description
    print(f"\n=== {current_room} ===")
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

def pick_random_monster(monsters=monster.MONSTERS):
    monster.validate_monsters(monsters)

    monster_names = list(monsters.keys())
    monster_count = len(monster_names)
    if monster_count == 0:
        raise ValueError("No monsters are available.")

    selected_index = random.randrange(monster_count)
    selected_name = monster_names[selected_index]
    return selected_name, monsters[selected_name]
