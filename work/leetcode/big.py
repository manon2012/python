def big(n):
    for i in range(len(n)):
        a=0
        b=[]
        c=[]
        for j in range(len(n)):
            a+=n[j]
            b.append(a)
        c.append(max(b))
    return max(c)

r=big([1,2,-3,9,8,0,-3])
print (r)

d={"a":1,"b":2}
r=d.get("c",[])
print (r)


