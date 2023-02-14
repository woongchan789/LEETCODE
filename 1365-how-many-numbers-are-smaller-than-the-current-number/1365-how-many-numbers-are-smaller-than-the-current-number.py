class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        
        rank_dict = {}
        temp = sorted(nums)
        final = []
        
        k = 0
        
        for i in temp:
            if i not in rank_dict:
                rank_dict[i] = k
                k += 1
            else:
                k += 1
        
        for i in nums:
            final.append(rank_dict[i])
        
        return final