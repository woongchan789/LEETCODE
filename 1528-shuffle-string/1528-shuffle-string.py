class Solution(object):
    def restoreString(self, s, indices):
        final = [''] * len(s)
        for idx, value in enumerate(indices):
            final[value] = s[idx]
        return ''.join(final)
            