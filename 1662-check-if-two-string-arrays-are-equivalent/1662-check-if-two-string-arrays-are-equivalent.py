class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        a,b = '',''
        for i in word1:
            a += i
        for j in word2:
            b += j
 
        if a != b:
            return False
        else:
            return True