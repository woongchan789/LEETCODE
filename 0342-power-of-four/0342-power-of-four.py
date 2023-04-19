class Solution(object):
    def isPowerOfFour(self, n):
        if n<=0:
            return False
        elif n==1:
            return True
        elif bin(n)[3:].count('1') == 0 and bin(n)[3:].count('0') % 2 == 0:
            return True
        else:
            return False