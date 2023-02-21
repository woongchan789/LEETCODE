class Solution(object):
    def countSegments(self, s):
        final = s.split(' ')
        return len(final) - final.count('')