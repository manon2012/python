
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #print (list(set(nums)))
        a=[]
        for i in nums:
            if i not in a:
                a.append(i)
        print (a)
        
        
s1=Solution()
s1.removeDuplicates([1,2,2,3,3,3])


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            print (nums.index(target))
        else:
            for i in nums:
                if target<i:
                    print (nums.index(i))
                    break
            else:
                print (len(nums))


s2=Solution()
s2.searchInsert([1,2,5,6],5)



#print (sum(1,2))


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n%3==0:
            print (True)
        else:
            print (False)
s3=Solution()
s3.isPowerOfThree(100)
s3.isPowerOfThree(9)




class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1=set(nums1)
        s2=set(nums2)
        print (s1&s2)
        
s4=Solution()
s4.intersect([1,2,2,3],[2,2])


a = [1, 2,2,2,2, 3]
b = [3, 2,2]
same_list = [m for m in a if m in b]
print (same_list)


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

def getprime(n):
    for i in range(2,n):
        if n%i==0:
            #print ("not p")
            return False
        else:
            #print ("p")
            return True
#getprime(7)

def getsum(n):
    a=[]
    b=list(filter(getprime,range(2,n)))
    print (b)
    a.extend(b)
    print (sum(a))

# b=list(filter(getprime,range(2,10)))
# print (b)

getsum(10)

# def getoushu(n):
#     if n%2==0:
#         return True
#
# n=[1,2,3,4,5,6]
# print (list(filter(getoushu(),n)))


s="abcasdfjkljklaba"
for i in s:

    if s.count(i) == 1:
        print(i)
        break

from math import sqrt
a=9

print (sqrt(a))



class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        a=[]
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                for k in range(j+1,len(nums)-1):
                    if nums[i]+nums[j]+nums[k]==0:
                        a.append(nums(i))
                        a.append(nums(j))
                        a.append(nums(k))
                        print (a)
                        return a
ss=Solution()
ss.threeSum([-1,0,1,2,-1,-4])