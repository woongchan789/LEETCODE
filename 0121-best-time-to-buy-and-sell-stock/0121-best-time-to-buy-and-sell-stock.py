class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        buy = prices[0]
        for i in prices[1:]:
            profit = i - buy
            if profit > 0:
                max_profit = max(profit, max_profit)
            else:
                buy = i
        return max_profit
            
        