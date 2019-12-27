a=[1,2,3]
print (a.index(1))


for i in range(2,2):
    print(a[i])


a=[2,4,5,6]
# b=list(range(a[0],len(a)+1))
#
# result=[]
# for i in b:
#     if i not in a:
#         result.append(i)
# print (result)

b=[2,4,6]
aa=set(a)
bb=set(b)
print (aa-bb)


c=[111,22,3]
from collections import Counter
d=Counter(c)
print (d[3])


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # print (list(set(nums)))
    a = []
    for i in nums:
        if i not in a:
            a.append(i)
    print(a)
removeDuplicates([1,2,1,1,2,3,2,1])
