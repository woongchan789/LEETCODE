class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        res, cnt = 0, 0
        
        for i in nums:
            if i:
                cnt += 1
            else:
                res = max(cnt, res)
                cnt = 0
        
        res = max(cnt, res)
        
        return res
                