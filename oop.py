# we've been mainly using the imperative style of programming up until now, imperative programming involves
# providing a series of instructions for the computer to follow in a defined order

# object-oriented programming aims to combine data and the processes that act on that data into objects which is called
# `encapsulation`, it's important to realize that the different paradigms are not necessarily exclusive for example
#  oop makes use of imperative programming within the methods that objects used to manipulate the data

# everything in Python is an object, even types are implemented as classes. Python is unusual in this respect because
# even though Python uses objects extensively you don't actually have to be aware of that to use so Python can be used
# for object-oriented programming but can also be used to write purely imperative programming code

# Python supports multiple programming paradigms including object-oriented, imperative and functional programming
# or procedural styles
class Kettle(object):
    # constructor by the way refers to a special method that is executed when an instance of a class is instantiated
    # in Python this is the __init__() method
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False
    # a reference to the instance of the class in C++ or Java `self`is equivalent to `this` and it's used to refer to
    # instance variables there's nothing really special about the name self or the parameter, and you have called it
    # anything you wanted avoiding name conflicts with other objects of course, but unlike to key word `this` in Java
    # for example `self` is  just the name of a parameter the important thing is the presence of the parameter
    # convention is to called self and although this is not enforced, it's not a good idea to change the convention

    def switch_on(self):
        self.on = True
    # functions that are bound to a class called methods and main difference between a method and a function is the
    # presence of this self parameter that's been added automatically


# think of a class as a template from which objects can be created so when we create objects of this kettle class they
# all have a name and a price now they won't have the same name nor the same price each instance of the class
# will have its own values for name and price but all the objects created from the same class will share the same
# characteristics. (an instance is just another name for an object created from a class definition)

kenwood = Kettle("Kenwood", 8.99)
print(kenwood.price, kenwood.price, sep=" : ")

hamilton = Kettle("Hamilton", 14.55)
print(hamilton.make, hamilton.price, sep=" : ")

# code on line 36 creates an instance of the kettle class, and we've given it the name kenwood and other instances is
# created on line 39 and this time it's called the hamilton so each instance has its own  values for naming and price
# and their access by using `.` annotations, we type in Kenwood.price or Hamilton.make for argument sake to access that


# (data attributes also called fields in languages such as Java or data members in C++)

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)
# we don't provide a value for the self parameter when calling the switch_on method when you call a method on a instance
# Python automatically provides a reference to the instance as the first parameter to the method

print(kenwood.on)
Kettle.switch_on(kenwood)
print(kenwood.on)




