def twoSum( nums, target):
    d={}
    for index,i in enumerate(nums):
        if target-i in nums:
            return [index,nums.index(target-i)]

r=twoSum([2, 7, 11, 15], target = 9)
print (r)
