class Solution:
    def mySqrt(self, x):
        low = 0
        high = x
        
        while low <= high:
            mid = (low + high) // 2
            sqr = mid * mid
            if sqr == x or (sqr < x and (mid + 1) * (mid + 1) > x):
                return mid
            
            elif sqr > x:
                high = mid - 1
                
            else:
                low = mid + 1