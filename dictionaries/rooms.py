
rooms = {
    "Dining Hall": {
        "north": "Kitchen",
        "south": "Music Room",
        "west": "Foyer",
        "item": "key"
    },
    "Kitchen": {
        "east": "Garden",
        "south": "Dining Hall",
        "item": "chainsaw"
    },
    "Garden": {
        "north": "Dining Hall",
        "west": "Kitchen",
        "item": "Chainsaw"
    },
    "Music Room": {
        "west": "Foyer",
        "north": "Dining Hall",
        "item": "potion",
        "south": "Garden"
    },
    "Foyer": {
        "north": "Upstairs Landing",
        "east": "Dining Hall",
        "west": "Library",
        "south": "Front Door",
        "item": "",
    },
    "Library": {
        "east": "Foyer",
        "north": "Study",
        "south": "Billiard Room",
        "item": ""
    },
    "Study": {
        "south": "Library",
        "item": ""
    },
    # UPSTAIRS
    "Upstairs Landing": {
        "south": "Foyer",
        "west": "Master Bedroom",
        "east": "HallwayOne",
        "north": "Balcony",
        "item": ""
    },
    "Master Bedroom": {
        "east": "Upstairs Landing",
        "item": ""
    },
    "HallwayOne": {
        "west": "Upstairs Landing",
        "south": "HallwayTwo",
        "east": "Boys Bedroom",
        "item": ""
    },
    "Boys Bedroom": {
        "west": "HallwayOne",
        "item": ""
    },
    "HallwayTwo": {
        "north": "HallwayOne",
        "east": "Bathroom",
        "south": "HallwayThree",
        "item": ""
    },
    "Bathroom": {
        "west": "HallwayTwo",
        "item": ""
    },
    "HallwayThree": {
        "east": "Girls Bedroom",
        "north": "HallwayTwo",
        "item": ""
    },
    "Master Bedroom": {
        "east": "Upstairs Landing",
        "south": "Waiting Room", 
        "item": ""
    },
    "Waiting Room": {
        "north": "Master Bedroom",
        "south": "Master Bathroom",
        "item": ""
    },
}


