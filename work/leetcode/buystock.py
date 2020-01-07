def buystock(n):
    sum=0
    for i in range(1,len(n)):
        if n[i]>n[i-1]:
            sum+=n[i]-n[i-1]
    return sum

r=buystock([1,6,2,9,6])
print (r)

def buystock2(n):
    sum=[]
    r=[]
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            sum.append(n[j]-n[i])
        r.append(max(sum))
    return max(r)

rr=buystock2([1,6,2,9,10])
print (rr)