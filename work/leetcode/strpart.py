def countSegments( s):
    """
    :type s: str
    :rtype: int
    """
    if s.strip():
        return len(s.split(" "))
    else:
        return 0

r=countSegments("Of all the gin joints in all the towns in all the world,   ")
print (r)

a="Of all the gin joints in all the towns in all the world,   "
b=a.strip().split(" ")
print (b)
print (len(b))