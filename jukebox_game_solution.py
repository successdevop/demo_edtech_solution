from nested_tuple import albums

SONG_LIST_INDEX = 3                 #always at index 3
SONG_TITLE_INDEX = 1                #always at index 1

while True:
    print("Please choose your album (invalid choices exits): ")
    for index, (album, artist, year, song) in enumerate(albums):
        print("{}: {}".format(index+1, album))
    choice = int(input())

    if 1 <= choice <= len(albums):
        song_list = albums[choice - 1][SONG_LIST_INDEX]
        print("Please choose your song")
        for index, (trackNo, track) in enumerate(song_list):
            print("{}: {}".format(trackNo, track))
        choice = int(input())
        if 1 <= choice <= len(song_list):
            particular_song = song_list[choice - 1][SONG_TITLE_INDEX]
            print("Playing {}".format(particular_song))
            print("=+"*50)
        else:
            print("You are starting all over again, please enter a valid number this time")
            print()
    else:
        break
