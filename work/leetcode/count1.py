from collections import Counter



def firstUniqChar( s):
    """
    :type s: str
    :rtype: int
    """
    if len(s)==0:
        return -1
    for i in s:

        if s.count(i)==1:
            return s.index(i)

            break
    else:
        return -1

r=firstUniqChar("bbcccde")
r2=firstUniqChar("aa")
print (r)
print (r2)

def first2(s):
    d={}
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    print (d)
    for index,char in enumerate(s):
        # if d[char]==1:
        #     return index
        print (index,char)
    return -1

r3=first2("bbcccd")
print (r3)

