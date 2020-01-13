
a=["a",1,"a"]

b="".join([str(i) for i in a])
print (b)


def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
   """
    if not s:
        return True
    i = 0
    for c in t:
        if c == s[i]:
            i += 1
        if i == len(s):
            break
    return i == len(s)

r=isSubsequence("abc","aaqboc")
print (r)


nums = [3, 30, 34, 5, 9]
def big(n):
    # a=[str(i) for i in num]
    # a.sort()
    # print (a)
    # a.reverse()
    # print (a)
    # b="".join(a)
    # print (b)
    return "".join(sorted(map(str, nums), key=lambda x: x * 3, reverse=True))   #

r=big(nums)
print (r)


def majorityElement( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # for i in nums:
    #     if nums.count(i)>len(nums)/2:
    #         return i
    #         break
    dictionary = {}
    for number in nums:
        if number not in dictionary:
            dictionary[number] = 1
        else:
            dictionary[number] += 1

    for key in dictionary:
        if dictionary[key] >= len(nums) / 2:
            return key
    return 0

r=majorityElement([6,5,5])
print (r)




def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    f = 1
    l = n

    while f < l:
        m = (f + l) // 2
        if isBadVersion(m):
            l = m
        else:
            f = m + 1

    return f