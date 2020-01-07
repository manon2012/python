def find3(n):
    for i in range(2):
        n.pop(n.index(max(n)))
    return max(n)

r=find3([1,2,2,2,2,3,4,5])
print (r)

def find3a(n):
    a=list(set(n))
    a.sort()
    return a[-3]

rr=find3a([1,2,3,2,3,4])
print (rr)