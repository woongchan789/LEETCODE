class Solution(object):
    def climbStairs(self, n):
        a = [0,1,2,3,5,8,13]
        temp = 0
        
        if n <= 6:
            return a[n]
        
        for i in range(7, n+1):
            a.append(a[i-2] + a[i-1])

        return a[n]
