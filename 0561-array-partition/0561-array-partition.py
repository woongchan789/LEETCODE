class Solution(object):
    def arrayPairSum(self, nums):
        nums = sorted(nums)
        return sum(nums[::2])