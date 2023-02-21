class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        for i in range(len(list(str(x)))//2):
            if list(str(x))[i] != list(str(x))[-(i+1)]:
                return False
        return True