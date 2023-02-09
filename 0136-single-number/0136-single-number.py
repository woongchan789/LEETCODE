class Solution(object):
    def singleNumber(self, nums):
        
        nums = sorted(nums)
        
        if len(nums)==1:
            return nums[0]
        
        i = 0
        while i <= len(nums)-3:
            if nums[i] == nums[i+1]:
                i += 2
            else:
                return nums[i]
        return nums[-1]