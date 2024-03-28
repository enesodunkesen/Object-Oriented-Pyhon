# an important part of object-oriented programming is the concept of encapsulation so the idea here is that objects
# contain the data and the methods that operate on that data and don't expose the actual implementation to the outside

# Python doesn't restrict us to using an object approach this is one of the important design decisions of the Python
# the basic principle being that we're all responsible adults at least when programming, many languages work by imposing
# restrictions on what can be done with encapsulated data Java and C++ for example restrict access to class fields
# by allowing them to be marked as private in Python you can indicate that a method or attribute should be considered
# non-public, but it's extremely difficult to fully enforce in Python

# neither approach is necessarily better they are just different and each has its own advantages and disadvantages

import datetime
import pytz
class Account:  # the convention is to start class names with a capital letter and to use camel case
    # you'll find many the built-in classes in Python do use lowercase nevertheless IntelliJ will give you a warning
    # if you use lowercase or separate paths of the class name with underscores

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
    # static methods (which is the same term used in Java and C++)  is shared by all instances of the class in the same
    # way that the powersource class attribute of our kettle class was shared by all instances. making the method static
    # is pretty simple we just remove the self parameter and put an annotation before the method definition

    # unlike class attributes we can't call static methods by instances instead we should call them by class names

    # the convention is that names starting with an underscore are non-public even though if you remember theirs nothing
    # in Python that enforces this so the account class is concerned with managing bank accounts not with date and time
    # so although clients can call the current underscore time method if they want to the underscore makes it clear that
    # this method isn't intended to be used outside of the class

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self.transactions_list = [(Account._current_time(), balance)]
        print(f"Account created for {self._name}")
        # In Python, using an underscore `_` in an attribute is a convention used to indicate that the attribute is
        # intended to be non-Public or internal to the class or module. It's a way to signal to other developers that
        # the attribute is not part of the public interface and should be accessed or modified only within the class
        # or module itself, rather than by external code.(but there's nothing to prevent you from accessing attributes)

        # Double leading underscores (__) trigger name mangling in Python. Name mangling is a mechanism that Python uses
        # to avoid naming conflicts between subclasses. When you have a method or attribute with double underscores as
        # a prefix,Python internally renames that attribute to include the class name, effectively making it more unique
        # This is useful in cases where you want to ensure that subclasses don't accidentally override methods or
        # attributes of their base class(We can still access these types of attributes, but not by normal means )

# we defined init method as constructor but really that's not strictly the Class creation process involves two steps:
# first - method to be called when a class instance is created is `__new__` and this takes care of the actual creation
# second - `__init__` method then customizes the instance performing tasks such as giving values to the data attributes

# technically the class constructor is the new method which is actually calling `__new__` as you probably expect
# generally speaking we don't need to define new except in special cases when subclassing certain types of classes

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transactions_list.append((Account._current_time(), amount))
        self.show_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.transactions_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more than your account balance")
        self.show_balance()

    def show_balance(self):
        print(f"Balance is {self.__balance}")

    def show_transactions(self):
        for date, amount in self.transactions_list:
            if amount >= 0:
                transaction_type = "deposited"
            else:
                transaction_type = "withdrawed"
                amount = -amount
            print(f"\t{amount} {transaction_type} on {date.astimezone()}")


# one advantage provided by encapsulation is that we can change the way that the methods are implemented as long as
# we don't change their signature in a way that is it that is incompatible with the current signature. signature is the
# definition of the name and parameters of a function as well as any return value and applies to methods as well


enes = Account("Enes", 0)
enes.show_balance()
enes.deposit(1000)
enes.withdraw(2000)
enes.withdraw(500)
enes.show_transactions()

enes.__balance = 200
enes.show_balance()  # output : balance is 500

# in Python if some attribute in class definition starts with `__` , it automatically does name mangling by
# appending _ClassName to the beginning of the identifier, where ClassName is the name of the current class.
# The idea of that is to prevent name clashes and  prevent subclasses to accidentally override these "private" members.

print(enes.__dict__)  # output: '_Account__balance': 500 ... '__balance': 200

enes._Account__balance = 200  # output : Balance is 200
enes.show_balance()
# so Python won't stop us doing something like changing the mangled attribute

# final comment on this is that ending an attribute name with 2 underscores doesn't result in the name being magnled
# so names are only mangled if they start with two underscores and if they end with no more than a single underscore
# so __init__() method for example is not mangled

