class Solution(object):
    def minSubsequence(self, nums):
        nums.sort()
        i = -1
        while sum(nums[i:]) <= sum(nums[:i]):
            i -= 1
        return sorted(nums[i:], reverse=True)
            