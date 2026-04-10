class Song:
    """
    Class to represent a song
    Attributes:
        title (str): Initialize the title attribute
        artist (Artist): An artist object representing the song creator
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title: str, artist: str, duration: int = 0):
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """
    Class to represent an album, using it's track list
    Attributes:
        name (str): The name of the album
        year (int): The year album was released
        artist (Artist): An artist object representing the album creator. If not specified, default to
            the name 'various artist'
        tracks (list([Song])): A list of songs on the album

    Methods:
        add_song: Used to add a song to the album track list
    """

    def __init__(self, album_name: str, year: int, artist=None):
        self.name = album_name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artist")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song: Song, position: int = None):
        if position is None:
            self.tracks.append(Song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Base class to store artist details"""

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)


def load_data():
    artist = None
    album = None
    artist_list = []
    songs = None

    with open("albums.txt", mode="r", encoding="utf-8") as file_reader:
        for line in file_reader:
            artist_field, album_field, year, song = line.strip("\n").split("\t")
            year = int(year)
            # print(artist_field, album_field, year, song)

            if artist is None:
                artist = Artist(artist_field)
            elif artist.name != artist_field:
                artist.add_album(album)
                artist_list.append(artist)
                artist = Artist(artist_field)
                album = None

            if album is None:
                album = Album(album_field, year, artist)
            elif album.name != album_field:
                artist.add_album(album)
                album = Album(album_field, year, artist)

            if songs is None:
                songs = Song(song, artist_field)
            else:
                album.add_song(song)

        if artist is not None:
            if album is not None:
                artist.add_album(album)
            artist_list.append(artist)
        print()

    return artist_list


def check_file(artists_list):
    with open("checkfile.txt", mode="w", encoding="utf-8") as file_checker:
        for artis in artists_list:
            for albums in artis.albums:
                for songs in albums.tracks:
                    print(f"{artis.name}\t{albums.name}\t{albums.year}\t{songs.title}", file=file_checker)


if __name__ == "__main__":
    artists = load_data()
    print(f"There are {len(artists)} artist in the list")

    # for artist in artists:
    #     for album in artist.albums:
    #         print(f"{album.tracks[0].}")
            # for song in album.tracks:
            #     print(f"{song.}")

    check_file(artists)

