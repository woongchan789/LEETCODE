class Solution(object):
    def findLHS(self, nums):
        cnt_dict = {}
        max_value = 0
        
        nums = sorted(nums)
        
        for i in nums:
            if i not in cnt_dict:
                cnt_dict[i] = 1
            else:
                cnt_dict[i] += 1
        
        for i in cnt_dict:
            if i+1 in cnt_dict:
                max_value = max(max_value, cnt_dict[i] + cnt_dict[i+1]) 
        
        return max_value
        
        