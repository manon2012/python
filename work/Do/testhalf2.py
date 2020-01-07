def half2(n,a):
    first=0
    last=len(n)-1

    while first<last:
        mid= (last+first)//2
        print (mid)
        if a==n[mid]:
            return True
        elif a>n[mid]:
            first=mid+1
        else :
            last=mid -1
    return False
print (half2([0,1,2,3,4,5,6,7,8,9,10,11],6))
