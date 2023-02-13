class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        final = []
        for i in candies:
            if (i + extraCandies) >= max_candies:
                final.append(True)
            else:
                final.append(False)
        return final