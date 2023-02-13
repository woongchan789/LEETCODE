class Solution(object):
    def differenceOfSum(self, nums):
        el_sum = sum(nums)
        di_sum = 0
        for i in nums:
            for j in range(len(str(i))):
                di_sum += int(str(i)[j])
        return abs(el_sum-di_sum)