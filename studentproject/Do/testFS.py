class Student():
    role="student"

s1=Student()
s1[id]='001'

if hasattr(s1,'role'):
    a=getattr(s1,'role')
    print (a)
print (s1.id)