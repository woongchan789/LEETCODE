class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        x = 0
        for i in arr1:
            c = 1
            for j in arr2:
                if abs(i-j) <= d:
                    c = 0
                    break
            if c:
                x += 1
        return x