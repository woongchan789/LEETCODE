class Solution(object):
    def frequencySort(self, nums):
        return sorted(sorted(nums, reverse=True), key=nums.count)