class Solution(object):
    def firstUniqChar(self, s):
        for idx, value in enumerate(s):
            if s.count(value) == 1:
                return idx
        return -1
        