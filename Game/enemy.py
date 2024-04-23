# we can define a base class that objects are based on in Python, things that are common for classes that derive from
# the base class. And then we can allow a class to define the unique characteristics of itself. So in other words,
# we have a base class, then something that inherits from that to make it something else again, making it unique.

# This concept is called `Inheritance` and it's really useful because : it allows you to write code once, and then for
# that code to be used automatically by other classes.So this leave you to define the unique characteristics of a class,
# rather than having to reinvent the wheel each time you create a new class.
from random import randint
from math import ceil

class Enemy:
    def __init__(self, name="enemy", lives=1, hit_points=0):
        self._name = name
        self._lives = lives
        self._hit_points = hit_points
        self._base_hit_points = hit_points
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print(f"\t{damage} dealt , {remaining_points} left")
        else:
            self._lives -= 1
            if self._lives > 0:
                print(f"{self._name} lost a life")
                self._hit_points = self._base_hit_points
            else:
                print(f"{self._name} is dead")
                self.alive = False

    def __str__(self):
        return f"name : {self._name}, lives : {self._lives}, hit points : {self._hit_points}"


class Troll(Enemy):
    # this is how you create a subclass. subclass remember is a class that inherits from another class.
    # we can also say that troll extends the enemy class, they both mean the same thing.
    # Now in fact, our enemy class is itself a subclass and that's because each class in Python 3 ultimately
    # inherits from a built-in class called object.

    # troll class will inherit from enemy and it'll have to access or have access to the attributes that
    # we defined in enemy. and it will be treated just like enemy class if we just write `pass`

    def __init__(self, name):
        # we actually need to call the init method of the superclass enemy inside our trolls init method
        # there's a few ways to do this

        # Enemy.__init__(self, name=name, lives=1, hit_points=23)

        super().__init__(name=name, lives=1, hit_points=23)
        # we can use the super method instead and if you want to cope with multiple inheritance you must use super
        # instead of specifying the base class

    def grunt(self):
        # subclasses can have additional attributes to extend their behavior and allow them to do things that
        # their base class doesn't do
        print(f"Me {self._name}! {self._name} stomp you !")


class Vampyre(Enemy):
    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=4)
    # In languages such as Java and C++ there are restrictions on the definition of an overriding method in Python
    # you just write a new method with the same name as the one that you want to override the new method doesn't even
    # have to have the same or accept the same number of parameters although it usually will so

    def take_damage(self, damage):
        chance = randint(1, 3)
        if chance == 1:
            print("\tAttack dodged")
        else:
            super().take_damage(damage)
    # subclass can implement a method from its superclass and actually do things differently that's called `overriding`
    # now vampire are shifty creatures, and they have a change to dodge the damage
    # we've overridden take_damage method so that vampires can dodge when attacked


# challenge part
# one important note here is that when we call super() method we're actually calling Vampyre not Enemy
class VampyreKing(Vampyre):
    def __init__(self, name):
        super().__init__(name=name)
        self._hit_points = 12
        self._base_hit_points = 12

    def take_damage(self, damage):
        damage_to_obj = ceil(damage/4)
        super().take_damage(damage_to_obj)
