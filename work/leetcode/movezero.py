def movezero(n):
    for i in range(len(n)):
        if n[i]==0:
            n.pop(i)
            n.append(0)
    return n

r=movezero([1,0,2,0,3,0])
print(r)