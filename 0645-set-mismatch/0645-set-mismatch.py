class Solution(object):
    def findErrorNums(self, nums):
        nums.sort()
        answer = []
        
        for i in range(1, len(nums)+1):
            if nums.count(i) == 2:
                answer.append(i)
        
        for i in range(1, len(nums)+1):
            if i not in nums:
                answer.append(i)
                return answer