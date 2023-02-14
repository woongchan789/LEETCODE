class Solution(object):
    def countKDifference(self, nums, k):
        cnt_dict = {}
        for i in set(nums):
            if i not in cnt_dict:
                cnt_dict[i] = nums.count(i)
        
        final = 0
        for i in cnt_dict.keys():
            if i + k in cnt_dict.keys():
                final += cnt_dict[i] * cnt_dict[i+k]
                
        return final