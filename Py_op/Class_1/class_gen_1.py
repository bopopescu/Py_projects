class test( ):
    def __init__(self, nick_name):
        self.nick_name = nick_name

    def callback(self):
        print('self is  ', self)


obj = test("log")
print("obj   is ", obj)
obj.callback()
# obj   is  <__main__.test object at 0x03108290>
# self is   <__main__.test object at 0x03108290>
print("*****************************************")

this_test = test(obj)
this_test.callback() # self is   <__main__.test object at 0x00718D10>
print("_______________________________________________")

print("obj.__dict__ is ", obj.__dict__) # {'nick_name': 'log'}
# print("_______________________________________________")

# print("\n")
# print("this test is ", this_test)#this test is  <__main__.test object at 0x000001905D614BE0>
# print ("obj is", obj) #obj is <__main__.test object at 0x000001905D614AC8>






