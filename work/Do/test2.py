nest=[1,2,3]
a=nest.__iter__()

while 1:
    try:
        print (a.__next__())
        print ("got it")
    except StopIteration as e:
        print (e)
        break
else:
    print ("test")


g=(x for x in range(10))
for i in g:
    print (i)

def outter(flag):
    def wrapper(func):
        def inner(*args,**kwargs):
            if flag:
                print("setup")
            ret=func(*args,**kwargs)
            if flag:
                print("teardown")
            return ret
        return inner
    return wrapper

@outter(True)
def func(year):
    print ("rich%s"%year)
@outter(False)
def f1():
    print ("cc")

func(2020)
f1()