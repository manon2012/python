class Student():
    role="student"

    def __init__(self,name):
        self.name=name
    def __str__(self):
        return  self.name

s1=Student("tom")
print(s1)
print (type(s1))
#s1[id]='001'

if hasattr(s1,'role'):
    a=getattr(s1,'role')
    print (a)
#print (s1.id)  #    s1[id]='001'
#TypeError: 'Student' object does not support item assignment