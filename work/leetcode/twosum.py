def twoSum( nums, target):
    d={}
    for index,i in enumerate(nums):
        if target-i in nums:
            print (d)
            return [index,nums.index(target-i)]
        else:
            d[i] = index
#
# r=twoSum([2, 7, 11, 15], target = 9)
# print (r)
# def twoSum(nums, target):
#     dic = {}
#     for i in range(len(nums)):
#         if nums[i] in dic:
#             return [dic[nums[i]], i]
#         else:
#             dic[target - nums[i]] = i
r=twoSum([1,18,2, 7, 11, 15], target = 9)

print (r)


