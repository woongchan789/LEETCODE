class Solution(object):
    def convertToTitle(self, columnNumber):
        a = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        final = []
        
        while columnNumber > 0:
            final.append(a[(columnNumber-1)%26])
            columnNumber = (columnNumber -1) // 26
        
        final.reverse()
        return ''.join(final)
