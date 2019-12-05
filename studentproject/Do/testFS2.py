
class Teacher():
    dic={"checkstudent":"checkstudent","checkclass":"checkclass"}

    def __init__(self):
        pass
    def checkstudent(self):
        print ("this is check student")

    def checkclass(self):
        print ("this is check class")

for i in Teacher.dic:
    print (i)
tom=Teacher()
while True:
    key=input("please select:")

    if hasattr(tom,Teacher.dic[key]):
        a=getattr(tom,Teacher.dic[key])
        a()



