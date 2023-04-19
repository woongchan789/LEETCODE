class Solution(object):
    def sortByBits(self, arr):
        arr.sort()
        bit_cnt = []
        for i in range(len(arr)):
            bit_cnt.append([arr[i], bin(arr[i]).count('1')])
        bit_cnt.sort(key=lambda x:x[1])
        return [num for num, cnt in bit_cnt]
