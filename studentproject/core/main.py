from core import auth
from core import student
from core import manager
import sys


def entry():
    print ("welcome to 3T system")
    user,ident=auth.login()
    print (sys.modules)


    file = sys.modules[__name__]
    print (file)
    cls=getattr(file,"core."+ident)
    obj=cls(user)
    newtodo= cls.TODO
    for num, i in enumerate(newtodo,1):
        print (num,i[0])
    choice = int(input("num>>"))
    choice_item = newtodo[choice-1]
    getattr(obj,choice_item)()




if __name__ == '__main__':
    entry()