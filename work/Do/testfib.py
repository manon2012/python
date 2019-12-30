
def fib(n):
    fiblist=[1,1]
    #print (type(fiblist))
    for i in range(n):
        #print (fiblist)
        fiblist.append(fiblist[-1]+fiblist[-2]  )
    return fiblist


a=fib(10)
print (a)

stra="helloworld"
strb=stra[::-1]
print (strb)

x = [1,5,2,3,4]
x.reverse()
print (x)
x.sort()
print (x)

x = [1,5,2,3,4]
y=sorted(x)
print (y)


x = [1,5,2,3,4]
x.reverse()
print (x)


a=["a",'b','c']
for k,v in enumerate(a,1):
    print (k,v)