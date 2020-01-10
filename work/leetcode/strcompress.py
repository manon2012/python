def compress( chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    d={}.fromkeys(chars,0)
    for i in chars:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return ['{}{}'.format(k, v) for k, v in d.items()]


r=compress(["a","a","b","b","c","c","c"])
print (r)

a={'a': 2, 'b': 2, 'c': 3}
# b=['{}{}'.format(k, v) for k, v in a.iteritems()]
# print (b)
s=""
for k,v in a.items():
    s+=k
    s+=str(v)
print (s)