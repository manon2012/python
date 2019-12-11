#
# def wrapper(func):
#     def inner(*args,**kwargs):
#         print("hi1")
#         func(*args,**kwargs)
#         print("hi2")
#         return  func
#     return  inner
#
#
# def wrapper2(func):
#     def inner(*args,**kwargs):
#         print("1111111")
#         func(*args,**kwargs)
#         print("2222222")
#         return  func
#     return  inner
#
# @wrapper2
# @wrapper
# def product():
#     print("here is product")
#     return True
#
# product()


def wrapper(flag):
    def timer(func):
        def inner(*args,**kwargs):
            if flag:
                print("setup")
            f=func(*args,**kwargs)
            if flag:
                print ('teardown')
            return f
        return  inner
    return timer

@wrapper(True)
def test_001(n):
    print ("test_00%s"%n)

#test_001(1)






from functools import wraps

def deco(func):
    @wraps(func)
    def inner(*args,**kwargs):
        print("haha1")
        return  func(*args,**kwargs)
        print("haha2")
    return  inner

def func():
    print ("haha")

