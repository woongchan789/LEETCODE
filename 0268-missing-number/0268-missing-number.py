class Solution(object):
    def missingNumber(self, nums):
        nums = sorted(nums)
        for idx, value in enumerate(nums):
            if idx != value:
                return idx
        return nums[-1] + 1