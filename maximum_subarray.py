def max_Subarray(nums):
    maxSub = curSum = nums[0]
    for x in nums[1:]:
        if curSum < 0:
            curSum = 0
        curSum += x
        maxSub = max(maxSub, curSum)
    return maxSub
