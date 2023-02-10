class Solution(object):
    def containsDuplicate(self, nums):
        temp_set = set()
        for i in nums:
            if i in temp_set:
                return True
            else:
                temp_set.add(i)
        return False