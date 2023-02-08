class Solution(object):
    def searchInsert(self, nums, target):
        i = 0
        while i <= len(nums)-1:
            if nums[i] < target:
                i += 1
            elif nums[i] == target:
                return i
            elif nums[i] > target:
                return i
        return i