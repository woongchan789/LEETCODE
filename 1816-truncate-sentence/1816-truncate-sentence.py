class Solution(object):
    def truncateSentence(self, s, k):
        a = s.split(' ')
        final = ''
        for i in range(k):
            if i == k-1:
                final += a[i]
            else:
                final += a[i] + str(' ')
        return final