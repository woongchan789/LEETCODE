class Solution(object):
    def cellsInRange(self, s):
        final = []
        for i in range(ord(s[0]), ord(s[-2])+1):
            for j in range(int(s[1]), int(s[-1])+1):
                final.append(chr(i)+str(j))
        return final