class Solution(object):
    def isValid(self, s):
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
        return False if len(s) != 0 else True