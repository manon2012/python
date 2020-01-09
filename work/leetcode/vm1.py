
def vm1(s):
    for i in s:
        if s.count(i)==1:
            return s.index(i)
    else:
        return -1

r=vm1("sdjfsdklajfkldsjlkafjsdaiojfdsiojfasdklfv")
print (r)

def vm2(s):
    d={}
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    print (d)

    for index,char in enumerate(s):
        if d[char]==1:
            return index
    return -1
r=vm2("sdjfsdklajfkldsjlkafjsdaiojfdsiojfasdklf")
print (r)

def c1(a,b ):
    aa=[]
    for i in a:
        if i in b:
            aa.append(i)
            b.remove(i)
    return aa
r=c1([1,2,2,1],[2,2])
print (r)

def p2(n):
    while n%2==0:
        n/=2
    return n==1

r1=p2(1024)
r2=p2(10)
print (r1)
print (r2)


def m3(n):
    n1=list(set(n))
    if len(n1)<3:
        return max(n1)
    n1.sort()
    return n1[-3]
r=m3([1,2,2,2,2,3,3])
print (r)

def anagram(a,b):
    aa="".join(sorted(a))
    bb="".join(sorted(b))
    if aa==bb:
        return True
    return False

r=anagram("abc","cba")
print (r)
#
#
# a="cba"
# b=sorted(a)
# print (b)


def a2(n):
    d={}
    for i in n:
        ii="".join(sorted(i))
        if ii not in d:
            d[ii]=[i]
        else:
            d[ii].append(i)
    return d.values()
r=a2(["eat", "tea", "tan", "ate", "nat", "bat"])
print (r)

def a3(n):
    d = {}
    for i in n:
        ii = "".join(sorted(i))
        v=d.get(ii,[])
        v.append(i)
        d[ii]=v
    return d.values()
r1=a3(["eat", "tea", "tan", "ate", "nat", "bat"])
print (r1)


