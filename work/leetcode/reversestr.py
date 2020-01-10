def reversestr(n,k):
    a=list(n)
    for i in range(len(a)):
        if i% (2*k) ==0:
            a[i], a[i + 1]= a[i + 1], a[i]
    return "".join(a)

r=reversestr("abcdefg",2)
print(r)


