class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        idx_dict = {}
        for idx, value in enumerate(nums):
            if value in idx_dict:
                dist = idx - idx_dict[value]
                if dist <= k:
                    return True
            idx_dict[value] = idx
        return False