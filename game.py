import dictionaries.functions as func
import dictionaries.rooms as rooms
import dictionaries.monsters as monster
import os
import random


def pick_random_monster(monsters=monster.MONSTERS):
    monster.validate_monsters(monsters)

    monster_names = list(monsters.keys())
    monster_count = len(monster_names)
    if monster_count == 0:
        raise ValueError("No monsters are available.")

    selected_index = random.randrange(monster_count)
    selected_name = monster_names[selected_index]
    return selected_name, monsters[selected_name]


func.show_instructions()

inventory = []
forced_monster_name = os.environ.get("FDM_MONSTER", "").strip()
if forced_monster_name:
    if forced_monster_name in monster.MONSTERS:
        current_monster_name = forced_monster_name
        current_monster = monster.MONSTERS[forced_monster_name]
    else:
        print(f"Unknown FDM_MONSTER '{forced_monster_name}'. Falling back to random monster.")
        current_monster_name, current_monster = pick_random_monster()
else:
    current_monster_name, current_monster = pick_random_monster()
current_room = current_monster["startingRoom"]
monster_defeated = False
hint_found = False
visited_rooms = set()

# Balcony is always locked, and its key is always in the Master Bathroom.
rooms.rooms["Master Bathroom"]["item"] = "balcony key"

locked_doors = {
    ("Upstairs Landing", "north"): {
        "room": "Balcony",
        "key": "balcony key",
    }
}


def place_key_in_room(key_name, preferred_room):
    if preferred_room != "Master Bathroom" and rooms.rooms[preferred_room].get("item", "") == "":
        rooms.rooms[preferred_room]["item"] = key_name
        return preferred_room

    for room_name, room_data in rooms.rooms.items():
        if room_name in ("Master Bathroom", "Green House"):
            continue
        if room_data.get("item", "") == "":
            room_data["item"] = key_name
            return room_name

    return preferred_room


lock_options = current_monster.get("lockOptions", [])
if lock_options:
    forced_lock_index = os.environ.get("FDM_LOCK_INDEX", "").strip()
    selected_lock = None
    if forced_lock_index:
        try:
            index = int(forced_lock_index)
            if 0 <= index < len(lock_options):
                selected_lock = lock_options[index]
        except ValueError:
            selected_lock = None

    if selected_lock is None:
        selected_lock = random.choice(lock_options)

    key_name = selected_lock["key"]
    key_room = place_key_in_room(key_name, selected_lock["keyRoom"])
    locked_doors[(selected_lock["from"], selected_lock["direction"])] = {
        "room": selected_lock["lockedRoom"],
        "key": key_name,
    }

    if key_room != selected_lock["keyRoom"]:
        print(f"You hear metal clink in the distance. A {key_name} was moved to {key_room}.")

print("Something is hunting you in this house. Find the hint to learn what it is.")

while True:
    print(f"You are currently in the {current_room}.")

    if current_room not in visited_rooms:
        print(rooms.rooms[current_room].get("description", ""))
        visited_rooms.add(current_room)

    if current_room == "Balcony" and not hint_found:
        print("A torn note catches in the wind...")
        print(current_monster["hint"])
        hint_found = True

    room_item = rooms.rooms[current_room].get("item", "")
    if room_item:
        print(f"You see {room_item}.")

    move = input("> ").strip().lower()
    if not move:
        continue

    parts = move.split(" ", 1)
    command = parts[0]
    argument = parts[1] if len(parts) > 1 else ""

    if command == "quit":
        print("Game over. Thanks for playing.")
        break

    if command == "get":
        if not argument:
            print("Get what?")
        elif argument == rooms.rooms[current_room].get("item", ""):
            print(f"You got the {argument}!")
            inventory.append(argument)
            rooms.rooms[current_room]["item"] = ""

            if argument == "balcony key":
                print("The lights snap out for a heartbeat.")
                print("A freezing whisper curls around your ears: 'You should not have touched that.'")
        else:
            print("There is nothing here.")

    elif command == "go":
        if not argument:
            print("Go where?")
        elif argument in rooms.rooms[current_room]:
            door_lock = locked_doors.get((current_room, argument))
            if door_lock and door_lock["key"] not in inventory:
                print(
                    f"The way to {door_lock['room']} is locked. You need the {door_lock['key']}."
                )
                continue

            current_room = rooms.rooms[current_room][argument]
            print(f"You are now in the {current_room}.")

            if current_room == "Green House" and not monster_defeated:
                has_weakness = current_monster["weakness"] in inventory
                has_needed_item = current_monster["neededItem"] in inventory
                if has_weakness and has_needed_item:
                    print(current_monster["success"])
                    monster_defeated = True
                else:
                    print(current_monster["failure"])
                    break
        else:
            print("You can't go that way.")

    elif command == "look":
        func.look(current_room, rooms)

    elif command == "inventory":
        print(f"You have: {', '.join(inventory)}")

    else:
        print("Unknown command.")

    if current_room == "Front Door" and "front door key" in inventory:
        print(
            f"After the vicious encounter with {current_monster_name}, you made your way out the front door running as fast as possible. Congratulations, you have beaten the monster and survived."
        )
        break