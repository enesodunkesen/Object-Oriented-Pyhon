# Python classes don't need getters and setters to allow you to read and change the values of their data attributes
# so it doesn't have the facility to make class attributes private like many other object-oriented languages do.
# but getters and setters are still useful in Python, even if they're not essential
# (tim's suggest :don't worry about them when you're creating your classes and that's because chances
# are you won't need them so don't spend time creating getters and setters that won't be needed)
class Player(object):
    def __init__(self, name):
        self.name = name
        self._lives = 3
        # we're hiding these methods by starting their names with an underscore. Of course, they're not really hidden,
        # but there's no need for clients to use them directly and the underscore at the start of the name gives
        # users of our class an indication that they shouldn't really be calling these methods.
        self._level = 1
        self.score = 0

    def _get_lives(self):
        return self._lives

    # get_attr() methods define the behavior for retrieving the value of the attribute. This method should take no
    # arguments (besides self, if it's a method of a class) and return the value of the attribute.

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            self._lives = 0

    # set_attr() methods define the behavior for setting the value of the attribute. This function should take one
    # argument (besides self, if it's a method of a class) which represents the new value being assigned to the
    # attribute. This function typically doesn't return anything.

    lives = property(_get_lives, _set_lives)

    # the last step now is to define a property called lives that uses these two methods when reading
    # and writing our lives attribute. The property() function takes two arguments: the function to be used for
    # getting the attribute (get_attribute) and the function to be used for setting the attribute (set_attribute).
    # Optionally, you can also provide a third function for deleting the attribute's value, but it's not present in this
    # (note that Python really isn't happy if you give your property the same name as the data attribute backing it.)

    # Now if you don't specify a method to use for the setter,then the property is gonna be read only which is sometimes
    # useful, now if you specify setter but no getter, then you can change the value of the property, but you can't
    # display it, and that's really the less useful, possibly maybe for a password attribute.

    def __str__(self):
        return "Name: {0.name}\tLives: {0.lives}\tLevel: {0.level}\tScore: {0.score}".format(self)

    # we can define str attribute of an object remember that print retrieves the str attribute and prints it
    # what we did here is actually an example of overriding(we've overridden the __str__() method from object class)

    # So although setters aren't needed as such in Python, they're very useful when you'd want to include validation
    # on the values that your data attributes can be set to.(like we did with the _set_lives() method)
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if level >= 1:
            self.score += (level - self._level) * 1000
            self._level = level
        else:
            print("Level cannot be less than 1")
            self.score -= (self._level - 1) * 1000
            self._level = 1

    # properties has an alternate way of coding them. in fact this alternative method is more common
    #  it uses something called decorators and does exactly the same thing as we've just seen on line 32
    #  it's just the syntax that differs now the decorator results in the property line being done for you
    #  which is why people tend to prefer it to the method on line 32
