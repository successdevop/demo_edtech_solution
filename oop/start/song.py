class Song:
    """
    Class to represent a song
    Attributes:
        title (str): Initialize the title attribute
        artist (Artist): An artist object representing the song creator
        duration (int): The duration of the song in seconds. May be zero
    """
    def __init__(self, title: str, artist: str, duration: int = 0):
        self.name = title
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
            self.artist = "Various Artist"
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position: int = None):
        found_song = find_object(song, self.tracks)
        if found_song is None:
            found_song = Song(song, self.artist)
            if position is None:
                self.tracks.append(found_song)
            else:
                self.tracks.insert(position, found_song)


class Artist:
    """Base class to store artist details"""
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, album_field, year, song):
        obj = find_object(album_field, self.albums)
        if obj is None:
            print(f"{album_field} not found")
            obj = Album(album_field, year, self.name)
            self.add_album(obj)
        else:
            print(f"{album_field} found")
        obj.add_song(song)


def find_object(field, object_list):
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    artist_list = []

    with open("albums.txt", mode="r", encoding="utf-8") as file_reader:
        for line in file_reader:
            artist_field, album_field, year, song = line.strip("\n").split("\t")
            year = int(year)
            # print(artist_field, album_field, year, song)
            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year, song)

    return artist_list


def check_file(artists_list):
    with open("checkfile.txt", mode="w", encoding="utf-8") as file_checker:
        for artis in artists_list:
            for albums in artis.albums:
                for songs in albums.tracks:
                    print(f"{artis.name}\t{albums.name}\t{albums.year}\t{songs.name}", file=file_checker)


if __name__ == "__main__":
    artists = load_data()
    print(f"There are {len(artists)} artist in the list")

    check_file(artists)
