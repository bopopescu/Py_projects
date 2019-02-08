
class TibetanSpaniel:
    family = "Companion, herding"
    area_of_origin = "Tibet"
    learning_rate = 9
    obedience = 3
    problem_solving = 8
    def __init__(self, name, favorite_toy, watchdog_ability):
        self.__name = name
        self.__watchdog_ability = watchdog_ability
        self.__favorite_toy = favorite_toy
    @property
    def name(self):
        return self.__name
    @property
    def favorite_toy(self):
        return self.__favorite_toy
    @favorite_toy.setter
    def favorite_toy(self, favorite_toy):
        self.__favorite_toy = favorite_toy
####
class Person:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def __str__(self):
        return self.name + " " + self.sex + " " + str(self.age)


Jake = Person("John Wick", "M", "33")
print(Jake)


#
class Person:
    def __init__(self, name, sex, age):
        self._name = name #public
        self.sex = sex
        self.__age = age #private
    def get_age(self):
        return self.__age

    def __str__(self):
        return self._name + " " + self.sex + " " + str(self.__age)


Jake = Person("John Wick", "M", "33")
print(Jake)
#print(Jake.__age) #not working
print(Jake.get_age())
#print(Jake.sex)
print(Jake._name) #ok
#print(Jake.__age) # Not Okay