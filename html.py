# Composition is a design principle where a class consists of one or more objects of other classes, rather than
# inheriting from them. It's a way to combine simple or complex objects to create more complex ones.

# has-a relationship: Composition is often described in terms of a "has-a" relationship. For example, if a Car class
# "has-a" Engine, it means the Engine is part of the Car.

# building blocks: Composition allows you to create complex objects by combining simpler ones. For instance,
# a Car object can be composed of Engine, Wheel, and Chassis objects.
class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = f"<{name}>"
        self.end_tag = f"</{name}>"
        self.contents = contents

    def __str__(self):
        return f"{self.start_tag}{self.contents}{self.end_tag}"

    def add_tag(self, name, content):
        new_tag = Tag(name, content)
        self.contents.append(new_tag)

    def display(self, file=None):
        print(self.start_tag, file=file)
        for tag in self.contents:
            print("\t", tag, file=file)
        print(self.end_tag, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC -//W3C//DTD HTML 4.01//EN""http://www.w3.org/TR/html4/strict.dtd"', "")
        self.end_tag = ""  # DOCTYPE doesn't have an end tag


class HtmlDoc(object):
    def __init__(self, title):
        self._doc_type = DocType()
        self._head = Tag("HEAD", [])
        self._body = Tag("BODY", [])
        self._head.add_tag(name="TITLE", content=title)
    # so our HTML dot class is made up of instances of the three other classes, so we can say that
    # it's composed of the three other classes and that's composition

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print("<HTML>", file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print("</HTML>", file=file)


my_page = HtmlDoc("My first HTML document")

my_page.add_tag("H1", "Main heading")
my_page.add_tag("H2", "sub-heading")
my_page.add_tag("P", "This is a paragraph that will appear on the page")

with open("test.html", "w", encoding="utf-8") as file:
    my_page.display(file)

my_page.display()
print(my_page._head.start_tag)
# in the init method for HtmlDoc class we've created a new Tag objects and assign it to the attributes of the
# HtmlDoc class now any HtmlDoc objects we create will have their own Tag objects and can use the attributes and methods
# of Tag class.When a class contains another object like this that's called composition

# in this example Head,Body and DocType classes are inherited from Tag class (is-a relation)
# and HtmlDoc is composed of Head,Body and DocType classes (has-a relation)

# we can use Composition over inheritance design principle which suggests favoring object composition over inheritance
# to achieve code reuse and flexibility in software design. Instead of inheriting behavior and properties from parent
# classes, you compose your classes by including instances of other classes that implement the desired functionality.
