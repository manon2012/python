def restr(str):
    r=str.split(" ")
    rr=[i[::-1] for i in r]
    return ' '.join(rr)

r=restr("hi hello world")
print (r)


def all(str):
    return str[::-1]

r=all("hi hello world")
print (r)

"""Input : str = "geeks quiz practice code"
Output : str = "code practice quiz geeks"""


def a1(str):
    a=str.split(" ")
    b=a[::-1]
    return  " ".join(b)

r=a1("geeks quiz practice code")
print (r)


"""Input : geeksforgeeks
Output : efgkos"""

def a2(str):
    # a=[]
    # for i in str:
    #     a.append(i)
    # b=list(set(a))
    # return "".join(b)

    return "".join(set(str))


r=a2("geeksforgeeks")
print (r)



"""Input  : list = [1, 2, 3] 
Output : [[], [1], [1, 2], [1, 2, 3], [2], 
         [2, 3], [3]]"""
a = [1, 2, 3]
r=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        r.append(a[i:j])
print (r)




"""Input : list = [10, 20, 30, 40, 50] 
        index = 2
Output : [10, 20, 40, 50] """

def test(a,index):
    a.remove(a[2])
    return a
r=test([10, 20, 30, 40, 50] ,2)
print (r)


def check(a,x):
    for i in a:
        if i>x:
            return True
    return   False

print (check([2,3,4,1],1))


"""
Input : [10, 20, 30, 40, 50, 60, 70, 80, 90]
Output : 30 60 90 40 80 50 20 70 10
"""
def removee3(n):
    index=0
    pos=3-1
    a=len(n)
    while a>0:
        index=(index+pos)%a
        print (n.pop(index))
        a-=1

removee3([10, 20, 30, 40, 50, 60, 70, 80, 90,100])




# a=[10, 20, 30, 40, 50, 60, 70, 80, 90]
# while len(a)>0:
#     a.pop()
#     len(a)-=1  can't assign to function call
print ("$$$$$")
a=[10, 20, 30, 40, 50, 60, 70, 80, 90]
n=len(a)
while n>0:
    print (a.pop())
    n-=1  #can't assign to function call
print (a)


def sum1(n):
    a=[]
    # for i in n:
    #     a.append(sum(i))
    # return max(a)

    for i in n:
        x = 0
        for y in i:
            x+=y
        a.append(x)
    return max(a)


r=sum1([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]] )
print (r)

d1={"a":1,"b":2,"c":3}
d2=dict([("a",1),("b",2),("c",3)])
d3=dict(a=1,b=2,c=3)

# print (d1)
# print (d2)
# print (d3)
a=['a','b','b','c','c','c']

b={}.fromkeys(a,[])
c={}.fromkeys(a,"vm")
print (b)
print (c)

print (c.get('a'))
#print (c.get(d))

aa={'a': 'vm', 'b': 'vm', 'c': 'vm'}
print (aa.get("a"))
print (aa.setdefault("d","VM"))
print (aa)


