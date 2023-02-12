class Solution(object):
    def moveZeroes(self, nums):
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt += 1
        while cnt != 0:
            nums.remove(0)
            nums.append(0)
            cnt -= 1
        return nums