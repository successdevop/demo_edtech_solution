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
        album_name (str): The name of the album
        year (int): The year album was released
        artist (Artist): An artist object representing the album creator. If not specified, default to
            the name 'various artist'
        track (list([Song])): A list of songs on the album

    Methods:
        add_song: Used to add a song to the album track list
    """
    def __init__(self, album_name: str, year: int, artist: None):
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
