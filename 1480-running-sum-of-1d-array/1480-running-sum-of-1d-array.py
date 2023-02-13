class Solution(object):
    def runningSum(self, nums):
        final = []
        running_sum = 0
        for i in nums:
            running_sum += i
            final.append(running_sum)
        return final