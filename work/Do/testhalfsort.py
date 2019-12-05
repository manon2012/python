
a=[1,2,3,4,5,6,7,8,9,11,66,99,200,900]

def bs(a,x):
    n=len(a)
    first=0
    last =n-1

    while first<=last:
        mid = (first+last) // 2
        if a[mid]==x:
            return  True

        elif x<a[mid]:
            last=mid
        else:
            first=mid
    return False


if __name__ == '__main__':
    #print (bs(a,9))
    print (bs(a,100))