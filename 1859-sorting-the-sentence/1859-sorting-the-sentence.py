class Solution(object):
    def sortSentence(self, s):
        test = {}
        for i in list(s.split(' ')):
            test[i[-1]] = i[:-1]
            
        temp = sorted(test.items())

        temp2 = ''
        for i in temp:
            temp2 += i[1] + ' '
        return temp2[:-1]