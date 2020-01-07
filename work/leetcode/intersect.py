def intersect(a,b):
    # d = {}
    # res = []
    #
    # for i in a:
    #     if i not in d:
    #         d[i] = 1
    #     else:
    #         d[i] += 1
    # print (d)
    # for i in b:
    #     if i in d and d[i] > 0:  # condition here to avoid appending i to the list when d[i] <= 0
    #         res.append(i)
    #         d[i] -= 1
    # print(d)
    # return res

    #      return list((Counter(nums1) & Counter(nums2)).elements())
    r=[]
    for i in a:
        if i in b:
            r.append(i)
            b.remove(i)
    return r



r=intersect([1,2,2,3],[2,2,8])
print (r)