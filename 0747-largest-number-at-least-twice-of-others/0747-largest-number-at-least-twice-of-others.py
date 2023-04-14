class Solution(object):
    def dominantIndex(self, nums):
        origin = [i for i in nums]
        nums.sort()
        if nums[-1] >= nums[-2]*2:
            return origin.index(nums[-1])
        else:
            return -1