class Solution(object):
    def titleToNumber(self, columnTitle):
        cnt = len(columnTitle)
        final = 0
        for i in list(columnTitle):
            final += 26**(cnt-1) * (ord(i)-64)
            cnt -= 1
        return final