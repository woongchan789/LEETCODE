class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        diff = (sum(aliceSizes)-sum(bobSizes))//2
        aliceSizes = set(aliceSizes)
        for i in set(bobSizes):
            if i+diff in aliceSizes:
                return [diff+i,i]