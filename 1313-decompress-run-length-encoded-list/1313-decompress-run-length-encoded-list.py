class Solution(object):
    def decompressRLElist(self, nums):
        final = []
        i = 0
        while i <= (len(nums)-2):
            cnt = nums[i]
            while cnt != 0:
                final.append(nums[i+1])
                cnt -= 1
            i += 2
        return final
            