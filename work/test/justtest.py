

def bubble_sort(n):
    for i in range(len(n)-1):
        for j in range(len(n)-i-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
    return  n

print (bubble_sort([3,2,1,9,8,7]))


def select_sort(n):
    for i in range(len(n)-1):
        min_index=i
        for j in range(i+1,len(n)):
            if n[j]<n[min_index]:
                min_index=j
        n[min_index],n[i]=n[i],n[min_index]
    return n

print (select_sort([1,3,2,1]))



def insert_sort(n):
    for i in range(1,len(n)):
        key=n[i]
        j=i-1
        while j>=0 and n[j] > key:
            n[j+1]=n[j]
            j-=1
        n[j+1]=key

    return n

print (insert_sort([3,2,1,10,9,8,7]))


alist=[2,1,1]
a = alist.__iter__()
while 1:
    try:

        print( a.__next__())
    except Exception as e:
        print (e)
        break
    else:
        print ("123")


# def testcount():
#     count=1
#     count+=1
#     print(count)
#     testcount()
# # testcount()
#
# def f(n):
#     print (n)
#     n+=1
#     f(n)
# f(1)


import time
def wrappe(func):
    def inner(*args,**kwargs):
        t1=time.time()
        ret= func(*args,**kwargs)
        t2=time.time()
        print ("used time %s"%(t2-t1))
        return ret
    print (inner.__dir__())
    return inner
print (wrappe.__dir__())
@wrappe
def test1(n):

    time.sleep(n)
    print (n)
test1(2)



def gen(n):
    for i in n:
        yield  i
a=gen([3,2,1])
print (type(a))
for i in a:
    print (i)
g=(x**2 for x in range(10))
print(type(g))
for i in g:
    print(i)


import threading
import  time
def f1(n):
    time.sleep(2)
    print ("f1%s"%n)
def f2(n):
    time.sleep(2)
    print ("f2%s"%n)

if __name__ == '__main__':
    t1=threading.Thread(target=f1,args=(123,))
    t2=threading.Thread(target=f2,args=(345,))
    t1.daemon=True
    t2.daemon=True
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print ('in main')

class TestThread(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name =name

    def run(self):
        print ("haharun%s"%self.name)
t3=TestThread("t3")
t4=TestThread("t4")
t3.start()
t4.start()
