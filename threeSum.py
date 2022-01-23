class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        #using two pointer method to each element of list
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                target = nums[l]+nums[i]+nums[r]
                if target == 0:
                    #cleaning data from duplicates
                    result.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                elif target > 0:
                    r-=1
                else:
                    l+=1
        #convert to list of lists in return
    
        return result
