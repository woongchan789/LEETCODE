class Solution(object):
    def majorityElement(self, nums):
        
        cnt = 0
        value = None
        
        for i in nums:
            if cnt==0:
                value = i
            cnt += (1 if i == value else -1)
            
        return value