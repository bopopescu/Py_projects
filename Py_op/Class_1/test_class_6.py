import random
class Animal():
    def __init__(self,name):
        self.name = name

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
        self.breed = random.choice(['Shih','Beagle','Mutt'])
        #self.name = name

    def fetch(self,thing):
        print ('%s goes after the %s' % ( self.name,thing))

d = Dog('dogname')
print (d.name)
print (d.breed)


