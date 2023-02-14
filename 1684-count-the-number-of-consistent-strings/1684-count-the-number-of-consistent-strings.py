class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowed = list(allowed)
        cnt = len(words)
        for i in words:
            for j in i:
                if j not in allowed:
                    cnt -= 1
                    break
                    
        return cnt