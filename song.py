class Song:
    """Class to represent a song
    Attributes:
        title(str): Title of ths song.
        artist(Artist): An artist object representing the song's creator.
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


class Album:
    """Class to represent an Album, using it's track list
    Attributes:
        name (str): The name of the album.
        year (int): The year was album was released.
        artist: (Artist): The artist responsible for the album. If not specified,
        the artist will default to an artist with the name "Various Artists".
        tracks (List[Song]): A list of the songs on the album.
    Methods:
        addSong: Use to add a new song to the album's track list.
    """
    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """Add a song to the tracks
        Args:
            song(Song) = a Song object to be added
            position(Optional[int]): If specified song will be added to that position
                in the tracks - inserting it between other songs if necessary.
                Otherwise, the song will be added the end of the tracks.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


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
    # This is called circular object reference: major problem with this design currently is that an artist object will
    # have a reference to an album and that album object will also have a reference to the artist.

    # the problems that that can cause are to do with garbage collection.when the program is no longer using these
    # the garbage collector might see that there's still a reference to both objects each from the other one and then
    # ultimately not reclaim the memory for either.(Python 3 garbage collector is quite advanced and can cope quite well
    # with these situations but circular object references like the one like this are still best avoided)

    # another problem with circular references like this is that it can seriously complicate saving the objects
    # to file or to a database when we try to write an artist object then we will go through all the attributes
    # and save them into disk when we get to the album's object the program will go through the album attributes
    # and save them to disk in the process it would find an artist attribute that would then need to be
    # saved so it will go through all the attributes and save them to disk in the process finding a collection of albums
    # each containing a reference to an artist object that contains a collection of objects and so on


def find_object(field, object_list):
    """Check object_list to see if an object with a name attribute equal to field exists, if so return it"""
    for object in object_list:
        if object.name == field:
            return object
    return None


def load_data():
    new_artist = None
    new_album = None
    artist_list = []
    with open("albums.txt", encoding="utf-8") as data_file:
        for line in data_file:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip().split("\t"))
            year_field = int(year_field)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                # we've just read details for a new artist
                # retrieve the artist object if there is one otherwise create a new artist and add it to the artist list
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None



            if new_album is None:
                new_album = Album(album_field, year_field, artist=artist_field)
                new_artist.add_album(new_album)
            elif new_album.name != album_field:
                # we've just read details for a new album
                # retrieve the album object if there is one otherwise create a new album object and restore it
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, artist=artist_field)
                    new_artist.add_album(new_album)

            # create a new song object and then add it to the current albums collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        # After read the last line of the text file, we will have an artist and album that haven't
        # been store - process them now

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
