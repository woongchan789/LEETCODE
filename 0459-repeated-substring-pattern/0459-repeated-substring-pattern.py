class Solution(object):
    def repeatedSubstringPattern(self, s):
        for i in range(1,len(s)):
            if len(s) % len(s[:i]) == 0 :
                if s[:i] * (len(s) // len(s[:i])) == s:
                    return True
        return False