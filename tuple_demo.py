albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

while True:
    print("Please choose your album (invalid choices exits): ")
    for index in range(len(albums)):
        print(f"{index + 1}:", albums[index][0])
    value = int(input()) - 1
    if 0 <= value <= 3:
        print("Please choose your song: ")
        for num, track in enumerate(albums[value][3]):
            index, song = track
            print(f"{index}: {song}")
        value1 = int(input()) - 1
        if 0 <= value1 < len(albums[value][3]):
            print("Playing {}".format(albums[value][3][value1][1]))
            print("="*50)
    else:
        break



