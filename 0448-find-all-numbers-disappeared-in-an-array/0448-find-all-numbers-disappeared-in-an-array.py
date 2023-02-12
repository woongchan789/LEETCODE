class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums1 = set(nums)
        nums2 = set(range(1,len(nums)+1))
        return nums2 - nums1