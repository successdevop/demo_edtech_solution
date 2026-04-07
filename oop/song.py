class Song:
    """
    class to represent a song
    Attributes:
        :title (str): the title of the song
        :artist (Artist): the artist object representing a song creator
        :duration (int): The duration of the song in seconds. Maybe zero
    """
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.album = []

help(Song.__init__)