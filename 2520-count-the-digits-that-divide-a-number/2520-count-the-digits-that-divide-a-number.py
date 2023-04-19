class Solution(object):
    def countDigits(self, num):
        cnt = 0
        for i in str(num):
            if num % int(i) == 0:
                cnt += 1
            else:
                continue
        return cnt