class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        i = 1
        while i <= k:
            nums.sort()
            nums[0] = -nums[0]
            i += 1
        return sum(nums)