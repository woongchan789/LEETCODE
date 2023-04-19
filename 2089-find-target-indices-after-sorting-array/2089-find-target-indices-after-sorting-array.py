class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        answer = []
        for idx, val in enumerate(nums):
            if val == target:
                answer.append(idx)
        return answer