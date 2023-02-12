class Solution(object):
    def summaryRanges(self, nums):
        
        final = []
        
        if not nums:
            return []
        
        a = nums[0]
        b = nums[0]
        
        def append_value(a, b):
            if a == b:
                return str(a)
            else:
                return str(a) + str("->") + str(b)
                
        for i in range(1,len(nums)):
            if nums[i] != (nums[i-1]+1):
                final.append(append_value(a,b))
                a = nums[i]
                b = nums[i]
            else:
                b = nums[i]
        final.append(append_value(a,b))
        
        return final