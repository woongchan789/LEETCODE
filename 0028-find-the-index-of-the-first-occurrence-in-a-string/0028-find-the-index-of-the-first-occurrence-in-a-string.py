class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            if haystack[i] == needle[0] and haystack[i:i+int(len(needle))] == needle:
                return i
            else:
                continue
        return -1