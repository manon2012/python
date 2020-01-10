def search( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # nums.sort()
    first = 0
    last = len(nums)

    while first < last:
        mid = (first + last) // 2
        if nums[mid] == target:
            return nums[mid]
        elif nums[mid] < target:
            first = nums[mid]
        else:
            last = nums[mid]
    return -1

r=search([-1,0,3,5,9,12],9)
print (r)