class Solution(object):
    def isPerfectSquare(self, num):
        if num==1:
            return True
        else:
            left, right = 1, num
            while left <= right:
                mid = (left+right) // 2
                square = mid*mid
                if square == num:
                    return True
                elif square <= num:
                    left = left + 1
                else:
                    right = mid - 1
            return False