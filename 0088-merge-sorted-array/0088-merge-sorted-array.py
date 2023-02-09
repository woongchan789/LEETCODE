class Solution(object):
    def merge(self, nums1, m, nums2, n):
        a = len(nums1) - m
        b = len(nums2) - n
        for i in range(a):
            nums1.remove(nums1[-1])
        for i in range(b):
            nums2.remove(nums2[-1])
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        return nums1