class Solution(object):
    def truncateSentence(self, s, k):

        final = ''
        for i in range(k):
            if i == k-1:
                final += s.split(' ')[i]
            else:
                final += s.split(' ')[i] + str(' ')
        return final