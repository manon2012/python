

a=['1','2','3']
print ([int(x) for x in a])


def f(x):
    return int(x)

print (list(map(f,a)))


b=['1','2','3','@']
def f2(x):
    return str(x).isalnum()

print (list(filter(f2,b)))

from functools import reduce
c=list(range(11))
print (c)
def f3(x,y):
    return  x+y
print(reduce(f3,c))


aa=[1,2,3,4,5]
def f(n):
    return n%2==1

print (list(filter(f,aa)))


#print (f(aa))


a="a   a  b c"
newa=""
for i in a:
    if i ==" ":
        continue
    else:
        newa+=i
print(newa)

b=a.split(" ")
print (b)
print ("".join(b))

newaa=a.replace(" ", "")
print (newaa)