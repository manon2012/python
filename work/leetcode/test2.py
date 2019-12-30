class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        all = []
        if len(nums)==3:
            if nums[0]+nums[1]+nums[2]==0:
                all.append(nums[0])
                all.append(nums[1])
                all.append(nums[2])
                return all

        else:
            for i in range(0,len(nums)-2):
                for j in range(i+1,len(nums)-1):
                    for k in range(j+1,len(nums)):

                        if nums[i]+nums[j]+nums[k]==0:
                            a = []
                            a.append(nums[i])
                            a.append(nums[j])
                            a.append(nums[k])
                            #print (a)

                            all.append(a)
            return all

ss=Solution()
result=ss.threeSum([-1,0,1,-2,3,2])
print (result)