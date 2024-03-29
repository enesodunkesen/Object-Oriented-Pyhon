class Song:
    """Class to represent a song
    Attributes:
        title(str): Title of ths song.
        artist(str): The name of the song's creator.
        duration(int): The duration of the song in seconds. May be zero.
        """

    def __init__(self, title, artist, duration=0):
        """Song init method
        Args:
            title(str): Initializes the `title` attribute.
            artist(Artist): An artist object representing the song's creator.
            duration(int): Initial value for the `duration` attribute.
                Will default to zero if not specified.
        """
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title
    name = property(get_title)


class Album:
    """Class to represent an Album, using it's track list
    Attributes:
        name (str): The name of the album.
        year (int): The year was album was released.
        artist(str): The name of the artist responsible for the album. If not specified,
        the artist will default to an artist with the name "Various Artists".
        tracks (List[Song]): A list of the songs on the album.
    Methods:
        addSong: Use to add a new song to the album's track list.
    """
    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Various Artists"
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """Add a song to the tracks
        Args:
            song(title) = The title of a song to be add
            position(Optional[int]): If specified song will be added to that position
                in the tracks - inserting it between other songs if necessary.
                Otherwise, the song will be added the end of the tracks.
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)


class Artist:
    """Basic store artist details.
    Attributes:
        name(str): The name of the artist
        albums(List[album]): The list of the albums by this artist.
            List includes only those albums in this collection. It is
            not an exhaustive list of the artist's published albums.
    Methods:
        add_album: Use to add a new album to artist's albums.
    """
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add new album to the albums
        Args:
            album(Album): An album object to add to the list.
                If the album object is already present, it will not added again.
        """
        self.albums.append(album)

    def add_song(self, name, year, title):
        """Add a new song to the collection of albums

        This method will add the song to an album in the collections.
        A new album will be created if the if it doesn't already exists.

        Args:
            name(str): The name of the album
            year(int): The year of the album produced
            title(str): The title of the song
        """
        album_found = find_object(name, self.albums)
        if album_found is None:
            album_found = Album(name, year, artist=self.name)
        album_found.add_song(title)


def find_object(field, object_list):
    """Check object_list to see if an object with a name attribute equal to field exists, if so return it"""
    for object in object_list:
        if object.name == field:
            return object
    return None


def load_data():
    artist_list = []
    with open("albums.txt", encoding="utf-8") as data_file:
        for line in data_file:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip().split("\t"))
            year_field = int(year_field)

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

    return artist_list


def check_file(artist_list):
    with open("checkfile.txt", "w", encoding="utf-8") as file:
        for artist in artist_list:
            for album in artist.albums:
                for song in album.tracks:
                    print(f"{artist.name}\t{album.name}\t{album.year}\t{song.title}", file=file)


data = load_data()
for artist in data:
    print(artist.name)
print(len(data))
check_file(data)