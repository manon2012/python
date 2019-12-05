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




# class Teacher:
#     dic = {'查看学生信息':'show_student','查看讲师信息':'show_teacher'}
#     def show_student(self):
#         print('show_student')
#
#     def show_teacher(self):
#         print('show_teacher')
#
#     @classmethod
#     def func(cls):
#         print('hahaha')
# alex = Teacher()
# for k in Teacher.dic:
#     print(k)
# key = input('输入需求 ：')
# # print(Teacher.dic[key])
# if hasattr(alex,Teacher.dic[key]):
#     func = getattr(alex,Teacher.dic[key])
#     func()




class Teacher():
    techdict={"check st":"show_student","check teacher": "show_teacher"}

    def show_student(self):
        print ("show student in China")
    def show_teacher(self):
        print ("show teacher in China")

for i in Teacher.techdict:
    print (i)

tom=Teacher()
while 1:
    key = input("input your choice:")
    if hasattr(tom, Teacher.techdict[key]):
        i=getattr(tom, Teacher.techdict[key])
        i()

