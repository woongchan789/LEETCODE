class Solution(object):
    def maximumWealth(self, accounts):
        richest = 0
        for i in range(len(accounts)):
            if richest < sum(accounts[i]):
                richest = sum(accounts[i])
        return richest
