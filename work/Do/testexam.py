
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



def plusone(n):
    sum=0
    for i in n:
        sum=sum*10 +i

    sum+=1
    return [int(i) for i in str(sum)]

result=plusone([1,2,3])
print(result)

a=[]
for i in "123":
    a.append(int(i))
print (a)


def yieldprime(n):
    for i in range(2,n):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            yield i


a = []
# for i in yieldprime(100000):
#
#     a.append(i)
# print (len(a))

for i in range(1,3):
    print ("hi")


def testyield(value):
    print("1")
    a=yield value
    print ("2")
    yield "haha"

testyield(100)



def bubble_sort(n):
    for i in range(len(n)-1):
        for j in range(len(n)-1-i):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
    return n

print (bubble_sort([3,2,1,0,100]))


def select_sort(n):
    for i in range(len(n)-1):
        min_index=i
        for j in range(i,len(n)):
            if n[j]<n[min_index]:
                min_index=j
        n[min_index],n[i]=n[i],n[min_index]
    return n
print (select_sort([3,2,1,100,0,1]))
            
            
def insert_sort(n):
    for i in range(len(n)-1):
        key=n[i]
        j=i-1
        while j>=0 and n[j]>key:
            n[j+1]=n[j]
            j-=1
        n[j+1]=key
    return n
print (select_sort([3,2,1,0,9,100,1]))


def getprime(n):
    a=[]
    for i in range(2,n):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            a.append(i)
    return a

print (getprime(1000))


def fib(n):
    a,b=0,1
    alist=[0,1]
    for i in range(n):
        alist.append(alist[-2]+alist[-1])
    return alist
print (fib(100))


def fib2(n):
    alist =[0,1]
    if n<=1:
        return n
    else:
        return fib2(n-1)+fib2(n-2)
print (fib(1))


# def fib3(n):
#     a,b=0,1


def yieldprime(n):
    for i in range(2,n):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            yield i


a = []
for i in yieldprime(100):
    a.append(i)

print (a)


a="abc"
b="123"
c="哈哈"

print (a,b,c)

aa=a.encode('utf8')
bb=b.encode('utf8')
cc=c.encode('utf8')
print (aa)
print (bb)
print (cc)

newa=aa.decode('utf-8')
newb=bb.decode()
newc=cc.decode()
print (newa,newb,newc)


a=b'\xe5\x93\x88\xe5\x93\x88'
aa=a.decode("utf8")
print (aa)
a1=aa.encode('gbk')
print (a1)