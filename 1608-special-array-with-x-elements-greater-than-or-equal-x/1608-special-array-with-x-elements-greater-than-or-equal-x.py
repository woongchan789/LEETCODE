class Solution(object):
    def specialArray(self, nums):
        nums.sort()
        i = 0
        while i <= len(nums):
            if len(list(filter(lambda x:x>=i, nums))) == i:
                return i
            else:
                i += 1
        return -1