# _____________________________________________________
class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages


class Ebook(Book):
    def __init__(self, title, publisher, pages, format_):
        Book.__init__(self, title, publisher, pages)
        self.format_ = format_


ebook = Ebook("Python", "Packet", 500, "PDF")


# print(ebook.title, ebook.publisher, ebook.pages, ebook.format_)  #Python Packet 500 PDF


# _____________________________________________________
class Book1:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages


class Ebook1(Book1):
    def __init__(self, title, publisher, pages, format_):
        super().__init__(title, publisher, pages)
        self.format_ = format_


ebook1 = Ebook1("Python", "Packet", 500, "PDF")


# print(ebook1.title, ebook1.publisher, ebook1.pages, ebook1.format_) # Python Packet 500 PDF

# _____________________________________________________
####
class Shape:
    geometry_type = "Generic Shape"

    def area(self):
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometry_type


class Plotter:
    def plot(self, ratio, topleft):
        print("plotting at {}, ratio {}.".format(
            topleft, ratio
        ))


class Polygon(Shape, Plotter):
    geometry_type = "Polygon"


class RegularPolygon(Polygon):
    geometry_type = "Regular Ploygon"

    def __init__(self, side):
        self.side = side