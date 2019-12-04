
def countupper():
    count =0
    #os.chdir('C:\Users\lifei\Desktop')
    with open ("a.txt","r") as f:
        for i in f.read():
            if i.isupper():
                count+=1
    print(count)

countupper()


mylist=[1,6,9,0,2]
from random import shuffle
shuffle(mylist)
print (mylist)


#join split

a="hello world"
b=a.split()
print (b)

c="123"
d='-'.join(c)
print(d)



def A(x):
    def B():
        print(x)
    return B

A(7)()


s = "ajldjlajfdljfddd"
s=set(s)
s=list(s)
s.sort()
print (s)
print ("".join(s))

