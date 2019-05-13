class Simplest():
    pass

# print(type(Simplest)) #<class 'type'>
simp = Simplest()
# print(type(simp)) # <class '__main__.Simplest'>

class Person:
    species = "Human"

# print(Person.species) # Human

Person.alive = True # added dynamically
# print(Person.alive) #True

man = Person()
# print(man.species) #Human
# print(man.alive) # True

man.name = "Jack"
man.surname = "Joan"
# print(man.name, man.surname) # Jack Joan

class Point:
    x = 10
    y = 7

p = Point()
# print(p.x, p.y)  # 10 7

p.x = 44
# print(p.x) #44
# print(Point.x) # 10

# del p.x
# print(p.x) # 10

p.z = 3
# print(p.z) #3
# print(Point.z) #AttributeError: type object 'Point' has no attribute 'z'

class Square:
    side = 8
    def area(self):
        return self.side ** 2
sq = Square()
# print(sq.area()) # 64
# print(Square.area(sq)) # 64

sq.side = 20
# print(sq.area()) # 400

class Price:
    def final_price(self, vat, discount=0):
        return self.net_price * (100 + vat) /100 - discount

p1 = Price()
p1.net_price = 100
# print(Price.final_price(p1, 20, 10))  # 110.0
# print(p1.final_price(20, 10))   # 110.0

## Initializer
class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
    def area(self):
        return self.side_a * self.side_b

r1 = Rectangle(10, 4)
# print(r1.side_a, r1.side_b) # 10, 4
# print(r1.area()) # 40

class Engine:
    def start(self):
        pass
    def stop(self):
        pass

class ElectricEngine(Engine):
    pass

class V8Engine(Engine):
    pass

class Car():
    engine_cls = Engine

    def __init__(self):
        self.engine = self.engine_cls()
    def start(self):
        print(
            "Starting engine {0} for car {1} ...."
            .format(
                self.engine.__class__.__name__,
                self.__class__.__name__)
            )
        self.engine.start()
    def stop(self):
        self.engine.stop()

class RaceCar(Car):
    engine_cls = V8Engine
class CityCar(Car):
    engine_cls = ElectricEngine
class F1Car(RaceCar):
    pass

car = Car()
racecar = RaceCar()
citycar = CityCar()
f1car = F1Car()

cars = [car, racecar, citycar, f1car]
# for car in cars:
#     car.start()

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



















