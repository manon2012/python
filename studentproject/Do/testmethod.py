
class student():
    def __init__(self,name,age):
        self.name =name
        self.age=age

    @classmethod
    def learn(cls):
        print (" student is learn ")

    @staticmethod
    def study():
        print ("student is study")

student.learn()
student.study()