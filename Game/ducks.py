# Polymorphism refers to the ability of different objects to respond to the same message (method call) in different ways
# This allows objects of different classes to be treated as objects of a common superclass. Polymorphism enables code
# flexibility and facilitates the implementation of generic algorithms that can operate on objects of various types
# without needing to know their specific classes.

class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print("Area:", shape.area())

# in Shape class example Polymorphism is provided by Inheritance(`is a relationship`)
# Inheritance isn't the only way to implement polymorphism a class can behave in the same way as another class
# as long as it's got the necessary methods and data attributes

class Duck(object):
    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on it, the water is lovely")

    def quack(self):
        print("Quack!")


class Penguin(object):

    def walk(self):
        print("Waddle, waddle, waddle. I am a penguin")

    def swim(self):
        print("Come on it, but the water is a bit chilly")

    def quack(self):
        print("Look at me I am a penguin")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()


donald = Duck()
test_duck(donald)

percy = Penguin()
test_duck(percy)

# duck function still works now percy may will be behaving a little bit strangely by duck standards but
# as far as the test_duck functions concerned percy walks like a duck swims like a duck and quacks like a duck

# python deals with objects unlike statically typed languages that require the type of every object to be declared
# when it's used pythons dynamic typing means that it's only really interested in what can be done with an object if an
# object has the necessary attributes then python quite happy for it to be used

# trivia : phrase is commonly used in dynamically type languages like python is duck typed.
