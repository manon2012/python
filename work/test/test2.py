from test1 import s1
from test1 import s1

print (s1)




class Singleston():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance=super(Singleston,cls).__init__(cls)
            return  cls._instance

    def __init__(self,name):
        self.name= name

s1=Singleston("a")
s2=Singleston("b")

print (s1 is s2)