class Solution(object):
    def createTargetArray(self, nums, index):
        final = []
        for idx, value in enumerate(index):
            final.insert(value, nums[idx])
        return final