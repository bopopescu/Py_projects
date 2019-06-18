class Animal():
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print("%s is eating %s." %(self.name,food))

class Dog(Animal):
    def fetch(self,thing):
        print("%s goes after the %s!" %(self.name,thing))

class Cat(Animal):
    def swatstring(self):
        print("%s shreds the string!" %(self.name))

r = Dog("Rover")
r.fetch("bone")
r.eat("dog food")

print()
d = Cat("Fluffy")
print(d) #<__main__.Cat object at 0x0000018C0D2A9F98>

f = Cat(d)
print(f) #<__main__.Cat object at 0x0000018C0D2A9FD0>

f.swatstring()     #<__main__.Cat object at 0x0000018C0D2A9F98> shreds the string!
f.eat("cat food") #<__main__.Cat object at 0x0000018C0D2A9F98> is eating cat food.
