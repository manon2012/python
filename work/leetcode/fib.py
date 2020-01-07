def fib(n):
    fiblist=[1,1]
    #print (type(fiblist))
    for i in range(n):
        #print (fiblist)
        fiblist.append(fiblist[-1]+fiblist[-2]  )
    return fiblist

r=fib(1)
print (r)