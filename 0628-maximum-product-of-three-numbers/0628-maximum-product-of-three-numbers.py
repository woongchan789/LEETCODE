class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        a = (nums[0] * nums[1] * nums[-1])
        b = (nums[0] * nums[-2] * nums[-1])
        c = (nums[-3] * nums[-2] * nums[-1])
        return max(a,b,c)