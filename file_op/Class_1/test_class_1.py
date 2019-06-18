class test(object):
    def __init__(self,nick_name):
        self.nick_name = nick_name
    def callback(self):
        print('calling "callback" method with instance: ', self)


obj = test("log")
this_test = test(obj)
this_test.callback() #<__main__.test object at 0x000001905D614BE0>
print("\n")
print("this test is ", this_test)#this test is  <__main__.test object at 0x000001905D614BE0>
print ("obj is", obj) #obj is <__main__.test object at 0x000001905D614AC8>


"""
if __name__ == "__main__":
    print()
    object_1 = test("Henry Sun")
    print("nick name is ", object_1.nick_name)
"""
print(obj.__dict__)
#{'nick_name': 'log'}



