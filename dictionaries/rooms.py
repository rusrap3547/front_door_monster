
rooms = {
    "Dining Hall": {
        "north": "Kitchen",
        "south": "Music Room",
        "west": "Foyer",
        "item": "",
        "randEvent": ""
    },
    "Kitchen": {
        "east": "Garden",
        "south": "Dining Hall",
        "item": "",
        "randEvent": ""
    },
    "Garden": {
        "north": "Dining Hall",
        "west": "Kitchen",
        "item": "",
        "randEvent": ""
    },
    "Music Room": {
        "west": "Foyer",
        "north": "Dining Hall",
        "item": "",
        "south": "Garden",
        "randEvent": ""
    },
    "Foyer": {
        "north": "Upstairs Landing",
        "east": "Dining Hall",
        "west": "Library",
        "south": "Front Door",
        "item": "",
        "randEvent": ""
    },
    "Library": {
        "east": "Foyer",
        "north": "Study",
        "south": "Billiard Room",
        "item": "",
        "randEvent": ""
    },
    "Study": {
        "south": "Library",
        "west": "Boarding Room",
        "item": "",
        "randEvent": ""
    },
    "Boarding Room": {
        "east": "Kitchen",
        "west": "Study",
        "item": "",
        "randEvent": ""
    },
    "Backyard": {
        "south": "boarding room",
        "west": "Green House",
        "item": "",
        "event": "Monster",
        "randEvent": ""
    },
    "Green House": {
        "east": "Backyard",
        "item": "",
        "randEvent": ""
    },
    # UPSTAIRS
    "Upstairs Landing": {
        "south": "Foyer",
        "west": "Master Bedroom",
        "east": "HallwayOne",
        "north": "Balcony",
        "item": "",
        "randEvent": ""
    },
    "Master Bedroom": {
        "east": "Upstairs Landing",
        "item": "",
        "randEvent": ""
    },
    "HallwayOne": {
        "west": "Upstairs Landing",
        "south": "HallwayTwo",
        "east": "Boys Bedroom",
        "item": "",
        "randEvent": ""
    },
    "Boys Bedroom": {
        "west": "HallwayOne",
        "item": "",
        "randEvent": ""
    },
    "HallwayTwo": {
        "north": "HallwayOne",
        "east": "Bathroom",
        "south": "HallwayThree",
        "item": "",
        "randEvent": ""
    },
    "Bathroom": {
        "west": "HallwayTwo",
        "item": "",
        "randEvent": ""
    },
    "HallwayThree": {
        "east": "Girls Bedroom",
        "north": "HallwayTwo",
        "item": "",
        "randEvent": ""
    },
    "Master Bedroom": {
        "east": "Upstairs Landing",
        "south": "Waiting Room", 
        "item": "",
        "randEvent": ""
    },
    "Waiting Room": {
        "north": "Master Bedroom",
        "south": "Master Bathroom",
        "item": "",
        "randEvent": ""
    },
    "Master Bathroom": {
        "north": "Waiting Room",
        "item": "",
        "randEvent": ""
    },
}


