class Solution(object):
    def findRelativeRanks(self, score):
        
        final = []
        temp = sorted(score, reverse=True)
        
        for i in score:
            if temp.index(i) == 0:
                final.append('Gold Medal')
            elif temp.index(i) == 1:
                final.append('Silver Medal')
            elif temp.index(i) == 2:
                final.append('Bronze Medal')
            else:
                final.append(str(temp.index(i) + 1))
        
        return final