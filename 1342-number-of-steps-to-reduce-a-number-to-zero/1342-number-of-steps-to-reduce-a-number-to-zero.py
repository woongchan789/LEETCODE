class Solution(object):
    def numberOfSteps(self, num):
        cnt = 0
        while num != 0:
            if num == 1:
                num = (num - 1)
                cnt += 1
                break
            if (num%2 == 0):
                num = (num / 2)
                cnt += 1
            else:
                num = (num - 1)
                cnt += 1
        return cnt