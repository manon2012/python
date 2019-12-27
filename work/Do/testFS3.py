
class Teacher():
    dic={"teach":"teachstudent","check":"checkstudent"}

    def __init__(self,name):
        self.name=name

    def teachstudent(self):
        print (" i can teach")

    def checkstudent(self):
        print ("i can check")

tom=Teacher("tom")

tom.age=20


while 1:
    key = input("")
    if hasattr(tom,key):
        delattr(tom,key)
        print ("%s is deleted"%key)
        continue
        try:
            print (tom.key)
        except Exception:
            pass
    else:
        print ("no it")

print (tom.age)

for i in Teacher.dic:
    print (i)
# while 1:
#     key = input("please input your choice:")
#     if key=="quit":
#         break
#     if hasattr(tom, tom.dic[key]):
#         getattr(tom, tom.dic[key])()
#     else:
#         "no this, please choice again"


