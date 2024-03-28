"""
Class: template for creating objects. ALL objects created using the same class will have the share characteristics.
Object: an instance of A class.
Instantiate: create an of и class.
Method: a function defined in a class.
Attributes a variable bound to an Instance of a class.
"""


class Kettle(object):
    # our kettle class is modelling electric kettles, so we can introduce a class attribute called power source that all
    # instances will share (this is very similar to static fields in Java similar but not exactly the same)
    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
hamilton = Kettle("Hamilton", 14.55)

kenwood.power = 1.5
print(kenwood.power)
# this case now the Kenwood instance of the kettle class now has another data attribute called power with the value 1.5
# now remember that variables in Python come into existence the first time they're assigned a value and the same thing
# data attributes so here attribute for the Kenwood object called power and it has a value of 1.5 so the term attribute
# is useful because it describes power as a variable that is bound to an instance of the kettle class


# print(hamilton.power)
# if we run this we get an error message attribute kettle object has not attribute power.reason for that is the
# Hamilton instance doesn't have a power attribute because we haven't created one by assigning a
# value to it like we did for the Kenwood instance

# this is the dynamic nature of Python that allows this kind of behaviour, and you can easily end up with instances
# that are created from the same class template but which ultimately have different attributes, and it can be useful
# feature but can also cause problems if you make a typing error when trying to assign a value to an existing attribute

# of course subclassing - where a new class is created from an existing one - may be preferable to adding attributes
# there are ways to prevent this kind of behaviour, and you can create classes in such a way that additional attributes
# can't be added to instances forcing classes to be subclass extra functionality is required but
# Python allow you to take either approach

print(Kettle.power_source)
print(hamilton.power_source)
print(kenwood.power_source)
# two instances are sharing the same attribute which only exists in the class and we can access the namespace
# via the dic attribute

print(Kettle.__dict__)  # output : 'power_source': 'electricity'
print(hamilton.__dict__)  # output : {'make': 'Hamilton', 'price': 14.55, 'on': False}
print(kenwood.__dict__)  # output : {'make': 'Kenwood', 'price': 8.99, 'on': False, 'power': 1.5}

# we can see that power_source attribute is only shows up in the class
# so what happens is that when we try to access the power_source attribute for the instances Python checks to see if
# the power source exists in the instance name space if it doesn't which is the case here it then checks the class for
# the instance and finds power source in the kettle class and that's why the reason it printed out because basically
# it got it from the class attribute


Kettle.power_source = "atomic"
print(Kettle.power_source)  # output : atomic
print(hamilton.power_source)  # output : atomic
print(kenwood.power_source)  # output : atomic

# what happens there is that atomic we are switching to atomic power and the three printouts are now all the same again
# as well and only updated the class attribute but it has changed the other two instances one automatically which is
# proof that the instances for Hamilton and kenwood are looking at the class attribute at that point
# but that's not true if you try and change this in different ways

kenwood.power_source = "gas"
print(Kettle.power_source)  # output : atomic
print(hamilton.power_source)  # output : atomic
print(kenwood.power_source)  # output : gas

# so what happened is Python created a new local variable that shattered the global one so a similar thing is actually
# happening in this scenario when we added the code to switch the kenwood power_source to gas

print(kenwood.__dict__)  # output: {'make': 'Kenwood', 'price': 8.99, 'on': False, 'power': 1.5, 'power_source': 'gas'}

# this is one of the ways that class attributes differ from Java static fields so this is definitely something to
# watch out for as it's quite easy to make the mistake of assigning a new value to a class attribute via an
# instance variable and Java will give you a  warning if you try to access as a static field via an instance variable
# but you won't get any such warnings in Python

a = 12
b = 30

print(a+b)
print(a.__add__(b))
# click on the plus note that it has gone to the __add__() method in the built-ins so what you can see by that is that
# whether you use this __add__() method or use a plus it's calling the same code that is built-in

# although this is not true of other oop languages in Python, a class is also exactly the same thing as a type
# other languages might refer to kenwood in our sample program is being of type kettle but they also have types
# that are not classes but in Python every type is a class, which is why we were able to call the add method.
