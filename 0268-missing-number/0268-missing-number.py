class Solution(object):
    def missingNumber(self, nums):
        answer = list(range(len(nums)+1))
        for i in answer:
            if i not in nums:
                return i