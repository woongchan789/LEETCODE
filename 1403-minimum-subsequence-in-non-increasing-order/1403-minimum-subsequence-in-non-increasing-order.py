class Solution(object):
    def minSubsequence(self, nums):
        nums.sort(reverse=True)
        i = 1
        while sum(nums[:i]) <= sum(nums[i:]):
            i += 1
        return nums[:i]
            