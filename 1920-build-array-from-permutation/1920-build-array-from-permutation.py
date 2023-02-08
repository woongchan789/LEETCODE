class Solution(object):
    def buildArray(self, nums):
        new = []
        for i in range(len(nums)):
            new.append(nums[nums[i]])
        return new
        