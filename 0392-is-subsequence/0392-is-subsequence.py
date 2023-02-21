class Solution(object):
    def isSubsequence(self, s, t):
        sub = ""
        for i in range(len(t)):
            if t[i] in s and t[i] == s[len(sub)]:
                sub += t[i]
        
        return sub == s