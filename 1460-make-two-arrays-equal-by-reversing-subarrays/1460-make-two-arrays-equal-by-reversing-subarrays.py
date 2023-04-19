class Solution(object):
    def canBeEqual(self, target, arr):
        dic1, dic2 = {}, {}
        for i in set(arr):
            dic1[i] = arr.count(i)
        for j in set(target):
            dic2[j] = target.count(j)
        return True if dic1 == dic2 else False