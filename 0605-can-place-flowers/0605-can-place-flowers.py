class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        k = n
        
        if n == 0:
            return True
        
        flowerbed = [0] + flowerbed + [0]
            
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                k -= 1
            if k == 0:
                return True

        return False