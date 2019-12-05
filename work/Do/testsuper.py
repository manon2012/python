#
# class Bird():
#     def __init__(self):
#         self.hungry=True
#
#     def eat(self):
#         if self.hungry:
#             print (" i eat")
#             self.hungry=False
#         else:
#             print("thank you.")
# class ABird(Bird):
#     def __init__(self):
#         #super().__init__()
#         Bird.__init__(self)
#         self.sound = "jjzz"
#
#     def song(self):
#         print (self.sound)
#
#
# b1=Bird()
# b1.eat()
# b1.eat()
#
# a1=ABird()
# a1.song()
# a1.eat()



class Bird():
    def __init__(self):
        self.hungry=True

    def eat(self):
        if self.hungry:
            print (" i am eat")
            self.hungry =False
        else:
            print ('thank you')

class StarBird(Bird):
    def __init__(self):
        #super(StarBird,self).__init__()
        Bird.__init__(self)
        self.sound ='lol'
    def song(self):
        print ("i can %s"%self.sound)


b1=Bird()
b1.eat()
b1.eat()

b2=StarBird()
b2.song()
b2.song()

b2.eat()