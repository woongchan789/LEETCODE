class Solution(object):
    def trimMean(self, arr):
        arr.sort()
        i = int(len(arr)*0.05)
        return sum(arr[i:-i])/(len(arr)*0.9)