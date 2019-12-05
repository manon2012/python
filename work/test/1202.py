# def bubble_sort(n):
#     for i in range(len(n)):
#         for j in range(len(n)-1-i):
#             if n[j]>n[j+1]:
#                 n[j],n[j+1]=n[j+1],n[j]
#     return  n
#
# print (bubble_sort([3,2,1,100,0,1]))
#
# def select_sort(n):
#     for i in range(len(n)):
#         min_index=i
#         for j in range(i+1,len(n)):
#             if n[j]<n[min_index]:
#                 min_index=j
#         n[i],n[min_index]=n[min_index],n[i]
#     return n
#
# print (select_sort([3,2,1,9,8,7]))


# def insert_sort(n):
#     for i in range(1,len(n)):
#         key=n[i]
#         j=i-1
#         while j>=0 and key<n[j]:
#             n[j+1]=n[j]
#             j-=1
#         n[j+1]=key
#     return n
# print (insert_sort([3,2,1]))

# class Emp():
#     count =0
#     def __init__(self,name, id):
#         self.name = name
#         self.id=id
#         Emp.count +=1
#     def say(self):
#         print ("hah, i am %s"%self.name)
#     def myid(self):
#         print ("hah, i am No %s"%self.count)
#
# tom = Emp('tom',"ufo")
# jdck=Emp("jack","lol")
# tom.say()
# jdck.myid()




class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def choose_class(self):
        print ("i choose class")

    def check_class(self):
        print ("i check it")

class Teacher():
    def __init__(self,name,age):
        self.name = name
        self.age =age

    def teach_course(self):
        print ("i teache course")


def wrapper(fun):
    def inner(*args,**kwargs):
        ret =fun()
        return ret
    return  inner









def print_msg(msg):

    def printer():

        print(msg)

    return printer # this got changed


another = print_msg("Hello")
another()
'''print_msg()函数被通过传入“Hello”所调用，返回的函数被绑定为another. 在调用another()的时候，我们对print_msg()函数已经完成调用了，但是“Hello”仍然被记住了！
这种将一些数据("Hello")附加到代码的技术，被称为python里面的closure.
闭合范围内的数据(非本地变量)能够一直被记住，即便它们已经脱离了闭合范围或者外部函数已经被从命名空间删除'''


def f1(x):
    return x*2

#print (list(map(lambda x:f1,[1,2,3])))
print (list(map(f1,[1,2,3])))

print (list(map(lambda x:x*2,[1,2,3])))

# items = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, items))
#
# 上面使用了匿名函数，也可以自定义函数：
#
# items = [1, 2, 3, 4, 5]
# def f(x):
#     return x**2
# squared = list(map(f, items))


from functools import reduce
def f1(x,y):
    return  x*y

print (reduce(f1,range(1,11)))

s=1
for i in range(1,11):
    s*=i
print (s)


class Bird():
    #hungry = True
    def __init__(self):
        self.hungry =True

    def eat(self):
        if self.hungry:
            print ("i eat")
            self.hungry = False
        else:
            print ("no,thank you.")

class ABird(Bird):
    def __init__(self):
        super(ABird,self).__init__()
        self.sound ="qiqi"
    #sound ="qiqi"
    def lala(self):
        print (self.sound)

b1=Bird()
b1.eat()
b1.eat()

a1=ABird()
a1.lala()
a1.eat()
a1.eat()



def f1(x):
    return x.isalnum()

print (list(filter(f1,['12','3',"a","*","."])))



def bubble_sort(n):
    for i in range(len(n)-1):
        for j in range(len(n)-1-i):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
    return  n

print (bubble_sort([3,2,1,2,10]))


def select_sort(n):
    for i in range(len(n)-1):
        min_index=i
        for j in range(i,len(n)):
            if n[j]<n[min_index]:
                min_index = j
        n[i],n[min_index]= n[min_index],n[i]
    return  n

print (select_sort([3,2,1,100,0]))


def insert_sort(n):
    for i in range(1,len(n)):
        key=n[i]
        j=i-1
        while j>=0 and n[j]>key:
            n[j+1]=n[j]
            j-=1
        n[j+1]=key
    return  n
print (insert_sort([3,2,1,100,0]))