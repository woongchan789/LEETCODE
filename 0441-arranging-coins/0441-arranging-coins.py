class Solution(object):
    def arrangeCoins(self, n):
        row=1
        total=1
        while total<=n:
            total=total+row+1
            row+=1
        return row-1