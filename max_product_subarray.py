def maxProduct_subArray(nums):  
    maxSub = prevMax = prevMin = nums[0]
    for x in nums[1:]:
        curMin = min(x, x * prevMax, x * prevMin)
        curMax = max(x, x * prevMax, x * prevMin)
        maxSub = max(maxSub, curMax)
        prevMin = curMin
        prevMax = curMax
    return maxSub
