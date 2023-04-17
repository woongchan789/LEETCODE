class Solution(object):
    def heightChecker(self, heights):
        origin = []
        for i in heights:
            origin.append(i)
        heights.sort()
        
        cnt = 0
        for i in range(len(heights)):
            if origin[i] != heights[i]:
                cnt += 1
        
        return cnt
        