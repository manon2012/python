
def merge2list(a,b):
    # if b[0]>a[-1]:
    #     a.extend(b)
    # else:
    #     for i in range(len(b)):
    for i in b:
        if i<a[-1]:
            for j in range(len(a)):
                if i<=a[j]:
                    a.insert(j,i)
                    break

        else:
            a.append(i)
            break
    return a



print (merge2list([1,2,3],[2,8]))