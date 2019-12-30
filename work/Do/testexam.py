
a=[1,2,3,4,5,6,7,8,9,10]


def found3(n):
    n.sort()
    return n[-3]

print (found3(a))

a.pop()

def prime(n):
    alist=[]
    for i in range(2,n):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            alist.append(i)
            
    return alist

print (prime(1000))
            