class Solution(object):
    def sortedSquares(self, nums):
        temp = []
        for i in nums:
            temp.append(i**2)
        temp.sort()
        return temp