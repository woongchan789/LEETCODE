class Solution(object):
    def thirdMax(self, nums):
        unique_nums = []
        
        for i in nums:
            if i not in unique_nums:
                unique_nums.append(i)
        
        unique_nums = sorted(unique_nums, reverse = True)
        
        if len(unique_nums) < 3:
            return unique_nums[0]
        else:
            return unique_nums[2]