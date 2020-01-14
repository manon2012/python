def dedup(n):
    #return list(dict.fromkeys(n))
    return dict.fromkeys(n)

r=dedup([1,2,3,1,2,3])
print (r)

d={1:2,3:4}
print (list(d))