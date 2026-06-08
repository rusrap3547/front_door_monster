import random


# Keep all monsters in the same shape so new ones are easy to add.
REQUIRED_FIELDS = (
    "startingRoom",
    "hint",
    "weakness",
    "neededItem",
    "success",
    "failure",
    "lockOptions",
)


def create_monster(
    startingRoom,
    hint,
    weakness,
    neededItem,
    success,
    failure,
    lockOptions,
):
    return {
        "startingRoom": startingRoom,
        "hint": hint,
        "weakness": weakness,
        "neededItem": neededItem,
        "success": success,
        "failure": failure,
        "lockOptions": lockOptions,
    }


MONSTERS = {
    "Vampire": create_monster(
        startingRoom="Master Bedroom",
        hint="You see a vampire guarding something in the Green House.",
        weakness="garlic",
        neededItem="stake",
        success="Seeing the garlic and stake in your hands, the vampire screams and runs away.",
        failure="The vampire sees you and attacks you. You have been defeated.",
        lockOptions=[
            {
                "from": "Boarding Room",
                "direction": "north",
                "lockedRoom": "Backyard",
                "key": "backyard key",
                "keyRoom": "Dining Hall",
            },
            {
                "from": "Library",
                "direction": "north",
                "lockedRoom": "Study",
                "key": "study key",
                "keyRoom": "Music Room",
            },
            {
                "from": "Kitchen",
                "direction": "east",
                "lockedRoom": "Garden",
                "key": "garden key",
                "keyRoom": "Billiard Room",
            },
        ],
    ),
    "Werewolf": create_monster(
        startingRoom="Boys Bedroom",
        hint="You hear a werewolf growling near the Green House.",
        weakness="meat",
        neededItem="silverware",
        success="Seeing the meat and silverware in your hands, the werewolf backs away and flees.",
        failure="The werewolf lunges before you can react. You have been defeated.",
        lockOptions=[
            {
                "from": "HallwayTwo",
                "direction": "south",
                "lockedRoom": "HallwayThree",
                "key": "hallway key",
                "keyRoom": "Master Bedroom",
            },
            {
                "from": "Dining Hall",
                "direction": "north",
                "lockedRoom": "Kitchen",
                "key": "kitchen key",
                "keyRoom": "Library",
            },
            {
                "from": "Foyer",
                "direction": "west",
                "lockedRoom": "Library",
                "key": "library key",
                "keyRoom": "Upstairs Landing",
            },
        ],
    ),
    "Water Monster": create_monster(
        startingRoom="Bathroom",
        hint="Something unnatural stirs near the Green House.",
        weakness="lightning",
        neededItem="taser",
        success="The lightning charge in your taser shocks the creature and it vanishes.",
        failure="Water surges around you and pulls you under. You have been defeated.",
        lockOptions=[
            {
                "from": "Library",
                "direction": "south",
                "lockedRoom": "Billiard Room",
                "key": "billiard key",
                "keyRoom": "Garden",
            },
            {
                "from": "HallwayOne",
                "direction": "east",
                "lockedRoom": "Boys Bedroom",
                "key": "bedroom key",
                "keyRoom": "Waiting Room",
            },
            {
                "from": "Foyer",
                "direction": "east",
                "lockedRoom": "Dining Hall",
                "key": "dining key",
                "keyRoom": "Balcony",
            },
        ],
    ),
}


def validate_monsters(monsters):
    for name, data in monsters.items():
        missing = [field for field in REQUIRED_FIELDS if field not in data]
        if missing:
            raise ValueError(f"Monster '{name}' is missing required fields: {', '.join(missing)}")


def get_random_monster(monsters=MONSTERS):
    validate_monsters(monsters)
    name = random.choice(list(monsters.keys()))
    return name, monsters[name]
