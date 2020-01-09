def swap01(str):
    #n=str.split("")
    n=[]
    for i in str:
        n.append(i)
    print (n)
    for i in range(len(n)):
        if n[i]=='0':
            n[i]=1
        else:
            n[i]=0
    print (n)
    return ("".join(n))
r=swap01("00100")
print (r)