def merge2list(a,b):
    for item in b:
        if item<=a[-1]:
            for i in range(len(a)):
                if item<a[i]:
                    a.insert(i,item)
        else:
            if b.index(item)==0:
                a.extend(b)
                return a
            else:
                a.append(item)

    return a

r=merge2list([1,2,3],[1,8,9,100])
print (r)

a=[1,2,3,4,5]
a.reverse()
print (a)