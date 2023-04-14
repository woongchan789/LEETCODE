class Solution(object):
    def minimumSum(self, num):
        a = []
        for i in str(num):
            a.append(int(i))
        a.sort()
        return (a[0] + a[1])*10 + a[2] + a[3]