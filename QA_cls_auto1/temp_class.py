class ComicCharacter:
    def __init__(self,nick_name):
        self.nick_name = nick_name

    def nick_name(self):
        return self.nick_name
    def draw_speech_ballon(self,message,destination):
        pass
    def draw_thought_ballon(self,message):
        pass
"""  
class GameCharacter:
    def __init__(self,full_name,initial_score,x,y):
        self.full_name = full_name
        self.score = initial_score
        self.x = x
        self.y = y
    @property
    def full_name(self):
        return self.full_name
    def draw(self,x,y):
        pass
    def move(self,x,y):
        pass
    def is_intersecting_with(self,other_character):
        pass
"""

class AngryCat(ComicCharacter):
    def __init__(self,nick_name,age):
        super().__init__(nick_name)
        self.age = age
        self.__height = 300
    def height(self):
        print("height is ", self.__height)
    def set_height(self,height_tmp = 500):
        self.__height = height_tmp
    def draw_speech_ballon(self,message,destination):
        if destination is None:
            composed_message = self.nick_name + ' -> "'
            if self.age > 5:
                meow = 'Meow'
            else:
                meow = 'Meeeeeew Meeeooow'
            composed_message = '{} -> "{} {}"'.format(self.nick_name,meow,message)
        else:
            composed_message = '{} ==={}---> {}'.format(
                destination.nick_name,
                self.nick_name,
                message
            )
        print(composed_message)
"""

class AngryDog(ComicCharacter):
    def _speak(self,message):
        print(self.nick_name + ' -> "' + message + '"')
    def _think(self,message):
        print(self.nick_name + '***' + message + '***')
    def draw_speech_ballon(self,message,destination):
        if destination is None:
            composed_message = message
        else:
            composed_message = destination.nick_name + ", "+message
        self._speak(composed_message)
    def draw_thought_ballon(self,message):
        self._think(message)


"""
"""
declare classes that override methods
"""
if __name__ == "__main__":
    angry_cat_1 = AngryCat("Garfield",10)
    print("angry_cat_1 name is {}".format(angry_cat_1.nick_name))
    print("angry_cat_1 age is ", angry_cat_1.age)
    print (angry_cat_1.__dict__)

    #can change
    angry_cat_1.__height = 200
    angry_cat_1.set_height()
    angry_cat_1.height()
    angry_cat_1.set_height(1000)
    angry_cat_1.height()














