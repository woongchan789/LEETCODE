class Solution(object):
    def leftRigthDifference(self, nums):
        answer = []
        for idx, value in enumerate(nums):
            if idx==0:
                answer.append(sum(nums[idx+1:]))
            elif idx==(len(nums)-1):
                answer.append(sum(nums[:idx]))
            else:
                answer.append(abs(sum(nums[:idx]) - sum(nums[idx+1:])))
        return answer