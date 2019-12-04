# import math
#
# class Circle():
#     def __init__(self,r):
#         self.r=r
#     @property
#     def area(self):
#         return  3.14*self.r*self.r
#
# c1=Circle(2)
# print (c1.area)



class Student():
    def __init__(self,name,age):
        self.__name =name
        self.age =age

    @property
    def name(self):
        print (self.__name)

    @name.setter
    def name(self,newname):
        if type(newname) ==str and str(newname).isdigit()==False:
            self.__name =newname
    @name.deleter
    def name(self):
        print ("1")
        del self.__name

s1=Student("tom",21)
s1.name
s1.name ="newname"
s1.name

s1.name = '123'
s1.name

del s1.name
s1.name


