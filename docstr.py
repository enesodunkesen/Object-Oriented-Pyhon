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

# a docstring is a string literal that occurs as the first statement in a module, function, class definition.
# It is used to provide documentation and information about the purpose, usage, parameters, return values
# and other details of the object it documents. docstring should provide information that is useful to understanding
# what the object does and also how to use it now you should also include other details that aren't obvious such as
# what will happen if a value wasn't specified, writing good documentation is a skill in itself
# check PEP 257 for more

# a docstring is enclosed within triple quotes and that keeps your doc strings consistent with everyone else's
# and also means you can include quotes in the documentation as well now if you intend to use escape characters
# you know such as /t or /n in your doc string then use r with 3 quotes to make it a raw string

# In Python, a raw string is a string literal prefixed with an r or R. Raw strings treat backslashes (\) as
# literal characters, rather than as escape characters as they are interpreted in regular strings.
# raw strings literals introduced in Python 2 mainly for using regular expressions, but we can use it for docstrings too


regular_string = "This is a regular string.\nIt has a newline character."
raw_string = r"This is a raw string.\nIt does not have a newline character."
alternative_string = "This is an alternative sting.\\nIt does not have a newline character"

print(regular_string)
print(raw_string)
print(alternative_string)

print("*"*80)
# help(Song)  # every docstring included
help(Song.__init__)  # __init__() method docstring
# help(Song.__doc__)  # class docstring

# one important note here is using help() for accessing documentations of classes and methods is essential
