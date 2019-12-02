
def wrapper(f):
    def inner(*args,**kwargs):
        print ("log info before")
        ret =f(*args,**kwargs)
        print("log info after")
        return  ret
    return  inner


@wrapper
def home():
    print ("this it home tv")
@wrapper
def fh():
    print ("this is fh")

home()
fh()


def cal(a):
    b=10
    def newadd():
        ret=int(a)+int(b)
        return  ret
    return  newadd

print (cal(10)())
