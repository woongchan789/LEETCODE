class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        cnt = 0
        for i in range(len(nums)-2):
            temp = set([nums[i], nums[i]+diff, nums[i]+diff*2])
            if temp.issubset(set(nums)):
                cnt += 1
        return cnt