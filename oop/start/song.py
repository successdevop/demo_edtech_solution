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
    Class to represent an album, using its track list
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
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Base class to store artist details"""

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)


def find_object(field, object_list):
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    artist = None
    album = None
    artist_list = []

    with open("albums.txt", mode="r", encoding="utf-8") as file_reader:
        for line in file_reader:
            artist_field, album_field, year, song = line.strip("\n").split("\t")
            year = int(year)
            # print(artist_field, album_field, year, song)

            if artist is None:
                artist = Artist(artist_field)
                artist_list.append(artist)
            elif artist.name != artist_field:
                artist = find_object(artist_field, artist_list)
                if artist is None:
                    artist = Artist(artist_field)
                    artist_list.append(artist)
                album = None

            if album is None:
                album = Album(album_field, year, artist)
                artist.add_album(album)
            elif album.name != album_field:
                album = find_object(album_field, artist.albums)
                if album is None:
                    album = Album(album_field, year, artist)
                    artist.add_album(album)

            songs = Song(song, artist_field)
            album.add_song(songs)
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

    check_file(artists)
