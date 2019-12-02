
class Bird():
    def __init__(self):
        self.hungry=True

    def eat(self):
        if self.hungry:
            print (" i eat")
            self.hungry=False
        else:
            print("thank you.")
class ABird(Bird):
    def __init__(self):
        #super().__init__()
        Bird.__init__(self)
        self.sound = "jjzz"

    def song(self):
        print (self.sound)


b1=Bird()
b1.eat()
b1.eat()

a1=ABird()
a1.song()
a1.eat()